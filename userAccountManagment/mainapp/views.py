from django.shortcuts import render, render_to_response

def main(request):

    my_dict = {'caption': 'Тестируем авторизацию и регистрацию и подключение к GitHub'}

    return render(request, 'index.html', my_dict)
