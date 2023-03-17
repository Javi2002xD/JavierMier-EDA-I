#include<stdlib.h>
#include<stdio.h>

size_t errors();
size_t table();
size_t printed();
size_t caballo();
size_t alfil();
size_t torre();
size_t reina();
size_t rey();
size_t panel[8][8];
int selection, x, y;

typedef struct{
	int lines;
	int columns;
}coordenada;
coordenada scaballo, salfil, storre, sreina, srey;

size_t main(){
int option = 1;
	while(option==1){
		printf("\nMovimientos de piezas de Ajedrez\n");
		printf("Elije que pieza deseas mover\n");
		printf("1)caballo, 2)alfil, 3)torre, 4)reina, 5)rey, 6)salir: ");
		scanf("%d", &selection);
		errors();
		printf("Inserte en que columna desea colocarla: ");
		scanf("%d", &x);
		errors();
		printf("Inserte en que fila desea colocarla: ");
		scanf("%d", &y);
		errors();

		switch(selection){
		case 1:
			caballo();
			break;
		case 2:
			alfil();
			break;
		case 3:
			torre();
			break;
		case 4:
			reina();
			break;
		case 5:
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
	if (selection==6){
		fprintf(stderr, "Gracias por su tiempo\n");
		exit(0);
	}
	
	if(selection>6){
		fprintf(stderr, "Error, elija una opcion de las tres opciones\n");
		exit(-1);
	}
	if (y>8 || x>8){
		fprintf(stderr, "Error, el tablero es 8x8\n");
		exit(-1);
	}
}

size_t table(){
	int x,y;
	for(y=0; y<8; ++y){
		for(x=0; x<8; x++)
			panel[y][x]=46;
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

size_t caballo(){
table();
scaballo.lines=y; scaballo.columns=x;
int i, j;
	for(i=1; i<9; ++i){
		for(j=1; j<9; ++j){
			if((i==scaballo.lines-1||i==scaballo.lines-2||i==scaballo.lines+1||i==scaballo.lines+2)
				&&(j==scaballo.columns-1||j==scaballo.columns-2||j==scaballo.columns+1||j==scaballo.columns+2)
				&&((i+j)!=(scaballo.lines+scaballo.columns))
				&&((i-j)!=(scaballo.lines-scaballo.columns)))
				panel[i-1][j-1]=88;
		}
	}
	panel[scaballo.lines-1][scaballo.columns-1]=67;
	printed();
}

size_t alfil(){
table();
salfil.lines=y; salfil.columns=x;
int j, i;
	for(i=1; i<9; ++i){
		for(j=1; j<9; ++j){
			if((i+j)==(salfil.lines+salfil.columns)||(i-j)==(salfil.lines-salfil.columns))
				panel[i-1][j-1]=88;
		}
	}
	panel[salfil.lines-1][salfil.columns-1]=65;
	printed();
}

size_t torre(){
table();
storre.lines=y; storre.columns=x;
int i, j;
	for(i=0; i<8; i++)
		panel[i][storre.columns-1]=88;
	for(j=0; j<8; ++j)
		panel[storre.lines-1][j]=88;
	panel[storre.lines-1][storre.columns-1]=84;

	printed();
}

size_t reina(){
table();
sreina.lines=y; sreina.columns=x;
int i, j;
	for(i=0; i<8; i++)
		panel[i][sreina.columns-1]=88;
	for(j=0; j<8; ++j)
		panel[sreina.lines-1][j]=88;
	panel[sreina.lines-1][sreina.columns-1]=84;

	for(i=1; i<9; ++i){
		for(j=1; j<9; ++j){
			if((i+j)==(sreina.lines+sreina.columns) || (i-j)==(sreina.lines-sreina.columns))
				panel[i-1][j-1]=88;
		}
	}
	panel[sreina.lines-1][sreina.columns-1]=82;
	printed();
}

size_t rey(){
table();
srey.lines=y; srey.columns=x;
int i, j;
	for(i=1; i<9; ++i){
		for(j=1; j<9; ++j){
			if((i==srey.lines-1||i==srey.lines+1||i==srey.lines)&&(j==srey.columns-1||j==srey.columns+1||j==srey.columns))
				panel[i-1][j-1]=88;
		}
	}
	panel[srey.lines-1][srey.columns-1]=82;
	printed();
}