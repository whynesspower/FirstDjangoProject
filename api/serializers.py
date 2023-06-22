from rest_framework import serializers
from baseApp.models import Item

class ItemSerializer(serializers.Model.Serializer):
	class Meta: 
		model=Item
		fields='__all__'