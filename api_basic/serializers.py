from rest_framework import serializers
from .models import Article

# TU ai creat BAZA.de DATE cu CAMP="date" >
# de aceea daca decomentezi acest COD nu iti va merge deloc < chiar si daca lasi comentata LINIA.cu "date"
# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     author = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#     # LINIA.asta cauzeaza PROBLEME
#     # date = serializers.DateTimeField()

#     # CREAZA un ELEMENT.nou de la POST
#     def create(self, validated_data):
#         return Article.objects.create(validated_data)
    
#     def update(self, instance, validated_data):
#         self.title = validated_data.get("title", instance.title)
#         instance.author = validated_data.get("author", instance.author)
#         instance.email = validated_data.get("email", instance.email)

#         instance.save()

#         return instance

# CLASA.de mai sus se simplifica la a scrie clasa de mai jos
# < aceasta CLASA era deja implementata > pentru a fi totul mai simplu

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		# fields = ["title", "author", "email", "date"]
		# THE SAME AS
		fields = '__all__' # aici vei vedea ca apare CAMP=ID = primary-KEY in BAZA=DATE