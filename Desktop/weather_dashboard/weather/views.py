

import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_weather(request):
    user = request.user
    api_key = settings.WEATHER_API_KEY

    if user.location_city and user.location_country:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={user.location_city},{user.location_country}&appid={api_key}&units=metric'
    elif user.latitude and user.longitude:
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={user.latitude}&lon={user.longitude}&appid={api_key}&units=metric'

    else:
        return Response({'error': 'Location not set'}, status=400)

    res = requests.get(url)
    data = res.json()
    print(data)


    if res.status_code == 200:
        return Response({
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'condition': data['weather'][0]['description'],
            'wind_speed': data['wind']['speed']
        })
    else:
        return Response({'error': 'Unable to fetch weather'}, status=400)


