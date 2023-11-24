from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
import requests
from .serializers import DepositOptionsSerializer, DepositProductsSerializer, SavingProductsSerializer, SavingOptionsSerializer
from .models import DepositOptions, DepositProducts, SavingProducts, SavingOptions
from rest_framework.decorators import api_view

from accounts.models import User
from accounts.serializers import CustomRegisterSerializer

from faker import Faker
import random

from django.conf import settings


API_KEY = '8ce1c2130fa3f759c31b0ef5c9b3050c'

# Create your views here.
@api_view(['GET'])
def save_data(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'

    response = requests.get(url).json()
    products_lst = response.get('result').get('baseList')
    
    for prdt in products_lst:
        prdt_data = {
            'kor_co_nm': prdt.get('kor_co_nm'),
            'fin_co_no': prdt.get('fin_co_no'),
            'fin_prdt_cd': prdt.get('fin_prdt_cd'),
            'fin_prdt_nm': prdt.get('fin_prdt_nm'),
            'dcls_month': prdt.get('dcls_month'),
            'join_member': prdt.get('join_member'),
            'join_deny': prdt.get('join_deny'),
            'join_way': prdt.get('join_way'),
            'mtrt_int': prdt.get('mtrt_int'),
            'spcl_cnd': prdt.get('spcl_cnd'),
            'etc_note': prdt.get('etc_note'),

        }

        existing_product = DepositProducts.objects.filter(fin_prdt_cd=prdt_data['fin_prdt_cd'])

        # 이미 존재하는 레코드의 정보를 업데이트
        if existing_product:
            existing_product1 = DepositProducts.objects.get(fin_prdt_cd=prdt_data['fin_prdt_cd'])
            serializer = DepositProductsSerializer(data=prdt_data, instance=existing_product1)
        
        # 존재하지 않는 경우, 새로운 레코드를 생성
        else:
            serializer = DepositProductsSerializer(data=prdt_data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

    # return JsonResponse({'message': 'ok'})


    # def dp_prdt_lst(request):
    #     if request.method == 'GET':
    #         dp_prdts = get_list_or_404(DepositProducts)
    #         serializer = DepositProductsSerializer(dp_prdts, many=True)
    #         return JsonResponse({'data': serializer.data})


    # def save_dp_optn(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'

    response = requests.get(url).json()
    options_lst = response.get('result').get('optionList')

    for optn in options_lst:
        optn_data = {
            'fin_prdt_cd': optn.get('fin_prdt_cd'),
            'fin_co_no': optn.get('fin_co_no'),
            'save_trm': optn.get('save_trm'),
            'intr_rate_type_nm': optn.get('intr_rate_type_nm'),
            'intr_rate': optn.get('intr_rate'),
            'intr_rate2': optn.get('intr_rate2'),
        }

        existing_product = DepositOptions.objects.filter(fin_prdt_cd=optn_data['fin_prdt_cd'], intr_rate=optn_data['intr_rate'], save_trm=optn_data['save_trm'])

        if existing_product:
            existing_product1 = DepositOptions.objects.get(fin_prdt_cd=optn_data['fin_prdt_cd'], intr_rate=optn_data['intr_rate'], save_trm=optn_data['save_trm'])
            serializer = DepositOptionsSerializer(data=optn_data, instance=existing_product1)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        else:
            serializer = DepositOptionsSerializer(data=optn_data)
            if serializer.is_valid(raise_exception=True):
                prdt = DepositProducts.objects.get(fin_prdt_cd=optn.get('fin_prdt_cd'))
                serializer.save(product=prdt)

    # return JsonResponse({'message': 'ok'})


    # def dp_optn_lst(request):
    #     if request.method == 'GET':
    #         dp_prdts = get_list_or_404(DepositOptions)
    #         serializer = DepositOptionsSerializer(dp_prdts, many=True)
    #         return JsonResponse({'data': serializer.data})


    # def save_sv_prdt(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'

    response = requests.get(url).json()
    products_lst = response.get('result').get('baseList')
    
    for prdt in products_lst:
        prdt_data = {
            'kor_co_nm': prdt.get('kor_co_nm'),
            'fin_co_no': prdt.get('fin_co_no'),
            'fin_prdt_cd': prdt.get('fin_prdt_cd'),
            'fin_prdt_nm': prdt.get('fin_prdt_nm'),
            'dcls_month': prdt.get('dcls_month'),
            'join_member': prdt.get('join_member'),
            'join_deny': prdt.get('join_deny'),
            'join_way': prdt.get('join_way'),
            'mtrt_int': prdt.get('mtrt_int'),
            'spcl_cnd': prdt.get('spcl_cnd'),
            'etc_note': prdt.get('etc_note'),
            'max_limit':prdt.get('max_limit'),
        }

        existing_product = SavingProducts.objects.filter(fin_prdt_cd=prdt_data['fin_prdt_cd'])
        
        if existing_product:
            existing_product1 = SavingProducts.objects.get(fin_prdt_cd=prdt_data['fin_prdt_cd'])
            serializer = SavingProductsSerializer(data=prdt_data, instance=existing_product1)

        else:
            # 존재하지 않는 경우, 새로운 레코드를 생성
            serializer = SavingProductsSerializer(data=prdt_data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

    # return JsonResponse({'message': 'ok'})


    # def sv_prdt_lst(request):
    #     if request.method == 'GET':
    #         dp_prdts = get_list_or_404(SavingProducts)
    #         serializer = SavingProductsSerializer(dp_prdts, many=True)
    #         return JsonResponse({'data': serializer.data})


    # def save_sv_optn(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'

    response = requests.get(url).json()
    options_lst = response.get('result').get('optionList')

    for optn in options_lst:
        optn_data = {
            'fin_prdt_cd': optn.get('fin_prdt_cd'),
            'fin_co_no': optn.get('fin_co_no'),
            'save_trm': optn.get('save_trm'),
            'intr_rate_type_nm': optn.get('intr_rate_type_nm'),
            'rsrv_type' : optn.get('rsrv_type'),
            'rsrv_type_nm' : optn.get('rsrv_type_nm'),
            'intr_rate': optn.get('intr_rate'),
            'intr_rate2': optn.get('intr_rate2'),
        }

        existing_product = SavingOptions.objects.filter(fin_prdt_cd=optn_data['fin_prdt_cd'], intr_rate=optn_data['intr_rate'], save_trm=optn_data['save_trm'], rsrv_type=optn_data['rsrv_type']).exists()

        if existing_product:
            existing_product1 = SavingOptions.objects.get(fin_prdt_cd=optn_data['fin_prdt_cd'], intr_rate=optn_data['intr_rate'], save_trm=optn_data['save_trm'])
            serializer = SavingOptionsSerializer(data=optn, instance=existing_product1)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        else:
            serializer = SavingOptionsSerializer(data=optn_data)
            if serializer.is_valid(raise_exception=True):
                prdt = SavingProducts.objects.get(fin_prdt_cd=optn.get('fin_prdt_cd'))
                serializer.save(product=prdt)

    return JsonResponse({'message': 'ok'})


# def sv_optn_lst(request):
#     if request.method == 'GET':
#         dp_prdts = get_list_or_404(SavingOptions)
#         serializer = SavingOptionsSerializer(dp_prdts, many=True)
#         return JsonResponse({'data': serializer.data})

@api_view(['GET'])
def get_data(request):

    deposits = DepositProducts.objects.all()
    deposit_options = DepositOptions.objects.all()
    savings = SavingProducts.objects.all()
    saving_options = SavingOptions.objects.all()
    
    deposit_serializer = DepositProductsSerializer(deposits, many=True)
    deposit_options_serializer = DepositOptionsSerializer(deposit_options, many=True)
    saving_serializer = SavingProductsSerializer(savings, many=True)
    saving_options_serializer = SavingOptionsSerializer(saving_options, many=True)

    res = {
        'deposits': deposit_serializer.data,
        'depositoptions': deposit_options_serializer.data,
        'savings': saving_serializer.data,
        'savingoptions': saving_options_serializer.data,
    }
    
    return JsonResponse(res)



@api_view(['GET'])
def test(request):
    userDummy = [
    {'id':1, 'money': 140604869, 'salary':8400000},
    {'id':2, 'money':8000000, 'salary':40000000},
    {'id':3, 'money':10000000, 'salary':40000000},
    {'id':4, 'money':7600000, 'salary':40000000}, 
    {'id':5, 'money':3000000, 'salary':30000000},
    {'id':6, 'money': 80000000, 'salary':8400000},
    {'id':7, 'money':6500000, 'salary':40000000},
    {'id':8, 'money':10000000, 'salary':40000000},
    {'id':9, 'money':7400000, 'salary':40000000}, 
    {'id':10, 'money':3000000, 'salary':30000000},
    {'id':11, 'money': 120000000, 'salary':8400000},
    {'id':12, 'money':10000000, 'salary':40000000},
    {'id':13, 'money':10000000, 'salary':40000000},
    {'id':14, 'money':10000000, 'salary':40000000}, 
    {'id':15, 'money':3000000, 'salary':30000000},
    {'id':16, 'money': 990000000, 'salary':8400000},
    {'id':17, 'money':10000000, 'salary':40000000},
    {'id':18, 'money':2400000, 'salary':40000000},
    {'id':19, 'money':10000000, 'salary':40000000}, 
    {'id':20, 'money':3000000, 'salary':30000000},
    ]
     
    arr = sorted(userDummy, key=lambda x: -x.get('money'))
    
    # 파레토 활용: 전체 부의 80%는 상위 20%가 가지고 있다는 이론 
    pareto = arr[int(len(arr) * 0.2)-1].get('money')

    # 재산 상위 리스트 뽑기 
    person = []
    sum_money = 0
    for i in userDummy:
        if i.get('money') >= pareto:
            person.append(i)
   


    # 위 코드는 파레토 법칙 으로 상위 20% 커트 구하는 방법
    # 아래 코드는 파레토 법칙을 이용하여 재산 상위/중위/하위를 구분하고 부자면 예금 나머지는 적금 상품을 추천할 계획

    # 예금 상품 목록  ( 상위 )
    arr = DepositProducts.objects.all()
    # 적금 상품 목록 ( 중위/하위 )
    crr = SavingProducts.objects.all()

    # 상위 분류에게 장기 복리 예금 상품 뽑아주기 made in yongsusie
    result_list = []

    # 중위/하위 분류에게 적금 상품 뽑아주기
    affordable_savings = []


    for i in userDummy:
        typeRich = False
        if i.get('money') >= pareto:
            typeRich = True
        
        if typeRich:
            richPerson = {
                'name' : i['id'],
                'money':i['money'], 
                'salary': i['salary'],
                'recommend' : [],
                
            }
            # 예금 상품 리스트 순환
            for j in arr:
                # Serializer로 직렬화 해준다. 
                t1 = DepositProductsSerializer(j)
                # data를 뽑아준다.
                t4 = t1.data
                # t4 안에 options 를 꺼낸다.
                t6 = t4['depositoptions_set']
                # 장기 복리 상품을 담을 리스트 t7
                t7 = []
                # 옵션들을 돌린다
                for k in t6:
                    t2 = k["intr_rate_type_nm"]
                    if t2 == "복리":
                        # 만기가 24, 36 개월 이라면 (장기 상품)
                        t3 = k["save_trm"]
                        if t3 in [24, 36]:
                            # t7에 옵션 k를 넣는다.
                            t7.append(k)
                # 장기 복리 상품이 들어있다면?
                if t7:
                    # t4에 해당되는 옵션들로 바꿔준다 (?)
                    t4['depositoptions_set'] = t7
                    # 재산 상위 리스트에 추천 상품을 넣어준다.
                    richPerson['recommend'] = t4
                    # 재산 상위 리스트에 넣어준다.
                    result_list.append(richPerson)


        # 재산 중위/하위라면? => 단기 & 적금 상품 추천해주기
        else: 
            richPerson = {
                'name' : i['id'],
                'money':i['money'], 
                'salary': i['salary'],
                'month_saving' : 0,
                'recommend' : [],
            }
        

            tax_rate = 0.06
            if 14_000_000 <= i.get('salary') <= 50_000_000:
                tax_rate = 0.15

            if i.get('salary') >= 50_000_000:
                tax_rate = 0.24 

            # 매달 납입할 금액 month_saving
            month_saving = int(i.get('salary') * tax_rate / 12 * 0.4)


            k3 = []
            # 적금 상품 순회
            for k in crr : 
                # Serializer로 직렬화 해준다. 
                k1 = SavingProductsSerializer(k)
                # data를 뽑아준다.
                k2 = k1.data


                k4 = k2['max_limit']
                # max_limit 값이 null도 있으므로 -> null 이면 0으로 바꿔주기
                if not k4:
                    k2['max_limit'] = 987654321
                # 만약 상품의 최대 납입 금액이 고객이 감당 가능한 month_saving 보다 낮다면 -> 추천해주기
                if k2['max_limit'] <= month_saving:
                    k3.append(k2)

            # 추천할 상품이 있다면 
            if k3:
                # 최대 납입 가능 금액을 내림차순으로 정렬해주기 (lambda 함수 내림차순 - )
                sorted_saving_products =  sorted(k3, key=lambda x: -x['max_limit'])
                richPerson['recommend'] = sorted_saving_products
                richPerson['month_saving'] = month_saving
                affordable_savings.append(richPerson)
                


    # 재산 상위 출력
    return JsonResponse({
        'forRich': result_list,
        'forPoor': affordable_savings,
        }, safe=False) 



@api_view(['GET'])
def test1(request):
    arr = SavingProducts.objects.all()
    brr = SavingProductsSerializer(arr, many=True)

    return Response(brr.data)




@api_view(['GET'])
def user_db(request):
            # 유저 데이터 생성 함수 (미완성) 
    first_name_samples = "편최김이박조전박강임남"
    middle_name_samples ="수용진해단인근종정규지"
    last_name_samples =  "지수영진비화렬혁수환수"


    def random_name():
        result = ""
        result += random.choice(first_name_samples)
        result += random.choice(middle_name_samples)
        result += random.choice(last_name_samples)
        return result + str(random.randint(1, 100))


    # dict_keys = ['username', 'gender', 'financial_products', 'age', 'money', 'salary']


    fake = Faker('ko_KR')
    
    
    
    username_list = []
    N = 100
    i = 0

    while i < N:
        rn = random_name()
        if rn in username_list:
            continue
        
        username_list.append(rn)
        i += 1


    for i in range(N):
        username = username_list[i]  # 유저 이름 랜덤 생성
        email = f'pk{i}@ssafy.com'
        age = int(random.randint(1, 100))  # 나이
        money = random.randint(1000000, 10000000)
        salary = random.randint(3000000, 100000000)
        password = "1234"
        nickname = None
        is_active = True
        is_staff = False
        is_superuser = False


        # 사용자 생성
        user = User.objects.create_user(
            username=username,
            password=password,
            email= email,
            age=age,
            money=money,
            salary=salary,
            nickname = nickname,
            is_active = is_active,
            is_staff = is_staff,
            is_superuser = is_superuser,
        )

    return Response({'message':'success'})


@api_view(['GET'])
def recommendproducts(request):
    result_list = []
    affordable_savings = []
    arr = DepositProducts.objects.all()
    brr = SavingProducts.objects.all()
    a = User.objects.get(username=request.user)
    b = CustomRegisterSerializer(a).data
    pareto = settings.PARETO

    typeRich = False
    if b['money'] >= pareto:
        typeRich = True
        
    if typeRich:
        richPerson = {
            'name' : b['username'],
            'money':b['money'], 
            'salary': b['salary'],
            'recommend' : [],
            }
        
        # 예금 상품 리스트 순환
        for j in arr:
            # Serializer로 직렬화 해준다. 
            t1 = DepositProductsSerializer(j)
            # data를 뽑아준다.
            t4 = t1.data
            # t4 안에 options 를 꺼낸다.
            t6 = t4['depositoptions_set']
            # 장기 복리 상품을 담을 리스트 t7
            t7 = []
            # 옵션들을 돌린다
            for k in t6:
                t2 = k["intr_rate_type_nm"]
                if t2 == "복리":
                    # 만기가 24, 36 개월 이라면 (장기 상품)
                    t3 = k["save_trm"]
                    if t3 in [24, 36]:
                        # t7에 옵션 k를 넣는다.
                        t7.append(k)
            # 장기 복리 상품이 들어있다면?
            if t7:
                # t4에 해당되는 옵션들로 바꿔준다 (?)
                t4['depositoptions_set'] = t7
                # 재산 상위 리스트에 추천 상품을 넣어준다.
                richPerson['recommend'] = t4
                # 재산 상위 리스트에 넣어준다.
                result_list.append(richPerson)


    # 재산 중위/하위라면? => 단기 & 적금 상품 추천해주기
    else: 
        poorPerson = {
            'name' : b['username'],
            'money':b['money'], 
            'salary': b['salary'],
            'month_saving' : 0,
            'recommend' : [],
        }
    

        tax_rate = 0.06
        if 14_000_000 <= b['salary'] <= 50_000_000:
            tax_rate = 0.15

        if b['salary'] >= 50_000_000:
            tax_rate = 0.24 

        # 매달 납입할 금액 month_saving
        month_saving = int(b['salary'] * tax_rate / 12 * 0.4)


        k3 = []
        # 적금 상품 순회
        for k in brr : 
            # Serializer로 직렬화 해준다. 
            k1 = SavingProductsSerializer(k)
            # data를 뽑아준다.
            k2 = k1.data


            k4 = k2['max_limit']
            # max_limit 값이 null도 있으므로 -> null 이면 0으로 바꿔주기
            if not k4:
                k2['max_limit'] = 987654321
            # 만약 상품의 최대 납입 금액이 고객이 감당 가능한 month_saving 보다 낮다면 -> 추천해주기
            if k2['max_limit'] <= month_saving:
                k3.append([k2])

        # 추천할 상품이 있다면 
        if k3:
            # 최대 납입 가능 금액을 내림차순으로 정렬해주기 (lambda 함수 내림차순 - )
            sorted_saving_products =  sorted(k3, key=lambda x: -x[0]['max_limit'])
            poorPerson['recommend'] = sorted_saving_products
            poorPerson['month_saving'] = month_saving
            affordable_savings.append(poorPerson)

    msg = '상품 추천을 완료했습니다'
    if not result_list and not affordable_savings:
        result_list = ['자린고비가 될 시간이에요']
        affordable_savings = ['형편에 맞는 상품이 없어요...']
        msg = '추천할 상품이 없습니다'
                
    # a = User.objects.get(username=request.user)
    # b = CustomRegisterSerializer(a)
    # keyword = recommendkeyword1( b['interest'])

    # 재산 상위 출력
    return JsonResponse({
        'forRich': result_list,
        'forPoor': affordable_savings,
        'msg': msg,
        # 'keyword': keyword,  #추천 리스트에 키워드 들어간 예금/적금 상품 넣어줄 것
        }, safe=False) 



@api_view(['GET'])
def recommendkeyword(request, keyword):
    result_list = []
    arr = DepositProducts.objects.all()
    brr = SavingProducts.objects.all()
    
    for a in arr:
        arr1 = DepositProductsSerializer(a).data
        t1 = arr1['fin_prdt_nm']
        if keyword in t1:
            result_list.append(arr1)
    
    for a in brr:
        arr1 = SavingProductsSerializer(a).data
        t1 = arr1['fin_prdt_nm']
        if keyword in t1:
            result_list.append(arr1)

    
    msg = '추천 완료'
    if not result_list:
        msg = 'NO DATA'
    return_data = {
        'data' : result_list,
        'msg' : msg
    }


    return JsonResponse(return_data, safe=False)


# def recommendkeyword1(keyword):
#     result_list = []
#     arr = DepositProducts.objects.all()
#     brr = SavingProducts.objects.all()
    
#     for a in arr:
#         arr1 = DepositProductsSerializer(a).data
#         print(arr1)
#         t1 = arr1['fin_prdt_nm']
#         if keyword in t1:
#             result_list.append(arr1)
    
#     for a in brr:
#         arr1 = SavingProductsSerializer(a).data
#         t1 = arr1['fin_prdt_nm']
#         if keyword in t1:
#             result_list.append(arr1)

    
#     msg = '추천 완료'
#     if not result_list:
#         msg = 'NO DATA'
#     return_data = {
#         'data' : result_list,
#         'msg' : msg
#     }


#     return return_data

@api_view(['GET'])
def pareto(request):
    arr = User.objects.all()

    serialized_data = []
    for user in arr:
        serializer = CustomRegisterSerializer(user)
        serialized_data.append(serializer.data)

    brr = sorted(serialized_data, key=lambda x: -x.get('money'))
    t1 = int(len(brr) * 0.2) - 1
    pareto = brr[t1]['money']
    settings.PARETO = pareto

    return JsonResponse({'msg':'ok'})

