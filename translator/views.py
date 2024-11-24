from requests.packages import target
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .llm.translator import translate_text


class TranslateMessageView(APIView):
    def post(self, request):
        original_text = request.data.get("original_text")
        target_language = request.data.get("target_language")

        translated_text = translate_text(original_text, target_language)

        return Response({"translated_text": translated_text}, status=status.HTTP_200_OK)
