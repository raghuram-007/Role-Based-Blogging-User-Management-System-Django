# blogs/views.py

from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required

from .models import Category, Post


@login_required
def create_post(request):
    # Only doctors can create posts
    if request.user.user_type != 'doctor':
        return redirect('patient_posts')  # redirect patients to view posts

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # assign current user as author
            post.save()
            return redirect('my_posts')
    else:
        form = PostForm()

    return render(request, 'blogs/create_post.html', {'form': form})


@login_required
def my_posts(request):
    # Only show posts by the logged-in doctor
    posts = Post.objects.filter(author=request.user)
    return render(request, 'blogs/my_posts.html', {'posts': posts})


def patient_posts(request):
    # Patients can view all published posts categorized
    categories = Category.objects.all()
    category_posts = {}
    for category in categories:
        posts = Post.objects.filter(category=category, status='published')
        category_posts[category] = posts
    return render(request, 'blogs/patient_posts.html', {'category_posts': category_posts})



