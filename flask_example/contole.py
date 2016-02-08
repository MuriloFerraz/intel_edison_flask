# Desenvolvido por: @muriloferraz125 - 02/2016


import mraa
import time
import os

# Importando o Flask
from flask import Flask, request, redirect, render_template, flash, Markup

# Importar script de leitura dos sensores
import sensorValues

# Declarando os leds e seus respectivos pinos
r_led = mraa.Gpio(2) # Vermelho
g_led = mraa.Gpio(3) # Verde
y_led = mraa.Gpio(4) # Amarelo ( deveria ser azul ne??? ;) )

# Definindo os pinos dos leds como saida digital
r_led.dir(mraa.DIR_OUT)
g_led.dir(mraa.DIR_OUT)
y_led.dir(mraa.DIR_OUT)

# criando o App Flask e toda a interacao com o usuario
app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/controle', methods = ['POST'])
def controller():
    buttonHit = request.form['buttonPress']
    print ("O botao pressionado foi: '" + buttonHit + "'")
    if buttonHit == 'Red_On':
        r_led.write(1) # acende o led Vermelho

    elif buttonHit == 'Red_Off':
        r_led.write(0) # desliga o led vermelho

    elif buttonHit == 'Yellow_On':
        y_led.write(1) 

    elif buttonHit == 'Yellow_Off':
        y_led.write(0)

    elif buttonHit == 'Green_On':
        g_led.write(1)
	
    elif buttonHit == 'Green_Off':
        g_led.write(0)

    elif buttonHit == 'Snap':
        # Tirar uma foto e salvar em ... (depende...)

        # Salvar no cartao SD
        # takepik ='fswebcam -d /dev/video0 -r 800x600 --no-banner /media/sdcard/pictures/IMG_%d%m%y-%H%M%S.jpg'
        #salvar na pasta: home/root/
        takepik ='fswebcam -d /dev/video0 -r 800x600 --no-banner /home/root/IMG_%d%m%y-%H%M%S.jpg'
        os.system(takepik)

    elif buttonHit =='Sensor':
        allSensorVal = " Temperatura: " + str("%.2f" %sensorValues.upm_temp()) + " C - Luminosidade: " + str("%.2f"%sensorValues.upm_light())
        
	flash(Markup(allSensorVal))
	print("valor dos sensores: '" + allSensorVal + "'")
        print (" Exibindo dados de sensores ")

    else:
        print("comando nao reconhecido :( ")

    return redirect('/')

if __name__=="__main__":
    # Ativar o streaming dde imagem da webcam
    os.system('mjpg_streamer -i "input_uvc.so -y -n -f 30 -r 176x144" -o "output_http.so -p 8080 -n -w /www"') # 176 x 144 @ 30 fps
    app.run(host='0.0.0.0', port=800, debug = True)
