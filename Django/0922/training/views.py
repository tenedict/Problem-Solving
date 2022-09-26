import imp
from threading import excepthook
from django.shortcuts import render
import random
# Create your views here.
def index(request):

    return render(request,'index.html')

def dinner(request):
    foods = [{"name" : '삼겹살', "src":'https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/201702/27/117f5b49-1d09-4550-8ab7-87c0d82614de.jpg'},
    {"name" : '상스치콤', "src":'http://imgur.com/Z6VCSYC.png'},
    {"name" : '빅맥', "src":'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6XnMhTVuQb2CQRr6ubZOp6hHHMEIofRsLeXm4_gnpnbtxZAVRwjGrbk37M6x9gFvD0KE&usqp=CAU'},
    {"name" : '스낵랩', "src":'https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbEV4pK%2FbtrgBDaTcf4%2F7DuNEErimMI2GJpKIcK2NK%2Fimg.png'},
    {"name" : '빵', "src":'https://thumbnews.nateimg.co.kr/view610///onimg.nate.com/orgImg/hr/2014/10/28/20141028000965_0.jpg'},
    {"name" : '불고기버거', "src":'https://blog.kakaocdn.net/dn/brZPp6/btrubvpQneM/sYNp2MQDFthobz8aj6NdiK/img.jpg'},
    {"name" : '떡볶이', "src":'https://blog.kakaocdn.net/dn/tTzV4/btrkANGFcxK/fxiScV4nSkOrvTYAinurG1/img.jpg'}]
    food = random.choice(foods)
    
    context = {
        'food': food,
        
        }

    return render(request, 'dinner.html',context)

# def lotto(request):
#     numbers = []
#     rank = []
#     ex = [3, 11, 15, 29 ,35, 44]
#     bonus = 10
    
    
#     for i in range(5):    
#         current = (random.sample(range(1,46),6))
#         numbers.append(current)
#         count_ = len(set(current+ex)) -6
#         if count_ == 0:
#             rank.append('1등')
#         if count_ == 1:
#             if 10 in current:
#                 rank.append('2등')
#             else:
#                 rank.append('3등')
#         if count_ == 2:
#             rank.append('4등')
#         if count_ == 3:
#             rank.append('5등')
#         else:
#             rank.append('꽝!')
    
#     n_r=zip(numbers,rank)

#     context = {
#         'n_r' : n_r
#     }
    

#     return render(request,'lotto.html',context)

# def lotto(request):
#     lottonums = []
    
#     ex = [3, 11, 15, 29 ,35, 44]
#     bonus = 10
    
    
#     for i in range(5):    
#         current = (random.sample(range(3,45),6))
#         dic = {}
#         dic['number'] = current
        
#         count_ = 12 - len(set(current+ex)) 
#         if count_ == 6:
#             dic['rank'] ='1등'
#         elif count_ == 5:
#             if bonus in current:
#                 dic['rank'] ='2등'
#             else:
#                 dic['rank'] ='3등'
#         elif count_ == 4:
#             dic['rank'] ='4등'
#         elif count_ == 3:
#             dic['rank'] ='5등'
#         else:
#             dic['rank'] ='꽝!'

#         lottonums.append(dic)

#     context = {
#         'lottonums'  : lottonums,
#         'ex' : ex
#     }
    

#     return render(request,'lotto.html',context)


def lotto(request):
    lottonums = []
    
    ex = [3, 11, 15, 29 ,35, 44]
    ex1 = [3, 11, 15, 29 ,35, 44,10]
    bonus = 10
    
    
    for i in range(5):    
        current = (random.sample(ex1,6))
        dic = {}
        dic['number'] = current
        
        count_ = 12 - len(set(current+ex)) 
        if count_ == 6:
            dic['rank'] ='1등'
        elif count_ == 5:
            if bonus in current:
                dic['rank'] ='2등'
            else:
                dic['rank'] ='3등'
        elif count_ == 4:
            dic['rank'] ='4등'
        elif count_ == 3:
            dic['rank'] ='5등'
        else:
            dic['rank'] ='꽝!'

        lottonums.append(dic)

    context = {
        'lottonums'  : lottonums,
        'ex' : ex
    }
    

    return render(request,'lotto.html',context)