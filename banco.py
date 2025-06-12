def cabecalho():
    # Imprime o cabeçalho do sistema
    print("=" * 40)
    print("Sistema Bancário PY - Desenvolvido por João V.")
    print("=" * 40)

def menu_principal():
    # Exibe o menu e retorna a opção escolhida pelo usuário em minúsculo
    return input("""
Escolha uma opção:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """).lower()

def registrar_deposito(saldo, historico):
    # Solicita valor para depósito e atualiza saldo e histórico
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        historico += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor inválido. Tente novamente.")
    return saldo, historico

def processar_saque(saldo, historico, limite, saques_realizados, LIMITE_SAQUES):
    # Solicita valor para saque e realiza validações antes de atualizar saldo e histórico
    valor = float(input("Informe o valor do saque: "))
    if valor <= 0:
        print("Valor inválido para saque.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print(f"O valor máximo por saque é R$ {limite:.2f}.")
    elif saques_realizados >= LIMITE_SAQUES:
        print("Limite diário de saques atingido.")
    else:
        saldo -= valor
        historico += f"Saque: R$ {valor:.2f}\n"
        saques_realizados += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    return saldo, historico, saques_realizados

def exibir_historico(saldo, historico):
    # Exibe o extrato com todas as movimentações e o saldo atual
    print("\n===== EXTRATO =====")
    print(historico if historico else "Nenhuma movimentação registrada.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("====================\n")

def sair():
    # Mensagem de encerramento do sistema
    print("Encerrando o sistema. Obrigado por usar o Banco PY.")

def opcao_invalida():
    # Mensagem para opção inválida no menu
    print("Opção inválida. Tente novamente.")

def main():
    cabecalho()

    saldo_atual = 0
    limite_saque = 500
    historico_movimentos = ""
    saques_diarios = 0
    LIMITE_SAQUES = 3

    # Dicionário que mapeia as opções do menu para as funções correspondentes
    acoes = {
        'd': lambda: registrar_deposito(saldo_atual, historico_movimentos),
        's': lambda: processar_saque(saldo_atual, historico_movimentos, limite_saque, saques_diarios, LIMITE_SAQUES),
        'e': lambda: (exibir_historico(saldo_atual, historico_movimentos), (saldo_atual, historico_movimentos, saques_diarios)),
        'q': sair
    }

    while True:
        opcao = menu_principal()

        if opcao == 'q':
            sair()
            break

        # Obtém a função associada à opção ou usa opcao_invalida se não existir
        func = acoes.get(opcao, opcao_invalida)

        # Executa a função e atualiza os valores de saldo, histórico e saques se necessário
        resultado = func()
        if resultado:
            if opcao == 'd':
                saldo_atual, historico_movimentos = resultado
            elif opcao == 's':
                saldo_atual, historico_movimentos, saques_diarios = resultado

if __name__ == "__main__":
    main()
