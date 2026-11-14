from django.shortcuts import render

def churnrate(request):
    initial= float(request.POST.get('length', '0'))
    costemers= float(request.POST.get('breath', '0'))

    a = (initial/costemers)*100 if request.method == 'POST' else 0

    print("initial customer count =",initial)
    print("costemer lost count =",costemers)
    print("churnrate =", a)

    return render(
        request,
        'myapp/mathserv.html',
        {'initial': initial, 'costemers': costemers, 'a': a}
    )