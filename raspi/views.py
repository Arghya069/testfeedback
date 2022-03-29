from django.http.response import JsonResponse
from django.shortcuts import redirect, render,HttpResponse
from .models import LedStat,UserDevices
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def AppLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            userdevice = UserDevices.objects.get(user=user)
            return HttpResponse(userdevice.device_id.device_id)
        else:
            return HttpResponse("can't login now please check username or password")
        


def getLED1stat(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.led1_status==0:
        return HttpResponse("LED is off")
    else:
        return HttpResponse("LED is On")

def getLED2stat(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.led2_status==0:
        return HttpResponse("LED is off")
    else:
        return HttpResponse("LED is On")

def getLED3stat(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.led3_status==0:
        return HttpResponse("LED is off")
    else:
        return HttpResponse("LED is On")

def getimp1stat(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.imp_1==0:
        return HttpResponse("input1 is low")
    else:
        return HttpResponse("input1 is high")

def getimp2stat(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.imp_2==0:
        return HttpResponse("input2 is low")
    else:
        return HttpResponse("input2 is high")

def getimp3stat(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.imp_3==0:
        return HttpResponse("input3 is low")
    else:
        return HttpResponse("input3 is high")

def ToggleLED1(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.led1_status==0:
        ledstat.led1_status=1
        ledstat.save()
        return redirect('getstat1',pk)
    else:
        ledstat.led1_status=0
        ledstat.save()
        return redirect('getstat1',pk)      

def ToggleLED2(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.led2_status==0:
        ledstat.led2_status=1
        ledstat.save()
        return redirect('getstat2',pk)
    else:
        ledstat.led2_status=0
        ledstat.save()
        return redirect('getstat2',pk) 

def ToggleLED3(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    if ledstat.led3_status==0:
        ledstat.led3_status=1
        ledstat.save()
        return redirect('getstat3',pk)
    else:
        ledstat.led3_status=0
        ledstat.save()
        return redirect('getstat3',pk)

def Toggleimp1(request,pk,stat):
    ledstat = LedStat.objects.get(device_id=pk)
    ledstat.imp_1 = float(stat)
    ledstat.save()
    return redirect('getip1',pk)
   

def Toggleimp2(request,pk,stat):
    ledstat = LedStat.objects.get(device_id=pk)
    ledstat.imp_2 = float(stat)
    ledstat.save()
    return redirect('getip2',pk)


def Toggleimp3(request,pk,stat):
    ledstat = LedStat.objects.get(device_id=pk)
    ledstat.imp_3 = float(stat)
    ledstat.save()
    return redirect('getip3',pk)

def sendControl(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    return JsonResponse({'led1':str(ledstat.led1_status),
    'led2':str(ledstat.led2_status),
    'led3':str(ledstat.led3_status)})


def getTemp(request,pk):
    ledstat = LedStat.objects.get(device_id=pk)
    return HttpResponse(str(ledstat.temprature))

def setTemp(request,pk,temp):
    ledstat = LedStat.objects.get(device_id=pk)
    ledstat.temprature = float(temp)
    ledstat.save()
    return redirect('gettemp',pk)

def led1control(request,pk,state):
    ledstat = LedStat.objects.get(device_id=pk)
    ledstat.led1_status = state
    ledstat.save()
    return redirect('getstat1',pk)

def led2control(request,pk,state):
    ledstat = LedStat.objects.get(device_id=pk)
    ledstat.led2_status = state
    ledstat.save()
    return redirect('getstat2',pk)

def led3control(request,pk,state):
    ledstat = LedStat.objects.get(device_id=pk)
    ledstat.led3_status = state
    ledstat.save()
    return redirect('getstat3',pk)

def imp1control(request,pk,state):
    ledstat = LedStat.objects.get(device_id=pk)
    ledstat.imp_1 = state
    ledstat.save()
    return redirect('getip1',pk)

def imp2control(request,pk,state):
    ledstat = LedStat.objects.get(device_id=pk)
    ledstat.imp_2 = state
    ledstat.save()
    return redirect('getip2',pk)

def imp3control(request,pk,state):
    ledstat = LedStat.objects.get(device_id=pk)
    ledstat.imp_3 = state
    ledstat.save()
    return redirect('getip3',pk)

 