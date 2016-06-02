from __future__ import unicode_literals

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200,verbose_name='Pregunta')
    pub_date = models.DateTimeField('date published',)

    #devuelvo el nombre para mostarrlo en la vista
    def __unicode__(self):
        return self.question_text

    #preguntas de fuera
    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'




class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200,verbose_name='Opcion')
    votes = models.IntegerField(default=0)
    class Meta:
        verbose_name = 'Opcion'
        verbose_name_plural = 'Opciones'

    # devuelvo el nombre para mostarrlo en la vista
    def __unicode__(self):
        return self.choice_text