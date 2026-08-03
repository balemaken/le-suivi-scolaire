from rest_framework import serializers
from .models import User, Enfant



class EnfantSerializer(serializers.ModelSerializer):

    class Meta:

        model = Enfant

        fields = [
            "nom",
            "classe",
            "sexe"
        ]





class ParentRegisterSerializer(serializers.ModelSerializer):

    enfants = EnfantSerializer(
        many=True
    )


    password = serializers.CharField(
        write_only=True
    )


    class Meta:

        model = User

        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "telephone",
            "ville",
            "type_parent",
            "enfants"
        ]



    def create(self, validated_data):

        enfants = validated_data.pop(
            "enfants"
        )


        user = User.objects.create_user(

            username=validated_data["email"],

            email=validated_data["email"],

            password=validated_data["password"],

            first_name=validated_data["first_name"],

            last_name=validated_data["last_name"],

            telephone=validated_data["telephone"],

            ville=validated_data["ville"],

            type_parent=validated_data["type_parent"],

            role="PARENT"

        )


        for enfant in enfants:

            Enfant.objects.create(

                parent=user,

                **enfant

            )


        return user





class EnseignantRegisterSerializer(serializers.ModelSerializer):


    password = serializers.CharField(
        write_only=True
    )


    class Meta:

        model = User

        fields = [

            "first_name",
            "last_name",
            "email",
            "password",
            "matricule"

        ]


    def create(self, validated_data):


        user = User.objects.create_user(

            username=validated_data["email"],

            email=validated_data["email"],

            password=validated_data["password"],

            first_name=validated_data["first_name"],

            last_name=validated_data["last_name"],

            matricule=validated_data["matricule"],

            role="ENSEIGNANT"

        )


        return user





class AdminRegisterSerializer(serializers.ModelSerializer):


    password = serializers.CharField(
        write_only=True
    )


    class Meta:

        model = User

        fields=[

            "first_name",
            "last_name",
            "email",
            "password"

        ]



    def create(self, validated_data):


        user = User.objects.create_user(

            username=validated_data["email"],

            email=validated_data["email"],

            password=validated_data["password"],

            first_name=validated_data["first_name"],

            last_name=validated_data["last_name"],

            role="ADMIN"

        )


        return user