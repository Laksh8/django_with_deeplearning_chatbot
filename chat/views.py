from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from ChatBot.chatgui import chatbot_response


# Create your views here.
class ChatView(APIView):

    def post(self,request):
        if request.headers.get("token") == settings.RANDOM_TOKEN:
            data = chatbot_response(request.data.get("message"))
            return Response(data,status=status.HTTP_200_OK)
        return Response(["You are Trying to Breach the Security stay Back"],status=status.HTTP_401_UNAUTHORIZED)

