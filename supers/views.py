from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import SuperSerializer
from rest_framework import status
from .models import Super
from django.shortcuts import get_object_or_404
from super_types.models import SuperType

# Create your views here.

@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET' and 'type' in request.GET:
        super_type_param = request.query_params.get('type')
        supers = Super.objects.all()
        supers = supers.filter(super_type__type=super_type_param)
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)

    elif request.method == 'GET':
        supertypes = SuperType.objects.all()
        custom_response_dictionary = {}
        
        for supertype in supertypes:
            supers = Super.objects.filter(super_type_id=supertype.id)
            serializer = SuperSerializer(supers, many=True)

            custom_response_dictionary[supertype.type + 's'] = {
                'Names': serializer.data
            }
        return Response(custom_response_dictionary)

    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    supers = get_object_or_404(Super, pk=pk)
    if request.method =='GET':
        serializer = SuperSerializer(supers)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
