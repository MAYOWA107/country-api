from django.shortcuts import render
from .services import get_country_api
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache


class CountryAPI(APIView):
    def get(self, request, country):

        cache_key = f"country: {country.lower()}"

        cached_data = cache.get(cache_key)

        if cached_data:
            print("cache hit")
            return Response(cached_data)

        print("cache miss")
        data = get_country_api(country)

        if data is None:
            return Response(
                {"error": "Failed to load"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        cache.set(cache_key, data, timeout=60 * 60 * 12)
        return Response(data)
