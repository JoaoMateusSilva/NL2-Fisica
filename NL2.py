import math

# Constantes
h = 6.626e-34  # Constante de Planck (J·s)
c = 3.0e8  # Velocidade da luz no vácuo (m/s)
eV_para_joules = 1.602e-19  # Conversão de eV para Joules
R_H = 2.18e-18  # Constante de Rydberg (J)

# Função para calcular o raio da órbita, energia e outras propriedades do átomo de Bohr
def atomo_bohr(n):
    r_orbita = (n**2 * 5.29e-11)
    v_eletron = (2.18e6 / n)
    K_joules = R_H / (n**2)
    U_joules = -2 * K_joules
    E_total_joules = K_joules + U_joules
    λ_eletron = h / (9.10938356e-31 * v_eletron)

    print(f"\nPara n = {n}:")
    print(f"Raio da órbita (r_n): {r_orbita:.4e} m")
    print(f"Velocidade do elétron (v_n): {v_eletron:.4e} m/s")
    print(f"Energia cinética (K_n): {K_joules:.4e} J")
    print(f"Energia potencial (U_n): {U_joules:.4e} J")
    print(f"Energia total (E_n): {E_total_joules:.4e} J")
    print(f"Comprimento de onda do elétron (λ_n): {λ_eletron:.4e} m")

# Função para calcular energia e frequência de fótons emitidos ou absorvidos
def energia_foton(n_inicial, n_final):
    if n_final > n_inicial:
        print("Transição inválida: o estado final deve ser menor que o inicial.")
        return

    E_foton = R_H * (1 / n_final**2 - 1 / n_inicial**2)
    ν_foton = E_foton / h
    λ_foton = c / ν_foton

    print(f"\nTransição de n = {n_inicial} para n = {n_final}:")
    print(f"Energia do fóton (E_fóton): {E_foton:.4e} J")
    print(f"Frequência do fóton (ν_fóton): {ν_foton:.4e} Hz")
    print(f"Comprimento de onda do fóton (λ_fóton): {λ_foton:.4e} m")

# Função para calcular n_final ou n_inicial dado ν_fóton ou λ_fóton
def calcular_n_com_foton(n_inicial=None, n_final=None, ν_fóton=None, λ_fóton=None):
    
    if ν_fóton is not None:
        E_fóton = h * ν_fóton
    
    elif λ_fóton is not None:
        ν_fóton = c / λ_fóton
        E_fóton = h * ν_fóton
    
    else:
        print("Você precisa fornecer a frequência (ν_fóton) ou o comprimento de onda (λ_fóton) do fóton.")
        return

    if n_inicial is not None:
        # Cálculo para encontrar o nível final (n_final)
        E_n_inicial = R_H / n_inicial**2
        E_n_final = E_n_inicial - E_fóton
        if E_n_final <= 0:
            print("Transição impossível com os valores fornecidos.")
            return
        n_final = math.sqrt(R_H / E_n_final)
        print(f"O estado final é: {n_final:.2f} (decimal) ou {round(n_final)} (inteiro)")

    elif n_final is not None:
        # Cálculo correto do n_inicial
        E_n_final = R_H / n_final**2
        E_n_inicial = E_n_final + E_fóton
        if (1 - (E_fóton / R_H)) <= 0:
            print("Transição impossível com os valores fornecidos.")
            return
        n_inicial = math.sqrt(1 / (1 - E_fóton / R_H))
        print(f"O estado inicial é: {n_inicial:.2f} (decimal) ou {round(n_inicial)} (inteiro)")

    else:
        print("Você precisa fornecer ou n_inicial ou n_final.")

# Função atualizada para calcular a energia de um fóton, comprimento de onda ou frequência
def calcular_energia_foton_completa():
    print("\nEscolha uma das opções para calcular as propriedades do fóton:")
    print("A. Entrada: frequência ou comprimento de onda do fóton")
    print("B. Entrada: energia do fóton (J ou eV)")

    escolha = input("\nDigite 'A' ou 'B': ").strip().upper()

    if escolha == 'A':
        tipo_foton = int(input("Você deseja fornecer (1) frequência ou (2) comprimento de onda? "))
        
        if tipo_foton == 1:
            ν_foton = float(input("Digite a frequência do fóton (Hz): "))
            E_foton = h * ν_foton  # Energia do fóton em Joules
            E_foton_ev = E_foton / eV_para_joules  # Conversão para eV
            print(f"Energia do fóton: {E_foton:.4e} J ou {E_foton_ev:.4e} eV")
        
        elif tipo_foton == 2:
            λ_foton = float(input("Digite o comprimento de onda do fóton (m): "))
            ν_foton = c / λ_foton  # Frequência do fóton
            E_foton = h * ν_foton  # Energia do fóton em Joules
            E_foton_ev = E_foton / eV_para_joules  # Conversão para eV
            print(f"Energia do fóton: {E_foton:.4e} J ou {E_foton_ev:.4e} eV")
        else:
            print("Opção inválida.")
    
    elif escolha == 'B':
        energia_foton = float(input("Digite a energia do fóton (J ou eV): "))
        unidade = input("A energia está em (J) ou (eV)? ").strip().lower()

        if unidade == 'j':
            E_foton = energia_foton
        
        elif unidade == 'ev':
            E_foton = energia_foton * eV_para_joules  # Conversão de eV para Joules
        
        else:
            print("Unidade inválida. Use 'J' ou 'eV'.")
            return

        ν_foton = E_foton / h  # Frequência do fóton
        λ_foton = c / ν_foton  # Comprimento de onda do fóton
        print(f"Frequência do fóton: {ν_foton:.4e} Hz")
        print(f"Comprimento de onda do fóton: {λ_foton:.4e} m")
    
    else:
        print("Opção inválida. Escolha 'A' ou 'B'.")

# Função para conversão de unidades (metros para nanômetros, Hz para THz, etc.)
def conversao_unidades():
    while True:
        print("\nEscolha a conversão que deseja realizar:")
        print("1 - Metros para Nanômetros (m -> nm)")
        print("2 - Nanômetros para Metros (nm -> m)")
        print("3 - Hz para THz")
        print("4 - THz para Hz")
        print("0 - Sair da Conversão de unidades")
        opcao_conv = int(input("\nDigite a opção de conversão: "))
        
        if opcao_conv == 1:
            metros = float(input("Digite o valor em metros: "))
            nm = metros * 1e9
            print(f"{metros} metros = {nm:.4e} nanômetros")
        
        elif opcao_conv == 2:
            nm = float(input("Digite o valor em nanômetros: "))
            metros = nm / 1e9
            print(f"{nm:.4e} nanômetros = {metros:.4e} metros")
        
        elif opcao_conv == 3:
            Hz = float(input("Digite o valor em Hz: "))
            THz = Hz / 1e12
            print(f"{Hz:.4e} Hz equivale a {THz:.4e} THz")
    
        elif opcao_conv == 4:
            THz = float(input("Digite o valor em THz: "))
            Hz = THz * 1e12
            print(f"{THz:.4e} THz equivale a {Hz:.4e} Hz")
        
        elif opcao_conv == 0:
            print("Saindo da conversão de unidades!")
            break
        
        else:
            print("Opção inválida.")

# Função principal com o menu atualizado
def menu_principal():
    while True:
        print("\nEscolha uma das opções abaixo:")
        print("1 - Atomo de Bohr (Raio, Velocidade, Energia, etc.)")
        print("2 - Energia do Fóton e Comprimento de Onda (n_inicial, n_final)")
        print("3 - Calcular n_final ou n_inicial com ν_fóton ou λ_fóton")
        print("4 - Calcular Energia, Frequência ou Comprimento de Onda do Fóton")
        print("5 - Conversão de Unidades")
        print("0 - Sair")
        
        opcao = int(input("\nDigite o número da sua escolha: "))

        if opcao == 1:
            n = int(input("\nDigite o valor de n: "))
            atomo_bohr(n)
        
        elif opcao == 2:
            n_inicial = int(input("Digite o estado inicial (n_inicial): "))
            n_final = int(input("Digite o estado final (n_final): "))
            energia_foton(n_inicial, n_final)
        
        elif opcao == 3:
            n_inicial = int(input("Digite o estado inicial (n_inicial) ou 0 se não souber: "))
            n_final = int(input("Digite o estado final (n_final) ou 0 se não souber: "))
            ν_foton = float(input("Digite a frequência do fóton (Hz) ou 0 se não souber: "))
            λ_foton = float(input("Digite o comprimento de onda do fóton (m) ou 0 se não souber: "))
            calcular_n_com_foton(n_inicial if n_inicial != 0 else None, n_final if n_final != 0 else None, ν_foton if ν_foton != 0 else None, λ_foton if λ_foton != 0 else None)
        
        elif opcao == 4:
            calcular_energia_foton_completa()
        
        elif opcao == 5:
            conversao_unidades()
        
        elif opcao == 0:
            print("Saindo do programa!")
            break
        
        else:
            print("Opção inválida! Escolha uma opção válida.")

# Executa o menu principal
menu_principal()
