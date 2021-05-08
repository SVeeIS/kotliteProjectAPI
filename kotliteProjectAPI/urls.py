# """kotliteProjectAPI URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.documentation import include_docs_urls
# from rest_framework.authtoken.views import obtain_auth_token

# urlpatterns = [
#     path('docs/', include_docs_urls(title='Kotlite Api')),
#     path('admin/', admin.site.urls),
#     path('users/api/', include("users.urls")),
#     path('passengers/api/', include("passengers.urls")),
#     path('drivers/api/', include("drivers.urls")),
#     path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
# ]

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken.views import obtain_auth_token

from drivers import views
drivers_router = routers.DefaultRouter()
drivers_router.register(r'order', views.orderViewSet)
drivers_router.register(r'finding_driver', views.finding_driverViewSet)

from passengers import views
passengers_router = routers.DefaultRouter()
passengers_router.register(r'request', views.requestViewSet)
passengers_router.register(r'transaction', views.transactionViewSet)

from users import views
router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)

urlpatterns = [
    path('docs/', include_docs_urls(title='Kotlite Api')),
    path('', include(router.urls)),
    path('drivers/', include(drivers_router.urls)),
    path('passengers/', include(passengers_router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]