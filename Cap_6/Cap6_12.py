def convNota():
    notas = {'A+':4.3,'A':4,'A-':3.7,'B+':3.3,'B':3,'B-':2.7,'C+':2.3,'C':4,'C-':1.7,
            'D+':1.3,'D':1,'D-':0.7,'F+':0.3,'F':0,'F-':0.7}
    nota = input('Digite uma NOTA: ')
    if nota in notas:
        print(f'{notas[nota]}')

