from django.urls import path


from users.views.sign_up import SignUpView
from users.views.sign_in import SignInView
from users.views.token import TokenView
from users.views.user import UserUpdateView


urlpatterns = [
    path('update/', UserUpdateView.as_view(), name='sign-up'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('refresh/', TokenView.as_view(), name='token'),
]
