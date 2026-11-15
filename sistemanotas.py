VERDE = "\033[92m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
AZUL = "\033[94m"
ROXO = "\033[95m"
CIANO = "\033[96m"
RESET = "\033[0m"

MAX_NOTAS = 4
NOTA_MINIMA = 7

nomes = []   
notas = []

def ler_int(texto, minimo, maximo):

    while True:
        try:
            valor = int(input(texto))
        except ValueError:
            print(f"{VERMELHO}Digite um número inteiro.{RESET}")
            continue
        if minimo <= valor <= maximo:
            return valor
        print(f"{VERMELHO}Digite entre {minimo} e {maximo}.{RESET}")


def ler_nota(texto):

    while True:
        try:
            valor = float(input(texto).replace(",", "."))
        except ValueError:
            print(f"{VERMELHO}Digite um número.{RESET}")
            continue
        if 0 <= valor <= 10:
            return valor
        print(f"{VERMELHO}A nota vai de 0 a 10.{RESET}")


def escolher_aluno():

    print()
    for i in range(len(nomes)):
        print(f"{i + 1} - {nomes[i]}")
    return ler_int("Escolha o aluno: ", 1, len(nomes)) - 1


def cadastrar_alunos():
    qtd_alunos = ler_int("Quantos alunos quer adicionar? ", 1, 100)
    qtd_notas = ler_int(f"Quantas notas por aluno (máx {MAX_NOTAS})? ", 1, MAX_NOTAS)

    for i in range(qtd_alunos):
        print(f"\n--- Aluno {i + 1} ---")
        nome = input("Nome: ").strip()
        lista = []
        for n in range(qtd_notas):
            lista.append(ler_nota(f"Nota {n + 1}: "))
        nomes.append(nome)
        notas.append(lista)


def adicionar_nota():
    i = escolher_aluno()
    if len(notas[i]) >= MAX_NOTAS:
        print(f"{VERMELHO}{nomes[i]} já tem {MAX_NOTAS} notas.{RESET}")
        return
    notas[i].append(ler_nota("Nova nota: "))
    print(f"{VERDE}Nota adicionada.{RESET}")


def remover_nota():
    i = escolher_aluno()
    if len(notas[i]) == 0:
        print(f"{VERMELHO}{nomes[i]} não tem notas.{RESET}")
        return
    for n in range(len(notas[i])):
        print(f"{n + 1} - {notas[i][n]}")
    escolha = ler_int("Qual nota remover? ", 1, len(notas[i])) - 1
    removida = notas[i].pop(escolha)
    print(f"{VERDE}Nota {removida} removida.{RESET}")


def media_do_aluno(i):

    if len(notas[i]) == 0:
        return None
    return sum(notas[i]) / len(notas[i])


def calcular_media():
    i = escolher_aluno()
    media = media_do_aluno(i)
    if media is None:
        print(f"{VERMELHO}{nomes[i]} não tem notas.{RESET}")
        return
    print(f"{VERDE}Média de {nomes[i]}: {media:.2f}{RESET}")


def maior_menor():
    i = escolher_aluno()
    if len(notas[i]) == 0:
        print(f"{VERMELHO}{nomes[i]} não tem notas.{RESET}")
        return
    print(f"{VERDE}Maior nota de {nomes[i]}: {max(notas[i])}{RESET}")
    print(f"{AMARELO}Menor nota de {nomes[i]}: {min(notas[i])}{RESET}")


def situacao():
    print(f"\n{AZUL}--- Situação da turma ---{RESET}")
    for i in range(len(nomes)):
        media = media_do_aluno(i)
        if media is None:
            print(f"{nomes[i]}: sem notas")
        elif media >= NOTA_MINIMA:
            print(f"{VERDE}{nomes[i]}: média {media:.2f} - APROVADO{RESET}")
        else:
            print(f"{VERMELHO}{nomes[i]}: média {media:.2f} - RECUPERAÇÃO{RESET}")


def menu():
    print(f"\n{AZUL}========== MENU =========={RESET}")
    print(f"{VERDE}1 - Adicionar nota{RESET}")
    print(f"{VERMELHO}2 - Remover nota{RESET}")
    print(f"{AMARELO}3 - Calcular média{RESET}")
    print(f"{ROXO}4 - Ver maior e menor nota{RESET}")
    print(f"{CIANO}5 - Ver aprovados e recuperação{RESET}")
    print(f"0 - Sair")


def main():
    cadastrar_alunos()

    while True:
        menu()
        opcao = ler_int("Escolha: ", 0, 5)
        if opcao == 1:
            adicionar_nota()
        elif opcao == 2:
            remover_nota()
        elif opcao == 3:
            calcular_media()
        elif opcao == 4:
            maior_menor()
        elif opcao == 5:
            situacao()
        else:
            print("Até mais!")
            break


main()