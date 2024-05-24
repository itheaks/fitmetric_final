from django.http import JsonResponse
import google.generativeai as gai
from django.conf import settings
from PIL import Image
import markdown2
from bs4 import BeautifulSoup

gai.configure(api_key=settings.GOOGLE_API_KEY)

model = gai.GenerativeModel("gemini-pro-vision")

def NutSearch(request):
    img = request.FILES.get('image')
    image = Image.open(img)
    prompt = "List the food dish present in the image"
    response = model.generate_content([prompt,image])
    plain_text = markdown2.markdown(response.text)
    soup = BeautifulSoup(plain_text, 'html.parser')
    text_content = soup.get_text(separator=' ', strip=True)
    return JsonResponse(text_content,safe=False)