from django.views.decorators.csrf import csrf_exempt
from api.serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.models import Post

@csrf_exempt
def putLike(request, pk):
if request.method == 'PUT':
try:
post = Post.objects.get(id=pk)
except Post.DoesNotExist as e:
raise Response(status = status.HTTP_404_NOT_FOUND)
post.like_count += 1
post.save()
return Response(status=status.HTTP_200_OK)
return Response({"error":"bad request"})