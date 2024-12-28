# Django
백엔드를 위한 DJANGO REST FRAMEWORK with 파이썬

### Chapter 2. Django의 기본
django는 MTV패턴을 기반으로 개발된다.
- Model : 데이터와 관련된 부분
- Template : 사용자에게 보여지는 부분. 탬플릿 태그 {} 사용 가능
- View : Model의 데이터를 Template로 전달하고 Template에서 발생하는 이벤트 처리

![image](https://github.com/user-attachments/assets/26e73c6d-3d6b-4357-9032-e49e938327da)
사진 출처 : https://velog.io/@hamcheese/Django-MTVMVC

1. 가상 환경 세팅
```
python3 -m venv myvenv # 가상환경 이름은 myvenv라고 가정
```

2. 가상 환경 실행
```
source myvenv/bin/activate # 윈도우의 경우 myvenv₩Scripts₩activate
```

3. Django 설치
```
pip install django
```

4. Django 프로젝트 생성
```
django-admin startproject myweb . # 프로젝트 명은 myweb으로 설정
```

5. Django 서버 실행
```
python manage.py runserver
```

6. 마이그레이션 방법
```
python manage.py makemigrations
python manage.py migrate
```

7. Django 관리자 계정 생성
```
python manage.py createsuperuser
```


### Chapter 3. ToDo 목록 웹 서비스 만들기

### Chapter 4. REST Framework

### Chapter 5. ToDo 목록 API 제작

### Chapter 6. REST Framework + React.js 게시판

