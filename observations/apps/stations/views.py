from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets
from .models import stations
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


def index(request):
    if not request.user.is_authenticated:
        return redirect(reverse("login") + "?next=" + request.path)
    else:
        return redirect(reverse(""))


@csrf_exempt
def Stations(request):
    # Your view code here
    return HttpResponse("Hello, world!")


class stationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = stations
        fields = "__all__"


class stationsViewSet(viewsets.ModelViewSet):
    serializer_class = stationsSerializer
    queryset = stations.objects.all()
    lookup_field = "_id"
    allowed_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
