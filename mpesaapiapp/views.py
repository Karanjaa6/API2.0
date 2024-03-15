from django.http import HttpResponse
from django.shortcuts import render, redirect
from django_daraja.mpesa.core import MpesaClient


# Create your views here.
def index(request):
    cl = MpesaClient()
    phone_number ='0703560705'
    amount = 1
    account_reference = 'reference'
    transaction_code = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express_payment'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_code, callback_url)

    return redirect('/buy/')

def stk_push_callback(request):
    data = request.body

    return HttpResponse('STK push in django')

def buy(request):
    return render(request,'buy.html')
