# 회원가입 코드 뼈대는 원래 이렇게 작성해줘야 함!!!
# 코드를 읽고 해석 가능한 정도로만 이해하기
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# signup 함수
# - 회원가입을 처리하는 함수형 뷰
# - POST / GET 요청을 분기 처리
    
# POST 요청
# - 사용자가 입력한 데이터 검증
# - 정상일 경우 사용자 계정 생성 후 로그인 페이지 이동
    
# GET 요청
# - 빈 회원가입 폼을 화면에 표시

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("login"))
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})
