#  Monitoramento de Temperatura e Umidade com  Sensor AHT10

Este projeto utiliza o sensor digital **AHT10** para medir **temperatura** e **umidade** do ambiente. As leituras são exibidas em um **display OLED SSD1306 128x64**, com alertas visuais para condições críticas (umidade alta ou temperatura baixa).

---

## Componentes Utilizados

| Componente        | Descrição                                       |
|-------------------|--------------------------------------------------|
| Raspberry Pi Pico | Microcontrolador                                |
| AHT10             | Sensor digital de temperatura e umidade (I2C)   |
| Display OLED      | SSD1306 128x64, comunicação via SoftI2C         |

---

## Conexões dos Pinos

| Função               | Pino (RP2040) |
|----------------------|---------------|
| AHT10 SDA            | GP2           |
| AHT10 SCL            | GP3           |
| OLED SDA (SoftI2C)   | GP14          |
| OLED SCL (SoftI2C)   | GP15          |

---

## Funcionamento do Código

### 🔹 Inicialização
- O sensor AHT10 recebe um comando de inicialização via I2C.
- O display OLED é iniciado usando SoftI2C.

### 🔹 Leitura do Sensor
- A cada 2 segundos, o AHT10 realiza uma nova medição.
- O sensor envia 6 bytes com os dados de temperatura e umidade.
- O código converte esses dados brutos para **°C** e **% de umidade relativa**.

### 🔹 Exibição no Display OLED
- O display mostra:
  - Temperatura atual (`Temp: xx.xx C`)
  - Umidade atual (`Umi : xx.xx %`)
- Alertas exibidos:
  - `"Umidade Alta!"` se a umidade for maior que **70%**
  - `"Temp Baixa!"` se a temperatura for menor que **20 °C**

### 🔹 Tratamento de Erros
- Se o sensor estiver ocupado ou falhar, o sistema exibe:  
  **"Erro na leitura!"** no display e imprime o erro no console.

---

## Comportamento Real

| Situação                    | Display OLED                   |
|-----------------------------|---------------------------------|
| Condições normais           | Temperatura e umidade atuais   |
| Umidade > 70%               | Mostra alerta "Umidade Alta!"  |
| Temperatura < 20 °C         | Mostra alerta "Temp Baixa!"    |
| Erro na leitura             | "Erro na leitura!"             |

---

## Conclusão

- Leituras confiáveis de **temperatura e umidade**
- Alertas visuais simples e diretos no OLED

---
