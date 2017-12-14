import time
import re
estu =[]
incorrectas=[]
pregutas =[]
puntos = 100
a = True
class estudiante(object):

    def __init__(self,nombre,ced,grupo,nota):
        self.nombre= nombre
        self.ced= ced
        self.grupo = grupo
        self.nota=nota
    def record (nombre,ced,nota):
        info = {'nombre':nombre,'cedula':ced,'nota':str(nota)}
        estu.append(info)
        for dato in estu[0:]:


            for llave,val in dato.items():
                arc.write(llave + ': '+ val+' ')

            arc.write('\n *********************************\n')

#     def examen (self):
#         while True:
#
#             file=arc.readline()
#             if 'pregunta ' in file:
#                 pregunt = file
#             elif 'opciones' in file:
#                 opc = file
#             elif 'respuesta ' in file:
#                 respuesta = file
# a
#             if len(file)== 0:
#                 break
#
#
#             pregun= {'pregunta':pregunt,'enunciado': opc, 'respuesta':respuesta}
#             pregutas.append(pregun)






    #def resultado (self):





def epacio (espacio):
    epa1 = ' '
    epa = ' '
    for x in range(espacio):
        epa =epa +epa1
    es =epa
    return es


if  __name__=='__main__':
    try:
        arc = open('info_examen.txt','x')
    except FileExistsError:
        arc = open('info_examen.txt', 'a')
        #estudiante.examen(str)
        #datos.documento(str)


    print(epacio(25),'Proyecto de progrmacion III')
    print(epacio(35),'python\n')
    nom=input('nombre: ')
    cedula=input('cedula: ')
    print('           hola',nom.capitalize(),'Este es un examen de conocimento popular')
    print('                          tiene un valor de 100 pts')
    print('          solo tines 1 intento, no lo desperdicies y buena suerte  \n\n')
    em =input('presiona enter para empezar\n')
    y=5
    for x in range(5):
        print(y)
        y -= 1
        time.sleep(1)
    while a==True :
        infile = open('info_examen.txt', 'r')
        for dato in pregutas[0:1]:
            for llave,valor in dato.items:
                print(valor)
                preg = input('valor\n')
        if preg == 'a' or preg == 'c' or preg == 'A' or preg == 'C':
            puntos -=5
            p = '¿Cual de estas palabras es correcta para nombrar el vegetal?'
            r = 'brócoli'
            resul = {'pregunta': p, 'respuesta': r}
            incorrectas.append(resul)
            break

        else:

            break
        break
    #
    #
    #
    while a == True:
        print('En la tabla periodica, \'ca\' representa a :')
        preg = input('a)Carbono'+'   b)Carburo'+'   c) Calcio\n')
        if preg == 'a' or preg=='b'or preg == 'A' or preg == 'B':
            puntos -= 5
            p = 'En la tabla periodica, \'ca\' representa a :'
            r = ' Calcio'
            resul = {'pregunta': p, 'respuesta': r}
            incorrectas.append(resul)
            break

        else:

            break
    while True:

        print('¿cual es el idioma mas hablado en del mundo?')
        preg = input('a)El aleman'+'   b)El ingles'+'   c) Español'+ '  d) El chino mandarin\n')

        if preg == 'a' or preg == 'b' or preg == 'c' or preg == 'A' or preg == 'B' or preg == 'C':
            puntos -= 5
            p = 'En la tabla periodica, \'Ca\' representa a :'
            r = ' Calcio'
            resul = {'pregunta': p, 'respuesta': r}
            incorrectas.append(resul)
            break

        else:

            break
    while a == True:
        print('¿Cual de estas series cuenta con un protagonista con displasia cleidocranel?')
        preg = input('a)Black mirror'+'   b)Game of thrones'+'   c) Stranger things\n')
        if preg == 'a' or preg == 'b'or preg == 'A' or preg == 'B' :
            puntos -= 5
            p = '¿Cual de estas series cuena con un protagonista con displasia cleidocraneal?'
            r = 'Stranger things'
            resul = {'pregunta': p, 'respuesta': r}
            incorrectas.append(resul)
            break

        else:

            break

    while a == True:
        preg = int(input('¿Cuantos dientes tine una persona normal?\n'))
        if preg != 32 or preg == re.match('[A-za-z]',str(preg)) :
            puntos -= 5
            p = '¿Cuantos dientes tine una persona normal?'
            r = '32'
            resul = {'pregunta': p, 'respuesta': r}
            incorrectas.append(resul)
            break

        else:

            break

    while a == True:
        print('¿Quien fue David Hume?')
        preg = input('a)un filosofo '+'   b)un youtuber'+'   c) un cientifico\n')
        if preg == 'b' or preg == 'B'or preg == 'c' or preg == 'C' :
            puntos -= 10
            p = '¿Quien fue David Hume?\n'
            r = 'un filosofo'
            resul = {'pregunta': p, 'respuesta': r}
            incorrectas.append(resul)
            break


        else:
            break

    while a == True:
        print('¿Quien escrbio El Principito?')
        preg = input('a) Victor hugo'+'   b) Antoine de Saint Exupéry'+'    c) Jorge Luis Borges\n')
        if preg == 'a' or preg == 'A'or preg == 'c' or preg == 'C' :
            puntos -= 10
            p = '¿Quien escrbio El Principito?\n'
            r = 'Antoine de Saint Exupéry'
            resul = {'pregunta': p, 'respuesta': r}
            incorrectas.append(resul)
            break

        else:

            break

    while a == True:
        print('¿Cuatas medallas tiene Teresa Peraless?')
        preg = input('a) 25'+'   b) 8'+'   c) 13\n')
        if preg == 'b' or preg == 'B'or preg == 'c' or preg == 'C' :
            puntos -= 10
            p = '¿Cuatas medallas tiene Teresa Peraless?'
            r = '25'
            resul = {'pregunta': p, 'respuesta': r}
            incorrectas.append(resul)
            break


        else:

            break

    while a == True:
        print('¿Cual de estos artistas fue nominado el 2017 a un grammy latino?')
        preg = input('a) Kase.0'+'   b) David Civera'+'   c) Erika Ender\n')
        if preg == 'a' or preg == 'A'or preg == 'b' or preg == 'B' :
            puntos -= 10
            p = '¿Cual de estos artistas fue nominado el 2017 a un grammy latino?'
            r = 'Erika Ender'
            resul = {'pregunta': p, 'respuesta': r}
            incorrectas.append(resul)
            break


        else:

            break

    while a == True:
        print('¿de que frase inglesa proviene el gringo?')
        preg = input('a) Going'+'   b)Green go home'+'   c) going to home\n')
        if preg == 'a' or preg == 'A' or preg == 'c' or preg == 'C' :
            puntos -= 10
            p = '¿de que frase inglesa proviene el gringo?'
            r = 'b) Green go home'
            resul = {'pregunta': p, 'respuesta': r}
            incorrectas.append(resul)

            break
        elif len(preg)== 0:

            break
        else:
            break
    print('parte 2')
    print('esta parte se trata de un pareo')
    print('coloque la letra de la columna A en la columna B')
    print('\t')

    print(
        'a- Panama           __' + 'destruyo Panama la vieja\n''b- 2+2              __' + '4\n' + 'c- henry morgan     __fue fundada el 15 de agosto de 1519 \n ')
    a = input()
    if a == 'c':
        puntos -= 5
    b = input()
    if b == 'b':
        puntos -= 5
    c = input()
    if c == 'a':
        puntos -= 5

    print(puntos)

    #puntos =

    print('estas son las malas')
    for dato in incorrectas[0:]:

        for llave, val in dato.items():
            print(llave + ':  ' + val + ' ')
    print(' ___________________________________')
    print('|                                   |')
    print('| esta es tu nota: ', puntos, 'puntos      |')
    estudiante.record(nom,cedula,puntos)

    print('|___________________________________|')
    if puntos < 71 :
        print("has reprobado mejor suerte la proxima")
    else:
        print(" felicidades crack eres el puto amo has aprobado")


    time.sleep(60)