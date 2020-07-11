from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import getListSerializer
from .models import Categories
from rest_framework.views import APIView
from rest_framework.response import Response
class CategoryList(APIView):

	def get(self,request):
		categories = Categories.objects.all()
		serializer = getListSerializer(categories,many=True)
		return Response(serializer.data) 