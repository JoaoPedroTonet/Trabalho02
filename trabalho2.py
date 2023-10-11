import hashlib

class User:
    def __init__(self, nome, password, atribuicao):
        self.__setNome(nome)
        self.__password_hash = self.__hash_password(password)
        self.__setAtribuicao(atribuicao)

    def __setNome(self, nome):
        if not (3 <= len(nome) <= 25):
            raise ValueError('Nome deve ter entre 3 e 25 caracteres')
        if not nome[0].isupper():
            raise ValueError('Nome deve começar com uma letra maiuscula')
        if not all(char.isalnum() or char.isspace() for char in nome):
            raise ValueError('Nome deve ter apenas caracteres alfanumericos')
        self.__nome = nome

    def __hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def __setAtribuicao(self, atribuicao):
        if atribuicao not in [1, 2, 3]:
            raise ValueError('Nivel de acesso deve ser 1, 2, ou 3')
        self.__atribuicao = atribuicao

    def verify_password(self, password):
        return self.__password_hash == self.__hash_password(password)

    def verify_atribuicao(self, atribuicao):
        return self.__atribuicao == self.atribuicao

def main():
    # Exemplo de usuario
    # user: Sel
    # password: usp
    user = User('Sel', 'usp', 3)

    input_userName = input('User name: ')
    input_userPassword = input('Password: ')

    # Verifica o usuario e senha
    if input_userName == user._User__nome and user.verify_password(input_userPassword):
        print(f'OK - Atribuicao = {user._User__atribuicao}')
    else:
        print('Acesso negado')

if __name__ == '__main__':
    main()
