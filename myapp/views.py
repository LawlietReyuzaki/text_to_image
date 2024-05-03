from django.shortcuts import render
from django.http import HttpResponse
import requests
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt
import json
from django.http import JsonResponse


def image_generator_function(user_input , negative_prompt):
        url = "https://api.runpod.ai/v2/kandinsky-v2/runsync"

        payload = { "input": {
                "prompt": user_input,
                "negative_prompt": negative_prompt,
                "num_steps": 100,
                "guidance_scale": 4,
                "h": 768,
                "w": 768,
                "sampler": "ddim",
                "prior_cf_scale": 4,
                "prior_steps": "5",
                "num_images": 1,
                "seed": -1
            } }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": "U1JT8CJAZ4PU315W7PZUFA550V0VIWNY8888USN2"
        }

        response = requests.post(url, json=payload, headers=headers)
        response_text = response.text


        response_dict = json.loads(response_text)

        # Extracting the image_url
        image_url = response_dict['output']['image_url']

        return image_url

def index_templete(request):
    return render(request, "myapp/index.html")


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request , "myapp/index.html")


def generate_index(request):

    print("============================================================================")
    print("req method", request.method)
    print("+++++++++++++++++++++++++++++++++++++++++++")
    print(request.GET.get('text',''))

    if request.method == 'GET':
        text = request.GET.get('text', '')
        negative_prompt = request.GET.get('negative_prompt', '')
        
        print('this call was invoked with the folloing text: ',text)
      
        
        image_url = image_generator_function(text ,negative_prompt)
        print("Image url : ",image_url)
        	
        return render(request, "myapp/generate.html", {'image_url': image_url} )


def pricing_index(request):
    return render(request, "myapp/Pricing.html")


def history_index(request):
    return render(request, "myapp/History.html")


def gallery_index(request):
    return render(request, "myapp/gallery.html")
