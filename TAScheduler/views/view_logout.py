from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views import View

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("/")