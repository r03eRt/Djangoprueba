from django.contrib import admin

# Register your models here.
from django.contrib import admin

#campos a mostrar
from .models import Question, Choice



class QuestionAdmin(admin.ModelAdmin):
    #campos solo
    # fields = ['pub_date', 'question_text']

    #grupos de campos , None 1er campo para no poner nada
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

#anadir al panel admin printipal el modelo
#admin.site.register(Question)
admin.site.register(Choice)

#anade los campos indicados en la clase
# al modelo que indicamos primero dentro de el opciones
admin.site.register(Question, QuestionAdmin)
