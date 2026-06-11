#función con parámetros y con retorno
def es_surfeable(altura):
    return altura >= 1.5

#función con parámetros y sin retorno 
def alertar_viento_peligroso(nudos_viento):
    if nudos_viento > 20:
        print("[ALERTA CRÍTICA]: Viento peligroso, peligro de corriente")
    else:
        print("Condiciones de viento dentro del límite")    

#función sin parámetros y con retorno
def obtener_temperatura_limite_traje():
    temperatura_limite = 13
    return temperatura_limite

#función sin parámetros y sin retorno
def mostrar_advertencia_marejada():
    print("-------------------------------------")
    print("AVISO DE LA ARMADA: MAREJADAS ACTIVAS") 
    print("-------------------------------------")