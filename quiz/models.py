from django.db import models
from django.contrib.auth.models import User

class QuestionBank(models.Model):
    question = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=64, verbose_name='Option A')
    option_2 = models.CharField(max_length=64, verbose_name='Option B')
    option_3 = models.CharField(max_length=64, verbose_name='Option C')

    answer = models.CharField(max_length = 255, verbose_name='Answer')
    def __str__(self):
        return self.question

class artsque(models.Model):
    question = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=64, verbose_name='Option A')
    option_2 = models.CharField(max_length=64, verbose_name='Option B')
    option_3 = models.CharField(max_length=64, verbose_name='Option C')

    answer = models.CharField(max_length = 255, verbose_name='Answer')
    def __str__(self):
        return self.question

class commerceque(models.Model):
    question = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=64, verbose_name='Option A')
    option_2 = models.CharField(max_length=64, verbose_name='Option B')
    option_3 = models.CharField(max_length=64, verbose_name='Option C')

    answer = models.CharField(max_length = 255, verbose_name='Answer')
    def __str__(self):
        return self.question

class scienceque(models.Model):
    question = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=64, verbose_name='Option A')
    option_2 = models.CharField(max_length=64, verbose_name='Option B')
    option_3 = models.CharField(max_length=64, verbose_name='Option C')

    answer = models.CharField(max_length = 255, verbose_name='Answer')
    def __str__(self):
        return self.question

class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    answer_1 = models.CharField(max_length=50)
    answer_2 = models.CharField(max_length=50)
    answer_3 = models.CharField(max_length=50)
    answer_4 = models.CharField(max_length=50)
    answer_5 = models.CharField(max_length=50)
    answer_6 = models.CharField(max_length=50)
    answer_7 = models.CharField(max_length=50)
    answer_8 = models.CharField(max_length=50)
    answer_9 = models.CharField(max_length=50)
    answer_10 = models.CharField(max_length=50)
    answer_11 = models.CharField(max_length=50)
    answer_12 = models.CharField(max_length=50)
    answer_13 = models.CharField(max_length=50)
    answer_14 = models.CharField(max_length=50)
    answer_15 = models.CharField(max_length=50)

    output = models.CharField(max_length=64, null = True, blank = True, default="")
    def __str__(self):
        return self.user.username

class PersonalityQues(models.Model):
    question = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=64, verbose_name='Option A')
    option_2 = models.CharField(max_length=64, verbose_name='Option B')
    option_3 = models.CharField(max_length=64, verbose_name='Option C')
    
    def __str__(self):
        return self.question

