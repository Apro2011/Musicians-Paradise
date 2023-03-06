from django.urls import path
from mysite import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('', MusicianListView.as_view(), name="Musician"),
    path('guitar_blog/<int:pk>/', MusicianDetailView.as_view(), name="blog_detail"),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', LogInView.as_view(), name="login"),
    path('logout/', LogOutView.as_view(), name="logout"),
    path('guitar_blog/create_musician/', MusicianCreationView.as_view(), name="create_musician"),
    path('likes/', post_likes, name="post_likes"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)