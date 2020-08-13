from django.urls import path
from dp15app import views
app_name="dp15app"

urlpatterns = [
    path('trail/',views.trial,name="Trial"),
    path('profile/',views.profile,name="profile"),
    path('get_demo/',views.get_demo,name="get_demo"),
    path('post_demo/',views.post_demo,name="post_demo"),
    path('register/',views.register,name="register"),
    path('multi/',views.multiplesel,name="multi"),
    path('imgupld/',views.imgupld,name="imgupld"),
    path('imgdisp/',views.imgdisl,name="imgdisplay"),
]