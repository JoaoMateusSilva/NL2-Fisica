import math

h = 6.626e-34
c = 3.0e8
eV_para_joules = 1.602e-19
R_H = 2.18e-18

def introducao():
    texto = """
    Nomes:  João Mateus E. B. da Silva RA:22.223.013-8

            Heron De Souza RA:22.223.009-6

            Sergio de Siqueira Santos RA:22.124.082-3
            
            Vinicius Trivellato Pereira RA:22.223.022-9

    O programa fornecido é uma implementação que explora as propriedades do átomo de Bohr, como raio da órbita, energia cinética, energia potencial, e comprimento de onda do elétron, 
    além de calcular propriedades relacionadas à emissão e absorção de fótons. O programa também realiza conversões entre unidades e calcula níveis de energia baseados em frequências 
    ou comprimentos de onda fornecidos.

    O objetivo é permitir a compreensão e cálculo de propriedades de transições eletrônicas em um átomo, utilizando a teoria de Bohr, bem como realizar análises relacionadas à energia 
    dos fótons emitidos ou absorvidos. As principais limitações do programa estão associadas ao fato de que a teoria de Bohr se aplica de maneira mais adequada a sistemas atômicos 
    simplificados (como o hidrogênio),sendo menos precisa para átomos com múltiplos elétrons.

    Ele possibilita um estudo detalhado de conceitos fundamentais em física atômica, oferecendo suporte ao cálculo e interpretação dos fenômenos de transição energética em átomos 
    e propriedades associadas à radiação eletromagnética, como comprimento de onda e frequência dos fótons.
    """
    print(texto)

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

def calcular_n_com_foton(n_inicial=None, n_final=None, ν_fóton=None, λ_fóton=None):
    if ν_fóton is not None:
        E_fóton = h * ν_fóton
    
    elif λ_fóton is not None:
        ν_foton = c / λ_fóton
        E_foton = h * ν_foton
    
    else:
        print("Você precisa fornecer a frequência (ν_fóton) ou o comprimento de onda (λ_fóton) do fóton.")
        return

    if n_inicial is not None:
        E_n_inicial = R_H / n_inicial**2
        E_n_final = E_n_inicial - E_fóton
        if E_n_final <= 0:
            print("Transição impossível com os valores fornecidos.")
            return
        n_final = math.sqrt(R_H / E_n_final)
        print(f"O estado final é: {n_final:.2f} (decimal) ou {round(n_final)} (inteiro)")

    elif n_final is not None:
        E_n_final = R_H / n_final**2
        E_n_inicial = E_n_final + E_fóton
        if (1 - (E_fóton / R_H)) <= 0:
            print("Transição impossível com os valores fornecidos.")
            return
        n_inicial = math.sqrt(1 / (1 - E_fóton / R_H))
        print(f"O estado inicial é: {n_inicial:.2f} (decimal) ou {round(n_inicial)} (inteiro)")

    else:
        print("Você precisa fornecer ou n_inicial ou n_final.")

def calcular_energia_foton_completa():
    print("\nEscolha uma das opções para calcular as propriedades do fóton:")
    print("A. Entrada: frequência ou comprimento de onda do fóton")
    print("B. Entrada: energia do fóton (J ou eV)")

    escolha = input("\nDigite 'A' ou 'B': ").strip().upper()

    if escolha == 'A':
        tipo_foton = int(input("Você deseja fornecer (1) frequência ou (2) comprimento de onda? "))
        
        if tipo_foton == 1:
            ν_foton = float(input("Digite a frequência do fóton (Hz): "))
            E_foton = h * ν_foton
            E_foton_ev = E_foton / eV_para_joules
            print(f"Energia do fóton: {E_foton:.4e} J ou {E_foton_ev:.4e} eV")
        
        elif tipo_foton == 2:
            λ_foton = float(input("Digite o comprimento de onda do fóton (m): "))
            ν_foton = c / λ_foton
            E_foton = h * ν_foton
            E_foton_ev = E_foton / eV_para_joules
            print(f"Energia do fóton: {E_foton:.4e} J ou {E_foton_ev:.4e} eV")
        else:
            print("Opção inválida.")
    
    elif escolha == 'B':
        energia_foton = float(input("Digite a energia do fóton (J ou eV): "))
        unidade = input("A energia está em (J) ou (eV)? ").strip().lower()

        if unidade == 'j':
            E_foton = energia_foton
        
        elif unidade == 'ev':
            E_foton = energia_foton * eV_para_joules
        
        else:
            print("Unidade inválida. Use 'J' ou 'eV'.")
            return

        ν_foton = E_foton / h
        λ_foton = c / ν_foton
        print(f"Frequência do fóton: {ν_foton:.4e} Hz")
        print(f"Comprimento de onda do fóton: {λ_foton:.4e} m")
    
    else:
        print("Opção inválida. Escolha 'A' ou 'B'.")

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

def menu_principal():
    introducao()
    while True:
        print("\nEscolha uma das opções abaixo:")
        print("1 - Atomo de Bohr")
        print("2 - Energia do Fóton")
        print("3 - Calcular n inicial ou n final")
        print("4 - Calcular Energia do Fóton Completa")
        print("5 - Conversão de Unidades")
        print("0 - Sair")

        opcao = int(input("\nDigite o número da opção desejada: "))

        if opcao == 1:
            n = int(input("Digite o número quântico n: "))
            atomo_bohr(n)
        
        elif opcao == 2:
            n_inicial = int(input("Digite o número quântico inicial n_i: "))
            n_final = int(input("Digite o número quântico final n_f: "))
            energia_foton(n_inicial, n_final)

        elif opcao == 3:
            print("Informe se deseja calcular n inicial ou n final:")
            tipo = input("(1) n inicial ou (2) n final: ").strip()
            if tipo == '1':
                n_final = int(input("Digite o valor de n final: "))
                ν_fóton = float(input("Digite a frequência do fóton (Hz), ou deixe em branco se não souber: ") or 0)
                λ_fóton = float(input("Digite o comprimento de onda do fóton (m), ou deixe em branco se não souber: ") or 0)
                calcular_n_com_foton(n_final=n_final, ν_fóton=ν_fóton, λ_fóton=λ_fóton)
            elif tipo == '2':
                n_inicial = int(input("Digite o valor de n inicial: "))
                ν_fóton = float(input("Digite a frequência do fóton (Hz), ou deixe em branco se não souber: ") or 0)
                λ_fóton = float(input("Digite o comprimento de onda do fóton (m), ou deixe em branco se não souber: ") or 0)
                calcular_n_com_foton(n_inicial=n_inicial, ν_fóton=ν_fóton, λ_fóton=λ_fóton)

        elif opcao == 4:
            calcular_energia_foton_completa()

        elif opcao == 5:
            conversao_unidades()

        elif opcao == 0:
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu principal
menu_principal()
