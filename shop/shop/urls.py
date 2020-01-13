"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from shopapp import views

from django.contrib.auth.views import LoginView, LogoutView

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('shopapp/sign_in/', LoginView.as_view(template_name='shopapp/sign_in.html'), name='shop-sign-in'),
    path('shopapp/sign_out/', LogoutView.as_view(next_page='/'), name='shop-sign-out'),
    path('shopapp/', views.shop_home, name='shop-home'),

    path('shopapp/sign_up', views.shop_sign_up, name='shop-sign-up'),

    path('shopapp/account/', views.shop_account, name='shop-account'),
    path('shopapp/shop/', views.shop_shop, name='shop-shop'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#    path('pizzashop/', views.pizzashop_home, name='pizzashop-home'),

 #   path('pizzashop/sign-up', views.pizzashop_sign_up, name='pizzashop-sign-up'),