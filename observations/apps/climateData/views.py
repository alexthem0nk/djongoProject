from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import climateData
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# from django.urls import reverse

# from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


def index(request):
    if not request.user.is_authenticated:
        return redirect(reverse("login") + "?next=" + request.path)
    else:
        return redirect(reverse("api-climate-data"))


@csrf_exempt
def ClimateData(request):
    # Your view code here
    return HttpResponse("Hello, world!")


class climateDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = climateData
        fields = "__all__"


class climateDataViewSet(viewsets.ModelViewSet):
    serializer_class = climateDataSerializer
    queryset = climateData.objects.all()
    lookup_field = "_id"
    http_method_names = ["get", "post", "put", "patch", "delete"]

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


"""
class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "registration/login.html"
    success_url = reverse_lazy("api-climate-data")
"""
