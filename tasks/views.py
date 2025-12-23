from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics



class ContactDetail(APIView):
    def put(self,request,pk):
        contact = get_object_or_404(Contact,id=pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)



class ContactDelete(APIView):
    def delete(self, request, pk):
        contact = get_object_or_404(Contact,id=pk)
        contact.delete()
        return Response({'Deleted':True})