from django.urls import path
from . import views


urlpatterns = [
    path("", views.login_view, name="login"),
    path("history/", views.history_view, name="history"),
    path("manual/", views.manual_view, name="manual"),
    path("logout/", views.logout_view, name="logout"),
    path("search/", views.search_view, name="search"),
    path("quote_detail/<slug:slug>", views.quote_detail, name="quote_detail"),
    path("current_offer/", views.current_offer, name="current_offer"),
    path("quote_create/", views.quote_create_view, name="quote_create_view"),
    path("quote_item_add/<slug:slug>", views.quote_item_add, name="quoteitem_add"),
]
