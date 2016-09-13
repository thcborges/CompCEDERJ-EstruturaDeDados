#include <stdio.h>
#include <stdlib.h>
void main() {
    /*Python tem um tratamento diferente para suas variaveis.
    Elas são objetos imutáveis que se referenciam a um determinado espaço da memória.
    Quando eu faço x = x + 1 em python, eu estou referenciando x a um novo
    espaço de memória com o valor de x + 1.
    Por exemplo, x = 42 (x aponta para um espaço de memória com valor = 42).
    Quando  eu faço x = x + 1, eu crio um novo espaço de memória e este passa a ter o valor 43.
    O espaço de memória com o valor 42 perde a referência então que ele tinha de x que passa a apontar outro
    espaço de memória.

    Sendo assim, torna-se impossível trabalhar com ponteiros como usado na aula 11A.
    Por esse motivo preferi usar C para escrever o código da aula por se tratar de uma
    linguagem que eu conheço e sei utilizar ponteiros.

    PARA ENTENDER O CÓDIGO:
    *p em C é semelhante ao p^ em pascal
    &x em C é semelhante ao @x em pascal*/

    int i, x;
    int *p;
    p = &i; // Para que se possa atribuir um valor a *p é preciso declarar uma variável e apontar o p para este endereço

    x = 19;
    *p = 34;
    //x = *p;
    printf("X = %d\n", x);

    printf("\n==================================\n\n");

    x = 19;
    p = &x;
    printf("Valor referenciado por P = %d\n", *p);
    printf("Endereco apontado por P = %d\n", p);
    printf("Endereco de X = %d\n", &x);


}
