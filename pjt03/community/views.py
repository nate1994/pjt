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



def create_review(request): # 받아온 것을 저장해서 redirect
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