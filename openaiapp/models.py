from django.db import models

# Create your models here.

class OpenAIResponse(models.Model):
    prompt = models.TextField()
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.prompt[:50]
