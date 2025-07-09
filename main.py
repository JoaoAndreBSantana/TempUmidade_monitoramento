from machine import Pin, I2C, SoftI2C
import time
from ssd1306 import SSD1306_I2C


# i2C do sensor  aht10 nos pinos GP3 SCL, GP2 SDA
i2c_sensor = I2C(1, scl=Pin(3), sda=Pin(2), freq=100_000)

#i2C do display olde nos pinos GP15 SCL, GP14 SDA
i2c_oled = SoftI2C(scl=Pin(15), sda=Pin(14))
oled = SSD1306_I2C(128, 64, i2c_oled)

# endereço i2c padrao do sensor
AHT10_ADDR = 0x38

# funções do sensor
def iniciar_aht10():
    #envia o comando de inicialização
    i2c_sensor.writeto(AHT10_ADDR, b'\xBE')
    time.sleep_ms(10)

def ler_aht10():
    #envia comando de medição
    i2c_sensor.writeto(AHT10_ADDR, b'\xAC\x33\x00')
    time.sleep_ms(80)

    # lendo 6 bytes do sensor
    data = i2c_sensor.readfrom(AHT10_ADDR, 6)

    # verifica se o primeiroo bit do primeiro byte tá pronto 
    if data[0] & 0x80:
        raise Exception("Sensor ocupado, tente novamente.")

    #processa temperatura e umidade 
    raw_hum = ((data[1] << 12) | (data[2] << 4) | (data[3] >> 4)) & 0xFFFFF
    raw_temp = ((data[3] & 0x0F) << 16) | (data[4] << 8) | data[5]

    hum = (raw_hum * 100.0) / 1048576.0
    temp = ((raw_temp * 200.0) / 1048576.0) - 50.0

    return temp, hum

#inicializar sensor
iniciar_aht10()

while True:
    try:
        temp, hum = ler_aht10()
        print("TEMPERATURA: {:.2f}  UMIDADE: {:.2f} %".format(temp, hum))

        # atualiza oled
        oled.fill(0)
        oled.text("Temp: {:.2f} C".format(temp), 0, 0)
        oled.text("Umi : {:.2f} %".format(hum), 0, 16)

        # monitora as condições
        if hum > 70:
            oled.text("Umidade Alta!", 0, 36)
        if temp < 20:
            oled.text("Temp Baixa!", 0, 48)

        oled.show()
        time.sleep(2)

    except Exception as e:
        print("Erro:", e)
        oled.fill(0)
        oled.text("Erro na leitura!", 0, 24)
        oled.show()
        time.sleep(2)