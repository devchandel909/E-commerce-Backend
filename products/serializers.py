from rest_framework import serializers
from .models import Product , ProductImage

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields='__all__'
        

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductImage
        fields='__all__'
        
        def validate(self,attrs):
            product=attrs.get('product')
            is_primary=attrs.get('is_primary')
            
            if is_primary:
                exists= ProductImage.objects.filter(
                
                product=product,
                
                is_primary=True
                
                 ).exists()
                
            if  exists:

                raise serializers.ValidationError(
                    "Primary image already exists."
                )

            return attrs
        
        
        
        
        
        
#is_primary '''यह database की पुरानी images को check कर रहा है। मतलब:
               # "क्या इस product की कोई image पहले से primary है?\
#product=product #ProductImage table में उन records को खोजो जिनकी product field की value इस variable product के बराबर हो।
                #ProductImage table me check karega ki jo valye aayi he woh mujhe Is product me de do #ProductImage table में उन records को खोजो जिनकी product field की value इस variable product के बराबर हो।
                #ProductImage table me check karega ki jo valye aayi he woh mujhe Is product me de do 
