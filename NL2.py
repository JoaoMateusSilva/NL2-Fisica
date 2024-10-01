import math

h = 6.626e-34
c = 3.0e8
eV_para_joules = 1.602e-19
R_H = 2.18e-18

def atomo_bohr(n):
    r_orbita = (n**2 * 5.29e-11)
    v_eletron = (2.18e6 / n)
    K_joules = R_H / (n**2)
    U_joules = -2 * K_joules
    E_total_joules = K_joules + U_joules
    λ_eletron = h / (9.10938356e-31 * v_eletron)

    print(f"Para n = {n}:")
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

    E_fóton = R_H * (1 / n_final**2 - 1 / n_inicial**2)
    ν_fóton = E_fóton / h
    λ_fóton = c / ν_fóton

    print(f"Transição de n = {n_inicial} para n = {n_final}:")
    print(f"Energia do fóton (E_fóton): {E_fóton:.4e} J")
    print(f"Frequência do fóton (ν_fóton): {ν_fóton:.4e} Hz")
    print(f"Comprimento de onda do fóton (λ_fóton): {λ_fóton:.4e} m")


def calcular_n_com_foton(n_inicial=None, n_final=None, ν_fóton=None, λ_fóton=None):
    if λ_fóton is not None:
        ν_fóton = c / λ_fóton
    if ν_fóton is None:
        print("Você precisa fornecer a frequência (ν_fóton) ou o comprimento de onda (λ_fóton).")
        return

    E_fóton = h * ν_fóton

    if n_inicial is not None:
        
        E_n_inicial = R_H / n_inicial**2
        E_n_final = E_n_inicial - E_fóton
        
        if E_n_final <= 0:
            print("Transição impossível com os valores fornecidos.")
            return
        n_final = math.sqrt(R_H / E_n_final)
        
        print(f"Com base na energia do fóton, o estado final é: {n_final:.2f} (decimal) ou {round(n_final)} (inteiro)")

    elif n_final is not None:
        E_n_final = R_H / n_final**2
        E_n_inicial = E_n_final + E_fóton
        if E_n_inicial <= 0:
            print("Transição impossível com os valores fornecidos.")
            return
        n_inicial = math.sqrt(R_H / E_n_inicial)
        print(f"Com base na energia do fóton, o estado inicial é: {n_inicial:.2f} (decimal) ou {round(n_inicial)} (inteiro)")

    else:
        print("Você precisa fornecer ou n_inicial ou n_final.")

def calcular_energia_foton(ν_fóton=None, λ_fóton=None):
    if ν_fóton is not None:
        E_fóton = h * ν_fóton
    elif λ_fóton is not None:
        ν_fóton = c / λ_fóton
        E_fóton = h * ν_fóton
    else:
        print("Você precisa fornecer a frequência (ν_fóton) ou o comprimento de onda (λ_fóton) do fóton.")
        return

    E_fóton_ev = E_fóton / eV_para_joules
    print(f"Energia do fóton: {E_fóton:.4e} J ({E_fóton_ev:.4e} eV)")

def calcular_comprimento_onda(E_fóton=None, E_fóton_ev=None):
    if E_fóton_ev is not None:
        E_fóton = E_fóton_ev * eV_para_joules

    if E_fóton is not None:
        ν_fóton = E_fóton / h
        λ_fóton = c / ν_fóton
        print(f"Comprimento de onda do fóton: {λ_fóton:.4e} m")
    
    else:
        print("Você precisa fornecer a energia do fóton em Joules ou eV.")

def conversao_unidades():
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
            Hz = float(input("Digite o valor em Hz: "))
            THz = Hz / 1e12
            print(f"{Hz:.4e} Hz equivale a {THz:.4e} THz")
    
        elif opcao_conv == 6:
            THz = float(input("Digite o valor em THz: "))
            Hz = THz * 1e12
            print(f"{THz:.4e} THz equivale a {Hz:.4e} Hz")
        
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
        print("3 - Calcular n_final ou n_inicial com ν_fóton ou λ_fóton")
        print("4 - Calcular energia do fóton (fóton -> energia)")
        print("5 - Calcular comprimento de onda do fóton (energia -> λ)")
        print("6 - Fazer conversão de unidades")
        print("0 - Sair")
        
        opcao = int(input("Digite a opção: "))
        
        if opcao == 1:
            n = int(input("Digite o número quântico n: "))
            atomo_bohr(n)
        
        elif opcao == 2:
            n_inicial = int(input("Digite o valor de n inicial: "))
            n_final = int(input("Digite o valor de n final: "))
            energia_foton(n_inicial, n_final)
        
        elif opcao == 3:
            escolha = int(input("Deseja fornecer (1) n inicial ou (2) n final? "))
            if escolha == 1:
                n_inicial = int(input("Digite o valor de n inicial: "))
                ν_fóton = float(input("Digite a frequência do fóton (Hz) ou comprimento de onda (m): "))
                λ_fóton = None
                try:
                    calcular_n_com_foton(n_inicial=n_inicial, ν_fóton=ν_fóton, λ_fóton=λ_fóton)
                except:
                    print("Erro nos valores inseridos.")
            elif escolha == 2:
                n_final = int(input("Digite o valor de n final: "))
                ν_fóton = float(input("Digite a frequência do fóton (Hz) ou comprimento de onda (m): "))
                λ_fóton = None
                try:
                    calcular_n_com_foton(n_final=n_final, ν_fóton=ν_fóton, λ_fóton=λ_fóton)
                except:
                    print("Erro nos valores inseridos.")
        
        elif opcao == 4:
            ν_fóton = float(input("Digite a frequência do fóton (Hz) ou comprimento de onda (m): "))
            calcular_energia_foton(ν_fóton=ν_fóton)
        
        elif opcao == 5:
            energia_fóton = float(input("Digite a energia do fóton (J ou eV): "))
            unidade = input("A energia está em (J) ou (eV)? ")
            if unidade == "J":
                calcular_comprimento_onda(E_fóton=energia_fóton)
            elif unidade == "eV":
                calcular_comprimento_onda(E_fóton_ev=energia_fóton)
        
        elif opcao == 6:
            conversao_unidades()
        
        elif opcao == 0:
            print("Saindo...")
            break
        
        else:
            print("Opção inválida.")

main()
