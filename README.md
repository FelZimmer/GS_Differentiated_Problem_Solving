# ☀️ AURON - Plataforma de Proteção Contra Anomalias Solares

## 📖 Sobre o Projeto

AURON é uma solução desenvolvida para simular os impactos financeiros causados por tempestades solares em infraestruturas críticas, como data centers, redes elétricas e usinas de energia solar.

O sistema utiliza modelos matemáticos para representar o comportamento dos danos causados por eventos solares e demonstrar como a automação pode reduzir prejuízos através de uma resposta rápida e inteligente.

O projeto foi desenvolvido como parte da disciplina **Differentiated Problem Solving (DPS)** da FIAP.

---

## 🎯 Objetivo

Demonstrar, por meio de modelagem matemática e simulação computacional, como tempestades solares podem gerar impactos financeiros significativos e como sistemas automatizados podem minimizar esses danos.

---

## 🚀 Funcionalidades

* Simulação da intensidade de tempestades solares.
* Cálculo do dano financeiro potencial utilizando função polinomial.
* Simulação do crescimento do dano ao longo do tempo através de função exponencial.
* Comparação entre cenário sem proteção e cenário protegido pela AURON.
* Geração de gráficos para análise visual dos resultados.
* Menu interativo para navegação pelo sistema.

---

## 🧮 Modelagem Matemática

### Função Polinomial

Relaciona a intensidade da tempestade solar com o dano financeiro estimado:

D(x) = ax² + bx + c

Onde:

* D(x): dano financeiro estimado.
* x: intensidade da tempestade solar (nT).
* a, b e c: coeficientes aleatórios utilizados na simulação.

---

### Função Exponencial

Representa o crescimento do dano ao longo do tempo:

D(t) = D₀ · e^(kt)

Onde:

* D(t): dano acumulado.
* D₀: dano inicial.
* k: taxa de crescimento.
* t: tempo sem proteção.

Após 15 minutos, a plataforma AURON realiza uma ação automática de contenção, interrompendo o crescimento dos danos.

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* Math
* Random
* Matplotlib

---

## 📂 Estrutura do Projeto

```text
AURON/
│
├── auron.py
├── README.md
├── relatorio_matematico.pdf
└── imagens/
    ├── menu.png
    ├── simulacao1.png
    └── simulacao2.png
```

## ▶️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/auron.git
```

### 2. Acesse a pasta do projeto

```bash
cd auron
```

### 3. Instale as dependências

```bash
pip install matplotlib
```

### 4. Execute o programa

```bash
python auron.py
```

---

## 🌎 Relação com a Indústria Espacial

Tempestades solares são fenômenos originados pela atividade do Sol capazes de afetar satélites, sistemas de comunicação, data centers e redes elétricas.

A proposta da AURON é utilizar monitoramento e automação para reduzir os impactos desses eventos, contribuindo para infraestruturas mais resilientes e seguras.

---

## 📊 Resultados Esperados

O sistema demonstra que:

* O aumento da intensidade de uma tempestade solar pode gerar crescimento acelerado dos danos.
* A ausência de resposta rápida aumenta significativamente os prejuízos.
* Sistemas automatizados de proteção conseguem reduzir perdas financeiras e operacionais.

---

## 👨‍💻 Integrantes

| RM     | Nome                          |
| ------ | ----------------------------- |
| 570860 | Esther Tozzo                  |
| 570863 | Felipe de Oliveira Zimmermann |
| 570316 | Izabela Pordeus               |
| 569949 | João Victor Santos Souza      |
| 571458 | Matheus Lopes Lima            |

---

## 🎓 Instituição

FIAP – Faculdade de Informática e Administração Paulista

Disciplina: Differentiated Problem Solving (DPS)

Professor: Prof. Rodolfo Paiva / Prof. Fernando Pizzo


2026
