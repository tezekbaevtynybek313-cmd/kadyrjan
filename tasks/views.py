from rest_framework import generics
from .models import Tasks
from .serializers import TasksSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Tasks




class TasksListCreateView(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer


class TasksDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer



class TasksDetail(APIView):
    def put(self,request,pk):
        tasks = get_object_or_404(Tasks,id=pk)
        serializer = TasksSerializer(Tasks)
        return Response(serializer.data)



class TasksDelete(APIView):
    def delete(self, request, pk):
        tasks = get_object_or_404(Tasks,id=pk)
        tasks.delete()
        return Response({'Deleted':True})



class TasksUpdate(APIView):
    def post(self,request,pk):
        tasks = get_object_or_404(Tasks,id=pk)
        serializer = TasksSerializer(tasks,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
