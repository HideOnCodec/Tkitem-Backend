# Tkitem-Backend

</div>

<br/>

## 1. Project Overview (프로젝트 개요)

- **프로젝트 이름**: Tk!tem(트킷템)
- **프로젝트 설명**: 여행, 준비물, 구매를 통합한 AI 스마트 여행 준비 플랫폼
- **성과** : 현대퓨처넷 풀스택 개발자 양성 교육 10기 최우수상(2위)

<img width="80%" alt="Screenshot 2025-11-07 at 8 43 08 PM" src="https://github.com/user-attachments/assets/0e77976d-1b7c-497a-9322-3ffbc54ae81e" />
<br/>
<br/>
<img width="80%" alt="Screenshot 2025-11-07 at 8 43 18 PM" src="https://github.com/user-attachments/assets/5c3c26e7-9933-4467-957b-6c180f6e314a" />



<br/>
<br/>

## 2. Team Members (팀원 및 팀 소개)

### 2.1 팀명
- **투게더**

### 2.2 팀원

| 김태연 (팀장) | 이나연 (부팀장) | 신은혜 | 박찬혁 |
|:-------------:|:------:|:------:|:------:|
| [GitHub](https://github.com/taeyeon0319) | [GitHub](https://github.com/yeon2lee) | [GitHub](https://github.com/HideOnCodec) | [GitHub](https://github.com/pch8349) |
| AI 체크리스트 추천 및 분석 <br> 여행 카테고리, 상품 분류 <br> 도시별 날씨 데이터 수집 | AI 상품 꾸러미 추천 <br> 상품 자동 태깅 구축 <br> 상품 데이터 수집/전처리 <br> 장바구니, 주문, 결제 구현 | AI 패션 취향 분석 구현 <br> 클라우드 인프라 구축 <br> 소셜 로그인, 인증 인가 구현 | AI 패키지 여행 추천 <br> 여행 데이터 수집/전처리 <br> 검색 및 임베딩 구축 <br> 여행 카테고리/일정 타입 분류

<br/>
<br/>

## 3. Technology Stack (기술 스택)

<img width="80%" alt="Screenshot 2025-11-07 at 8 39 40 PM" src="https://github.com/user-attachments/assets/1ba7624d-5f4a-4f8d-94e0-cdef2d35ea53" />

<br/>
<br/>

<img width="80%" alt="Screenshot 2025-11-07 at 8 39 50 PM" src="https://github.com/user-attachments/assets/0c8aeffd-b5f0-4901-8f98-b63b70328dc1" />

<br/>
<br/>


## 4. 담당 역할(기여도 20%)

### 4.1 로그인 및 회원 가입 구현(Spring Security, JWT, Kakao Oauth2.0)
[일반 로그인과 소셜 로그인을 필터를 통해 분기 처리](https://github.com/HideOnCodec/Tkitem-Backend/tree/develop/src/main/java/tkitem/backend/global/security/login)
- [/auth/login : 일반 로그인(General)](https://github.com/HideOnCodec/Tkitem-Backend/blob/develop/src/main/java/tkitem/backend/global/security/login/CustomJsonUsernameAuthenticationFilter.java)

- [/auth/login/kakao : 소셜 로그인(Social)](https://github.com/HideOnCodec/Tkitem-Backend/blob/develop/src/main/java/tkitem/backend/global/security/login/CustomSocialLoginAuthenticationFilter.java)

- [OIDC 프로토콜을 이용한 서명 검증 구현](https://github.com/HideOnCodec/Tkitem-Backend/blob/develop/src/main/java/tkitem/backend/global/security/login/OidcService.java)

- [Hash 처리 및 비밀번호 암호화](https://github.com/HideOnCodec/Tkitem-Backend/blob/develop/src/main/java/tkitem/backend/domain/member/service/MemberServiceImpl.java)

- [Redis를 이용한 토큰 검증, 자동 만료 구현](https://github.com/HideOnCodec/Tkitem-Backend/blob/develop/src/main/java/tkitem/backend/global/security/jwt/JwtAuthenticationProcessingFilter.java)
<img width="60%" alt="image" src="https://github.com/user-attachments/assets/c511964e-2691-498b-97a1-3fc4043cbab5" />
<img width="40%" alt="image" src="https://github.com/user-attachments/assets/4730cbe1-b45b-432f-8ae5-d02bd2cb00bd" />

<div/>
<div/>
    
### 4.2 설문 조사를 통한 사용자 패션 취향 MBTI(16가지) 계산
- [HuggingFace의 Fashion-Clip 모델을 이용한 패션 이미지 분석](https://github.com/HideOnCodec/Tkitem-Backend/blob/develop/src/main/resources/prompts/fashion_clip.py)

- [Spring AI, Open AI를 통한 사용자 첨부 이미지 실시간 분석](https://github.com/HideOnCodec/Tkitem-Backend/blob/develop/src/main/java/tkitem/backend/domain/preference/service/PreferenceAnalyzeServiceImpl.java)
<img width="90%" alt="image" src="https://github.com/user-attachments/assets/9895f5a8-70a3-4466-a239-857bfc810484" />


### 4.3 AWS, OCI, Docker, Github Actions 블루 그린 무중단 배포 

- Nginx를 이용한 블루 그린 배포 전략 적용
<img width="1708" height="804" alt="image" src="https://github.com/user-attachments/assets/018065ab-40dc-4c2e-bad2-e307bb45255b" />

- 배포 성공 또는 cpu 임계치 초과 시 알림
<img width="80%" alt="image" src="https://github.com/user-attachments/assets/40e0a897-20d3-4eeb-af30-3aa80a564309" />


### 4.4 CloudFront를 이용한 S3 이미지 조회 속도 향상 (CDN)
- [이미지 조회 시 Cloud Front 적용](https://github.com/HideOnCodec/Tkitem-Backend/blob/develop/src/main/java/tkitem/backend/global/util/CloudFrontUtil.java)

<br/>
<br/>

## 5. 기능 소개

### 5.1 메인 화면
<img src="https://github.com/user-attachments/assets/c1257e10-446f-4207-81cb-b3e7bbc553fa" width="300"/>
<br/>

---

### 5.2 여행

#### 5.2.1 여행 취향 조사 후 추천
<img src="https://github.com/user-attachments/assets/dca1f0cf-80ce-40f7-af85-4527a2441755" width="300"/>
<br/>

#### 5.2.2 여행 일정에 맞는 준비물 리스트 자동 생성  
<img src="https://github.com/user-attachments/assets/d0320fb5-609d-498b-8a69-37ac01b1f5f8" width="300"/>
<br/>

#### 6.3.2 준비물 리스트에 맞는 여행 상품 추천
<img src="https://github.com/user-attachments/assets/d1f03bff-b065-4132-8549-7524b944df9e" width="300"/>
<br/>

---

### 6.4 ✍️ 패션 취향 분석
 
#### 6.4.1 패션 취향 조사 후 분석 결과
<video src="https://github.com/user-attachments/assets/28e85ad1-4eb1-4e9e-8611-cb7c5a3a990d" autoplay loop muted playsinline></video>
<br/>

#### 6.4.2 패션 취향 MBTI 리스트
<img src="https://github.com/user-attachments/assets/ecab8d78-cd68-4afa-a643-713c3bd77619" width="300"/>
<br/>

---

### 6.5 주문

#### 6.5.1 여행 일정별로 장바구니 담기
<img src="https://github.com/user-attachments/assets/cc3a3289-5c93-4b82-8476-a6a60a6ea5ea" width="300"/>
<br/>

#### 6.5.2 주문 내역 확인
<img src="https://github.com/user-attachments/assets/750a8369-a827-4ba9-a5a4-fa1ee45b8293" width="300"/>
<br/>
