from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.login_view, name="login"),
    path("history/", views.history_view, name="history"),
    path("manual/", views.manual_view, name="manual"),
    path("logout/", views.logout_view, name="logout"),
]
