from django.urls import path
from . import views #장고 함수 paht와 blog앱에서 사용할 모든 views가져오기

urlpatterns = [
    path('', views.post_list, name='post_list'),    #post_list라는 view가 루트 URL에 할당
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  #post/<int:pk/>/는 URL 패턴 > url이 post문자를 포함, 정수값이 pk라는 변수로 뷰에 전송
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name="post_draft_list"),
    path('post/<pk>/puslish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<pk>)/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<pk>/remove/', views.comment_remove, name='comment_remove'),
]
