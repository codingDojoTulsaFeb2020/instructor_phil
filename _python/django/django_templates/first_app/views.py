from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    print(request.method)
    return render(request, 'index.html')

def show(request, user_id):
    context = {
        "name": "Phil",
        "id": user_id,
        "end_loop": range(10)
    }
    return render(request, 'show.html', context)

def process(request):
    print(request.method)
    print(request.path)
    print('*'*90)
    if request.method == 'POST':
        print('post')
        print(request.POST)
    else:
        print(request.GET)
        print('get')
    return redirect('/')