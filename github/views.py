from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json
    api_request = requests.get("https://api.github.com/users/yubuntu0109/followers?per_page=1000")
    api_content  = json.loads(api_request.content)
    return render(request, 'home.html', {"api_content":api_content})
