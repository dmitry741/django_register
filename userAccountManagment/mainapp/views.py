from django.shortcuts import render, render_to_response

def main(request):
    return render(request, 'index.html')
