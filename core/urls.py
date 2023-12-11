from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reserva.urls')),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'registration/password-reset-form.html'), name = 'reset_password'),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(template_name = 'registration/password-reset-done.html'), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'registration/password-reset-confirm.html', success_url=reverse_lazy('login')), name = 'password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name = 'password_reset_complete'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
