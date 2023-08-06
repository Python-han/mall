from rest_framework import serializers


class Serializer(serializers.Serializer):
    pass


class ModelSerializer(serializers.ModelSerializer):
    
    add_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    pub_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)


class BatchDestroySerializer(Serializer):
    
    ids = serializers.ListField(min_length=1, child=serializers.IntegerField(min_value=1))