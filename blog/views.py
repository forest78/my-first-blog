from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts': posts})    # request:사용자가 요청하는 모든것, 요청을 넘겨받아 render메서드를 호출합니다. 이 함수는 render메서드를 호출하여 받은 blog/post_list.html템플릿을 보여줌

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
    
