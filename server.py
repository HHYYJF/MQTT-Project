import asyncio
import ssl
from gmqtt import Client

async def on_message(client, topic, payload, qos, properties):
    print("ПРИШЛО ОТ SIM800C:", payload.decode())

async def main():
    ssl_ctx = ssl.create_default_context()
    ssl_ctx.check_hostname = False
    ssl_ctx.verify_mode = ssl.CERT_NONE

    client = Client("server")
    client.on_message = on_message
    client.set_auth_credentials("sim800_test", "Grok2025")
    
    await client.connect("0.0.0.0", 8883, ssl=ssl_ctx)
    client.subscribe("#")
    print("MQTTS сервер запущен на 8883 — жду SIM800C...")
    await asyncio.sleep(365*24*3600)

asyncio.run(main())
