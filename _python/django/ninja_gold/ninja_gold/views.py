from django.shortcuts import render, redirect
from django.http import JsonResponse
from random import randint

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request, 'index.html')

def process(request):
    # post request from form
    print('-'*40)
    print(request.session['gold'])
    print(request.POST['farmbuilding'])
    if request.POST['farmbuilding'] == 'farm':
        print('farm')
        rand_num = randint(10,20)
    if request.POST['farmbuilding'] == 'cave':
        print('cave')
        rand_num = randint(5,10)
    if request.POST['farmbuilding'] == 'house':
        print('house')
        rand_num = randint(2,5)
    if request.POST['farmbuilding'] == 'casino':
        print('casino')
        rand_num = randint(-50,50)

    request.session['gold'] += rand_num
    print(rand_num)
    print(request.session['gold'])

    if rand_num < 0:
        activity = f'Entered a casino and lost {rand_num} golds...Ouch'
    else:
        activity = f'Earned {rand_num} from the {request.POST["farmbuilding"]}!'

    request.session['activities'].append(activity)

    print('-'*40)
    return redirect('/')















# def send_json(request):
#     json_obj = {
#         "orders":
#         [
#             {
#                 "orderno": 784692,
#                 "date": "June 30, 2088 1:54:23 AM",
#                 "trackingno": "TN000391",
#                 "customer": {
#                     "custid": 11045,
#                     "fname": "Sue",
#                     "lname": "Hatfield",
#                     "address": "1409 Silver Street",
#                     "city": "Ashland",
#                     "state": "NE",
#                     "zip": 68003
#                 }
#             }
#         ]
#     }
#     return JsonResponse(json_obj)