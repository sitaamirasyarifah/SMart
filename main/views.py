from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Smartphone',
        'amount': '2',
        'description' : 'Smart'
    }

    return render(request, "main.html", context)

