from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect, HttpResponseNotModified
from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.http import HttpResponseNotAllowed, HttpResponseGone
from django.http import HttpResponseServerError, HttpResponseNotFound, JsonResponse
from django.http import StreamingHttpResponse, FileResponse
from django.template import Template, Context
import os, random

def msgproc(request):
    datalist = []
    if request.method == "POST":
        userA = request.POST.get("userA", None)
        userB = request.POST.get("userB", None)
        msg = request.POST.get("msg", None)
        time = datetime.now()
        with open("msgdata.txt", "a+") as f:
            f.write("{}--{}--{}--{}\n".format(userB, userA, msg, time.strftime("%Y-%m-%d %H:%M:%S")))
    
    if request.method == "GET":
        userC = request.GET.get("userC", None)
        if userC != None:
            with open("msgdata.txt", "r") as f:
                cnt = 0
                for line in f:
                    linedata = line.split("--")
                    if linedata[0] == userC:
                        cnt = cnt + 1
                        d = {"userA": linedata[1], "msg": linedata[2], "time": linedata[3]}
                        datalist.append(d)
                    if cnt >= 10:
                        break
    
    return render(request, "MsgSingleWeb.html", {"data": datalist})

def proc1(request):
    response = HttpResponse()
    response.write("<h1>This is the home page, for specific functions, please visit <a href='../0'>here</a>.</h1>")
    response.write("<h1>This is the second line.</h1>")
    return response

def proc2(request):
    t = Template("<h1>The name of this program is {{ name }}</h1>")
    c = Context({"name": "proc2"})
    return HttpResponse(t.render(c))
