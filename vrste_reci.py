def choosy(tekst):
    import re
    import time
    vrsta = input('Molim Vas izaberite slovo ispred reci koje su Vam potrebne:\nA)promenljive\nB)nepromenljive\nVas odgovor: ')
    if vrsta == 'A' or vrsta == 'a':
        vrsta1=input('Sada Vas molim da izaberete vrstu promenljivih reci koja Vam je potrebna:\nA)imenice\nB)zamenice\nC)glagoli\nD)pridevi\nE)brojevi\nVas odgovor: ')
        if vrsta1=='A' or vrsta1=='a':
            vrsta2=input('Sada izaberite vrstu imenica koja Vam je potrebna:\nA)zajednicke\nB)vlastite\nC)sve imenice\nVas odgovor: ')
            if vrsta2 == 'A' or vrsta2 == 'a':
                print('Izabrali ste zajednicke imenice')
                uslov='Nc'
                time.sleep(2)
            if vrsta2 == 'B' or vrsta2 == 'b':
                print('Izabrali ste vlastite imenice')
                uslov='Np'
                time.sleep(2)
            if vrsta2 == 'C' or vrsta2 == 'c':
                print('Izabrali ste sve imenice')
                uslov='N'
                time.sleep(2)
        elif vrsta1 == 'B' or vrsta1 == 'b':
            vrsta2 = input('Sada izaberite vrstu zamenica koja Vam je potrebna:\nA)odnosne\nB)pokazne\nC)upitne\nD)povratne\nE)licne\nF)sve zamenice\nVas odgovor: ')
            if vrsta2 == 'A' or vrsta2 == 'a':
                print('Izabrali ste odnosne zamenice.')
                uslov='Pi'
                time.sleep(2)
            if vrsta2 == 'B' or vrsta2 == 'b':
                print('Izabrali ste pokazne zamenice.')
                uslov='Pd'
                time.sleep(2)
            if vrsta2 == 'C' or vrsta2 == 'c':
                print('Izabrali ste upitne zamenice.')
                uslov='Pd'
                time.sleep(2)
            if vrsta2 == 'D' or vrsta2 == 'd':
                print('Izabrali ste upitne zamenice.')
                uslov='Pq'
                time.sleep(2)
            if vrsta2 == 'E' or vrsta2 == 'e':
                print('Izabrali ste povratne zamenice.')
                uslov='Px'
                time.sleep(2)
            if vrsta2 == 'F' or vrsta2 == 'f':
                print('Izabrali ste sve zamenice.')
                uslov= 'P'
                time.sleep(2)
            else:
                print('ne razumem')
        elif vrsta1 == 'C' or vrsta1 == 'c':
            vrsta2 = input('Sada izaberite vrstu glagola koja Vam je potrebna:\nA)osnovni\nB)pomocni\nC)svi glagoli\nVas odgovor: ')
            if vrsta2 == 'A' or vrsta2 == 'a':
                print('Izabrali ste osnovne glagole.')
                uslov = 'Vm'
                time.sleep(2)
            if vrsta2 == 'B' or vrsta2 =='b':
                print('Izabrali ste pomocne glagole.')
                uslov = 'Va'
                time.sleep(2)
            if vrsta2 == 'C' or vrsta2 == 'c':
                print('Izabrali ste sve glagole.')
                uslov = 'V'
                time.sleep(2)
        elif vrsta1 == 'D' or vrsta1 == 'd':
            vrsta2 = input('Sada izaberite vrstu prideva koja Vam je potrebna:\nA)opisni\nB)trpni glagolski\nC)svi pridevi\nVas odgovor: ')
            if vrsta2 == 'A' or vrsta2 == 'a':
                print('Izabrali ste opisne prideve.')
                uslov = 'Ag'
                time.sleep(2)
            if vrsta2 == 'B' or vrsta2 == 'b':
                print('Izabrali ste trpne glagolske prideve.')
                uslov = 'Ap'
                time.sleep(2)
            if vrsta2 == 'C' or vrsta2 == 'c':
                print('Izabrali ste sve prideve.')
                uslov = 'A'
                time.sleep(2)
        elif vrsta1 == 'E' or vrsta1 == 'e':
            vrsta2 = input('Sada izaberite kakvi brojevi su vam potrebni:\nA)zapisani ciframa\nB)zapisani recima\nC)svi brojevi\nVas odgovor: ')
            if vrsta2 == 'A' or vrsta2 == 'a':
                print('Izabrali ste brojeve zapisane ciframa.')
                uslov = 'Md'
                time.sleep(2)
            if vrsta2 == 'B' or vrsta2 == 'b':
                print('Izabrali ste brojeve zapisane recima.')
                uslov = 'Ml'
                time.sleep(2)
            if vrsta2 == 'C' or vrsta2 == 'c':
                print('Izabrali ste sve prideve.')
                uslov = 'M'
                time.sleep(2)
        else:
            print('ne razumem')
    elif vrsta == 'B' or vrsta == 'b':
        vrsta1 = input('Sada Vas molim da izaberete vrstu nepromenljivih reci koja vam treba:\nA)prilozi\nB)predlozi\nC)recce\nD)veznici\nVas odgovor: ')
        if vrsta1=='A' or vrsta1=='a':
            print('izabrali ste priloge')
            uslov='R'
            time.sleep(2)
        elif vrsta1 == 'B' or vrsta1 == 'b':
            print('izabrali ste predloge')
            uslov='S'
            time.sleep(2)
        elif vrsta1 == 'C' or vrsta1 == 'c':
            print('izabrali ste recce')
            uslov='Q'
        elif vrsta1 == 'D' or vrsta1 == 'd':
            print('izabrali ste veznike')
            uslov='C'
        else:
            print('ne razumem')
    else:
        print('Ne mogu da Vas razumem, molim vas upisite SLOVO ISPRED onog sta trazite')
    leme_ili_reci=input('trebaju li vam leme ili reci? A)leme B)reci C)leme i reci')
    if leme_ili_reci=='a' or leme_ili_reci=='A':
        uslov2='l'
    elif leme_ili_reci=='b' or leme_ili_reci=='B':
        uslov2='r'
    elif leme_ili_reci=='c' or leme_ili_reci=='C':
        uslov2='lr'
    time.sleep(2)
    for red in tekst:
        try:
            rec,lowercase,lemma,pos=red.split('\t')
            if pos.startswith(uslov):
                if uslov2=='l':
                    print(lemma)
                elif uslov2=='r':
                    if uslov=='Np':
                        print(rec)
                    else:
                        print(lowercase)
                elif uslov2=='lr':
                    if uslov=='Np':
                        print(rec,lemma)
                    else:
                        print(lowercase,lemma)
        except:
            pass
srwac=open('korpus.txt','r',encoding='UTF-8')
choosy(srwac)
