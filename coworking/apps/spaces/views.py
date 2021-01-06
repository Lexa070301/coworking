from django.http import HttpResponse
from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
# from rest_framework.response import Response
# from rest_framework.views import APIView

from .models import Space
from .serializers import SpaceSerializer


def index(request):
    space_features = Space.objects.filter(
        name='Райский остров'
    ).values('name', 'feature')
    return HttpResponse(space_features)

#
# class SpaceView(APIView):
#     def get(self, request):
#         spaces = Space.objects.all()
#         serializer = SpaceSerializer(spaces, many=True)
#         return Response({"spaces": serializer.data})
#
#     def post(self, request):
#         space = request.data.get("space")
#         # Create an article from the above data
#         serializer = SpaceSerializer(data=space)
#         if serializer.is_valid(raise_exception=True):
#             space_saved = serializer.save()
#         return Response({"success": "Space '{}' created successfully".format(space_saved.title)})
#
#     def put(self, request, pk):
#         saved_space = get_object_or_404(Space.objects.all(), pk=pk)
#         data = request.data.get('space')
#         serializer = SpaceSerializer(instance=saved_space, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             space_saved = serializer.save()
#         return Response({
#             "success": "Space '{}' updated successfully".format(space_saved.title)
#         })
#
#     def delete(self, request, pk):
#         # Get object with this pk
#         space = get_object_or_404(Space.objects.all(), pk=pk)
#         space.delete()
#         return Response({
#             "message": "Space with id `{}` has been deleted.".format(pk)
#         }, status=204)

class SpaceView(ListCreateAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer

    # def perform_create(self, serializer):
    #     author = get_object_or_404(Space, id=self.request.data.get('author_id'))
    #     return serializer.save(author=author)


class SingleSpaceView(RetrieveUpdateDestroyAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer
