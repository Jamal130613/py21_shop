from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from applications.account.views import ForgotPasswordCompleteView, RegisterApiView, ActivationView, LoginApiView,\
    ChangePasswordView, LogOutApiView, ForgotPasswordView

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('active/<uuid:activation_code>/', ActivationView.as_view()),
    # path('login/', LoginApiView.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
    # path('logout/', LogOutApiView.as_view()),
    path('forgot_password/', ForgotPasswordView.as_view()),
    path('forgot_password_confirm/', ForgotPasswordCompleteView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
