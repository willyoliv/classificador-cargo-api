from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from historicos.models import Historico
from historicos.serializers import HistoricoSerializer
from rest_framework.views import APIView
import copy

nlp = copy.copy(settings.NLP)
nlp_teste = copy.copy(settings.NLP_TESTE)

# Create your views here.
class HistoricoPredict(APIView):
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = HistoricoSerializer
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:        
                historico = request.POST.get('historico')
                texto = Historico.removeStopWords(historico, nlp_teste)
                doc = nlp(texto)
                categoria, maior_valor = Historico.classificacao(doc.cats)
                return Response({"Historico":historico, "HistoricoSemStopWords":texto,"Classificação":categoria,"Porcentagem":maior_valor}, status.HTTP_200_OK)
            except Exception as message:
                return Response({'message': "Erro, verifique o campo enviado!"}, status.HTTP_400_BAD_REQUEST)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    