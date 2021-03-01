from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer
# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def api_question(request, id):
    if request.method == 'GET':
        list_question = Question.objects.all()
        question_serializers = QuestionSerializer(list_question, many=True)
        if not question_serializers.is_valid:
            mydata = {
                "status": False
            }
            return JsonResponse(data=mydata)

        return Response(data=question_serializers.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        question_data = JSONParser().parse(request)
        question_serializers = QuestionSerializer(data=question_data)
        if question_serializers.is_valid():
            question_serializers.save()
            mydata = {
                "status": True,
                "data": list(question_data.value("id", "question_text", "time_pub"))
            }

            return JsonResponse(data=mydata, status=status.HTTP_200_OK)
        mydata = {
            "status": False
        }

        return JsonResponse(mydata)

    elif request.method == 'PUT':
        question = Question.objects.all()
        quetions_data = JSONParser().parse(request)
        quetions_serializers = QuestionSerializer(question, data=quetions_data)
        if quetions_serializers.is_valid():
            quetions_serializers.save()
            my_response = {
                "status": True,
                "data": list(quetions_data.value("id", "question_text", "time_pub"))
            }

            return JsonResponse(my_response)

        my_response = {
            "status": False
        }

        return JsonResponse(my_response)

    elif request.method == 'DELETE':
        try:
            question = Question.objects.all().delete()
            my_response = {
                "status": True
            }
            return JsonResponse(my_response)
        except:
            my_response = {
                "status": False
            }
            return JsonResponse(my_response)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def api_choice(request, id):
    if request.method == 'GET':
        list_choice = Choice.objects.get(id)
        if not list_choice.is_valid:
            mydata = {
                "status": False
            }
            return JsonResponse(data=mydata)

        return Response(data=list_choice.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        choice_data = JSONParser().parse(request)
        choice_serializers = ChoiceSerializer(data=choice_data)
        if choice_serializers.is_valid():
            choice_serializers.save()
            mydata = {
                "status": True,
                "data": list(choice_data.value("id", "choice", "type", "Datatime"))
            }

            return JsonResponse(data=mydata, status=status.HTTP_200_OK)
        mydata = {
            "status": False
        }

        return JsonResponse(mydata)

    elif request.method == 'PUT':
        choice = Choice.objects.get(id)
        choice_data = JSONParser().parse(request)
        choice_serializers = QuestionSerializer(choice, data=choice_data)
        if choice_serializers.is_valid():
            choice_serializers.save()
            my_response = {
                "status": True,
                "data": list(choice_data.value("id", "question_text", "time_pub"))
            }

            return JsonResponse(my_response)

        my_response = {
            "status": False
        }

        return JsonResponse(my_response)

    elif request.method == 'DELETE':
        try:
            question = Choice.objects.get(id).delete()
            my_response = {
                "status": True
            }
            return JsonResponse(my_response)
        except:
            my_response = {
                "status": False
            }
            return JsonResponse(my_response)

def index(request):
    return render(request, "polls/index.html")
