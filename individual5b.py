import time
import random
cont_bl=0
ordenes_de_sandwiches = [
    ['Ave palta','Barros Luco','Atún mayo','Chacarero','Lomito italiano'],['Ave palta','Choclo queso','Atún mayo','Chacarero','Lomito italiano'],['Ave palta','Barros Luco','Atún mayo','Chacarero','Lomito italiano'],
    ['Ave palta','Barros Luco','Atún mayo','Chacarero','Lomito italiano'],['Ave palta','Barros Luco','Atún mayo','Chacarero','Lomito italiano'],['Ave palta','Barros Luco','Atún mayo','Chacarero','Lomito italiano'],
    ['Ave palta','Barros Luco','Atún mayo','Chacarero','Lomito italiano'],['Ave palta','Choclo queso','Atún mayo','Chacarero','Lomito italiano'],['Ave palta','Barros Luco','Atún mayo','Chacarero','Lomito italiano'],
    ['Ave palta','Barros Luco','Atún mayo','Chacarero','Lomito italiano'],['Ave palta','Barros Luco','Atún mayo','Chacarero','Lomito italiano'],['Ave palta','Barros Luco','Atún mayo','Chacarero','Lomito italiano'],
    ['Ave palta','Barros Luco','Atún mayo','Chacarero','Lomito italiano'],['Ave palta','Choclo queso','Atún mayo','Chacarero','Lomito italiano'],['Ave palta','Barros Luco','Atún mayo','Chacarero','Lomito italiano'],
    ['Ave palta','Barros Luco','Atún mayo','Chacarero','Lomito italiano'],['Ave palta','Barros Luco','Atún mayo','Chacarero','Lomito italiano'],['Ave palta','Barros Luco','Atún mayo','Chacarero','Lomito italiano'],
    ['Ave palta','Barros Luco','Atún mayo','Chacarero','Lomito italiano'],['Ave palta','Choclo queso','Atún mayo','Chacarero','Lomito italiano']]
sandwiches_terminados =[]
cont=0
for n in range(0,len(ordenes_de_sandwiches)):   
    for i in ordenes_de_sandwiches[n]:
        print("Su sandwich de ",i, " se está preparando, por favor espere. \n")
       # tiempo_espera = random.randint(1,2)
       # time.sleep(tiempo_espera)
        sandwiches_terminados.append(i)
        cont = cont+1
#print (cont)
for a in range(0,len(sandwiches_terminados)):
    print(a+1,"Sandwich ",sandwiches_terminados[a], " preparado.\n")  

#___________________________________________________________________________

#verificar cantidad de Barros Luco y elliminarlos de la lista inicial

cont_bl =0
for n in range(0,len(ordenes_de_sandwiches)):   
    for i in ordenes_de_sandwiches[n]:
        if i == 'Barros Luco':
            cont_bl =cont_bl+1

if cont_bl>3:
    j=0
    print("Nos quedamos sin Barros Luco :( \n")
b=0
while b < len(ordenes_de_sandwiches):
    for i in ordenes_de_sandwiches[b]:
        if i == 'Barros Luco':
            ordenes_de_sandwiches[b].remove(i)     
    #print(ordenes_de_sandwiches)  
    b+=1 
ordenes2 = ordenes_de_sandwiches
terminados =[]
for n in range(0,len(ordenes2)):   
    for i in ordenes2[n]:
        terminados.append(i)
print ("Barros Luco : ",cont_bl)
print("lista final de pedidos, con Barros Luco sin preparar: \n",terminados)