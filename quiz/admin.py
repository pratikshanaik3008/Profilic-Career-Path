from django.contrib import admin
from .models import QuestionBank, UserResponse, artsque, commerceque, scienceque, PersonalityQues

admin.site.register(PersonalityQues)
admin.site.register(QuestionBank)
admin.site.register(UserResponse)
admin.site.register(artsque)
admin.site.register(commerceque)
admin.site.register(scienceque)
