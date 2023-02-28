/*Universidad Nacional Autónoma de México
Estructura de dat0s y algoritmos I
Grupo 19
Mier Ramírez Javier*/

#include<stdlib.h>
#include<stdio.h>

size_t alfil();
size_t torre();
size_t errors();
size_t printed();
size_t table();
size_t panel[8][8];
int columns, lines, selection, option=1;

size_t main(){

	while(option==1){
		printf("\nMovimientos de Alfil y Torre\n");
		printf("Elije que pieza deseas mover\n");
		printf("1)Alfil, 2)Torre, 3)Salir\n");
		scanf("%d", &selection);
		printf("Inserte en que columna desea colocarla: ");
		scanf("%d", &columns);
		printf("Inserte en que fila desea colocarla: ");
		scanf("%d", &lines);
		errors();

		switch(selection){
		case 1:
			alfil();
			break;
		case 2:
			torre();
			break;
		case 3:
			fprintf(stderr, "Gracias por su tiempo");
			break;
		}
		printf("Desea volver a ejecutar el programa?\n");
		printf("1) Si, cualquier otra tecla para salir: ");
		scanf("%d", &option);
	}
	printf("Gracias por su tiempo\n");
	return 0;
}

size_t table(){
	int x, y;
	for(y=0; y<8; ++y){
		for(x=0; x<8; x++)
			panel[y][x]=35;
	}
}
size_t errors(){
	
	if(selection>=3){
		fprintf(stderr, "Error, elija una opcion de las tres\n");
		exit(-1);
	}
	if (lines && columns >8){
		fprintf(stderr, "Error, el tablero es 8x8\n");
		exit(-1);
	}
}
size_t printed(){
int i, j;
	for(i=0; i<=8; ++i){
		for(j=0; j<8; j++){
			printf("%c", panel[i][j]);
		}
		printf("\n");
	}
}
size_t torre(){
table();
int i, j;
	for(i=0; i<8; i++)
		panel[i][columns-1]=88;
	for(j=0; j<8; ++j)
		panel[lines-1][j]=88;
	panel[lines-1][columns-1]=84;
	printed();
}
size_t alfil(){
table();
int j, i;
	for(i=1; i<9; ++i){
		for(j=1; j<9; ++j){
			if((i+j)==(lines+columns) || (i-j)==(lines-columns))
				panel[i-1][j-1]=88;
		}
	}
	panel[lines-1][columns-1]=84;
	printed();
}
