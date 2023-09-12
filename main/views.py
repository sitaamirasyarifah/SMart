from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Snack Murmer',
        'amount': '4',
        'description' : 'Lezat dan Bergizi',



        'author' : 'Sita Amira Syarifah',
        'class' : 'PBP B'
    }

    return render(request, "main.html", context)

