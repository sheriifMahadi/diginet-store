from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('store/', views.vendor_store, name='vendor_store'),
    path('store/add-product/', views.add_product, name='add_product'),
    path('store/edit-product/<int:pk>/', views.edit_product, name='edit_product'),
    path('store/delete-product/<int:pk>/', views.delete_product, name='delete_product'),
    path('vendors/<int:pk>/', views.vendor_detail, name='vendor_detail')

]
