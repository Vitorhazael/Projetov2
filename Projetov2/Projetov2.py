entrada = input('[E]entrar [S]sair: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456' 

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('ENTRAR')

else:
    print('SAIR')    

# VOCE DIGITA O 'E' MAISCULO OU O 'e' MINUSCULO AI NA HORA DE DIGITAR A SENHA SO ENTRA COM A SENHA PERMITIDA '123456'