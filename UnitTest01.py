#Isto aqui é um comentário no código! Tudo que se escreve depois do '#' é ignorado pelo compilador.

#Def é usado para declarar uma função.
def funcaoSoma(a, b):
  total = 0;
  #Sonic vai escrever o código aqui dentro
  #Return retorna o valor obtido na variável
  return total;

def FuncaoMultiPlica(a, b):
  total = 0;
  #Sonic vai escrever a lógica da funcao multiplica aqui
  return total

#Aqui a framework valida os tests do Exercicio01
resultado1 = funcaoSoma(3,2);
resultado2 = funcaoSoma(5,1);
resultado3 = funcaoSoma(8,10);
resultado4 = FuncaoMultiPlica(2, 2);
resultado5 = FuncaoMultiPlica(5, 5);
resultado6 = FuncaoMultiPlica(2, 10);

print("Rodando testes");
assert(resultado1) == 5, f'Esperava encontrar 5 e encontrou {resultado1}';
assert(resultado2) == 6, f'Esperava encontrar 6 e encontrou {resultado2}';
assert(resultado3) == 18, f'Esperava encontrar 18 e encontrou {resultado3}';
assert(resultado4) == 4, f'Esperava encontrar 4 e encontrou {resultado4}';
assert(resultado5) == 25, f'Esperava encontrar 25 e encontrou {resultado5}';
assert(resultado6) == 20, f'Esperava encontrar 25 e encontrou {resultado6}';
print("Testes passaram!");

#Se passou não vai dar nenhuma mensagem de erro! 