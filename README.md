# Codestates-Section3

# 1. 프로젝트 개요
많은 사람들의 꿈인 내 집 마련을 꿈꾸며  
[구, 동, 층, 건물용도]를 선택 후 서울의 내가 살고 싶은 집값을 예측하는 프로젝트
<br/>
<br/>
# 2. 프로젝트 개발 환경 및 구조 

<img width="1025" alt="image" src="https://user-images.githubusercontent.com/102211628/198208729-d05d4999-34ce-465c-b5e7-84ec1e1c3d83.png">
데이터 수집  : 서울 열린 데이터 광장 <br/>
개발언어 : Python<br/>
<br/>
# 3. 데이터 분석 및 시각화
-Google 대시보드
<img width="932" alt="image" src="https://user-images.githubusercontent.com/102211628/198210852-94d652da-9fbd-4277-9918-ef691dc4c326.png">
평균 집값이 가장 높은 구 / 건물용도에 따른 평균 집값<br/>
<img width="975" alt="image" src="https://user-images.githubusercontent.com/102211628/198211791-6901f928-71c9-4b62-ab66-aef9a52d547c.png">
평균 집값이 높은 동 / 층별 평균 집값 순
<br/>
<br/>
# 4. 모델 
 RandomForest를 사용한 리모델링 <br/>
 자치구명, 법정동명, 건물용도는 OrdinalEncoder <br/>
 모델을 PKL를 사용하여 저장.<br/>
 <br/>
# 5. 결과
<img width="954" alt="image" src="https://user-images.githubusercontent.com/102211628/198212667-4ec87362-3d29-458e-885f-2e1f2a4f04f7.png">
<img width="975" alt="image" src="https://user-images.githubusercontent.com/102211628/198212715-efafcbcb-8c7b-4d18-9e13-15ee2d66b280.png">

<img width="954" alt="image" src="https://user-images.githubusercontent.com/102211628/198212667-4ec87362-3d29-458e-885f-2e1f2a4f04f7.png">
<img width="864" alt="image" src="https://user-images.githubusercontent.com/102211628/198212754-303b2ed4-665e-465b-8863-d9418feb052a.png">


