from django.urls import include, path
# from .views import UserProfileImageUpload

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/register/', include('rest_auth.registration.urls')),
    # path('admin/create/', UserProfileImageUpload.as_view(), name='createuser'),
]
