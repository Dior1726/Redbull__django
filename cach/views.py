from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Company, Bank
from .serializers import *


class CompanyListView(APIView):

    def get(self, request):
        company = Company.objects.all()
        serializer = CompanyListSerializer(company, many=True)
        return Response(serializer.data)
