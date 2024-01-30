from django.urls import path
from .views import delete_product, update_product, delete_customer, update_customer, create_customer, create_product, delete_orderapp, update_orderapp, create_orderapp
from . import views

urlpatterns = [
    path ('', views.home_page, name="homepage"),
    path ('home/', views.home_page, name="homepage"),
    path ('dashboard/', views.dash_board, name="dashboard"),
    path ('productsadmin/', views.product_admin, name="productadmin"),
    path ('create_customer/', create_customer, name='create_customer'),
    path ('create_product/', create_product, name='create_product'),
    path ('create_orderapp/', create_orderapp, name='create_orderapp'),
    path ('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path ('delete_customer/<int:customer_id>/', delete_customer, name='delete_customer'),
    path ('delete_orderapp/<int:approve_id>/', delete_orderapp, name='delete_orderapp'),
    path ('update_orderapp/<int:pk>/', update_orderapp, name='update_orderapp'),
    path ('update/<int:pk>/', update_product, name='update_product'),
    path ('update_customer/<int:customer_id>/', update_customer, name='update_customer'),
    path ('approvals/', views.approvals_page, name="approvalspage"),
    path ('registercustomer/', views.register_customer, name="regiscusto"),
    path ('about/', views.about_page, name="aboutpage"),
    path ('products/', views.product_page, name="productpage"),
    path ('order/', views.orders_page, name="orderspage"),
    path ('add_shippadd/', views.shipping_add, name='shipping_add'),


]
