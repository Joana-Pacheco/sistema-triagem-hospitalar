# SISTEMA DE TRIAGEM DA JÔ

# [EXIGÊNCIA DE CÓDIGO 1 de 7]
# Implementação da Lista Encadeada Simples
class Nodo:
    def __init__(self, numero, cor):
        # Armazena o número do cartão
        self.numero = numero

        # Armazena a cor do cartão (A ou V)
        self.cor = cor

        # Ponteiro para o próximo paciente da fila
        self.proximo = None


class ListaEspera:
    def __init__(self):
        # Início da lista encadeada
        self.head = None

        # Contadores para gerar os cartões automaticamente
        self.contador_verde = 1
        self.contador_amarelo = 201

    # [EXIGÊNCIA DE CÓDIGO 2 de 7]
    # Inserção sem prioridade (pacientes verdes)
    def inserirSemPrioridade(self, nodo):
        # Começa pelo primeiro paciente da fila
        atual = self.head

        # Percorre a lista até o último paciente
        while atual.proximo is not None:
            atual = atual.proximo

        # Insere o paciente verde no final da fila
        atual.proximo = nodo

    # [EXIGÊNCIA DE CÓDIGO 3 de 7]
    # Inserção com prioridade (pacientes amarelos)
    def inserirComPrioridade(self, nodo):
        # Se o primeiro paciente for verde,
        # o paciente amarelo assume a primeira posição
        if self.head.cor == "V":
            nodo.proximo = self.head
            self.head = nodo

        else:
            atual = self.head

            # Percorre todos os pacientes amarelos
            while atual.proximo is not None and atual.proximo.cor == "A":
                atual = atual.proximo

            # Insere o novo amarelo após os demais amarelos
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    # [EXIGÊNCIA DE CÓDIGO 4 de 7]
    # Criação e inserção de pacientes na fila
    def inserir(self):
        # Solicita a cor do cartão
        cor = input("Informe a cor do cartão (A/V): ").upper()

        # Valida a entrada do usuário
        if cor != "A" and cor != "V":
            print("Cor inválida.")
            return

        # Gera a numeração automática dos cartões verdes
        if cor == "V":
            numero = self.contador_verde
            self.contador_verde += 1

        # Gera a numeração automática dos cartões amarelos
        else:
            numero = self.contador_amarelo
            self.contador_amarelo += 1

        # Cria o paciente
        nodo = Nodo(numero, cor)

        # Se a fila estiver vazia, o paciente será o primeiro
        if self.head is None:
            self.head = nodo

        # Pacientes verdes entram sem prioridade
        elif cor == "V":
            self.inserirSemPrioridade(nodo)

        # Pacientes amarelos entram com prioridade
        else:
            self.inserirComPrioridade(nodo)

        # Confirma a inserção do paciente
        print(f"Paciente com cartão {cor}{numero} adicionado à fila.")

    # [EXIGÊNCIA DE CÓDIGO 5 de 7]
    # Impressão da lista de espera
    def imprimirListaEspera(self):
        if self.head is None:
            print("A fila está vazia.")
            return

        atual = self.head

        print("\nLista de espera:")

        while atual is not None:
            print(f"[{atual.cor}, {atual.numero}]")
            atual = atual.proximo

        print()

    # [EXIGÊNCIA DE CÓDIGO 6 de 7]
    # Atendimento do primeiro paciente da fila
    def atenderPaciente(self):
        # Verifica se existe paciente na fila
        if self.head is None:
            print("Não há pacientes na fila.")
            return

        # Remove o primeiro paciente da fila
        paciente = self.head
        self.head = self.head.proximo

        # Exibe o paciente chamado
        print(
            f"Atendendo o paciente cartão cor "
            f"{paciente.cor} e número {paciente.numero}"
        )


# [EXIGÊNCIA DE CÓDIGO 7 de 7]
# Menu principal do sistema
fila = ListaEspera()

# Mantém o sistema funcionando até o usuário escolher sair
while True:
    print("\n1 - Adicionar paciente a fila")
    print("2 - Mostrar pacientes na fila")
    print("3 - Chamar paciente")
    print("4 - Sair")

    opcao = input(">> ")

    if opcao == "1":
        fila.inserir()

    elif opcao == "2":
        fila.imprimirListaEspera()

    elif opcao == "3":
        fila.atenderPaciente()

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")