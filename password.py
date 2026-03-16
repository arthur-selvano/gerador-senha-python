import random
import string

def gerar_senha(tamanho, usar_numeros, usar_simbolos):
    
    caracteres = string.ascii_letters
    
    if usar_numeros:
        caracteres += string.digits
        
    if usar_simbolos:
        caracteres += string.punctuation
    
    senha = ""
    
    for i in range(tamanho):
        senha += random.choice(caracteres)
        
    return senha


def main():
    
    try:
        tamanho = int(input("Digite o tamanho da senha: "))
        
        numeros = input("Incluir números? (s/n): ").lower() == "s"
        simbolos = input("Incluir símbolos? (s/n): ").lower() == "s"
        
        senha = gerar_senha(tamanho, numeros, simbolos)
        
        print("\nSenha gerada:")
        print(senha)
        
    except ValueError:
        print("Por favor, digite um número válido.")


main()