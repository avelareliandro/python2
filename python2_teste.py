import time
print("funcionouuuu!")
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)
    print("Lista de frutas concluída.")
frutas.append('uva')
print("Adicionando uva à lista de frutas.")
print(frutas)
print("Lista final de frutas:", frutas)
print("Programa encerrado.")
valore = [1, 2, 3, 4, 5]
for numero in valore:
    print("Número atual:", numero)
print("Todos os números foram exibidos.")
print("Fim do código.")
print("Iniciando o programa...")
print("Programa iniciado com sucesso.")
print("Processando dados...")
print("Dados processados com sucesso.")
print("Finalizando o programa...")
print("Programa finalizado.")
print("Programa concluído com êxito.")
valore.append(22)
print(max(valore))
valore = [2, 4, 5, 6, 45, 43, 5, 6, 7, 54, 56, 64, 76,
          76, 76, 876, 67, 876, 34, 543, 342, 55, 667, 7]
print('o máximo da lista é', max(valore))


def numero_maior(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior


print(valore)
valore.sort(reverse=True)
print(valore)


def maximo(lista):
    max = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > max:
            max = lista[i]
    return max


print(' O valor máximo da lista é', maximo(valore))
t1 = time.process_time()
maximo(valore)
t2 = time.process_time()
print('Tempo de execução:', t2 - t1, 'segundos')
time.sleep(0.005)
print('Fim do programa')  # busca binária
estudantes = ['Arthur', 'Bianca', 'Daiane', 'Eliandro', 'Carlos']
if ('Eliandro' in estudantes):
    print('nessa lista há eliandro')
estudantes.sort()
print(estudantes)
print('Eliandro está na lista?....', 'Eliandro' in estudantes)


def busca_linear(lista, alvo):
    for elemento in lista:
        if (elemento == alvo):
            return True
    return False
print('Eliandro está na turma? ....', busca_linear(estudantes, 'Eliandro'))

students = ['Arthur', 'Bianca', 'Daiane', 'Eliandro', 'Carlos']
students.sort() 
def busca_binaria(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return True
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return False
print('Eliandro está na turma? ....', busca_binaria(students, 'Eliandro'))
print('Eliandro está na turma? ....', busca_binaria(students, 'Eliandro'))
print('Eliandro está na turma? ....', busca_binaria(students, 'Eliandro'))

minimo_valores = [1, 5, 4, 8, 32, 23, 32, 36, 52,365, 23, 45, 67, 89, 90]
def minimo(lista):
    min = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < min:
            min = lista[i]
    return min
print(' O valor mínimo da lista é', minimo(minimo_valores))

minimo_valores = [1, 5, 4, 8, 32, 23, 32, 36, 52,365, 23, 45, 67, 89, 90]
def selection(lista):
    i = 0
    while (i < len(lista) -1):
        minimo = lista[i]
        ind_minimo = i
        for j in range(i+1, len(lista)):
            if (lista[j] < minimo):
                minimo = lista[j]
                ind_minimo = j
        lista[ind_minimo] = lista[i]
        lista[i] = minimo
        i += 1  
        return lista

selection(minimo_valores)
print(minimo_valores)

