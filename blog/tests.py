# mqtt_server.py — сохрани в ту же папку
import asyncio
import ssl
from mqtt import MQTTBroker

# Создаём брокер
broker = MQTTBroker()

# Логин/пароль
users = {"device_001": "SuperSecret123"}

async def auth(username, password):
    return users.get(username) == password

# SSL контекст
ssl_ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_ctx.load_cert_chain("cert.pem", "key.pem")  # key.pem сгенерируем ниже

# Запускаем на порту 8883 с TLS
async def main():
    await broker.start(
        host="0.0.0.0",
        port=8883,
        auth=auth,
        ssl=ssl_ctx
    )
    print("MQTTS брокер запущен на 8883 — жду SIM800C...")
    while True:
        await asyncio.sleep(3600)

# Печатаем все сообщения
@broker.on_topic("#")
async def print_all(msg):
    print(f"Пришло от SIM800C: {msg.payload.decode()} на топик {msg.topic}")

if __name__ == "__main__":
    asyncio.run(main())