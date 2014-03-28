#! usr/bin/python 

import modulo                                   # importamos el modulo 
PI = 3.14159265358979323846264338327950288      # ponemos el valor de pi

def error (interv, test, umbral):               # definimos la funcion 

 fallo = 0                                   # inicializamos fallo 
 for i in range ( 1, test+1):                   # recorremos la cantidad de la variable test
 
  aprox = modulo.aproximacion (interv)          
  error = abs (aprox - PI)                      
  if error > umbral:                     # Suma la cantidad de errores que tiene 
  
    fallo = fallo + 1 
    
 porcent = (fallo/ float (test))* 100     # inicializamos el porcentaje 
 
 return porcent                          # devolvemos el porcentaje del error 
if __name__ == "__main__" : 
interv = int (raw_input (' Introducir numero de intervalos : ')) 
test = int (raw_input ('Introduzca la cantidad de veces que quiera que se repita:')) 
umbral = float (raw_input (' Introducir el valor que considere minimo')) 

m = error (interv,test, umbral) 

print m   # muestra el error 
 
 