from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from drf_api.permissions import IsOwnerOrReadOnly

class ProfileList(APIView):
## Get method: fetch's all profile objects, serializes and returns in Response.
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(
            profiles,
            many=True,
            context={'request': request}
            )
        return Response(serializer.data)

class ProfileDetail(APIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    # setting serializer class attribute in this view, the rest framework with automatically render the form based on our serializer fields, as opposed to raw Json.
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    def get_object(self, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404

## Get method fetching profile detail using pk.
    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(
            profile,
            # As the logged in user is part of the request object, we need to pass it as context object when we call our serializers in our views.
            context={'request': request}
            )
        return Response(serializer.data)

## Put Method: Updating data. 
# Fetches profile, calls serializer and saves if serializer is valid.
## Else, 400_BAD_REQUEST
    
    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(
            profile,
            data=request.data,
            context={'request': request}
            )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)