from django.shortcuts import render, get_object_or_404 # html에 데이터를 불러주기 위함
from django.http import HttpResponse # http와 연동하기 위해서 필요
from .models import Question, Choice # models.py에서 불러옴 -> view.py(매개체) -> detail.html/index.html 에서 구현
from django.views import generic
from django.db.models import F
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

# index(최신글 list)
# def index(request):
# 	# return HttpResponse("Hello) 기존코드
# 	latest_question_list = Question.objects.order_by("-pub_date")[:5]
# 	context = {"latest_question_list": latest_question_list}
# 	return render(request, "polls/index.html", context)

class IndexView(generic.ListView): # 일반적으로 .이 붙어있으면 상속됐다는 의미로 이해
    template_name = "polls/index.html" # 이동할 위치
    context_object_name = "latest_question_list" 

    def get_queryset(self):
        return Question.objects.filter (pub_date__lte=timezone.now()).order_by("-pub_date")[:5]




# def detail(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, "polls/detail.html", {"question": question})

class DetailView(generic.DetailView):
    model = Question # get_queryset으로 데이터를 참조하지 않아서 model로 선언해줌
    template_name = "polls/detail.html"
    def get_queryset(self):
        """
        미래에 게시될 질문은 제외합니다.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())



# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    context_object_name = "question"





# def vote(request, question_id):
#     return HttpResponse(f"You're voting on question {question_id}.")

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message":"You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1 #.으로 상속하지 않았다면 로직 안에서 호출됐다고 추론해야 함
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))




# # aa 함수 데이터
# def aa(request):
#     # 1. 모델에서 데이터 불러오기
#     choice_list = Choice.objects.all()
#     lastest_question_list = Question.objects.all()
#     # 2. 불러온 데이터를 html에 출력하기
#     # -데이터 형식을 딕셔너리 데이터로 받아야 한다. json 형식과 비슷하다. (같은 형식으로 민들기가 편하기 떄문에)
#     context = {"latest_question_list": lastest_question_list, 
#                "choice_list": choice_list,
#     } # 딕셔너리데이터 호출 방법: 키를 부르면 값이 나온다.
#     # 3. html에 context를 넘겨주기
#     return render(request, 'polls/aa.html', context)

