from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret! 
# 장고키-라이센스, 설치할 때 마다 다른 키가 생성됨
# .env 파일로 원본 시크릿 키 옮기고 settings.py로 불러오기
SECRET_KEY = (
    os.environ.get("DJANGO_SECRET_KEY")
    or os.environ.get("SECRET_KEY")
    or "ci-dev-secret-key"
    )

DEBUG = os.environ.get("DEBUG", "0") == "1"
              
              

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls.apps.PollsConfig',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [ # UI 화면 설계 세팅
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [BASE_DIR / "templates"],   # ✅ 공통 템플릿 폴더(templates 경로가 변경되었기 떄문)
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3', # 개발을 위한 DB
#     }
# }

DATABASES = {
   "default": dj_database_url.config(
        default=(
            os.environ.get("DATABASE_URL")
            or f"postgresql://{os.environ.get('POSTGRES_USER','django_user')}:"
               f"{os.environ.get('POSTGRES_PASSWORD','strong-password')}@"
               f"{os.environ.get('POSTGRES_HOST','127.0.0.1')}:"
               f"{os.environ.get('POSTGRES_PORT','5432')}/"
               f"{os.environ.get('POSTGRES_DB','django_first2_db')}"
        ),
        conn_max_age=600,
        ssl_require=bool(os.environ.get("DATABASE_URL")),  # Fly에서만 SSL 강제
    )
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static", # ✅ 공통 static 폴더(static 파일 경로가 변경되었기 때문)
]

STATIC_ROOT = BASE_DIR / "staticfiles"

LOGIN_REDIRECT_URL = "polls:index"   # 로그인 성공 후 polls 홈으로
LOGOUT_REDIRECT_URL = "polls:index"  # 로그아웃 후 polls 홈으로 (원하면)

ALLOWED_HOSTS = ["django-first-quiet-pine-2575.fly.dev", "localhost", "127.0.0.1"]
CSRF_TRUSTED_ORIGINS = ["https://django-first-quiet-pine-2575.fly.dev"]
