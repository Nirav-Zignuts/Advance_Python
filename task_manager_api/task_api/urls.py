from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,TokenVerifyView
from task_api.views import UserAPI,TaskAPI
urlpatterns = [
    path("UserAPI/", UserAPI.as_view(), name="UserAPI"),
    path("UserAPI/<int:pk>/", UserAPI.as_view(), name="UserAPI_id"),
    path("TaskAPI/", TaskAPI.as_view(), name="TaskAPI"),
    path("TaskAPI/<int:pk>/", TaskAPI.as_view(), name="TaskAPI_id"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/token_refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/token_verify/", TokenVerifyView.as_view(), name="token_verify"),
]
