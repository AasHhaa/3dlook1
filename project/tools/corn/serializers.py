import time
from rest_framework import serializers
from .models import *
from PIL import Image


class ProductSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        im = Image.open(validated_data['logo'])
        start_time = time.time()
        im_rotate = im.rotate(180, expand=True)
        im_rotate.save(validated_data['logo'])
        end_time = time.time()
        rotate_duration = end_time - start_time
        validated_data['rotate_duration'] = rotate_duration
        return super(ProductSerializer, self).create(
            validated_data)

    def update(self, instance, validated_data):
        if instance.modified is True:
            raise serializers.ValidationError(
                detail=f"Product '{validated_data['name']}' is already modified")
        else:
            validated_data['modified'] = True

        return super(ProductSerializer, self).update(instance, validated_data)

    class Meta:
        fields = ["id", "name", "description", "logo"]
        model = Product
