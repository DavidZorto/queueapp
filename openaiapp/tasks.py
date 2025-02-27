import os, time
from openai import OpenAI
from celery import shared_task
from .models import OpenAIResponse
from dotenv import load_dotenv

load_dotenv() 

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@shared_task
def fetch_openai_response(prompt, obj_id):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    output_text = response.choices[0].message.content  # Updated syntax

    obj = OpenAIResponse.objects.get(id=obj_id)
    obj.response = output_text
    obj.save()

    return output_text


@shared_task
def long_running_task():
    print("Task started")
    time.sleep(10)  # Simulates a long task
    print("Task finished")
    return "Done"