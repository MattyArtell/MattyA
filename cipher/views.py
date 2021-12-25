from django.shortcuts import render
import random

# Create your views here.

def ciphermap(adict, ptext): #given a dictionary which assigns each letter in the alphabet to another letter, returns the ciphertext
    ciphered=''
    for i in range(len(ptext)):
            if not (65<=ord(ptext[i])<=90):
                ciphered+=ptext[i]
                continue              
            ciphered+=adict.get(ptext[i])
    return(ciphered)

def alphashift(input, n): #shifts all characters in a string by n characters
    ciphered = ''
    for i in range(len(input)):
            shifted = ord(input[i])
            if not (65<=shifted<=90):
                ciphered+=chr(shifted)
                continue
            if (n>=26):
                n = n % 26
            shifted+=n
            if (shifted > 90):
                while(shifted>90):
                    shifted = shifted - 26
            if (shifted < 65):
                while(shifted < 65):
                    shifted = shifted + 26                
            shifted = chr(shifted)
            ciphered += shifted
    return(ciphered)

def home(request):
    return render(request, 'cipher/home.html')

def cipher(request):
    return render(request, 'cipher/cipher.html')

def result(request):
    ptext = request.GET.get('plaintext').upper()
    ctype = request.GET.get('type')
    alphabet= list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    alphabet2 = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    ciphered = ''
    adict = {}
    showtr = False

    if (ctype == 'shift'): # Shifts all characters in the plaintext by shiftby characters
        shiftby = int(request.GET.get('shiftby'))
        ciphered = alphashift(ptext, shiftby)
        return render(request, 'cipher/result.html', {'plaintext':ptext, 'ciphered':ciphered})

    if (ctype == 'rmap'): # Maps each character to a different, randomly chosen character
        rseed = request.GET.get('rseed')
        if not (rseed == ''):
            seed = rseed
            random.seed(seed)        
        key = []
        for i in range(len(alphabet2)): #assigns each letter in the alphabet to another random letter
            rletter = random.randint(0,len(alphabet)-1)
            adict.update({alphabet2[i]:alphabet[rletter]})
            key += alphabet[rletter]
            alphabet.pop(rletter)
        ciphered = ciphermap(adict,ptext)
        key = str(key)
        rseed = str(rseed)
        mapkey = 'The key is as follows:\n' + '\n' + key
        return render(request, 'cipher/result.html', {'plaintext':ptext, 'ciphered':ciphered, 'mapkey':mapkey})

    if (ctype == 'smap'): # Maps each character to a user-specified character
        map = request.GET.get('maptext')
        alphabet2 = list(map)
        for i in range(len(alphabet)):
            adict.update({alphabet[i]:alphabet2[i]})
        ciphered = ciphermap(adict,ptext)
        return render(request, 'cipher/result.html', {'plaintext':ptext, 'ciphered':ciphered, 'mapkey':map})

    if (ctype == 'keyword'): # The start of the alphabet is replaced with a keyword, followed by the normal alphabet with repeated letters removed
        keyword = request.GET.get('keywordin').upper()
        keyword2 = ""
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        #remove all duplicate letters in keyword to make a new one
        while len(keyword) > 0:
            first = keyword[0]
            keyword2 += first
            keyword = keyword.replace(first, "")
        #remove all of the resulting letters from the alphabet and insert keyword at the start
        for i in range(len(keyword2)):
            alphabet = alphabet.replace(keyword2[i], "")
        map = list(keyword2 + alphabet)
        alphabet = list(alphabet)
        for i in range(len(alphabet)):
            adict.update({map[i]:alphabet[i]})

        ciphered = ciphermap(adict,ptext)

        return render(request, 'cipher/result.html', {'plaintext':ptext, 'ciphered':ciphered, 'mapkey':map})


    if (ctype == 'vigenere'): #this does not work with spaces etc.
        keyword = request.GET.get('keywordin').upper()
        keywordconst = request.GET.get('keywordin').upper()

        #remove all non-letters from keyword
        for i in range(len(keywordconst)):            
            if not (65<=ord(keywordconst[i])<=90):
                keyword = keyword.replace(keywordconst[i], "")

        if (len(keyword) < len(ptext)): #repeats keyword to be as long as ptext            
            current = 0
            while(len(keyword) < len(ptext)):                
                keyword += keyword[current]                
                current += 1

        elif (len(keyword) > len(ptext)): #trims keyword to be as long as ptext
            keyword = keyword[:len(ptext)]

        keyworddisplay = keyword #variable for display before we add spaces to keyword

        for i in range(len(ptext)):
            if not (65<=ord(ptext[i])<=90):
                ciphered+=ptext[i] #the problem is, we will now be using the wrong keyletter
                keyword = keyword[:i] + " " + keyword[i:] #add a space to the keyword at position i to account for this
                continue
            keyletter = ord(keyword[i])
            ptextletter = ord(ptext[i])
            cipheredletter = (keyletter + ptextletter)%26
            ciphered += chr(cipheredletter+65)

        return render(request, 'cipher/result.html', {'plaintext':ptext, 'ciphered':ciphered, 'mapkey':keyworddisplay, 'showtr':True})
      
    return render(request, 'cipher/result.html', {'plaintext':ptext})
    

