from django.shortcuts import render, render_to_response

def home_view(request):
    return render_to_response('home.html')
