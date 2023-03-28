from rest_framework import serializers

from measurement.models import Sensor, Measurement


# 1,4. Создать датчик, Получить список датчиков
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', ]


# 3. Добавить измерение
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor_id', 'temperature', 'image']


# 5. Для получения информации по конкретному датчику
class Measure2SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'date', 'image']


# 2,5. Изменить датчик, Получить информацию по конкретному датчику
class SensorFullSerializer(serializers.ModelSerializer):
    measurements = Measure2SensorSerializer(read_only=True, many=True)
    # measurements - ссылается на related_name='measurements' в классе Measurements

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
        # depth = 1 # автоматически добавляет вложенность, т.е. measurements в нашем случае

