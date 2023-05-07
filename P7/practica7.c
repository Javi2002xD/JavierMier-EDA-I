
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
  int data;
  struct Node* next;
}Node;

Node* addToEmpty(struct Node* last, int data) {
  if (last != NULL) return last;
  Node* newNode = (Node*)malloc(sizeof(struct Node));
  newNode->data = data;
  last = newNode;
  last->next = last;
  return last;
}

// agregar nodo por el frente
Node* addFront(Node* last, int data) {
  if (last == NULL) return addToEmpty(last, data);
  Node* newNode = (Node*)malloc(sizeof(struct Node));
  newNode->data = data;
  newNode->next = last->next;
  last->next = newNode;
  return last;
}

// agregar nodo al final
Node* addEnd(Node* last, int data) {
  if (last == NULL) return addToEmpty(last, data);
  Node* newNode = (Node*)malloc(sizeof(struct Node));
  newNode->data = data;
  newNode->next = last->next;
  last->next = newNode;
  last = newNode;
  return last;
}

// insertar nodo después de un nodo específico
Node* addAfter(Node* last, int data, int item) {
  if (last == NULL) return NULL;
  Node *newNode, *p;
  p = last->next;
  do {
  // si se encontró el elemento, se coloca el nuevo nodo después de él
    if (p->data == item) {
      newNode = (Node*)malloc(sizeof(Node));
      newNode->data = data;
      newNode->next = p->next;
      p->next = newNode;
      if (p == last) last = newNode;
      return last;
    }

  p = p->next;
  } while (p != last->next);
  printf("\nEl nodo dado no esta presente en la lista");
  return last;
}

void traverse(struct Node* last) {
  struct Node* p;
  if (last == NULL) {
    printf("La lista esta vacia");
    return;
  }
  p = last->next;
  do {
  printf("%d -> ", p->data);
  p = p->next;
  } while (p != last->next);
}

void search(struct Node* last, int value) {
  struct Node* p;
  if (last == NULL) {
    printf("La lista esta vacia");
    return;
  }
  p = last->next;
  do {
  printf("%d -> ", p->data);
  p = p->next;
  if(p->data==value) printf("\nEl valor se encuentra en la estructura\n");
  } while (p != last->next);
}

int menu(){
  int op= 0; 
  do{
    printf("\n1)Añadir un elemento por el frente\n");
    printf("2)Añadir un elemento por detras\n");
    printf("3)Añadir antes de un elemento\n");
    printf("4)Ver contenido\n");
    printf("5)Buscar un elemento\n");
    printf("Cualquier otro numero para salir\n");
    scanf("%d", &op);
    if(op>5)exit(0);
    fflush(stdin);
  }
  while(op<1||op>5);
  return op;
}
int main() {
  struct Node* last = NULL;
  int opcion, dato, dato2, buscar;

  while(1){
    opcion=menu();
    switch(opcion){
    case 1:
      printf("añadir el dato\n");
      scanf("%d", &dato);
      last=addFront(last, dato);
      traverse(last);
      break;
    case 2:
      printf("añadir el dato\n");
      scanf("%d", &dato);
      last=addEnd(last, dato);
      traverse(last);
      break;
    case 3:
      printf("añadir el dato\n");
      scanf("%d", &dato);
      printf("añadir antes de:\n");
      scanf("%d", &dato2);
      last=addAfter(last, dato, dato2);
      traverse(last);
      break;
    case 4:
      traverse(last);
    case 5:
      printf("añada el dato a buscar: ");
      scanf("%d", &buscar);
      search(last, buscar);
      traverse(last);
    }
  }
  return 0;
}

