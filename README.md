# Design Label - webGenerator
Guía de instalación y ejecución del proyecto desarrollado por el grupo Design Label para la cursada 2024 de la materia Ingeniería de Software

## Requisitos previos

- Python 3.8

### Instrucciones

- Descargar el instalador correspondiente (https://www.python.org/downloads/release/python-380/) y ejecutarlo
- Tildar la opción "Add Python 3.8 to PATH" y seleccionar "Customize installation" ![](https://i.imgur.com/3qwTAJY.jpg)
- Corroborar que las opciones de la imagen estén tildadas y avanzar ![](https://i.imgur.com/FZkRxXy.jpg)
- Tildar las opciones "Install for all users" y "Add Python to enviroment variables" e instalar![](https://i.imgur.com/TOc9LXs.jpg)

## Instalación

### Requisitos previos

- Python 3.8

### Instrucciones

- Abrir una terminal como administrador y posicionarse en el directorio con el instalador.
- Ejecutar el comando ```py -3.8 installer.py```
- Finalizada la instalación, verifique que las siguientes entradas se encuentren en las variables de entorno del sistema:
    * PATH: C:\Program Files\Python38\
    * PATH: C:\Program Files\Python38\Scripts\
    * PATH: C:\ProgramData\chocolatey\bin
    * PATH: C:\Program Files\nodejs
- Y la siguiente entrada entre las variables de entorno del usuario:
    * PythonPath: Directorio del proyecto. Ejemplo: D:\Desarrollo\Ingenieria-de-Software-2024\Web-Generator
- Si todo está en orden reiniciar la PC. En caso de que falte alguna de las entradas agregarlas verificando que se correspondan con la instalación de Python, Chocolatey, Node y Web-Generator en su PC y reiniciarla.


### Configurar Ngrok

- Finalizada la instalación y después de reiniciar la PC, registrarse en https://dashboard.ngrok.com/
- Finalizado el registro y sin salir de la página serán redirigidos a un tutorial para la instalación en windows. De ese tutorial hay que copiar el comando con la forma ```ngrok config add-authtoken <SU_TOKEN>```
- Abrir un terminal y ejecutar ese comando tal cual se vea en la página

## Ejecución

### Requisitos previos

- Python 3.8
- Instalación completada

### Instrucciones
- Abrir una terminal y ejecutar el comando ```ngrok http 5005```
- Copiar la dirección que aparezca en la línea Forwarding antes de la "->"
- Abrir Web-Generator/chatbot/credentials.yml y en la línea webhook_url de la sección telegram pegar la dirección copiada + "/webhooks/telegram/webhook"
- Abrir la siguiente dirección https://api.telegram.org/bot6804076373:AAGVfw6smnTUmLXzReSdSmVHmcYvvempgI0/setWebhook?url=<WEBHOOK_URL> remplazando la parte final por la línea completa de la url en Credentials.yml
- Abrir dos terminales y en ambas posicionarse en el directorio "Web-Generator/venv/Scripts" y ejecutar el script "activate" (```./activate```) para activar el venv.
- Con el venv activado, posicionar ambas terminales en el directorio "Web-Generator/chatbot"
- En una de ellas ejecutar el comando ```rasa run```
- En la otra ejecutar el comando ```rasa run actions```
- Si no hay errores se le puede hablar al bot en https://t.me/webGeneratorBot