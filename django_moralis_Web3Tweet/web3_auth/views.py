import json
import requests
import os


from django.shortcuts import render


from moralis import evm_api


API_KEY = 'type your API key'

def homepage(request):
    return render(request, 'homepage.html', {})


def transaction_detail(request):
    if request.method == 'POST':
        transaction_hash = request.POST.get('transaction_hash')
        params = {
            "transaction_hash": transaction_hash,
            "chain": "sepolia",
        }

        result = evm_api.transaction.get_transaction(
            API_KEY,
            params,
        )

        input_hex = result.get('input')
        input = bytes.fromhex(input_hex[2:]).decode('utf-8')

        from_address = result.get('from_address')

        return render(request, 'transaction_detail.html', {'input': input, 'from_address' : from_address })
        
    return render(request, 'homepage.html', {})

