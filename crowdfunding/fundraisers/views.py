from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import Http404
from .models import Fundraiser, Pledge
from django.db.models import Count, Sum
from .serializers import FundraiserSerializer, PledgeSerializer, FundraiserDetailSerializer, PledgeDetailSerializer
from .permissions import IsOwnerOrReadOnly

class FundraiserList(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        ]

    def get(self, request):
        fundraisers = Fundraiser.objects.all()
        serializer = FundraiserSerializer(fundraisers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = FundraiserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class FundraiserDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]
        
    def get_object(self, pk):
        try:
            fundraiser = Fundraiser.objects.get(pk=pk)
            self.check_object_permissions(self.request, fundraiser)
            return fundraiser
        except Fundraiser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        fundraiser = self.get_object(pk)
        serializer = FundraiserDetailSerializer(fundraiser)
        return Response(serializer.data)
    
    def put(self, request, pk):
        fundraiser = self.get_object(pk)
        serializer = FundraiserDetailSerializer(
            instance = fundraiser,
            data = request.data,
            partial = True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )


class PledgeList(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        ]
    
    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response (
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        

class PledgeDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]

    def get_object(self, pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(pledge)
        return Response(serializer.data)   
    
    def put(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(
            instance = pledge,
            data = request.data,
            partial = True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

class LatestFundraisers(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        ]

    def get(self, request):
        fundraisers = Fundraiser.objects.all().order_by('-date_created')[:5]
        serializer = FundraiserSerializer(fundraisers, many=True)
        return Response(serializer.data)
    

class TrendingFundraisers(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        ]

    def get(self, request):
        fundraisers = Fundraiser.objects.annotate(num_pledges= Count("pledges")).order_by("-num_pledges")[:5]
        num_pledges = Fundraiser.objects.annotate(num_pledges= Count("pledges"))
        print(f'NUMBER OF PLEDGES: {num_pledges}')
        serializer = FundraiserSerializer(fundraisers, many=True)
        return Response(serializer.data)