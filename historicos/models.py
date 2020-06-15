from django.db import models
import re

# Create your models here.
class Historico(models.Model):
    historico = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    
    def __str__(self):
        return self.historico
    
    def removeStopWords(historico, nlp):
        text = re.sub(r'[^\w\s]',' ',historico)
        text = text.replace('º'," ")
        doc = nlp(text)
        text_aux = []
        for token in doc:
            if token.is_stop == False and token.is_digit == False and token.is_space == False and token.like_num == False:
                text_aux.append(token.text)            
        return " ".join(text_aux)
    def classificacao(dicionario):
        categorias = list(dicionario.keys())
        valores = list(dicionario.values())
        maior_valor = max(valores)
        index = valores.index(maior_valor)
        categoria = categorias[index]
        return categoria, maior_valor
        