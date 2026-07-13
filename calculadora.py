def calculadora():
    while True:
        # 2. Exibir o menu com as opções
        print("\n--- Menu da Calculadora ---")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
       
        # 3. Capturar a escolha do usuário
        opcao = input("Escolha a operação desejada (1-5): ").strip()
       
        # Verificar se o usuário quer sair antes de pedir os números
        if opcao == '5':
            print("Obrigado por usar a calculadora! Até logo.") # 9. Mensagem de despedida
            break
           
        # 7. Tratamento de operação inválida
        if opcao not in ['1', '2', '3', '4']:
            print("Erro: Operação inválida! Por favor, escolha uma opção de 1 a 5.")
            continue
           
        # 4. Solicitar ao usuário que insira dois números
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: Por favor, insira apenas valores numéricos válidos.")
            continue

        # 5. Condicionais para executar a operação
        if opcao == '1':
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")
           
        elif opcao == '2':
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")
           
        elif opcao == '3':
            resultado = num1 * num2
            print(f"Resultado: {num1} * {num2} = {resultado}")
           
        elif opcao == '4':
            # 6. Verificação para evitar divisão por zero
            if num2 == 0:
                print("Erro: Não é possível dividir por zero!")
            else:
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado}")

        # 9. Perguntar se o usuário deseja realizar outra operação
        continuar = input("\nDeseja realizar outra operação? (s/n): ").strip().lower()
        if continuar != 's':
            print("Encerrando o programa. Até logo!") # Mensagem de despedida
            break

# Executar a calculadora
if __name__ == "__main__":
    calculadora()
