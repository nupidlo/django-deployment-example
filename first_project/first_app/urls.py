from django.urls import path
from . import views


# TEMPLATE TAGGING
app_name = 'first_app'

urlpatterns = [
    path('', views.index, name="index"),
    path('gallery/', views.gallery, name="gallery"),
    path('acc_recs/', views.acc_recs, name="acc_recs"),
    path('formpage/', views.form_name_view, name="form_name"),
    path('relative/', views.relative, name="relative"),
    path('other/', views.other, name="other"),
    path('ind/', views.ind, name="ind"),
    path('register/', views.register, name="register"),
    path('logout/', views.user_logout, name="logout"),
    path('special/', views.special, name="special"),
    path('user_login', views.user_login, name="user_login"),
]
