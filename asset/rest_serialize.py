#__author:  Administrator
from rest_framework import serializers
from asset import models

class UserProfileSerializer(serializers.ModelSerializer):
     class Meta:
         model = models.UserProfile
         fields = ('email','name')


class IDCSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IDC
        fields = ('name',)


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Asset
        depth = 2
        fields = ('sn', 'name', 'admin','idc','status', 'asset_type','create_date','id')