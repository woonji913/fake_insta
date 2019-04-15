from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Post, Image
from .forms import PostForm, ImageForm

# Create your views here.
def list(request):  # index임
    posts = get_list_or_404(Post.objects.order_by('-pk'))
    form = PostForm()
    context = {'posts':posts,}
    return render(request, 'posts/list.html', context)

@require_POST
@login_required
def create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False) # 게시글 내용 처리 끝
            post.user = request.user
            post.save()
            # 이미지 여러장 받기
            for image in request.FILES.getlist('file'):
                request.FILES['file'] = image
                image_form = ImageForm(files=request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.post = post
                    image.save()
            return redirect('posts:list')
            
    else:
        post_form = PostForm()
        image_form = ImageForm()
    context = {
        'post_form':post_form,
        'image_form': image_form,
    }
    return render(request, 'posts/form.html', context)

# def read(request, post_pk):
#     post = get_object_or_404(Post, pk=post_pk)
#     context = {
#         'post':post,
#     }
#     return render(request, 'posts/read.html', post.pk)

@login_required
def update(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    
    if post.user != request.user:
        return redirect('posts:list')
        
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post) 
        if post_form.is_valid():
            post_form.save() 
            return redirect('posts:list')
    else:
        post_form = PostForm(instance=post)
    
    context = {
        'post_form': post_form,
        'post': post,
    }
    return render(request, 'posts/form.html', context)

@login_required
def delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if post.user != request.user:
        return redirect('posts:list')
        
    if request.method == 'POST':
        post.delete()
        return redirect('posts:list')
    else:
        return redirect('posts:list')
        
    