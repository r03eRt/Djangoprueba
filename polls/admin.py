from django.contrib import admin

# Register your models here.
from django.contrib import admin

#campos a mostrar
from .models import Question, Choice


#para poner modelo en linea
#class ChoiceInline(admin.StackedInline):
#    model = Choice
#    extra = 0

#Para tabular modelo
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
