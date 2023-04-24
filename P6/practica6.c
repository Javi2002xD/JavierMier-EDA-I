/*UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO
ESTRUCTURA DE DATOS Y ALGORITMOS
MIER RAMÍREZ JAVIER*/

#include <stdio.h>
#include <string.h>

size_t palindromo(int longitud);
char palabra[100];
int longitud, es_palindromo = 1;

int main() {

    printf("\n\n\tIntroduce una palabra: ");
    scanf("%s", palabra);

    longitud = strlen(palabra);
    palindromo(longitud);

    
}

size_t palindromo(int longitud){

    for(int i = 0; i < longitud / 2; i++) {
        if(palabra[i] != palabra[longitud-i-1]) {
            es_palindromo = 0;
            break;
        }
    }
     if(es_palindromo) {
        return(printf("\t%s es un palindromo.\n\n", palabra));
    } else {
        return(printf("\t%s no es un palindromo.\n\n", palabra));
    }
}
