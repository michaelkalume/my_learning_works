# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import Question,Choice

def index(response):
	latest_questions_list = Question.objects.order_by('-pub_date')[:5]
	output = ', '.join([q.question_text for q in latest_questions_list])
	return HttpResponse(output);

# Create your views here.
def detail(request, question_id):
	return HttpResponse('You are looking at question_id %s.' %question_id)

def result(request, question_id):
	response = 'You are looking at the result of question_id %s.'
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse('You are voting on question_id %s.' %question_id)