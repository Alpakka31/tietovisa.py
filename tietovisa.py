# Lisätään os ja sys kirjastot
import os
import sys

# Tehdään Pääfunktio
def tietovisa():

    #Tyhjennetään ruutu
    os.system('clear')

    #Kysytään haluatko aloittaa visan
    print("Halutko aloittaa visan?")
    print("Vaihtoehdot: jatka, exit")

    #Tehdään while loop, jossa kysytään haluatko jatkaa, vai lopettaa
    while True:
        vaiht = input(">_ ")
        if vaiht == "jatka":
            break
        else:
            vaiht == "exit"
            os.system('clear')
            #Poistutaan skriptistä
            sys.exit()

    #Tehdään muuttuja score ja annettaan sille arvoksi 0
    score = 0

    os.system('clear')

    #Pelin aloitus teksti
    print("Aloitetaan!")

    input("")
    os.system('clear')

    #Kysymys 1
    q1 = input("Mikä on tietokoneen tärkein osa? >_ ")
    if q1 == "Emolevy" or q1 == "emolevy":
        score += 1
        print("Oikein! " + "Pisteesi on " + str(score) + " tällä hetkellä.")
    else:
        print("Väärin! " + "Pisteesi on " + str(score))

    print("")
    input("Jatka painamalla enteriä.")
    os.system('clear')


    #Kysymys 2
    q2 = input("Mitä Ctrl+Z tekee wordissa? >_ ")
    if q2 == "Kumoaa" or q2 == "kumoaa":
        score += 1
        print("Oikein! " + "Pisteesi on " + str(score) + " tällä hetkellä.")
    else:
        print("Väärin! " + "Pisteesi on " + str(score))

    print("")
    input("Jatka painamalla enteriä.")
    os.system('clear')


    #Kysymys 3
    q3 = input("Kuinka monta megatavua on gigatavussa? >_ ")
    if q3 == "1024":
        score += 1
        print("Oikein! " + "Pisteesi on " + str(score) + " tällä hetkellä.")
    else:
        print("Väärin! " + "Pisteesi on " + str(score))

    print("")
    input("Jatka painamalla enteriä.")
    os.system('clear')


    #Kysymys 4
    q4 = input("Mikä on tietokoneväylä englanniksi? >_ ")
    if q4 == "Bus" or q4 == "bus":
        score += 1
        print("Oikein! " + "Pisteesi on " + str(score) + " tällä hetkellä.")
    else:
        print("Väärin! " + "Pisteesi on " + str(score))

    print("")
    input("Jatka painamalla enteriä.")
    os.system('clear')


    #Kysymys 5
    q5 = input("Minkä merkkinen oli ensimmäinen tietokone? >_ ")
    if q5 == "IBM" or q5 == "ibm":
        score += 1
        print("Oikein! " + "Pisteesi on " + str(score) + " tällä hetkellä.")
    else:
        print("Väärin! " + "Pisteesi on " + str(score))

    print("")
    input("Jatka painamalla enteriä.")
    os.system('clear')


    #Kysymys 6
    q6 = input("Kuinka monta merkkiä on tavussa? >_ ")
    if q6 == "8":
        score += 1
        print("Oikein! " + "Pisteesi on " + str(score) + " tällä hetkellä.")
    else:
        print("Väärin! " + "Pisteesi on " + str(score))

    print("")
    input("Jatka painamalla enteriä.")
    os.system('clear')


    #Kysymys 7
    q7 = input("Kuinka monta arvoa bitissä voi olla? >_ ")
    if q7 == "2":
        score += 1
        print("Oikein! " + "Pisteesi on " + str(score) + " tällä hetkellä.")
    else:
        print("Väärin! " + "Pisteesi on " + str(score))

    print("")
    input("Jatka painamalla enteriä.")
    os.system('clear')


    #Kysymys 8
    q8 = input("Mistä sanasta tulle LAN verkon L kirjain? >_ ")
    if q8 == "Local" or q8 == "local":
        score += 1
        print("Oikein! " + "Pisteesi on " + str(score) + " tällä hetkellä.")
    else:
        print("Väärin! " + "Pisteesi on " + str(score))

    print("")
    input("Jatka painamalla enteriä.")
    os.system('clear')


    #Kysymys 9
    q9 = input("Mikä on BIOS koko nimeltään? >_ ")
    if q9.lower() == "basic input/output system":
        score += 1
        print("Oikein! " + "Pisteesi on " + str(score) + " tällä hetkellä.")
    else:
        print("Väärin! " + "Pisteesi on " + str(score))

    print("")
    input("Jatka painamalla enteriä.")
    os.system('clear')


    #Kysymys 10
    q10 = input("Mikä on .exe koko nimeltään? 1. executable 2. execute 3. executed >_ ")
    if q10 == "1":
        score += 1
        print("Oikein! " + "Pisteesi on " + str(score) + " tällä hetkellä.")

    elif q10 == "2":
        print("Väärin! " + "Pisteesi on " + str(score))

    else:
        q10 == "3"
        print("Väärin! " + "Pisteesi on " + str(score))

    print("")
    input("Jatka painamalla enteriä.")
    os.system('clear')


    #Kysymys 11
    q11 = input("Mikä on HTTP koko nimeltään? >_ ")
    if q11.lower() == "hypertext transfer protocol":
        score += 1
        print("Oikein! " + "Pisteesi on " + str(score) + " tällä hetkellä.")

    else:
        print("Väärin! " + "Pisteesi on " + str(score))

    print("")
    input("Jatka painamalla enteriä.")
    os.system('clear')


    #Kysymys 12
    q12 = input("Mikä on HTTPS koko nimeltään? >_ ")
    if q12.lower() == "hypertext transfer protocol secure":
        score += 1
        print("Oikein! " + "Pisteesi on " + str(score) + " tällä hetkellä.")

    else:
        print("Väärin! " + "Pisteesi on " + str(score))

    print("")
    input("Jatka painamalla enteriä.")
    os.system('clear')

    #Kysymys 13
    q13 = input("Mikä on FTP koko nimeltään? >_ ")
    if q13.lower() == "file transfer protocol":
        score += 1
        print("Oikein! " + "Pisteesi on " + str(score) + " tällä hetkellä.")

    else:
        print("Väärin! " + "Pisteesi on " + str(score))

    print("")
    input("Jatka painamalla enteriä.")
    os.system('clear')


    #Kysymys 14
    q14 = input("Mikä on SFTP koko nimeltään? >_ ")
    if q14.lower() == "ssh file transfer protocol":
        score += 1
        print("Oikein! " + "Pisteesi on " + str(score) + " tällä hetkellä.")

    else:
        print("Väärin! " + "Pisteesi on " + str(score))

    print("")
    input("Jatka painamalla enteriä.")
    os.system('clear')


    #Kysymys 15
    q15 = input("Mikä on SGI koko nimeltään? >_ ")
    if q15 == "Silicon Graphics" or q15 == "silicon graphics":
        score += 1
        print("Oikein! " + "Pisteesi on " + str(score) + " tällä hetkellä.")

    else:
        print("Väärin! " + "Pisteesi on " + str(score))

    print("")
    input("Jatka painamalla enteriä.")
    os.system('clear')


    #Kysymys 16
    q16 = input("Mikä on Bourne Shell toiselta nimeltään? 1. shell 2. sh >_ ")
    if q16 == "2":
        score += 1
        print("Oikein! " + "Pisteesi on " + str(score) + " tällä hetkellä.")

    elif q16 == "1":
        print("Väärin! " + "Pisteesi on " + str(score))

    else:
        print("Väärin! " + "Pisteesi on " + str(score))

    print("")
    input("Jatka painamalla enteriä.")
    os.system('clear')


    #Jos käyttäjällä on vähintään 8 pistettä, voittaa tämän visan
    if score > 7:
        print("Onneksi olkoon! " + "Pisteesi oli " + str(score))

    #Jos käyttäjällä on 7 pistettä tai alle, häviää tämän visan
    else:
        print("Hävisit visan! " + "Pisteesi oli " + str(score))


#Suoritetaan pääfunktio
tietovisa()

"""Kun funktio suoritettu
Kysytään käyttäjältä syötettä python skriptin lopettamiseksi"""
input("")
os.system('clear')
sys.exit()
