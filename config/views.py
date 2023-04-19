from django.http import HttpResponse
from django.shortcuts import render
from burgers.models import Burger

def main(request):
    return render(request,'main.html')

def burger_list(request):
    burgers = Burger.objects.all()
    print('전체 햄버거 목록:', burgers)
    # burgers 라는 키에 burgers라는 변수를 전달한다
    context = {
        'burgers':burgers,
    }
    return render(request,'burger_list.html',context)

def burger_search(request):
    keyword = request.GET.get('keyword')
    print(keyword)
    # print(request.GET)
    return render(request,'burger_search.html')