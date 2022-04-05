import random
import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


from user.models import UserCategoryChoice
from game.models import Product, ProductCategoryChoice, UserResponse



class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if request.user.what_best_describe_you == UserCategoryChoice.STUDENT:
            queryset1 = Product.objects.filter(product_category=ProductCategoryChoice.FURNITURE)
            queryset2 = Product.objects.filter(product_category=ProductCategoryChoice.ELECTRONICS)
            queryset = queryset1 | queryset2
        elif request.user.what_best_describe_you == UserCategoryChoice.JOB_HOLDER:
            queryset1 = Product.objects.filter(product_category=ProductCategoryChoice.FURNITURE)
            queryset2 = Product.objects.filter(product_category=ProductCategoryChoice.ELECTRONICS)
            queryset = queryset1 | queryset2
        elif request.user.what_best_describe_you == UserCategoryChoice.HOUSE_WIFE:
            queryset1 = Product.objects.filter(product_category=ProductCategoryChoice.FURNITURE)
            queryset2 = Product.objects.filter(product_category=ProductCategoryChoice.ELECTRONICS)
            queryset = queryset1 | queryset2
        queryset = sorted(queryset, key=lambda L: random.random())[:10]
        user_response = UserResponse.objects.create(
            user=request.user
        )
        for qs in queryset:
            user_response.question.add(qs)
        return render(request, 'index.html', {'quiz_id': user_response.id})


@login_required
@csrf_exempt
def take_quiz(request, quiz_id):
    user_response = UserResponse.objects.filter(id=quiz_id).first()
    questions = user_response.question.all()
    paginator = Paginator(questions,1)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {'questions': questions, 'page_obj': page_obj}

    if request.method == 'GET':
        request.session['previous_page'] = request.path_info + "?page=" + request.GET.get("page", '1')
        return render(request, 'game.html', context)
    
    if request.method == 'POST':
        question_id = request.POST['question_id']
        user_answer = request.POST.get('user_answer')
        user_response.response[f'{question_id}'] = user_answer
        user_response.save()
        # response_data = {}
        # response_data['result'] = 'Response recorded!'
        # return HttpResponse(
        #     json.dumps(response_data),
        #     content_type="application/json"
        # )
        # messages.success(request, 'Response recorded!')
        return HttpResponseRedirect(request.session['previous_page'])