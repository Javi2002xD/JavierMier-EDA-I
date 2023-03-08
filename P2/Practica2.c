/*Universidad Nacional Autónoma de México
Estructura de dat0s y algoritmos I
Grupo 19
Mier Ramírez Javier*/

#include<stdlib.h>
#include<stdio.h>

size_t reina();
size_t rey();
size_t errors();
size_t printed();
size_t table();
int panel[8][8];
int columns, lines, selection;

size_t main(){
int option = 1;
	while(option==1){
		printf("\nMovimientos de Alfil y Torre\n");
		printf("Elije que pieza deseas mover\n");
		printf("1)Reina, 2)Rey, 3)Salir\n");
		scanf("%d", &selection);
		errors();
		printf("Inserte en que columna desea colocarla: ");
		scanf("%d", &columns);
		errors();
		printf("Inserte en que fila desea colocarla: ");
		scanf("%d", &lines);
		errors();

		switch(selection){
		case 1:
			reina();
			break;
		case 2:
			rey();
			break;
		}
		printf("Desea volver a ejecutar el programa?\n");
		printf("1) Si, 2) No: ");
		scanf("%d", &option);
	}
	printf("Gracias por su tiempo\n");
	return 0;
}
size_t errors(){
	if (selection==3){
		fprintf(stderr, "Gracias por su tiempo\n");
		exit(0);
	}
	
	if(selection>3){
		fprintf(stderr, "Error, elija una opcion de las tres opciones\n");
		exit(-1);
	}
	if (lines>8 || columns>8){
		fprintf(stderr, "Error, el tablero es 8x8\n");
		exit(-1);
	}
}
size_t table(){
int i, j, (*ptr)[8];
ptr=panel;
	int x, y;
	for(y=0; y<8; ++y){
		for(x=0; x<8; x++)
			ptr[y][x]=46;
	}
}
size_t printed(){
int i, j, (*ptr)[8];
ptr=panel;
	for(i=0; i<=8; ++i){
		for(j=0; j<8; j++){
			printf("%c", ptr[i][j]);
		}
		printf("\n");
	}
}
size_t reina(){

	table();
	int (*apt)[8], i, j;
	apt=panel;

	for(i=0; i<8; i++)
		apt[i][columns-1]=88;
	for(j=0; j<8; ++j)
		apt[lines-1][j]=88;

	for(i=1; i<9; ++i){
		for(j=1; j<9; ++j){
			if((i+j)==(lines+columns) || (i-j)==(lines-columns))
				apt[i-1][j-1]=88;
		}
	}
	apt[lines-1][columns-1]=82;
	printed();
}
size_t rey(){
	table();
	int (*apt)[8], i, int_columns=columns-1, int_lines=lines-1;
	apt=panel;

	for(i=int_lines-1; i<=int_lines+1; i++){
		apt[i][int_columns]=88;
		apt[i][int_columns-1]=88;
		apt[i][int_columns+1]=88;
	}
	apt[int_lines][int_columns]=82;
	printed();
}
