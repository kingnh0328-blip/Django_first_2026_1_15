from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("polls/", include("polls.urls")), 
    # http://127.0.0.1:8000/polls/
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/admin/
    path("accounts/", include("accounts.urls")),
    # http://127.0.0.1:8000/accounts/
    path("accounts/", include("django.contrib.auth.urls")),
    path('', RedirectView.as_view(url='/polls/', permanent=False)),
]

