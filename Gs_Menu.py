import math
import random
import matplotlib.pyplot as plt


def menu():
    print("Plataforma de Proteção Solar B2B")
    print(" 1. Calcular dano causado por anomalia")
    print(" 2. Sobre a solução")
    print(" 3. Sair ")


def funcao_polinomial(ax):
    # Relação entre intensidade da tempestade solar (nT) e o dano causado
    # D(x) = ax² + bx + c — cresce de forma não linear com a intensidade

    a = random.uniform(0.8, 1.5)
    b = random.uniform(-120, -80)   
    c = random.uniform(-5000, 5000)
    x_max = random.radiant (0, 500)

    intensidade = []
    danos = []
    

    for x in range(0, x_max + 1):
        dx = a * x**2 + b * x + c
        intensidade.append(x)
        danos.append(max(0, dx)) 

    ax.plot(intensidade, danos, color="#E8570D")
    ax.set_title("Intensidade da Tempestade Solar vs Dano")
    ax.set_xlabel("Intensidade da tempestade solar (nT)")
    ax.set_ylabel("Dano estimado (R$)")
    ax.grid(True)

    return max(danos)              


def funcao_exponencial(ax, dano_inicial):
    # Crescimento exponencial do dano sem proteção ativa
    # D(t) = D₀ · e^(kt)

    k = random.uniform(0.0, 0.12)

    tempos = []
    danos = []
    danos_com_auron = []

    for t in range(0, 121):
        dt = dano_inicial * math.exp(k * t)
        tempos.append(t)
        danos.append(dt)
        # Com Auron: automação acionada em t=15min — dano congela
        if t <= 15:
            danos_com_auron.append(dano_inicial * math.exp(k * t))
        else:
            danos_com_auron.append(danos_com_auron[-1])

    ax.plot(tempos, danos, color="#C0392B", label="Sem proteção")
    ax.plot(tempos, danos_com_auron, color="#00C2E0",linestyle="--", label="Com Auron (ação em t=15min)")
    ax.axvline(x=15, color="#F5923A", linestyle=":", label="Automação acionada")
    ax.set_title("Crescimento do Dano sem Proteção vs Com Auron")
    ax.set_xlabel("Tempo sem proteção (min)")
    ax.set_ylabel("Dano acumulado (R$)")
    ax.legend()
    ax.grid(True)

    return danos[-1]


def calcular_dano():
    try:
        fig, eixos = plt.subplots(1, 2, figsize=(14, 5))
        fig.suptitle("AURON — Simulação de Impacto de Anomalias Solares", fontsize=13, fontweight="bold")

        dano_maximo = funcao_polinomial(eixos[0])   

        print(f"\n Intensidade máxima simulada resultou em "f"R$ {dano_maximo:.2f} de dano potencial.")

        if dano_maximo > 0:
            print("Evento solar detectado — simulando crescimento do dano...")
            dano_final = funcao_exponencial(eixos[1], dano_maximo)
            print(f" Dano máximo sem proteção: R$ {dano_final:.2f}")
            print(f" Com a Auron (ação em t=15min), o dano foi contido.")
        else:
            eixos[1].set_visible(False)
            print(" Nenhum evento solar significativo detectado.")
            print("   A infraestrutura está segura — monitoramento ativo.")

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Erro encontrado: {e}")


def sobre():
    print("\n" + "="*50)
    print("AURON é uma plataforma B2B de monitoramento e")
    print("proteção contra anomalias solares. Integra dados")
    print("orbitais em tempo real com IA preditiva para")
    print("acionar automações de segurança em data centers")
    print("e instalações de energia solar.")
    print("="*50)


while True:
    menu()
    opcao = input("\nEscolha uma opção: ")

    match opcao:
        case "1":
            calcular_dano()
        case "2":
            sobre()
        case "3":
            print("\nSaindo do sistema Auron.")
            break
        case _:
            print(" Opção inválida. Tente novamente.")