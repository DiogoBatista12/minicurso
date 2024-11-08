import DAO

saida = DAO.inserir_usuario('diogoqgbatista@gmail.com','Diogo','diogo123')
#saida = DAO.buscar_usuario('Diogo')
#saida = DAO.atualizar_usuario('2','Diogo Queiroga','juracema123@gmail.com')
#print(saida)
saida = DAO.deletar_usuario('2')
print(saida)

inserir = input('Digite seu nome: ')
email = input('Digite seu e-mail: ')
senha = input('Digite sua senha: ')
DAO.inserir_usuario(inserir,email,senha)
print(inserir)