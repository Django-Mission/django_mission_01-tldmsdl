from ast import While, operator
from multiprocessing import context
import numbers
from unittest import result
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.
def calculator(request):
    # return HttpResponse('계산기 기능 구현 시작입니다. 이게 맞나요?')
    print(f'request = {request}')
    print(f'request type = {type(request)}')
    print(f'request._dict__ = {request.__dict__}')

    #1. 데이터 확인
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operators = request.GET.get('operators')

    #2. 계산
    if operators == '+':
        result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    elif operators == '*':
        result = int(num1) * int(num2)
    elif operators == '/':
        result = int(num1) / int(num2)
    else:
        result = 0


    #3. 응답
    return render(request, 'calculator.html', {'result': result})


import random

def lotto(request):
    lotto_result = random.sample(range(1,47),7) 
    lotto_result.sort() #오름차순 정렬
    print(lotto_result)

    return render(request, 'lotto.html', {'lotto_result': lotto_result})
