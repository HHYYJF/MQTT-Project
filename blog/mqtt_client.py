# # mqtt_client.py
# import paho.mqtt.client as mqtt
# import threading
#
#
# BROKER = "broker.hivemq.com"
# PORT = 1883
# USERNAME = "my_django_client"  # ← логин
# PASSWORD = "SuperSecretPass123!"  # ← пароль
#
# TOPIC_SUB = "test/mqttx/demo"
# TOPIC_PUB = "test/mqttx/response"
#
#
# def on_connect(client, userdata, flags, rc):
#     if rc == 0:
#         print("[MQTT] Успешно подключено к брокеру!")
#         client.subscribe(TOPIC_SUB)
#         print(f"[MQTT] Подписались на топик: {TOPIC_SUB}")
#     else:
#         print(f"[MQTT] Ошибка подключения, код: {rc}")
#
#
# def on_message(client, userdata, msg):
#     payload = msg.payload.decode()
#     print(f"[MQTT] Получено на '{msg.topic}': {payload}")
#
#     response = f"✅ Django получил: {payload}"
#     client.publish(TOPIC_PUB, response)
#     print(f"[MQTT] Отправлен ответ на '{TOPIC_PUB}': {response}")
#
#
# def start_mqtt():
#     client = mqtt.Client(client_id="django_mqtt_server_001")
#     client.username_pw_set(USERNAME, PASSWORD)
#
#     client.on_connect = on_connect
#     client.on_message = on_message
#
#     client.connect(BROKER, PORT, keepalive=60)
#
#     thread = threading.Thread(target=client.loop_forever, daemon=True)
#     thread.start()
#
#     print(f"[MQTT] Клиент запущен с пользователем: {USERNAME}")
#     return client