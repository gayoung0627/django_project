from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('kbouniform', views.kbouniform, name='kbouniform'),
    path('mypage', views.mypage, name='mypage'),
    path('product_list/', views.ProductList.as_view(), name='product_list'),
    path('product_list/<int:pk>/', views.ProductDetail.as_view(),  name='detail'),
    path('product_list/category/<str:slug>/', views.category_page),
    path('product_list/manufacturer/<str:slug>/', views.manufacturer_page),
    path('product_list/<int:pk>/new_comment/', views.new_comment),
    path('product_list/update_comment/<int:pk>/', views.CommentUpdate.as_view()),
    path('product_list/delete_comment/<int:pk>/', views.delete_comment),
    path('product_list/tag/<str:slug>/', views.tag_page),
    path('product_list/create_product/', views.ProductCreate.as_view()),
    path('product_list/update_product/<int:pk>/', views.ProductUpdate.as_view()),
    path('product_list/search/<str:q>/', views.ProductSearch.as_view()),
    ]