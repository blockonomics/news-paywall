from django.urls import path
from . import views

app_name = 'NewsArticle'

urlpatterns = [
    path('', views.free_news, name='free_news'),
    path('premium-news', views.premium_news, name='premium_news'),
    path('read-more/<pk>', views.read_more, name='read_more'),
    path('payment-webhook', views.payment_webhook, name='payment_webhook'),
    path('cancel-payment/<pk>', views.cancel_payment, name='cancel_payment')
]
