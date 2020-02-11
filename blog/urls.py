from django.urls import path
from . import views #장고 함수 paht와 blog앱에서 사용할 모든 views가져오기

urlpatterns = [
    path('', views.post_list, name='post_list'),    #post_list라는 view가 루트 URL에 할당
]
