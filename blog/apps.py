from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

# from django.apps import AppConfig
#
# class MqttAppConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'mqtt_app'
#
#     def ready(self):
#         from .mqtt_client import start_mqtt
#         start_mqtt()