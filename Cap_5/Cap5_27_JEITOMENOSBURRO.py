def nota(nota):
    for i in range(len(nota)):
        if nota[0] == 'A':
            n_conv = 4
            if nota[i] == '-':
                esco = -0.3
            elif nota[i] == ' ':
                esco = 0
            elif nota[i] == '+':
                esco = +0.3
        if nota[0] == 'B':
            n_conv = 3
            if nota[i] == '-':
                esco = -0.3
            elif nota[i] == ' ':
                esco = 0
            elif nota[i] == '+':
                esco = +0.3
        if nota[0] == 'C':
            n_conv = 2
            if nota[i] == '-':
                esco = -0.3
            elif nota[i] == ' ':
                esco = 0
            elif nota[i] == '+':
                esco = +0.3
        if nota[0] == 'D':
            n_conv = 1
            if nota[i] == '-':
                esco = -0.3
            elif nota[i] == ' ':
                esco = 0
            elif nota[i] == '+':
                esco = +0.3
        if nota[0] == 'F':
            n_conv = 0
            if nota[i] == '-':
                esco = -0.3
            elif nota[i] == ' ':
                esco = 0
            elif nota[i] == '+':
                esco = +0.3
    print(f'{n_conv+esco}')    