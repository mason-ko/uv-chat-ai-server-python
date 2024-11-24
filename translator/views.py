from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os

class TranslateMessageView(APIView):
    def post(self, request):
        original_text = request.data.get("original_text")
        target_language = request.data.get("target_language")

        return Response({"translated_text": original_text}, status=status.HTTP_200_OK)
