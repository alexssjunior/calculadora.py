#calculadora simples 

def calculadora():
    while True:
        print("\n1. Somar | 2. Subtrair | 3. Multiplicar | 4. Dividir | 5. Sair")
        escolha = input("Escolha uma operação (1/2/3/4/5): ")

        if escolha == '5':
            print("Saindo... Obrigado por usar a calculadora!")
            break

        if escolha in ['1', '2', '3', '4']:
            num1 = float(input("Primeiro número: "))
            num2 = float(input("Segundo número: "))

            if escolha == '1': print(f"Resultado: {num1 + num2}")
            elif escolha == '2': print(f"Resultado: {num1 - num2}")
            elif escolha == '3': print(f"Resultado: {num1 * num2}")
            elif escolha == '4': print(f"Resultado: {num1 / num2 if num2 != 0 else 'Erro! Divisão por zero.'}")
        else:
            print("Opção inválida. Tente novamente.")

calculadora()
