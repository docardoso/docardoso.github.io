import agenda

ac = agenda.Agenda('agenda.db')

#O método filtra deve retornar uma lista no qual cada item é um par nome-contato
registro = ac.filtra('m')[1]

print(registro[0], '>>', registro[1])

#O método apaga deve retornar quantos registros foram apagados ao ser realizado
print(ac.apaga('multi'))

#O método todos também deve retornar uma lista no qual cada item é um par nome-contato
for registro in ac.todos():
    print(registro[0], '>>', registro[1])
