from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html',{})    # 요청을 넘겨받아 render메서드를 호출합니다. 이 함수는 render메서드를 호출하여 받은 blog/post_list.html템플릿을 보여줌
