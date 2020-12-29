"""online_barter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


from OnlineBarter.views import loginaccount
from OnlineBarter.views import registeraccount
from OnlineBarter.views import logoutaccount
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
    path('admin/', admin.site.urls),
    path('LoginAccount/',auth_views.LoginView.as_view(template_name='code/login.html'),name='loginaccount'),
    path('ResgisterAccount/',registeraccount,name='registeraccount'),
    path('LogoutAccount/',logoutaccount,name='logoutaccount'),
    path('UpdateProfile/',updateprofile,name='updateprofile'),
    path('CartAccount/',cart,name='cart'),
    path('ExchangeItem/',exchange,name='exchange'),
    path('FavouriteAccount/',favourite,name='favourite'),
    path('HomePage/',index,name='index'),
    path('InboxAccount/',message,name='message'),
    path('ProductDetail/',detail,name='detail'),
    path('MarketProduct/',product,name='product'),
    path('ProfileAccount/',profile,name='profile'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='code/password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='code/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='code/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='code/password_reset_complete.html'),name='password_reset_complete'),
    path('',include('OnlineBarter.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
