def convertirSimple(message):
    nvMess = ""
    taille = len(message)
    for i in range(taille):
        if message[i]==' ':
            if i!=taille-1:
                if message[i+1]==' ':
                    while message[i]==' ' and i!=(taille-1):
                        nvMess+=message[i]
                        i=i+1
        else:
            nvMess+=message[i]
    return nvMess
