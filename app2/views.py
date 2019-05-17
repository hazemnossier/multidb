from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import fill_me_form


def fill_view2(request):

    if request.method == 'POST':
        print('watashi ga kitta 2 ')
        form = fill_me_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            print(data)
    else:
        form = fill_me_form()

    return render(request, "Page2.html", {'form': form})
