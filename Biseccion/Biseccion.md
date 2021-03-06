Método de la Bisección Pseudocódigo

Entradas:

Xi=Límite inferior
Xs=Límite superior
Xa= (Xi+Xs)/2 #Nuevo límite promedio
Error= {[Xa(anterior)-Xa(actual)]/Xa(actual)}*100
Proceso:

Ingresar la función
Definir intervalo (comprobación Xs>Xa)
Bucle(mientras el error>.0001 ó se determine número de iteraciones ó f(Xa)=<0)

Evaluar f(Xi) y f (Xa)
Multiplicar f(Xi)*f (Xa) si el signo es negativo se elimina mitad superior, si es positivo se elimina mitad inferior
Actualizar límite
Calcular error
Salidas:

Raiz
