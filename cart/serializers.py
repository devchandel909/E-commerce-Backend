from .models import Cart_item
from  rest_framework  import serializers

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart_item
        fields='__all__'
        
        read_only_fields =['user']
    