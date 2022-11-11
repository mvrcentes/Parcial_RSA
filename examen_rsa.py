"""
Universidad del Valle de Guatemala
Matematica Discreta
Seccion 20
Examen Parcial 3
Practica Criptografia RSA
Javier Luis Angel Chavez Escobar
21016
"""

def modularExp(b, y, m):
    y = baseExp(y, 2)
    x = 1
    potencia = b % m
    for i in range(0, len(y)):
        if y[i] == 1:
            x = (x*potencia) % m
        potencia = (potencia*potencia) % m
    return x

def baseExp(n,b):
    x = n
    y = []
    while x != 0:
        y.append(x % b)
        x = x // b
    return y

def convertirTexto(texto):
    texto2 = ''    
    for i in range(0, len(texto)):
        texto2 += str.lower(texto[i])
    
    key = "abcdefghijklmnopqrstuvwxyz" 
    codificado = []
    for i in texto2:
        for y in range(00, len(key)):
            if i == key[y]:
                codificado.append("%02d" % y)
    _temp = '' 
    msjCodificado = []   
    count = 0       
    for i in range(0, len(codificado)):
        _temp += str(codificado[i])
        count += 1
        if count == 2:
            count = 0
            msjCodificado.append(_temp)
            _temp = ''
  
    numCodificado = []
    for i in range(0, len(msjCodificado)):
        numCodificado.append(int(msjCodificado[i]))
    return numCodificado

def revertir(x):
    count = 0
    _temp = ''
    lista = []
    for i in x:
        count += 1
        _temp += i
        if count == 4:
            lista.append(int(_temp))
            _temp = ''
            count = 0
    return  lista

def convertlisttotext(x):
    tempints = []
    for i in x:
        tempints.append(str("%04d" % i))
    
    ints = []
    tempstr = ''
    count = 0
    for i in tempints:
        for y in i:
            tempstr += y
            count += 1
            if count == 2:
                count = 0
                ints.append(int(tempstr))
                tempstr = ''
    key = "abcdefghijklmnopqrstuvwxyz"
    string2 = ''
    for i in ints:
        for y in range(0, len(key)):
            if i == y:
                string2 += key[y]
    return string2
    
def rsaEncriptar(texto, valor_N, valor_P, valor_Q, valor_E):
    if valor_N == 0:
        valor_N = valor_P * valor_Q
    n = valor_N
    numbers = convertirTexto(texto)
    values = []
    for i in numbers:
        values.append(modularExp(i, valor_E, n))
    _temp = ''
    for i in values:
        _temp += "%04d" % i
    return _temp

def maximoComunDivisor(x, y):
    if y == 0:
        return x, 1, 0
    mdc, s1, t1 = maximoComunDivisor(y, x % y)
    resultado, t = t1, s1 - t1 * (x // y)
    return mdc, resultado, t

def inversoModulo(x, y):
    x %= y
    mdc, resultado, t = maximoComunDivisor(x, y)
    if mdc != 1:
        return 0
    resultado %= y
    return resultado

def rsaDescifrar(texto, valor_P, valor_Q, valor_E):
    n = valor_P * valor_Q
    phi = (valor_P - 1) * (valor_Q - 1)

    d = inversoModulo(valor_E, phi)

    lista = revertir(texto)
    values = []
    for i in    lista:
        values.append(modularExp(i, d, n))
    str = convertlisttotext(values)
    return str

if __name__ == "__main__":
    opcion = 99
    while opcion != 3:
        print ("ENCRIPTACIONES EBEN EZER")
        print ("Ingrese una opcion:\n[1] Encriptar\n[2] Descifrar\n[3] Salir")
        opcion = int(input("Opcion: "))
        if opcion == 1:
            M = input("\n\nIngrese el texto a encriptar: ")
            opcion2 = input("Desea utilizar\n[1] n\n[2] p y q\n>>")
            if opcion2 == '1':
                N = int(input("Ingrese n: "))
                E = int(input("Ingrese e: "))
                print (f"\n\nTexto '{M}' encriptado: {rsaEncriptar(M, N, 0, 0, E)}\n\n")
            elif opcion2 == '2':
                P = int(input("Ingrese el valor de p: "))
                Q = int(input("Ingrese el valor de q: "))
                E = int(input("Ingrese el valor de e: "))
                print (f"\n\nTexto '{M}' encriptado: {rsaEncriptar(M, 0, P, Q, E)}\n\n")
        elif opcion == 2:
            C = input("\n\nIngrese el texto a descifrar: ")
            P = int(input("Ingrese el valor de p: "))
            Q = int(input("Ingrese el valor de q: "))
            E = int(input("Ingrese el valor de e: "))
            print (f"\n\nTexto '{C}' desencriptado: {rsaDescifrar(C, P, Q, E)}\n\n")
        elif opcion == 3:
            break
        else:
            print ("\n\nOpcion invalida\n\n")

    print("\n\nGracias por usar el programa\n\n")