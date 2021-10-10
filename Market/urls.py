from django.urls import path

from . import views


urlpatterns = [
    path('product-category-l/', views.ProductCategoryListAPIView.as_view(), name = 'product_category_l'),

    path('product-l/<int:organization>/', views.ProductListAPIView.as_view(), name = 'product_l'),
    path('product-r/<int:id>/<int:organization>/', views.ProductRetrieveAPIView.as_view(), name = 'product_r'),
    path('product-c/', views.ProductCreateAPIView.as_view(), name = 'product_c'),
    path('product-ud/<int:organization>/', views.ProductUpdateDestroyAPIView.as_view(), name = 'product_ud'),

    path('cashbox-l/<int:organization>/', views.CashboxListAPIView.as_view(), name = 'cashbox_l'),
    path('cashbox-r/<int:id>/<int:organization>/', views.CashboxRetrieveAPIView.as_view(), name = 'cashbox_r'),
    path('cashbox-c/', views.CashboxCreateAPIView.as_view(), name = 'cashbox_c'),
    path('cashbox-ud/<int:id>/<int:organization>/', views.CashboxUpdateDestroyAPIView.as_view(), name = 'cashbox_ud'),

    path('purchase-l/<int:organization>/', views.PurchaseListAPIView.as_view(), name = 'purchase_l'),
    path('purchase-r/<int:id>/<int:organization>/', views.PurchaseRetrieveAPIView.as_view(), name = 'purchase_r'),
    path('purchase-c/', views.PurchaseCreateAPIView.as_view(), name = 'purchase_c'),
    path('purchase-ud/<int:id>/<int:organization>/', views.PurchaseUpdateDestroyAPIView.as_view(), name = 'purchase_ud'),

    path('sale-l/<int:organization>/', views.SaleListAPIView.as_view(), name = 'sale_l'),
    path('sale-r/<int:id>/<int:organization>/', views.SaleRetrieveAPIView.as_view(), name = 'sale_r'),
    path('sale-c/', views.SaleCreateAPIView.as_view(), name = 'sale_c'),
    path('sale-ud/<int:id>/<int:organization>/', views.SaleUpdateDestroyAPIView.as_view(), name = 'sale_ud'),

    path('work-done-l/<int:organization>/', views.WorkDoneListAPIView.as_view(), name = 'work_done_l'),
    path('work-done-r/<int:id>/<int:organization>/', views.WorkDoneRetrieveAPIView.as_view(), name = 'work_done_r'),
    path('work-done-c/', views.WorkDoneCreateAPIView.as_view(), name = 'work_done_c'),
    path('work-done-ud/<int:id>/<int:organization>/', views.WorkDoneUpdateDestroyAPIView.as_view(), name = 'work_done_ud'),

    path('product-order-l/<int:organization>/', views.ProductOrderListAPIView.as_view(), name = 'product_order_l'),
    path('product-order-r/<int:id>/<int:organization>/', views.ProductOrderRetrieveAPIView.as_view(), name = 'product_order_r'),
    path('product-order-c/', views.ProductOrderCreateAPIView.as_view(), name = 'product_order_c'),
    path('product-order-ud/<int:id>/<int:organization>/', views.ProductOrderUpdateDestroyAPIView.as_view(), name = 'product_order_ud'),
]
