from urllib.request import Request
from django.forms import model_to_dict
from rest_framework.views import APIView, status
from rest_framework.response import Response
from .validator import ContentValidator

from content.models import Content

# Create your views here.
class ContentView(APIView):
    def get(self, request):
        contents = Content.objects.all()

        contents_dict = [model_to_dict(content) for content in contents]

        return Response(contents_dict)
    
    def post(self, request):

        validator = ContentValidator(**request.data)
        
        if not validator.is_valid():
            return Response(validator.errors, status.HTTP_400_BAD_REQUEST)
        
  
        course = Content.objects.create(**validator.data)
        course_dict = model_to_dict(course)

        return Response(course_dict, status.HTTP_201_CREATED)



class ContentRouteView(APIView):
    def get(self, request, content_id):
        try:
            content = Content.objects.get(pk=content_id)
        except Content.DoesNotExist:
            return Response({"message": "Content not found."}, status.HTTP_404_NOT_FOUND)
     
        content_dict = model_to_dict(content)

        return Response(content_dict)

    def patch(self, request: Request, content_id):
        try:
            content = Content.objects.get(pk=content_id)
        except Content.DoesNotExist:
            return Response({"message": "Content not found."}, status.HTTP_404_NOT_FOUND)


        for key, value in request.data.items():
            setattr(content, key, value)

        content.save()
        content_dict = model_to_dict(content)

        return Response(content_dict)
        
    def delete(self, request, content_id):
        try:
            content = Content.objects.get(pk=content_id)
        except Content.DoesNotExist:
            return Response({"message": "Content not found."}, status.HTTP_404_NOT_FOUND)
     
        content.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


    

class ContentTitleFindView(APIView):
    def get(self, request: Request):
        title = request.query_params.get('title', None)

        contents = Content.objects.filter(title__iexact=title)
        
        contents_dict = [model_to_dict(content) for content in contents]
       
        return Response(contents_dict)



    