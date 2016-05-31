from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.http import Http404
from django.template import loader
from django.core.urlresolvers import reverse


#def index(request):
    #defino los objetos que voy a pasar
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template que voy a coger
    #template = loader.get_template('polls/index.html')
    #parametros que paso a la vista
    #context = {
    #    'latest_question_list':latest_question_list,
    #}
    #renderizo la vista
    #return HttpResponse(template.render(context, request))

def index(request):
    #defino objetos que voy a lanzar a la vista
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #lista que voy a pasar a la vista
    context = {'latest_question_list': latest_question_list}
    #objeto que paso,template donde y el contexto
    return render(request, 'polls/index.html', context)


#def detail(request, question_id):
#    return HttpResponse("Pagina para ver la preguta numero %s." % question_id)

#def detail(request, question_id):
#    try:
#        question_id = Question.objecssssts.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("La pregunta no existe")
#    return render(request, 'polls/detail.html', {'question': question_id})
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        #redisplay vote form
        return render(request, 'polls/details.html',
                      {'question':question,
                       'error:message':"you didnt select a choice"
                       })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id ):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})
