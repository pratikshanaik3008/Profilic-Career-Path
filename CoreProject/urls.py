from django.contrib import admin
from django.urls import path
from quiz.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),  # Remove the trailing slash from the name parameter
    path('signin/', signin, name="signin"),
    path('signup/', signup, name="signup"),
    path('quiz/', quiz, name="quiz"),
    path('stream/', stream, name="stream"),
    path('result/', result, name="result"),
    path('index/', index, name="index"),  # Remove the trailing slash from the name parameter
    path('eng', eng, name="eng"),
    path('about/', about, name="about"),
    path('profile/', profile, name="profile"),
    path('home/', home, name="home"),
    path('logout/', logout_user, name="logout_user"),
    path('removeuser/', removeuser, name="removeuser"),
    path('profile_view/',profile_view,name="profile_view"),
    path('userlist/', userlist, name="userlist"),
    path('choose/', choose, name="choose"),
    path('arts/', arts, name="arts"),
    path('commerce/', commerce, name="commerce"),
    path('medical/', medical, name="medical"),
    path('science/', science, name="science"),
    path('artsdisplay/', artsdisplay, name="artsdisplay"),
    path('commercedisplay/', commercedisplay, name="commercedisplay"),
    path('sciencedisplay/', sciencedisplay, name="sciencedisplay"),
    path('artsresult/', artsresult, name="artsresult"),
    path('commerceresult/', commerceresult, name="commerceresult"),
    path('scienceresult/',scienceresult, name="scienceresult"),
    path('other/', other, name="other"),
    path('<int:pk>/remove/',remove, name='remove'),
    path('personalitytest/', personalitytest, name="personalitytest"),
    path('personalitytestresult/', personalitytestresult, name="personalitytestresult"),
]

