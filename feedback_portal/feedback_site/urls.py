from django.urls import path,include
from rest_framework import routers
from . import views
from .views import FeedbackViewSet
router = routers.DefaultRouter()

router.register(r'feedbacks', FeedbackViewSet)

urlpatterns = [
    path("index", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_feedback, name='create'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
