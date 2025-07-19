  ● art.py:

    Criei esse arquivo apenas para colocar a logo em ACII

------------------------

  ● main.py:
    
    arquivo principal
    
------------------------

<img width="315" height="179" alt="image" src="https://github.com/user-attachments/assets/7966c76a-8811-484e-9b04-54324e01dd27" />

 ● Importei a logo e a armazenei em uma variável 
 
 ● Criei um while() para o programa continuar rodando até que o usuário não queira mais

------------------------

<img width="912" height="416" alt="image" src="https://github.com/user-attachments/assets/979e12e5-227e-4486-910b-ddc814ce8e23" />

● Criei uma lista contendo os 26 alfabetos

● Depois criei os inputs com as respostas do usuário e as armazenei em variáveis

------------------------

<img width="1017" height="496" alt="image" src="https://github.com/user-attachments/assets/d165ec83-16a2-4872-a89d-b3ec0c011449" />

● Criei uma função com 3 parãmetros = (1 - Direction: Se o usuário vai querer criptografar uma mensagem) (2 - text: Contém o texto do usuário) (3 - A quantidade de casas para trás ou para frente)

● Se o usuário quiser criptografar:

    Crio uma variável vazia que irá conter o texto criptografado

    Faço um loop For para verificar cada letra que o usuário digitou
      
      Se digitou algum caractere especial, números, espaços e outros elementos que não estão
      na lista de alfabetos, então apenas adiciono esse caractere à variável "cipher_text"
      sem precisar mexer na posição dela

    Porém se o caractere estiver na lista de alfabetos, então:

      Armazeno a posição dela usando index() e em seguida adiciono o número de casas que o usuário digitou na variável "shift"

      Verifico se essa posição é maior ou menor que o tamanho máximo ou mínimo da lista utilizando %=
      Dessa forma evito erro caso o usuário ultrapasse o limite da lista

      No final incremento com o caractere na lista de alfabetos na posição alterada da variável anterior

      Depois disso imprimo o resultado para o usuário

------------------------

<img width="941" height="437" alt="image" src="https://github.com/user-attachments/assets/fa3a3ef5-9d48-4e2b-aeb4-73697103f7d2" />

● É a mesma lógica que a criptografia, porém dessa vez está decodificando a mensagem, ou seja, apenas mudo o sinal para " - ".
  Dessa forma ao invés de ir para a direita no alfabeto, irá para a esquerda

------------------------

<img width="1315" height="318" alt="image" src="https://github.com/user-attachments/assets/90288ec6-0dc0-4be4-9799-28470f20b1a5" />

● Primeiramente, chamo a função e passo os argumentos (os inputs iniciais do usuário)

● Em seguida crio um input para saber se o usuário deseja ou não continuar com o programa

    Se sim, então limpo a tela

    Se não, defino a variável "over" para True, para que dessa forma o loop while() termine 
