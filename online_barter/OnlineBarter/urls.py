from django.contrib import admin
from django.urls import path


from OnlineBarter.views import registeraccount
from OnlineBarter.views import loginaccount
from OnlineBarter.views import updateprofile
from OnlineBarter.views import cart
from OnlineBarter.views import exchange
from OnlineBarter.views import favourite
from OnlineBarter.views import index
from OnlineBarter.views import message
from OnlineBarter.views import detail
from OnlineBarter.views import product
from OnlineBarter.views import profile
from OnlineBarter.views import itemform
from OnlineBarter.views import itemlist

from django.contrib.auth import views as auth_views
from OnlineBarter import views

urlpatterns = [
    
    path('LoginAccount/',auth_views.LoginView.as_view(template_name='code/login.html'),name='loginaccount'),
    path('ResgisterAccount/',registeraccount,name='registeraccount'),
    path('UpdateProfile/',updateprofile,name='updateprofile'),
    path('CartAccount/',cart,name='cart'),
    path('ExchangeItem/',exchange,name='exchange'),
    path('FavouriteAccount/',favourite,name='favourite'),
    path('HomePage/',index,name='index'),
    path('InboxAccount/',message,name='message'),
    path('ProductDetail/',detail,name='detail'),
    path('MarketProduct/',product,name='product'),
    path('ProfileAccount/',profile,name='profile'),
]