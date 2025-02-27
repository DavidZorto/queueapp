from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import OpenAIResponse
from .serializers import OpenAIResponseSerializer
from .tasks import fetch_openai_response, long_running_task


class OpenAIRequestView(APIView):
    def post(self, request):
        prompt = request.data.get("prompt")
        
        if not prompt:
            return Response({"error": "Prompt is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        openai_obj = OpenAIResponse.objects.create(prompt=prompt)
        fetch_openai_response.delay(prompt, openai_obj.id)

        return Response({"message": "Processing your request"}, status=status.HTTP_202_ACCEPTED)


class LongTaskView(APIView):
    def post(self, request):
        long_running_task.delay()
        return Response({"message": "Long task started"}, status=status.HTTP_202_ACCEPTED)
