from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
import paho.mqtt.publish as publish


def index(request: HttpRequest):
    if request.method == "GET":
        return render(
            request=request,
            template_name='core/index.html'
        )

    elif request.method == "POST":
        pass

    return HttpResponse("here")


def positive_message(request: HttpRequest):
    # if request.method == "POST":

    publish.single(
        topic="WN/positive_message",
        payload="Y",
        hostname="test.mosquitto.org"
    )

    return HttpResponse("positive_message")


def play_music(request: HttpRequest):
    # if request.method == "POST":

    publish.single(
        topic="WN/play_music",
        payload="Y",
        hostname="test.mosquitto.org"
    )

    return HttpResponse("play_music")
