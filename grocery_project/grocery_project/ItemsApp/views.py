from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

# Create your views here.
@api_view(['POST'])
def create_item(request):
    serializer = ItemSerializer(data = request.data) # DeSerialization - Converting data from JSON -> Model Instance.

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def item_details(request, id):
    try:
        item = Item.objects.get(pk=id)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    except Item.DoesNotExist:
        return Response({ 'error': 'Item not found' }, status = status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_item(request, id):
    try:
        item = Item.objects.get(pk=id)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Item.DoesNotExist:
        return Response({ 'error': 'Item not found' }, status = status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_item(request, id):
    try:
        item = Item.objects.get(pk=id)
        item.delete()
        return Response({ 'message': 'Item deleted successfully' })
    except Item.DoesNotExist:
        return Response({ 'error': 'Item not found' }, status = status.HTTP_404_NOT_FOUND)

