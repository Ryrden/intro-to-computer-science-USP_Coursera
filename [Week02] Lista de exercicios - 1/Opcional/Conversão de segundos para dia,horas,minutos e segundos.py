Stotal = int(input("Digite a quantidade de segundos que você deseja converter: "))

dia = Stotal // 3600 // 24
horas = (Stotal // 3600) % 24
minutos = (Stotal // 60) % 60
segundosFinal = Stotal % 60

print(dia, "dias,", horas, "horas,", minutos, "minutos e", segundosFinal, "segundos.")