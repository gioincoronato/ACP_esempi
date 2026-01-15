def media_voti(voti):
    try:
        return sum(voti)/len(voti)
    except ZeroDivisionError:
        print("non ci sono voti disponibili per lo studente ")
        return 0.0

def media_voti2(voti):
    assert len(voti) != 0, 'no voti'
    return sum(voti)/len(voti)

if __name__ == "__main__":
     

    lista = [
        [["marco", "cicatiello"], [20, 21, 25]],
        [["barbara", "trombetta"], [30, 26, 28]],
        [["Luca"], [21, 23]],
        [["salvio"], []]
    ]    

    for e in lista:
        print(f"la media del signor : {e[0]}  é : {media_voti2(e[1])}")