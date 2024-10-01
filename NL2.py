import math

# Constantes físicas
h = 6.626e-34  # Constante de Planck (J·s)
c = 3.0e8  # Velocidade da luz no vácuo (m/s)
R_H = 2.18e-18  # Constante de Rydberg (J)
e_charge = 1.60217662e-19  # Carga do elétron (C)
epsilon_0 = 8.854e-12  # Constante de permissividade do vácuo (F/m)
me = 9.10938356e-31  # Massa do elétron (kg)

# Função para calcular as propriedades do átomo de Bohr
def bohr_atom(n):
    # Raio da órbita (em metros)
    rn = (n**2 * 5.29e-11)  # Convertido para metros diretamente

    # Velocidade do elétron na órbita (em m/s)
    vn = (2.18e6 / n)

    # Energia cinética (em joules)
    Kn_joules = R_H / (n**2)

    # Energia potencial (em joules)
    Un_joules = -2 * Kn_joules

    # Energia total (em joules)
    En_joules = Kn_joules + Un_joules

    # Comprimento de onda do elétron (em metros)
    lambda_n = h / (me * vn)

    # Saída formatada
    print(f"Para n = {n}:")
    print(f"Raio da órbita (r_n): {rn:.4e} m")
    print(f"Velocidade do elétron (v_n): {vn:.4e} m/s")
    print(f"Energia cinética (K_n): {Kn_joules:.4e} J")
    print(f"Energia potencial (U_n): {Un_joules:.4e} J")
    print(f"Energia total (E_n): {En_joules:.4e} J")
    print(f"Comprimento de onda do elétron (λ_n): {lambda_n:.4e} m")
    
# Função para calcular a energia e frequência do fóton emitido/absorvido
def photon_energy(n_inicial, n_final):
    if n_final > n_inicial:
        print("Transição inválida: o estado final deve ser menor que o inicial.")
        return

    # Energia do fóton (em joules)
    E_foton_joules = R_H * (1 / n_final**2 - 1 / n_inicial**2)

    # Frequência do fóton (em Hz)
    f_foton = E_foton_joules / h

    # Comprimento de onda do fóton (em metros)
    lambda_foton = c / f_foton

    print(f"Transição de n = {n_inicial} para n = {n_final}:")
    print(f"Energia do fóton (E_foton): {E_foton_joules:.4e} J")
    print(f"Frequência do fóton (f_foton): {f_foton:.4e} Hz")
    print(f"Comprimento de onda do fóton (λ_foton): {lambda_foton:.4e} m")

# Função para encontrar n final ou n inicial dado f_foton ou λ_foton
def transition_with_photon(n_inicial=None, n_final=None, f_foton=None, lambda_foton=None):
    if f_foton:
        E_foton_joules = h * f_foton
    elif lambda_foton:
        f_foton = c / lambda_foton
        E_foton_joules = h * f_foton
    else:
        print("É necessário fornecer f_foton ou λ_foton.")
        return

    if n_inicial:
        E_n_inicial = R_H / n_inicial**2
        E_n_final = E_n_inicial - E_foton_joules
        n_final = math.sqrt(R_H / E_n_final)
        print(f"Estado final (n_final): {n_final:.2f} (decimal) ou {round(n_final)} (inteiro)")
    
    elif n_final:
        E_n_final = R_H / n_final**2
        E_n_inicial = E_n_final + E_foton_joules
        n_inicial = math.sqrt(R_H / E_n_inicial)
        print(f"Estado inicial (n_inicial): {n_inicial:.2f} (decimal) ou {round(n_inicial)} (inteiro)")

# Função de conversão de unidades
def conversor_de_unidades():
    while True:
        print("\nEscolha a conversão que deseja realizar:")
        print("1 - Metros para Nanômetros (m -> nm)")
        print("2 - Nanômetros para Metros (nm -> m)")
        print("5 - Hz para THz")
        print("6 - THz para Hz")
        print("0 - Sair da Conversão de unidades")
        opcao_conv = int(input("Digite a opção de conversão: "))
        
        if opcao_conv == 1:
            metros = float(input("Digite o valor em metros: "))
            nm = metros * 1e9
            print(f"{metros} metros = {nm:.4e} nanômetros")
        
        elif opcao_conv == 2:
            nm = float(input("Digite o valor em nanômetros: "))
            metros = nm / 1e9
            print(f"{nm:.4e} nanômetros = {metros:.4e} metros")
        
        elif opcao_conv == 5:
            hz = float(input("Digite o valor em Hz: "))
            thz = hz / 1e12
            print(f"{hz:.4e} Hz equivale a {thz:.4e} THz")
    
        elif opcao_conv == 6:
            thz = float(input("Digite o valor em THz: "))
            hz = thz * 1e12
            print(f"{thz:.4e} THz equivale a {hz:.4e} Hz")
        
        elif opcao_conv == 0:
            print("Saindo da conversão de unidades!")
            break
        
        else:
            print("Opção inválida.")

# Função principal
def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Calcular propriedades para um valor de n")
        print("2 - Calcular energia e frequência de fóton emitido/absorvido")
        print("3 - Transição com energia ou comprimento de onda do fóton")
        print("4 - Fazer conversão de unidades")
        print("0 - Sair")
        
        opcao = int(input("Digite a opção: "))
        
        if opcao == 1:
            n = int(input("Digite o número quântico n: "))
            bohr_atom(n)
        
        elif opcao == 2:
            n_inicial = int(input("Digite o valor de n inicial: "))
            n_final = int(input("Digite o valor de n final: "))
            photon_energy(n_inicial, n_final)
        
        elif opcao == 3:
            
            escolha = int(input("Deseja fornecer (1) n inicial ou (2) n final? "))
            
            if escolha == 1:
                n_inicial = int(input("Digite o valor de n inicial: "))
                f_foton = float(input("Digite a frequência do fóton (Hz) ou comprimento de onda (m): "))
                transition_with_photon(n_inicial=n_inicial, f_foton=f_foton)
            
            elif escolha == 2:
                n_final = int(input("Digite o valor de n final: "))
                f_foton = float(input("Digite a frequência do fóton (Hz) ou comprimento de onda (m): "))
                transition_with_photon(n_final=n_final, f_foton=f_foton)
        
        elif opcao == 4:
            conversor_de_unidades()
        
        elif opcao == 0:
            print("Saindo...")
            break
        
        else:
            print("Opção inválida.")

main()
