#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

struct Stack* createStack(unsigned capacity);
int isFull(struct Stack* stack);
int isEmpty(struct Stack* stack);
size_t push(struct Stack* stack);
int peek(struct Stack* stack);

struct Stack {
	int top;
	unsigned capacity;
	int* array;
};

int main(){
	struct Stack* stack = createStack(10);
	int option = 1;
	while(option==1){
		printf("Bienvenido al sistema de turnos.\n 1)Formarse, 2)Salir.\n");
		scanf("%d", &option);
		if(option==1){
			push(stack);
			printf("El elemento se encuentra formado en la cola numero: %d\n", peek(stack));

		}
		if(option==2){
			printf("Su turno es: %d\n", peek(stack));
		}
		if(option>2)
			return(fprintf(stderr, "No está en las opciones"));
	}
	return 0;
}
struct Stack* createStack(unsigned capacity){
	struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
	stack->capacity = capacity;
	stack->top = -1;
	stack->array = (int*)malloc(stack->capacity * sizeof(int));
	for (int i = 0; i < 10; ++i){
		stack->array[i]=i+1;
	}
	return stack;
}

int isFull(struct Stack* stack){
	return stack->top == stack->capacity - 1;
}

int isEmpty(struct Stack* stack){
	return stack->top == -1;
}

size_t push(struct Stack* stack){
	if (isFull(stack)){
		return(fprintf(stderr, "Ya no hay turnos disponibles...\n"));
		exit(-1);
	}
	stack->top=stack->top+1;
}

int peek(struct Stack* stack){
	if (isEmpty(stack))
		return INT_MIN;
	return stack->array[stack->top];
}