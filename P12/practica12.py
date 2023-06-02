import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import random 

times=0

def quicksort(arr):
    global times
    if len(arr) <= 1:
        times+=1
        return arr
    else:
        times+=1
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(lesser) + [pivot] + quicksort(greater)
    
def merge_sort(arr):
    global times
    if len(arr) <= 1:
        times+=1
        return arr
    
    # Dividir la lista en mitades
    times+=1
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Aplicar recursivamente MergeSort a las mitades
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Combinar las mitades ordenadas
    return merge(left_half, right_half)


def merge(left, right):
    global times
    merged = []
    left_index, right_index = 0, 0
    
    # Combinar los elementos de las mitades en orden
    while left_index < len(left) and right_index < len(right):
        global times
        if left[left_index] <= right[right_index]:
            times+=1
            merged.append(left[left_index])
            left_index += 1
        else:
            times+=1
            merged.append(right[right_index])
            right_index += 1
    
    # Agregar los elementos restantes de la mitad izquierda (si los hay)
    while left_index < len(left):
        times+=1
        merged.append(left[left_index])
        left_index += 1
    
    # Agregar los elementos restantes de la mitad derecha (si los hay)
    while right_index < len(right):
        times+=1
        merged.append(right[right_index])
        right_index += 1
    return merged
    

TAM=101 
eje_x = list(range(1, TAM, 1))
eje_y =[]
lista_variable = []

for num in eje_x:
    lista_variable=random.sample(range(0, 1000), num)
    print(lista_variable)
    times = 0
    lista_variable=quicksort(lista_variable)
    eje_y.append(times)
print(lista_variable)

fig, ax = plt.subplots(facecolor='w', edgecolor='k')
ax.plot(eje_x, eje_y, marker="o", color="r", linestyle='None')

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)
ax.legend(["Quick Sort"])

plt.title("Quick Sort")
plt.show()


TAM=101 
eje_x3 = list(range(1, TAM, 1))
eje_y3 =[]
lista_variable3 = []


for num in eje_x3:
	lista_variable3=random.sample(range(0,1000), num)
	print(lista_variable3)
	times = 0
	lista_variable3=merge_sort(lista_variable3)
	eje_y3.append(times)

print(lista_variable3)

fig, ax = plt.subplots(facecolor='w', edgecolor='k')
ax.plot(eje_x3, eje_y3, marker="o", color="m", linestyle='None')

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)
ax.legend(["Merge Sort"])

plt.title("Merge Sort")
plt.show()