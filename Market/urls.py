from django.urls import path

from . import views


urlpatterns = [
    path('product-category-l/', views.ProductCategoryListAPIView.as_view(), name = 'product_category_l'),
    path('transaction-l/<int:organization>', views.TransactionListAPIView.as_view(), name = 'transaction_l'),

    path('product-l/<int:organization>/', views.ProductListAPIView.as_view(), name = 'product_l'),
    path('product-r/<int:id>/<int:organization>/', views.ProductRetrieveAPIView.as_view(), name = 'product_r'),
    path('product-c/', views.ProductCreateAPIView.as_view(), name = 'product_c'),
    path('product-ud/<int:organization>/', views.ProductUpdateDestroyAPIView.as_view(), name = 'product_ud'),

    path('cashbox-l/<int:organization>/', views.CashboxListAPIView.as_view(), name = 'cashbox_l'),
    path('cashbox-r/<int:id>/<int:organization>/', views.CashboxRetrieveAPIView.as_view(), name = 'cashbox_r'),
    path('cashbox-c/', views.CashboxCreateAPIView.as_view(), name = 'cashbox_c'),
    path('cashbox-ud/<int:id>/<int:organization>/', views.CashboxUpdateDestroyAPIView.as_view(), name = 'cashbox_ud'),

    path('purchase-request-l/<int:organization>/', views.PurchaseRequestListAPIView.as_view(), name = 'purchase_request_l'),
    path('purchase-request-r/<int:id>/<int:organization>/', views.PurchaseRequestRetrieveAPIView.as_view(), name = 'purchase_request_r'),
    path('purchase-request-c/', views.PurchaseRequestCreateAPIView.as_view(), name = 'purchase_request_c'),
    path('purchase-request-ud/<int:id>/<int:organization>/', views.PurchaseRequestUpdateDestroyAPIView.as_view(), name = 'purchase_request_ud'),

    path('purchase-accept-l/<int:organization>/', views.PurchaseAcceptListAPIView, name = 'purchase_l'),
    path('purchase-accept-r/<int:id>/<int:organization>/', views.PurchaseAcceptRetrieveAPIView, name = 'purchase_r'),
    path('purchase-accept-u/<int:id>/<int:organization>/', views.PurchaseAcceptUpdateAPIView, name = 'purchase_u'),

    path('sale-product-l/<int:organization>/', views.SaleProductListAPIView.as_view(), name = 'sale_product_l'),
    path('sale-product-r/<int:id>/<int:organization>/', views.SaleProductRetrieveAPIView.as_view(), name = 'sale_product_r'),
    path('sale-product-c/', views.SaleProductCreateAPIView.as_view(), name = 'sale_product_c'),
    path('sale-product-ud/<int:id>/<int:organization>/', views.SaleProductUpdateDestroyAPIView.as_view(), name = 'sale_product_ud'),

    path('sale-order-l/<int:organization>/', views.SaleOrderListAPIView.as_view(), name = 'sale_order_l'),
    path('sale-order-r/<int:id>/<int:organization>/', views.SaleOrderRetrieveAPIView.as_view(), name = 'sale_order_r'),
    path('sale-order-c/', views.SaleOrderCreateAPIView.as_view(), name = 'sale_order_c'),
    path('sale-order-ud/<int:id>/<int:organization>/', views.SaleOrderUpdateDestroyAPIView.as_view(), name = 'sale_order_ud'),

    path('work-done-l/<int:organization>/', views.WorkDoneListAPIView.as_view(), name = 'work_done_l'),
    path('work-done-r/<int:id>/<int:organization>/', views.WorkDoneRetrieveAPIView.as_view(), name = 'work_done_r'),
    path('work-done-c/', views.WorkDoneCreateAPIView.as_view(), name = 'work_done_c'),
    path('work-done-ud/<int:id>/<int:organization>/', views.WorkDoneUpdateDestroyAPIView.as_view(), name = 'work_done_ud'),

    path('product-order-l/<int:organization>/', views.ProductOrderListAPIView.as_view(), name = 'product_order_l'),
    path('product-order-r/<int:id>/<int:organization>/', views.ProductOrderRetrieveAPIView.as_view(), name = 'product_order_r'),
    path('product-order-c/', views.ProductOrderCreateAPIView.as_view(), name = 'product_order_c'),
    path('product-order-ud/<int:id>/<int:organization>/', views.ProductOrderUpdateDestroyAPIView.as_view(), name = 'product_order_ud'),
]
