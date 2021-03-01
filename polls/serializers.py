from dataclasses import field

from rest_framework import serializers
from .models import Question, Choice

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields=('id', 'question_text', 'time_pub')

class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ('id', 'choice', 'Datatime')
