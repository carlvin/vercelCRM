# config/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView,
    PasswordResetDoneView, PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from client_relationship_manager.views import SignupView

# Base URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('client_relationship_manager.urls', namespace='crm')),
    path('agents/', include('agents.urls', namespace='agents')),
    path('inventory/', include('inventory.urls', namespace='inventory')),
    
    # Authentication URLs
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    
    # Password Reset URLs
    path('reset-password/', PasswordResetView.as_view(), name='reset_password'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', 
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', 
         PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

# Debug configuration
if settings.DEBUG:
    # try:
        # Debug Toolbar URLs - Add these first
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    # except ImportError:
    #     pass
    
    # Static and Media URLs - Add these last
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import path,include
# from django.contrib.auth.views import (
#     LoginView,LogoutView,PasswordResetView,
#     PasswordResetDoneView,PasswordResetConfirmView,
#     PasswordResetCompleteView,
#     )
# from client_relationship_manager.views import SignupView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',include('client_relationship_manager.urls',namespace='crm')),
#     path('agents/',include('agents.urls',namespace='agents')),
#     path('inventory/',include('inventory.urls',namespace='inventory')),
        
#     path('login/',LoginView.as_view(),name='login'),
#     path('logout/',LogoutView.as_view(),name='logout'),
#     path('signup/',SignupView.as_view(),name='signup'),    
#     path('reset-password/',PasswordResetView.as_view(),name='reset_password'),
#     path('password-reset-done/',PasswordResetDoneView.as_view(),name='password_reset_done'),
#     path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),    
#     path('password-reset-complete/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),    
    
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns