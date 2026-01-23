from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [  
    # path("", views.index, name = "index"),
    # http://27.0.0.1:8000/polls/
    # (도메인주소, views로 부터 함수 또는 클래스 호출, 템플릿 이름 = html에서 호출될 이름)
    

    # FBV 기반
    # path("<int:question_id>/", views.detail, name="detail"),
    # path("<int:question_id>/results/", views.results, name="results"),
    # path("<int:question_id>/vote/", views.vote, name="vote"), 
    # path("aa/", views.aa, name = "aa"),


    # CBV 기반
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),


    # CRUD 기반
    path("create/", views.QuestionCreateView.as_view(), name="question_create"),
    # http://27.0.0.1:8000/polls/create/
    # generic에 CreateView를 상속받아서 Class(글 생성 기능) 구현
    # URL polls:question_create 탬플릿(HTML)에서 링크 형태로 호출

    path("<int:pk>/update/", views.QuestionUpdateView.as_view(), name="question_update"),
    # http://27.0.0.1:8000/polls/id/update/
    # generic에 UpdateView를 상속받아서 Class(글 수정 기능) 구현
    # URL polls:question_update 템플릿(HTML)에서 링크 형태로 호출

    path("<int:pk>/delete", views.QuestionDeleteView.as_view(), name="question_delete"),
    # http://27.0.0.1:8000/polls/id/delete/
    # generic에 UpdateView를 상속받아서 Class(글 삭제 기능) 구현
    # URL polls:question_delete 템플릿(HTML)에서 링크 형태로 호출
    
]