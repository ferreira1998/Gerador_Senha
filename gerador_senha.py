import string 

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)


import random 
random.choice(string.digits)

random.choices(string.digits, k=5)

escolhas = random.choices(string.digits, k=5)
print(escolhas)

random.shuffle(escolhas)
print(escolhas)

def gerar_senha(tamanho):
    if tamanho < 4:
       print("O tamanho da senha deve ser de pelo menos 4 caracteres")
    else:
        senha = [
            random.choice(string.ascii_letters),
            random.choice(string.digits),
            random.choice(string.punctuation),
        ]
        possibilidades = "".join([string.ascii_letters, string.digits, string.punctuation])
        senha.extend(random.choices(possibilidades, k=tamanho-3))
        
        random.shuffle(senha)
        
        return "".join(senha)
    
tamanho = int(input("Digite comprimento da senha: "))
print(gerar_senha(tamanho))
