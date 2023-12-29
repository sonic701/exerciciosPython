#Aqui a gente faz as importações de recursos que vamos usar, por exemplo eu importei o "time" que é 
#um recurso do Python para fazer operações relacionadas a contar tempo, hora e etc.
import time;

#Isto aqui é um comentário no código! Tudo que se escreve depois do '#' é ignorado pelo compilador.

#Crie uma função usando a declaração "def funcaoSomaTresNumeros(a, b, c):"
#Igual o que foi feito no exercício anterior! 
#A função deverá retornar a soma de 3 numeros;
def funcaoSomaTresNumeros ( a ,b ,c ) : 
  return a+b+c 


#Aqui você deve criar uma função chamada funcaoDivide(a, b):
#A função deverá retornar a divisão de dois números que serão recebidos como parâmetros
def funcaoDivide (a,b):
  return  a/b  



#Aqui você deve criar uma função que vai receber primeiro o nome 
#E depois a idade do usuário. 
#No caso o usuário vai inserir seu nome e em seguida a idade.
#Então a função vai retornar um texto, dizendo: "Olá **** sua idade é de ** anos!"
#No lugar dos asteriscos é para aparecer os dados inseridos pelo usuário.
#Observação: 
# A função não vai usar "print", pois não é para mostrar os dados na tela, é para retornar o texto! 
#Exemplo: def funcaoInserirNomeIdade(): 
#Observação 2: 
# A função não vai receber parâmetros! Observe que os parênteses estão vazios.
# O nome do usuário e a idade deversão ser lidos usando a função input, como já vimos no passado
#Observação 3: A função deverá se chamar funcaoInserirNomeIdade, e não vai receber nenhum parâmetro.

def funcaoInserirNomeIdade ():
  nome = input (f'olá seu nome: ')
  idade = input (f'quantos anos você tem? ')
  soma = 1+1
  soma2 = "1" + "1"

  return  f'Olá {nome} sua idade é de {idade} em anos!'





















#Aqui pra baixo não deve mudar nada, aqui eu escrevi os testes.
#Aqui a framework valida os tests do Exercicio01
resultado1 = funcaoSomaTresNumeros(3,2,5);
resultado2 = funcaoSomaTresNumeros(5,1,1);
resultado3 = funcaoSomaTresNumeros(8,10,15);
resultado4 = funcaoDivide(4, 2);
resultado5 = funcaoDivide(10, 5);
resultado6 = funcaoDivide(20, 5);

resultado7 = funcaoInserirNomeIdade();

resEsperado1 = 10;
resEsperado2 = 7;
resEsperado3 = 33;
resEsperado4 = 2;
resEsperado5 = 2;
resEsperado6 = 4;

tempoTimer = 1;

print("Rodando testes");
time.sleep(tempoTimer);

assert(resultado1) == resEsperado1, f'Esperava encontrar 10 e encontrou {resultado1}';
print(f"Teste 1 passou! Esperava {resEsperado1} e encontrou {resultado1}");
time.sleep(tempoTimer);

assert(resultado2) == 7, f'Esperava encontrar 7 e encontrou {resultado2}';
print(f"Teste 2 passou! Esperava {resEsperado2} e encontrou {resultado2}");
time.sleep(tempoTimer);

assert(resultado3) == 33, f'Esperava encontrar 33 e encontrou {resultado3}';
print(f"Teste 3 passou! Esperava {resEsperado3} e encontrou {resultado3}");
time.sleep(tempoTimer);

assert(resultado4) == 2, f'Esperava encontrar 2 e encontrou {resultado4}';
print(f"Teste 4 passou! Esperava {resEsperado4} e encontrou {resultado4}");
time.sleep(tempoTimer);

assert(resultado5) == 2, f'Esperava encontrar 2 e encontrou {resultado5}';
print(f"Teste 5 passou! Esperava {resEsperado5} e encontrou {resultado5}");
time.sleep(tempoTimer);

assert(resultado6) == 4, f'Esperava encontrar 4 e encontrou {resultado6}';
print(f"Teste 6 passou! Esperava {resEsperado6} e encontrou {resultado6}");
time.sleep(tempoTimer);

print(f"Texto obtido:");
print(resultado7);

assert("Olá") in resultado7, f'Esperava encontrar Olá e não encontrou no texto';
print(f"Teste 7 passou! Encontro a palavra Olá no texto");
time.sleep(tempoTimer);

assert("sua idade é de") in resultado7, f'Esperava encontrar \"sua idade é de\" e não encontrou no texto';
print(f"Teste 7 passou! Encontro a palavra \"sua idade é de\" no texto");
time.sleep(tempoTimer);

assert("anos!") in resultado7, f'Esperava encontrar \"anos!\" e não encontrou no texto';
print(f"Teste 7 passou! Encontro a palavra \"anos!\" no texto");
time.sleep(tempoTimer);

print("Parabéns!!! Todos os testes passaram!");

#Se passou não vai dar nenhuma mensagem de erro! 