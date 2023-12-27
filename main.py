from datetime import datetime

# Obtenemos la fecha y hora actual
fecha_hora_actual = datetime.now()

# Convertimos la fecha a un tipo de fecha con el formato deseado (año-mes-dia)
fecha_formateada = fecha_hora_actual.strftime('%Y-%m-%d')

print(type(fecha_formateada))
import datetime

print(datetime.date.today())