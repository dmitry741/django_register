from django.shortcuts import render, render_to_response

def main(request):

    my_dict = {'caption': 'Тестируем авторизацию'}

    return render_to_response('index.html', my_dict)
