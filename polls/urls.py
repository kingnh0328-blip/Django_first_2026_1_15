from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [  
    # path("", views.index, name = "index"),
    # # http://27.0.0.1:8000/polls/
    # # (도메인주소, views로 부터 함수 또는 클래스 호출, 템플릿 이름 = html에서 호출될 이름)
    # # FBV 기반

    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),

    # path("<int:question_id>/", views.detail, name="detail"),
    # path("<int:question_id>/results/", views.results, name="results"),
    # path("<int:question_id>/vote/", views.vote, name="vote"), 
    # path("aa/", views.aa, name = "aa"),
]