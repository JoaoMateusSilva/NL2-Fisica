import math

# Constantes físicas
h = 6.626e-34  # Constante de Planck (J·s)
c = 3.0e8  # Velocidade da luz no vácuo (m/s)
eV = 1.602e-19  # 1 eV = 1.602 × 10^−19 J (ainda usada para conversão se necessário)
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

def unit_conversion():
    while True:
        print("\nEscolha a conversão que deseja realizar:")
        print("1 - Metros para Nanômetros (m -> nm)")
        print("2 - Nanômetros para Metros (nm -> m)")
        print("3 - Joules para eV (J -> eV)")
        print("4 - eV para Joules (eV -> J)")
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
        
        elif opcao_conv == 3:
            joules = float(input("Digite o valor em Joules: "))
            ev = joules / eV
            print(f"{joules:.4e} Joules = {ev:.4e} eV")
        
        elif opcao_conv == 4:
            ev = float(input("Digite o valor em eV: "))
            joules = ev * eV
            print(f"{ev:.4e} eV = {joules:.4e} Joules")
        
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

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Calcular propriedades para um valor de n")
        print("2 - Calcular energia e frequência de fóton emitido/absorvido")
        print("3 - Fazer conversão de unidades")
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
            unit_conversion()
        
        elif opcao == 0:
            print("Saindo...")
            break
        
        else:
            print("Opção inválida.")

main()
