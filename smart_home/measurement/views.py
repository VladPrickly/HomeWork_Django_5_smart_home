# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Sensor
from .serializers import SensorSerializer


@api_view(['GET', 'POST'])
def sensor_data(request):
    if request.method == 'GET':
        sensors = Sensor.objects.all()
        ser = SensorSerializer(sensors, many=True)
        # data = {'message': 'Hello'}
        return Response(ser.data)
    if request.method == 'POST':
        return Response({'status': 'OK'})