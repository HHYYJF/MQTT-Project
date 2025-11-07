#!/bin/bash
echo "Запускаю Mosquitto с TLS..."

# Генерируем сертификат с SAN=IP (для SIM800C)
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=playit" -addext "subjectAltName=DNS:playit.gg,IP:127.0.0.1" >/dev/null 2>&1

# Конфиг Mosquitto
cat > mosquitto.conf << 'EOL'
listener 8883
certfile /config/cert.pem
keyfile /config/key.pem
allow_anonymous false
password_file /config/passwd
EOL

# Логин/пароль
mkdir -p config
docker run --rm -v $(pwd)/config:/config eclipse-mosquitto mosquitto_passwd -c /config/passwd sim800_test Grok2025

# Запускаем Mosquitto
docker run -d --name mqtt -p 8883:8883 -v $(pwd)/cert.pem:/config/cert.pem -v $(pwd)/key.pem:/config/key.pem -v $(pwd)/mosquitto.conf:/mosquitto.conf -v $(pwd)/config/passwd:/passwd eclipse-mosquitto

echo "Mosquitto запущен на 8883"

# Скачиваем playit.gg (бесплатный туннель без карты)
curl -SsL https://playit.gg/downloads/playit-macos_0.15.0 > playit
chmod +x playit

echo "Запускаю туннель playit.gg (нажми Enter, потом Claim tunnel)"
./playit
