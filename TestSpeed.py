import speedtest
from datetime import datetime
import pandas as pd
from threading import Timer

# função para gravar dados da velocidade da internet
def internet():
    df = pd.read_excel('dados.xlsx', sheet_name='base')
    s = speedtest.Speedtest()
    data_atual = datetime.now().strftime('%d/%m/%Y')
    hora_atual = datetime.now().strftime('%H:%M')
    velocidade_down = s.download(threads=None)*(10**-6)
    velocidade_up = s.upload(threads=None)*(10**-6)
    teste_ = "teste"
    df.loc[len(df)] = [data_atual, hora_atual, round(velocidade_down), round(velocidade_up), teste_ ]
    df.to_excel('dados.xlsx', sheet_name='base', index=False)
    Timer(5,internet).start()


internet()


