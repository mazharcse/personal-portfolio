from django.shortcuts import render
from blog.models import Post, Comment
from .forms import CommentForm, PostForm
from rest_framework import viewsets
from personal_portfolio.serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.



def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)

def blog_create(request):
    #posts = BlogPost.objects.all()
    print("blog_create_view")
    # print(request.user)
    postForm = PostForm()
    # images = request.FILES.getlist('images')
    if request.method == "POST":
        postForm = PostForm(request.POST)
        #postForm.save()
        # postForm.save()
        # images = request.FILES.getlist('images')
        # print(images)

    if postForm.is_valid():
        print(request.POST)
    #     # post_form = postForm.save(commit=False)
    #     # for image in images:
    #     #     # photo = Image(image=image) #Images.objects.create(image=image, )
    #     #     photo = Image.objects.create(image=image, post = post_form)
    #     #     print(photo)
    #     #     photo.save()
        postForm.save()
        postForm = PostForm()

    my_context = {
        'post_form': postForm,
        # 'images': images
    }

    return render(request, "blog_create.html", my_context)

# def blog_category(request, category):
#     posts = Post.objects.filter(
#         categories__name__contains=category
#     ).order_by(
#         '-created_on'
#     )
#     context = {
#         "category": category,
#         "posts": posts
#     }
#     return render(request, "blog_category.html", context)

def blog_detail_old(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "blog_detail.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog_detail.html", context)

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = (IsAuthenticated,)

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# class PostDetailViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.get(pk=pk)
#     serializer_class = PostSerializer






# def get_(request, car_name):
#     if request.method == 'GET':
#         try:
#             car = Car.objects.get(name=car_name)
#             response = json.dumps([{ 'Car': car.name, 'Top Speed': car.top_speed}])
#         except:
#             response = json.dumps([{ 'Error': 'No car with that name'}])
#     return HttpResponse(response, content_type='text/json')