
from django.shortcuts import render
from django.http import  HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    #if the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        #if the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()

            #Redirect to home
            return HttpResponseRedirect('/')

        else:
            # No, Show Error
            return HttpResponseRedirect(form.errors.as_json)

    posts = Post.objects.all()[:20]
    return render(request, 'posts.html',  
                    {'posts': posts})

def edit(request, post_id):
    #if the method is POST
    posts = Post.objects.get(id = post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance = posts)
        #if the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()

            #Redirect to home
            return HttpResponseRedirect('/')

        else:
            # No, Show Error
            return HttpResponseRedirect(form.errors.as_json)



    # Get all post limit = 20
   
  
    return render(request, 'edit.html',  
                    {'posts': posts})

def delete(request, post_id):
    #find post
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')

def like(request, post_id):
    post = Post.objects.get(id = post_id)
    new_value = post.likes + 1
    post.likes = new_value
    post.save()
    return HttpResponseRedirect('/')