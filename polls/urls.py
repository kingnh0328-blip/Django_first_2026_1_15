from django.urls import path
from . import views, practice_views

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
    
    # 연습용 (브라우저 확인)
    path("practice/1/", practice_views.practice_1, name="practice_1"),
    path("practice/2/", practice_views.practice_2, name="practice_2"),
    path("practice/3/", practice_views.practice_3, name="pracitce_3"),
    path("practice/4/", practice_views.practice_4, name="practice_4"),
    path("practice/5/", practice_views.practice_5, name="practice_5"),

    # 연습용 (플랫폼 확인: JSON)
    path("practice/api/1/", practice_views.practice_api_1, name="practice_api_1"),
    path("practice/api/2/", practice_views.practice_api_2, name="practice_api_2"),
    path("practice/api/3/", practice_views.practice_api_3, name="practice_api_3"),
    path("practice/api/4/", practice_views.practice_api_4, name="practice_api_4"),
    path("practice/api/5/", practice_views.practice_api_5, name="practice_api_5"),
]