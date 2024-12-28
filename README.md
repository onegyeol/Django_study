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

#### 트러블 슈팅
1. ModuleNotFoundError: No module named 'myweb.settings'
   
프로젝트가 2번 생성되면서 myweb>myweb 형식으로 되어있어서 Django가 myweb.settings 파일을 인식하지 못함.
프로젝트 1개를 삭제한 후 다시 실행.

2. django.db.utils.OperationalError: no such table:
모델을 생성한 후 데이터베이스에 적용하기 위한 마이그레이션 작업을 하지 않아서 발생함.
마이그레이션 이후 정상 실행.

### Chapter 3. ToDo 목록 웹 서비스 만들기

### Chapter 4. REST Framework

### Chapter 5. ToDo 목록 API 제작

### Chapter 6. REST Framework + React.js 게시판

