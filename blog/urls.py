from django.urls import path, include
from .views import blog_index, blog_detail, blog_create,  PostViewSet, CommentViewSet #, PostDetailViewSet
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register("", PostViewSet)
router.register("comments", CommentViewSet)

urlpatterns = [
    path("", blog_index, name = "blog_index"),
    path("blog_create/", blog_create, name = "blog_create"),
    path("<int:pk>/", blog_detail, name = "blog_detail"),
    # # path("<category>/", blog_category, name="blog_category"),
    # # path("blog_api/", include('rest_framework.urls', namespace='rest_framework'), name="blog_api"),
    # path('create_post_api/', PostViewSet.as_view({"post": "create"}), name='create_post_api'),
    # path("blogapi", PostViewSet.as_view({"get": "list"}), name='get_list_api'),
    # path("blogapi2", PostViewSet, name='get_list_api2'),
    # path("blogapi/<int:pk>/", PostViewSet.as_view({"get": "list"}), name="blog_detail"),
    #path('get_detail_api/', PostViewSet.as_view(), name='get_detail_api'),
    path("blogapi/", include(router.urls)),
    path("api/token/", jwt_views.TokenObtainPairView.as_view(), name = "token_obtain_pair"),
    path("api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name = "token_refresh"),
]