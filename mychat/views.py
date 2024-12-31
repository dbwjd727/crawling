import openai
from myproject import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

openai.api_key = settings.OPENAI_API_KEY

print("openai.api_key:", openai.api_key)


@csrf_exempt
def chat_with_ai(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message")

        if user_message:
            # 새로운 API 호출 방식 사용
            response = openai.chat.completions.create(
                messages=[
                    {"role": "user", "content": user_message}  # 사용자가 보낸 메시지
                ],
                model="gpt-3.5-turbo",  # 사용하려는 모델
            )
            ai_message = response["choices"][0]["message"]["content"].strip()
            return JsonResponse({"response": ai_message})
        else:
            return JsonResponse({"error": "No message provided"}, status=400)
    else:
        # GET 요청은 chat.html을 렌더링하여 반환
        return render(request, "chat.html")
