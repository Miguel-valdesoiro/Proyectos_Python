 Ejercicio Extra (opcional). PyQuest:

import random

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.__nombre = nombre
        self.__vida = vida
        self.__ataque = ataque
        self.__defensa = defensa

    def __str__(self):
        return f"{self.__nombre} con {self.__vida} de vida"

    @property
    def nombre(self):
        '''Método getter del atributo nombre'''
        return self.__nombre

    @property
    def vida(self):
        '''Método getter del atributo vida'''
        return self.__vida

    @property
    def ataque(self):
        '''Método getter del atributo ataque'''
        return self.__ataque

    @property
    def defensa(self):
        '''Método getter del atributo defensa'''
        return self.__defensa

    @nombre.setter
    def nombre(self, nuevo_nombre):
        '''Método setter del atributo nombre'''
        self.__nombre = nuevo_nombre

    @vida.setter
    def vida(self, nuevo_vida):
        '''Método setter del atributo vida'''
        self.__vida = nuevo_vida

    @ataque.setter
    def ataque(self, nuevo_ataque):
        '''Método setter del atributo ataque'''
        self.__ataque = nuevo_ataque

    @defensa.setter
    def defensa(self, nuevo_defensa):
        '''Método setter del atributo defensa'''
        self.__defensa = nuevo_defensa

    def estar_vivo(self):
        return self.__vida > 0

    def atacar(self):
        impactos = 0
        for _ in range(self.__ataque):
            dado = Dado()
            resultado = dado.tira()
            if resultado > 3:
                impactos += 1
        return impactos

class Momia(Personaje):
    def __init__(self):
        super().__init__("Momia Nefertiti", 5, 3, 6)

    def defender(self, num_impactos):
        bloqueos = 0
        for _ in range(self.defensa):
            dado = Dado()
            resultado = dado.tira()
            if resultado == 6:
                bloqueos += 1
        impactos_sufridos = num_impactos - bloqueos
        nueva_vida = self.vida - impactos_sufridos
        self.vida = nueva_vida
        return bloqueos

class Barbaro(Personaje):
    def __init__(self):
        super().__init__("Barbaro Conan", 8, 4, 5)

    def defender(self, num_impactos):
        bloqueos = 0
        for _ in range(self.defensa):
            dado = Dado()
            resultado = dado.tira()
            if resultado > 4:
                bloqueos += 1
        impactos_sufridos = num_impactos - bloqueos
        nueva_vida = self.vida - impactos_sufridos
        self.vida = nueva_vida
        return bloqueos

class Dado:
    def tira(self, caras=6):
        return random.randint(1, caras)

def partida(max_turnos):
    momia = Momia()
    barbaro = Barbaro()

    for turno in range(1, max_turnos+1):
        print(f"\n # TURNO {turno} > {barbaro.nombre} vs {momia.nombre}")
        num_impactos_barbaro = barbaro.atacar()
        bloqueos_momia = momia.defender(num_impactos_barbaro)
        print(f" >>> La momia {momia.nombre} pudo bloquear {bloqueos_momia} impactos y queda con {momia.vida} de vida")

        if not momia.estar_vivo():
            print(f"\n > GANADOR {barbaro.nombre}")
            print(f"     >>> {barbaro} \n     >>> {momia}")
            break

        num_impactos_momia = momia.atacar()
        bloqueos_barbaro = barbaro.defender(num_impactos_momia)
        print(f" >>> El Barbaro {barbaro.nombre} pudo bloquear {bloqueos_barbaro} impactos y queda con {barbaro.vida} de vida")

        if not barbaro.estar_vivo():
            print(f"\n > GANADOR {momia.nombre}")
            print(f"     >>> {momia} \n     >>> {barbaro}")
            break
    else:
        print("\n > RESULTADO: TABLAS")
        print(f"     >>> {momia} \n     >>> {barbaro}")

# Ejemplo de uso
turnos_maximos = int(input("¿Cuántos turnos máximos quiere jugar?: "))
partida(turnos_maximos)
