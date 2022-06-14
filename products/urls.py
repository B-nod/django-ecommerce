from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('test/', views.testFunc),
    path('addproduct/', views.post_product),
    path('addcategory/', views.post_category),
    path('updateproduct/<int:product_id>', views.update_product),
    path('deleteproduct/<int:product_id>', views.delete_product),
    path('category/', views.show_category),
    path('updatecategory/<int:category_id>',views.update_category),
    path('deletecategory/<int:category_id>',views.delete_category),
    path('add_to_cart/<int:product_id>',views.add_to_cart),
    path('mycart',views.show_cart_item),
    path('deletecartitems/<int:cart_id>', views.remove_cart_item),
    path('orderitemform/<int:product_id>/<int:cart_id>', views.order_item_form),
    path('esewa_verify',views.esewa_verify),
    path('my_order',views.my_order),
    path('allorder',views.all_order),
]