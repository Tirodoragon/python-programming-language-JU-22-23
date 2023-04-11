def odwracanie(L, left, right):
    i = left
    j = right
    while j > i:
        L[i], L[j] = L[j], L[i]
        i += 1
        j -= 1
    
def odwracanie_rekurencyjnie(L, left, right):
    if left > right:
        return
    else:
        L[left], L[right] = L[right], L[left]
        odwracanie_rekurencyjnie(L, left + 1, right - 1)
        
lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [7, 6, 5, 4, 3, 2, 1]

odwracanie(lista1, 2, 5)
odwracanie_rekurencyjnie(lista2, 3, 5)

print(lista1)
print(lista2)
