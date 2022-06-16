import simplicite97

def teste():
    msg=(simplicite97.erase("  Salut Ca  Va   Bien    ou     bien      ?       "))
    if(msg==  "  SalutCa  Va   Bien    ou     bien      ?       "):
        print("test ok")
    else :
        print("test pas ok")
        print(msg)

teste()
