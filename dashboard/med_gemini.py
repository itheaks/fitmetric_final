from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as gai
import markdown2
from bs4 import BeautifulSoup
from django.conf import settings
from PIL import Image
import json

gai.configure(api_key=settings.GOOGLE_API_KEY)

model = gai.GenerativeModel("gemini-pro-vision")

def med_gemini(request):
    return render(request, 'dashboard/med_gemini.html')

def MedSearch(request):
    prompt = "find the names of the medicines present in the image and give a brief description of each medicine."
    img = request.FILES.get('image')
    image = Image.open(img)
    response = model.generate_content([prompt,image])
    plain_text = markdown2.markdown(response.text)
    soup = BeautifulSoup(plain_text, 'html.parser')
    text_content = soup.get_text(separator=' ', strip=True)
    return JsonResponse(text_content,safe=False)