from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import SuperSerializer
from rest_framework import status
from .models import Super

# Create your views here.

@api_view(['GET'])
def supers_list(request):

    super_type_param = request.query_params.get('type')
    sort_param = request.query_params.get('sort')

    supers = Super.objects.all()
    
    if super_type_param:
        supers = supers.filter(super_type__type=super_type_param)
    
    if sort_param:
        supers = supers.order_by(sort_param)
    
    serializer = SuperSerializer(supers, many=True)
    return Response(serializer.data)