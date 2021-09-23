from django.urls import include, path
from checkout.views import GetInfoView

app_name = "checkout"

urlpatterns = [
    path("info/", GetInfoView.as_view(), name="info"),
]
