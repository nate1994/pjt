# README



### 🐱‍🚀pjt03 

Django의 flow인 model -> url -> view -> template 흐름에 맞추어 절차적으로 하나하나 만들어가면서 프로젝트를 진행했습니다.

### 1.  models 

```python
from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    rank = models.IntegerField(default=1)
```

 데이터베이스 모델을 위한 migrate하였습니다.

### 2. url  

```python
from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path("", views.index, name="index"),
    path("new_review/", views.new_review, name="new_review"), # new -> create_review
    path("create_review/", views.create_review, name ='.create_review'), 
    path("review_detail/<int:review_pk>/", views.review_detail, name="review_detail"), #디테일
]
```

new_review 와 create_review를 통해 create 작업을 하게 만들었습니다.

### 3. views 

```python
from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews' : reviews
    }
    return render(request, 'review_list.html',context)


def new_review(request):
    return render(request, 'new_review.html')


def create_review(request):
    title = request.POST.get('title')
    content = request.POST.get('content') 
    rank = request.POST.get('rank')
    # print(title , content, rank) 받아온거 확인
    review = Review()
    review.title = title
    review.content = content
    review.rank = rank
    review.save() 
    return redirect('community:index') # 초기화면으로~


def review_detail(request, review_pk):
    review = Review.objects.get(pk = review_pk)
    context ={
        'review' : review
    }
    return render(request, 'review_detail.html', context)
```



### admin.py

```python
from django.contrib import admin

# Register your models here.
from .models import Review # 명시적 상대경로 표현
admin.site.register(Review)
```

$ python manage.py createsuperuser 

로 관리자 계정을 만든 후 admin.py 파일을 수정했습니다.





## 소감✌

2주동안 학습한 Django를 통해 기본적인 프레임워크 사용법 그리고 가상환경에서 프로젝트를 관리하는 방법에 대해서 배울 수 있었습니다. 

Django의 강력한 기능을 통해 다양한 프로젝트를 추가적으로 진행하고 싶은 계획과 자신감을 가지게 되었습니다.

앞으로 Django에 더 관심을 갖고 웹 개발 역량을 키워나가겠습니다.