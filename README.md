# Django
백엔드를 위한 DJANGO REST FRAMEWORK with 파이썬

## Chapter 2. Django의 기본
django는 MTV패턴을 기반으로 개발된다.
- Model : 데이터와 관련된 부분
- Template : 사용자에게 보여지는 부분. 탬플릿 태그 {} 사용 가능
- View : Model의 데이터를 Template로 전달하고 Template에서 발생하는 이벤트 처리
<img width="700" src="https://github.com/user-attachments/assets/26e73c6d-3d6b-4357-9032-e49e938327da"/> <br>
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

## Chapter 3. ToDo 목록 웹 서비스 만들기
CRUD?
- Create
- Read
- Update
- Delete

위 4가지 기능을 포함하고 있는 Todo 목록 웹 서비스를 제작함.

1. models
```
title = models.CharField(max_length=100)
description = models.TextField(blank=True)
created = models.DateTimeField(auto_now_add=True)
complete = models.BooleanField(default=False)
important = models.BooleanField(default=False)
```

2. html page
완료 리스트 목록, 리스트 생성, 생성된 리스트 목록, 리스트 상세 정보

### 트러블 슈팅
1. 책 92쪽 완료된 목록 코드 잘못됨

책에 적힌 코드가 잘못 나와있어서 코드에 오류가 났음.
```
def done_list(request):
    dones = Todo.objects.filter(complete=False)
    return render(request, 'todo/done_list.html', {'dones':dones})
```
위와 같이 수정하여 실행.

## Chapter 4. REST Framework
Django REST Framework는 Django를 기반으로 REST API서버를 만들기 위한 라이브러리
이를 사용하면 기존 자체적인 웹 템플릿에게 바로 데이터를 전달해주었던 방식에서 JSON과 같은 양식으로 다양한 플랫폼의 클라이언트들에게 데이터 제공 가능해짐 <br>
<img width="700" src="https://github.com/user-attachments/assets/6a36f704-3340-44c8-a009-0c05cd6f254f"/> <br>

```
pip install djangorestframework # 해당 명령어 사용해 가상환경에 설치함
```

그리고 시리얼라이저라는 개념 등장
시리얼라이저는 Django 모델을 JSON으로 변환해주는 것임

```
#model은 ch.2에 나오는 모델을 사용함
from rest_framework import serializers
from .models import Todo

class TodoSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'complete', 'important') # 해당 필드의 모델 데이터를 JSON으로 변환
```


## Chapter 5. ToDo 목록 API 제작
API 테스트를 위해 Insomnia라는 툴 사용함. 
```
https://insomnia.rest/ # 환경에 맞춰 설치
```
터미널 창에서 서버를 띄워준 뒤 API 테스트 진행하면 됨.
<img width="700" alt="스크린샷 2025-01-04 오후 11 52 31" src="https://github.com/user-attachments/assets/0ef017f4-f365-4958-a5c6-d04c57bae654" /> <br>


