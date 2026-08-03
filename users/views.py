from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate

from .serializers import (
    ParentRegisterSerializer,
    EnseignantRegisterSerializer,
    AdminRegisterSerializer
)




class ParentRegisterView(APIView):


    def post(self,request):

        serializer = ParentRegisterSerializer(
            data=request.data
        )


        if serializer.is_valid():

            serializer.save()

            return Response(
                {
                    "message":
                    "Compte parent créé"
                },
                status=201
            )


        return Response(
            serializer.errors,
            status=400
        )






class EnseignantRegisterView(APIView):


    def post(self,request):

        serializer = EnseignantRegisterSerializer(
            data=request.data
        )


        if serializer.is_valid():

            serializer.save()

            return Response(
                {
                    "message":
                    "Compte enseignant créé"
                }
            )


        return Response(
            serializer.errors,
            status=400
        )







class AdminRegisterView(APIView):


    def post(self,request):

        serializer = AdminRegisterSerializer(
            data=request.data
        )


        if serializer.is_valid():

            serializer.save()


            return Response(
                {
                    "message":
                    "Compte admin créé"
                }
            )


        return Response(
            serializer.errors,
            status=400
        )






class LoginView(APIView):

    def post(self, request):

        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user:

            return Response({
                "message": "Connexion réussie",
                "role": user.role,
                "email": user.email
            })

        return Response(
            {
                "error": "Email ou mot de passe incorrect"
            },
            status=400
        )