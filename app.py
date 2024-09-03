def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

def count_a(string):
    count = string.lower().count('a')
    return count

def calculate_soma():
    INDICE = 12
    SOMA = 0
    K = 1
    while K <= INDICE:
        SOMA = SOMA + K
        K = K + 1
    return SOMA

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Verificar se um número pertence à sequência de Fibonacci")
        print("2 - Contar quantas vezes a letra 'a' aparece em uma string")
        print("3 - Calcular o valor de SOMA")
        print("4 - Sair")
        choice = input("Opção: ")

        if choice == '1':
            numero = int(input("Informe um número: "))
            if is_fibonacci(numero):
                print(f"O número {numero} pertence à sequência de Fibonacci.")
            else:
                print(f"O número {numero} não pertence à sequência de Fibonacci.")
        elif choice == '2':
            string = input("Informe uma string: ")
            contagem = count_a(string)
            print(f"A letra 'a' aparece {contagem} vezes na string.")
        elif choice == '3':
            soma = calculate_soma()
            print(f"O valor de SOMA é {soma}.")
        elif choice == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
