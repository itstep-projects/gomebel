from django.shortcuts import render


def form(request):
    data = {'title': 'Форма заказа'}
    return render(request, 'orders/form.html', context=data)
