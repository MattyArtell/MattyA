from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request, 'cipher/home.html')

def cipher(request):
    ptext = request.GET.get('plaintext').upper()
    ctype = request.GET.get('type')

    if (ctype == 'shift'): # Shifts all characters in the plaintext by shiftby characters
        shiftby = int(request.GET.get('shiftby'))
        ciphered = ''
        for i in range(len(ptext)):
            shifted = ord(ptext[i])
            if not (65<=shifted<=90):
                ciphered+=chr(shifted)
                continue
            if (shiftby>=26):
                shiftby = shiftby % 26
            shifted+=shiftby
            if (shifted > 90):
                shifted = (shifted % 90) + 65
            shifted = chr(shifted)
            ciphered += shifted
        return render(request, 'cipher/cipher.html', {'plaintext':ptext, 'ciphered':ciphered})

    if (ctype == 'rmap'): # Maps each character to a different, randomly chosen character
        rseed = request.GET.get('rseed')
        if not (rseed == ''):
            seed = rseed
            random.seed(seed)
        ciphered = ''
        adict = {}
        alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        alphabet2 = alphabet
        key = []
        for i in range(len(alphabet2)): #assigns each letter in the alphabet to a value from 0-26
            rletter = random.randint(0,len(alphabet)-1)
            adict.update({i:alphabet[rletter]})
            key += alphabet[rletter]
            alphabet.pop(rletter)
        for i in range(len(ptext)):    
            if not (65<=ord(ptext[i])<=90):
                ciphered+=ptext[i]
                continue             
            letter = ord(ptext[i])-65            
            ciphered+=adict.get(letter)
        key = str(key)
        rseed = str(rseed)
        mapkey = 'The key is as follows:\n' + '\n' + key
        return render(request, 'cipher/cipher.html', {'plaintext':ptext, 'ciphered':ciphered, 'mapkey':mapkey})

    return render(request, 'cipher/cipher.html', {'plaintext':ptext})
    

