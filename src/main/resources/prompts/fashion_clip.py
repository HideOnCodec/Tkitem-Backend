# -*- coding: utf-8 -*-
from transformers import CLIPModel, CLIPProcessor
from PIL import Image
import requests, io, torch, numpy as np
import pandas as pd
from IPython.display import display  # Jupyter/Colab 환경에서 표 렌더링

MODEL_ID = "patrickjohncyh/fashion-clip"
device = "cuda" if torch.cuda.is_available() else "cpu"
model = CLIPModel.from_pretrained(MODEL_ID).to(device)
processor = CLIPProcessor.from_pretrained(MODEL_ID)
model.eval()

AXIS_PROMPTS = {
    "b": {
        "neg": [
            "a dark outfit",
            "an outfit in mostly black tones",
            "low brightness clothing",
            "a dark brown outfit in earthy tones",
            "a dark khaki or olive toned outfit",
            "deep earth-tone clothing with low lightness"
        ],
        "pos": [
            "a bright outfit",
            "an outfit in light pastel or white tones",
            "high brightness clothing",
            "a light beige or cream toned outfit",
            "off-white minimal clothing with high lightness"
        ]
    }
}

def load_image_from_url(url: str) -> Image.Image:
    resp = requests.get(url, timeout=20)
    resp.raise_for_status()
    return Image.open(io.BytesIO(resp.content)).convert("RGB")

@torch.no_grad()
def embed_image(img: Image.Image):
    inputs = processor(images=img, return_tensors="pt").to(device)
    feats = model.get_image_features(**inputs)
    return torch.nn.functional.normalize(feats, p=2, dim=-1)

@torch.no_grad()
def embed_text(texts):
    inputs = processor(text=texts, return_tensors="pt", padding=True).to(device)
    feats = model.get_text_features(**inputs)
    return torch.nn.functional.normalize(feats, p=2, dim=-1)

def cosine_sim(img_emb, txt_emb):
    return (img_emb @ txt_emb.T).squeeze(0).cpu().numpy()

def softmax(x, tau=0.07):
    x = np.array(x, dtype=float) / tau
    x -= x.max()
    e = np.exp(x)
    return e / e.sum()

def bucketize(x: float) -> int:
    if x <= -0.70: return -2
    if x < -0.35: return -1
    if x <= 0.35: return 1
    return 2

@torch.no_grad()
def avg_sim(img_emb, texts):
    txt_emb = embed_text(texts)
    sims = cosine_sim(img_emb, txt_emb)
    return float(np.mean(sims))

def score_axis(img_emb, axis_key="b", tau=0.07):
    groups = AXIS_PROMPTS[axis_key]
    s_neg = avg_sim(img_emb, groups["neg"])
    s_pos = avg_sim(img_emb, groups["pos"])
    probs = softmax([s_neg, s_pos], tau=tau)
    cont = probs[1] - probs[0]
    return s_pos, s_neg, probs, cont, bucketize(cont)

def run_tests(urls):
    rows = []
    for url in urls:
        img = load_image_from_url(url)
        img_emb = embed_image(img)
        s_pos, s_neg, probs, cont, bucket = score_axis(img_emb, "b")

        rows.append({
            "밝은옷 유사도": round(float(s_pos), 2),
            "어두운옷 유사도": round(float(s_neg), 2),
            "밝을 확률": round(float(probs[1]), 2),
            "어두울 확률": round(float(probs[0]), 2),
            "확률 차이": round(float(cont), 2),
            "버킷 매핑": bucket
        })

    df = pd.DataFrame(rows)
    display(df)   # Jupyter/Colab에서 예쁘게 표 출력
    return df

# -------------------------
# 테스트 실행
# -------------------------
urls = [
    "https://tkitem-s3.s3.ap-northeast-2.amazonaws.com/survey/female/young/1/Q1-3.png"
]
run_tests(urls)
