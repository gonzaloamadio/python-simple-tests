class Pila:
    def __init__(self):
        self.pila = []

    def apilar(self, valor):
        self.pila.append(valor)

    def desapilar(self):
        if not self.pila:
            return None
        else:
            return self.pila.pop(-1)

    def __bool__(self):
        return bool(self.pila)

    def __len__(self):
        return len(self.pila)


class Cola:
    def __init__(self):
        self.cola = []

    def encolar(self, valor):
        self.cola.append(valor)

    def desencolar(self):
        if not self.cola:
            return None
        else:
            return self.cola.pop(0)


class ColaSobrePila:
    """Una cola puede ser implementada sobre una pila de forma muy elegante.

    Para encolar, simplemente agrego un valor a la pila (apilo)
    Para desencolar, uso una pila auxiliar para invertir el orden de la pila y saco el primero


    """
    def __init__(self):
        self.pila_interna = Pila()

    def encolar(self, valor):
        self.pila_interna.apilar(valor)

    def desencolar(self):
        # Creo pila auxiliar para invertir el orden y sacar el valor de mas abajo de la pila
        pila_invertida = Pila()
        # Por Ej: si la pila_interna tiene
        # | 3 |
        # | 2 |
        # | 1 |
        # La auxiliar va a invertir el orden quedando asi
        # | 1 |
        # | 2 |
        # | 3 |
        # De esta forma, el primer valor en ingresar, queda mas arriba y lo puedo obtener con un pop
        if not self.pila_interna:
            return None

        # Mientras haya valores en la pila
        while self.pila_interna:
            # Sacando los elementos de una pila y apilandolos en otra, invierto el orden de la pila
            pila_invertida.apilar(self.pila_interna.desapilar())

        # El valor de mas arriba de la pila invertida
        # Es el valor de mas abajo de la pila interna
        # Es decir, el primer valor ingresado
        # En una cola, el primer valor ingresado es el que debe salir
        # Este es el 'truco' de la cola sobre pilas
        valor_a_desencolar = pila_invertida.desapilar()

        # Vuelvo a popular mi pila interna respetando el orden original
        # Desapilar una pila e ir metiendola en otra es invertir el orden de la pila
        while pila_invertida:
            self.pila_interna.apilar(pila_invertida.desapilar())

        return valor_a_desencolar

def test_todo():
    c = Cola()
    c.encolar(1)
    c.encolar(2)
    c.encolar(3)

    assert c.desencolar() == 1
    assert c.desencolar() == 2
    assert c.desencolar() == 3
    assert c.desencolar() is None

    p = Pila()
    p.apilar(3)
    p.apilar(4)
    p.apilar(5)
    assert p.desapilar() == 5
    assert p.desapilar() == 4
    assert p.desapilar() == 3
    assert p.desapilar() is None


    cp = ColaSobrePila()
    assert cp.desencolar() is None
    cp.encolar(10)
    cp.encolar(20)
    cp.encolar(500)

    assert cp.desencolar() == 10
    assert cp.desencolar() == 20
    assert cp.desencolar() == 500
    assert cp.desencolar() is None
