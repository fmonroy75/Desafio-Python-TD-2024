def choose_level(n_pregunta, p_level):
    
    # Construir lógica para escoger el nivel
    ##################################################
    if n_pregunta/p_level > 2:
        return "avanzadas"
    elif n_pregunta/p_level > 1:
        return "intermedias"
    elif n_pregunta/p_level > 0:
        return "basicas"
    
    
    ##################################################
    return
    #return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias