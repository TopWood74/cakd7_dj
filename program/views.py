from django.shortcuts import render, redirect

def inputdata(request):
    if request.POST:
        lis = []        
        lis_mode = request.POST['mode']
        lis.append(request.POST['a'])
        lis.append(request.POST['b'])

        sum = 0

        if lis_mode == 'add':
            mode_kr = "덧셈" 
        elif lis_mode == 'sub':
            mode_kr = "뺄셈"         
        elif lis_mode == 'mul':
            mode_kr = "곱셈"         
        elif lis_mode == 'div':
            mode_kr = "나눗셈" 

        for i, l in enumerate(lis):
            if lis_mode == 'add':
                sum += int(l)
            elif lis_mode == 'sub':
                if i == 0:
                    sum = int(l)
                else: 
                    sum -= int(l)
            elif lis_mode == 'mul':
                if i == 0:
                    sum = int(l)
                else: 
                    sum *= int(l)
            elif lis_mode == 'div':
                if i == 0:
                    sum = int(l)
                elif int(l) == 0: 
                    sum = "None - '0'으로 나눌 수 없습니다."
                    break
                else:
                    sum /= int(l)

        ans = sum
        context = {'ans': ans, 'lis': lis, 'mode': lis_mode, 'mode_kr': mode_kr}        
    else:
        context = {}

    return render(request, 'program/inputdata.html', context)

def result(request):
    lis = []
    lis_mode = ""
    mode_kr = ""

    if request.POST:
        lis_mode = request.POST['mode']
        lis.append(request.POST['a'])
        lis.append(request.POST['b'])

    sum = 0
    if lis_mode == 'add':
        mode_kr = "덧셈" 
    elif lis_mode == 'sub':
        mode_kr = "뺄셈"         
    elif lis_mode == 'mul':
        mode_kr = "곱셈"         
    elif lis_mode == 'div':
        mode_kr = "나눗셈" 

    for i, l in enumerate(lis):
        if lis_mode == 'add':
            sum += int(l)
        elif lis_mode == 'sub':
            if i == 0:
                sum = int(l)
            else: 
                sum -= int(l)
        elif lis_mode == 'mul':
            if i == 0:
                sum = int(l)
            else: 
                sum *= int(l)
        elif lis_mode == 'div':
            if i == 0:
                sum = int(l)
            elif int(l) == 0: 
                sum = "None - '0'으로 나눌 수 없습니다."
                break
            else:
                sum /= int(l)

    ans = sum
    context = {'ans': ans, 'lis': lis, 'mode': lis_mode, 'mode_kr': mode_kr}  

    return render(request, 'program/result.html', context)
