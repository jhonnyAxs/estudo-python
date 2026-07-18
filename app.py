import os
restaurantes = [
    { 'nome': 'Restaurante A', 'categoria': 'Italiano', 'cnpj': 12345678901234, 'endereco': 'Rua A, 123', 'telefone': 11999999999, 'email': 'restaurantea@email.com', 'senha': 'senha123', 'ativo': False },
    { 'nome': 'Restaurante B', 'categoria': 'Brasileiro', 'cnpj': 98765432109876, 'endereco': 'Rua B, 456', 'telefone': 11988888888, 'email': 'restauranteb@email.com', 'senha': 'senha456', 'ativo': True }
]

def exibir_nome_app():
    print('Sabor express\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar/Desativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('''
          Obrigado por utilizar o Sabor Express''')
    
def retorno_menu():
    input('\nPressione Enter para voltar ao menu...\n')
    main()
    
def opcao_invalida():
    print('''
          Opção inválida''')
    retorno_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '-' * (len(texto) + 4)
    print(f'{linha}\n  {texto}\n{linha}\n')
    
def cadastrar_restaurante():
    exibir_subtitulo('Cadastrar restaurante')
    nome = input('Digite o nome do restaurante: ')
    categoria = input('Digite a categoria do restaurante: ')
    cnpj = int(input('Digite o CNPJ do restaurante: '))
    endereco = input('Digite o endereço do restaurante: ')
    telefone = int(input('Digite o telefone do restaurante: ')) 
    email = input('Digite o email do restaurante: ')
    senha = input('Digite a senha do restaurante: ')
    ativo = False  # Novo restaurante começa como inativo
    restaurante = {
        'nome': nome,
        'cnpj': cnpj,
        'endereco': endereco,
        'telefone': telefone,
        'email': email,
        'senha': senha,
        'categoria': categoria,
        'ativo': ativo
    }
    restaurantes.append(restaurante)
    print(f'''
        Restaurante cadastrado com sucesso!\nNome: {nome}\nCNPJ: {cnpj}\nEndereço: {endereco}\nTelefone: {telefone}\nEmail: {email}\nCategoria: {categoria}\nSituação: { "Ativo" if ativo else "Inativo" }'''    )
    retorno_menu()
    
def listar_restaurantes(): 
    exibir_subtitulo('Listar restaurantes')
    if len(restaurantes) == 0:
        print('Nenhum restaurante cadastrado.')
    else:
        for restaurante in restaurantes:
            print(f'''
                Nome: {restaurante['nome']}
                CNPJ: {restaurante['cnpj']}
                Endereço: {restaurante['endereco']} 
                Telefone: {restaurante['telefone']}
                Email: {restaurante['email']}
                Categoria: {restaurante['categoria']}''')
            situação = 'Ativo' if restaurante.get('ativo', False) else 'Inativo'
            print(f'Situação: {situação}\n')
    retorno_menu()

def ativar_desativar_restaurante():
    exibir_subtitulo('Ativar/Desativar restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar\\desativar: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante.lower() == restaurante['nome'].lower():
            restaurante['ativo'] = not restaurante['ativo']  # Alterna o status de ativo para inativo
            status = f'O restaurante {nome_restaurante} foi ativado com sucesso.' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso.'
            restaurante_encontrado = True
            print(status)
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado.')

    retorno_menu()


def escolher_opcao():
    try:
        opçao_escolhida = int(input('Escolha uma opção: \n'))
        if opçao_escolhida == 1:
            print('Cadastrar Restarante')
            cadastrar_restaurante()
        elif opçao_escolhida == 2:
            print('Listar Restaurante')
            listar_restaurantes()
        elif opçao_escolhida == 3:
            print('Ativar/Desativar restaurante')
            ativar_desativar_restaurante()
        elif opçao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()       

def main():
    os.system('cls')
    exibir_nome_app()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()