# límite para el tamaño de la matriz  
N  =  100000 ;  
  
# Tamaño máximo del árbol  
árbol  = [ 0 ] * ( 2  *  N );  
  
# función para construir el árbol  
def  build ( arr ):
  
    # insertar nodos de hoja en el árbol  
    para  i  en  rango ( n ):  
        árbol [ n  +  i ] =  arr [ i ];  
      
    # construir el árbol calculando padres  
    para  i  en  rango ( n  -  1 , 0 , - 1 ):  
        árbol [ i ] =  árbol [ i  <<  1 ] +  árbol [ i  <<  1  |  1 ];  
  
# función para actualizar un nodo de árbol  
def  updateTreeNode ( p , valor ):  
      
    # valor establecido en la posición p  
    árbol [ p  +  n ] =  valor ;  
    p  =  p  +  n ;  
      
    # moverse hacia arriba y actualizar a los padres  
    i  =  p ;
      
    mientras  yo  >  1 :
          
        árbol [ i  >>  1 ] =  árbol [ i ] +  árbol [ i  ^  1 ];  
        i >> = 1 ;  
  
# función para obtener la suma en el intervalo [l, r)  
 consulta de def ( l , r ):  
  
    res  =  0 ;  
      
    # loop para encontrar la suma en el rango  
    l  + =  n ;
    r  + =  n ;
      
    mientras  l  <  r :
      
        si ( l  &  1 ):
            res  + =  árbol [ l ];  
            l  + =  1
      
        si ( r  &  1 ):
            r  - =  1 ;
            res  + =  árbol [ r ];  
              
        l >> = 1 ;
        r >> = 1
      
    volver  res ;  
  
# Código del conductor 
if  __name__  ==  "__main__" :  
  
    a  = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 ];  
  
    # n es global  
    n  =  len ( a );  
      
    # construir árbol  
    construir ( a );  
      
    # imprime la suma en el rango (1,2) basado en índices  
    print ( consulta ( 0 , 12 ));  
      
    # modificar elemento en el 2do índice  
    updateTreeNode ( 2 , 1 );  
      
    # imprime la suma en el rango (1,2) basado en índices  
    print ( consulta ( 1 , 2 ));