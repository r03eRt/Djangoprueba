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
    #anado a lista de preguntas los campos antes de entrar en la individual
    list_display = ('question_text', 'pub_date', )
    #muestri filtro por campo puba_date
    list_filter = ['pub_date']
    #anado modulo de busqueda a la pagina
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
