#esta questão deve ser usada no shell. Basta copiar e colar.

def paga(valo, hora):
    h_ext = 0
    if hora > 40:
        h_ext = hora - 40
        return (hora*valo) + (h_ext*1.5) 
    return (hora*valo)

# para valores acima de 40h não estou encontrando o valor da resposta do livro.
# ou o valor da resposta esta errado ou o cálculo da hora extra é outro 
# ou eu errei mesmo, kkk...   
