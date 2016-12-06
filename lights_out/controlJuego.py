import tableroNiveles


def nivelCompleto(tableronivel):
    for i in tableronivel:
        for elemento in i:
             if elemento != ".":
                return False
    return True