from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    # path('save_dp_prdt/', views.save_dp_prdt, name='save_dp_prdt'),
    # path('save_dp_optn/', views.save_dp_optn, name='save_dp_optn'),
    # path('dp_prdt_lst/', views.dp_prdt_lst, name='dp_prdt_lst'),
    # path('dp_optn_lst/', views.dp_optn_lst, name='dp_optn_lst'),
    # path('save_sv_prdt/', views.save_sv_prdt, name='save_sv_prdt'),
    # path('save_sv_optn/', views.save_sv_optn, name='save_sv_optn'),
    # path('sv_prdt_lst/', views.sv_prdt_lst, name='sv_prdt_lst'),
    # path('sv_optn_lst/', views.sv_optn_lst, name='sv_optn_lst'),
    path('save_data/', views.save_data, name='save_data'),
    path('get_data/', views.get_data, name='get_data'),


    # 알고리즘 테스트 url
    path('test/', views.test),
    path('test1/', views.test1),


    # 추천 알고리즘 적용
    path('recommend/products/', views.recommendproducts),
    path('recommend/keyword/<str:keyword>/', views.recommendkeyword),


    # 유저 정보를 이용하여 pareto를 계산 
    path('caculate/pareto/', views.pareto),
    path('makeuser/user_db/', views.user_db),
]