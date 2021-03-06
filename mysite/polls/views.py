from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice, Customer
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
#
#
# def customers(request):
#     customers_list = Customer.objects.order_by('name')[:10]
#     return render(request, 'polls/mycustomers.html', context={
#                                                         'customer_list': customers_list
#                                                         }
#            )


# class CustomersView(generic.ListView):
#     model = Customer
#     template_name = 'polls/mycustomers.html'


from .filters import *
class FilterCustomerListView(SingleTableMixin, FilterView):
    table_class = CustomersTable
    model = Customer
    template_name = 'polls/mycustomers.html'

    filterset_class = CustomerFilter


def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(
        template.render(context, request)
    )

#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/details.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return  HttpResponseRedirect(
#             reverse('polls:result', args=(question.id,))
#         )
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))  # after any good post


def resulsts(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', context={
        'question': question
    })


