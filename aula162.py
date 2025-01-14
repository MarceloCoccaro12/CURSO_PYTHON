# Criando dados com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DADOS', 'FORMATO')
# data e hora.agora()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para fusos horários
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime

# from pytz import timezone

data = datetime.now()
print(data.timestamp()) # Isso está na base de dados
print(datetime.fromtimestamp(1736817082))
# data_str_data = '2025/01/13 21:44:23'
# data_str_data = '13/01/2025'
# data_str_fmt = '%d/%m/%Y'

# data = datetime(2025, 1, 13, 21, 44, 23, tzinfo=timezone('Asia/Tokyo'))
# data = datetime.strptime(data_str_data, data_str_fmt)
