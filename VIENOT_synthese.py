#synthèse de la parole - Alix Sirven-Viénot - 2023-2024 

import matplotlib.pyplot as plt 
import parselmouth as pm
import textgrids
from parselmouth.praat import call
import spacy


def main(): 
    global synthèse
    ouverture_fichiers()
    intro()
    # lance l'intro appel la fonction que_dire et propose le menu phrase ou une phrase par défaut 

    # comparaison de phrase et phrase verif + print message
    while True:
        phrase_trouvé = verif_phrase(phrase)
        if phrase_trouvé:
            print("Nous allons vous synthétiser tout ça !")
            break
        else:
            print("La phrase n'est pas disponible à la synthèse.")
    
    traitement_phrase()
    synthèse = extraction_diphone()
    
    print("C'est bon pour moi! Vous pouvez maintenant ouvrir le fichier resultat.wav, pour découvrir votre synthèse.")
    oscillo = input("Voulez-vous voir l'oscillogramme associé au signal sonore de notre synthèse ?\n Si oui, tapez 1.\n")
    if oscillo == "1":
        oscillogramme()
    else:
        print("Merci, passez une bonne journée!\n")


def traitement_phrase():
    global verb
    global à_allonger
    global pitch_bas
    global pitch_haut
    global phrase_phonetique

    verb = trouver_VERB(phrase)
    print(verb)

    liste_mot_phrase = phrase.split(" ")
    print(liste_mot_phrase)

    à_allonger =[]
    #liste des mots à allonger
    pitch_haut = []
    pitch_bas = []

    for i in range(0, len(liste_mot_phrase)-1):
        mot1= liste_mot_phrase[i]
        mot2 = liste_mot_phrase[i + 1]
        #print(mot1 , mot2)
        if mot2 == str(trouver_VERB(phrase)):
            #print(f"{mot1} la dernière voyelle est à allonger")
            à_allonger.append((dico[mot1])[-2:])
            pitch_haut.append((dico[mot2])[-2:])
            # mot entier ou seulement diphone ?
            #suis née ? prend né / avait ??
        elif mot2 == "," or mot2 == "et" or mot2 == "." or mot2 == "puis":
            #print( f"{mot1} mot à allonger")
            à_allonger.append((dico[mot1])[-2:])
            pitch_bas.append((dico[mot1])[-2:])
        elif mot1 == "," or mot1 == "et" or mot1 == "." or mot1 == "puis":
            pitch_haut.append(dico[mot2][-2:])
        #else: 
            #print("extraction du diphone normale")
        
    print(à_allonger)
    print(pitch_haut, pitch_bas)

    #Enlever la ponctuation pour permetter la transformation en phrase phonétique
    phrase_sans_ponct = remove_punctuation(liste_mot_phrase)
    phrase_phonetique = transformation_phon(phrase_sans_ponct)
    #donne la phrase choisi en phonetique 
    print(phrase_phonetique)


def ouverture_fichiers():
    global sound
    global segmentation
    global synthese
    global dico
    son = 'VIENOT.wav'
    #son = '{nom}.wav'
    grille = 'VIENOT.TextGrid'
    #grille = '{nom}.TextGrid'
    synthese = 'ASV_resultat.wav'
    sound = pm.Sound(son)
    #Sound.get_sampling_frequency()
    segmentation = textgrids.TextGrid(grille)
    #création dico avec boucle qui lit le fichier + ouverture dico 
    dico = {}
    with open('dico_UTF8.txt', 'r') as file: 
        for line in file: 
            key,value = line.strip().split('\t')
            #split rend un tuple
            dico[key] = value 
    #print(dico)


def intro():
    global phrase
    global choix_prosodie
    print("Bonjour, aujourd'hui nous allons synthétiser une phrase ensemble. \nVoulez-vous que la phrase soit brut ou avec un ajout de prosodie artficielle ?\n")
    choix_prosodie = input("Tapez brut pour la phrase sans modifications et tapez 1 pour ajouter la prosodie.\n")
    choix = input("Voulez-vous choisir une phrase ou synthétiser une phrase par défaut?\nPour synthétiser une phrase par defaut, taper 1. \nPour choisir la phrase que vous voulez synthètiser, taper autre chose.\n")
    if choix == "1":
        print()
        phrase = "mon grand-père avait des pêches et des poires dans son jardin ."
    else: 
        phrase = que_dire()
    return phrase

def que_dire():
    global phrase
    # QCM pour choisir la phrase à dire
    forme = input ("Dans ce programme cing formes de phrases sont disponibles à la synthèse: \n 1. J'aime les (fruits) (couleur) et (membre_famille) les (fruit) (couleur) \n 2. On plante les (fruit) en (mois) et les (fruit) en (mois) \n 3. (membre_famille) avait des (fruit) et des (fruit) dans son jardin \n 4. Je suis né(e) en (mois) et (membre_famille) en (mois) \n 5. Pour la recette, il faut mettre les (fruit) puis les (fruit) \n Pour choisir taper 1, 2, 3, 4 ou 5. \n")
    print(forme)
    if forme not in ["1", "2", "3", "4", "5"]:
        print("Vous devez choisir un nombre entre 1 et 5.")
        que_dire()
    elif forme == "1":
        fruit1 = input("Maintenant choisissez un fruit que vous aimez. \n Vous avez le choix entre : \n 1. pomme, \n 2. poire, \n 3. pêche, \n 4. pastèque, \n 5. cerise, \n 6. banane, \n 7. jujube. \n Tapez un chiffre entre 1 et 7.\n")
        match fruit1:
            case "1":
                fruit1= "pommes"
            case "2":
                fruit1= "poires"
            case "3":
                fruit1= "pêches"
            case "4":
                fruit1= "pastèques"
            case "5":
                fruit1= "cerises"
            case "6":
                fruit1= "bananes"
            case "7":
                fruit1= "jujubes"
        print(fruit1)
        couleur1 = input("Choisissez la couleur de ce fruit entre rouge ou vert. \n Tapez 1 pour rouge et 2 pour vert.\n")
        match couleur1:
            case "1":
                couleur1= "rouges"
            case "2":
                couleur1= "vertes"
        famille = input("Quelle membre de votre famille aime les fruits ? \n 1. mère, \n 2. père, \n 3. grand-mère, \n 4. grand-père, \n 5. soeur. Tapez le chiffre correspondant au membre de la famille.\n")
        match famille:
            case "1":
                famille= "ma mère"
            case "2":
                famille= "mon père"
            case "3":
                famille= "ma grand-mère"
            case "4":
                famille= "mon grand-père"
            case "5":
                famille= "ma soeur"
        fruit2 = input(f" Maintenant choisissez un fruit que {famille} aime. \n Vous avez le choix entre : \n 1. pomme, \n 2. poire, \n 3. pêche, \n 4. pastèque, \n 5. cerise, \n 6. banane, \n 7. jujube.\n Tapez un chiffre entre 1 et 7.\n")
        match fruit2:
            case "1":
                fruit2= "pommes"
            case "2":
                fruit2= "poires"
            case "3":
                fruit2= "pêches"
            case "4":
                fruit2= "pastèques"
            case "5":
                fruit2= "cerises"
            case "6":
                fruit2= "bananes"
            case "7":
                fruit2= "jujubes"
        couleur2 = input("Choisissez la couleur de ce fruit entre rouge ou vert. \n Tapez 1 pour rouge et 2 pour vert. \n")
        match couleur2:
            case "1":
                couleur2= "rouges"
            case "2":
                couleur2= "vertes"
        phrase = f"J' aime les {fruit1} {couleur1} et {famille} les {fruit2} {couleur2} ." 
        print(phrase)

    elif forme == "2":
        fruit1 = input("Maintenant choisissez un fruit que vous aimez. \n Vous avez le choix entre : \n 1. pomme, \n 2. poire, \n 3. pêche, \n 4. pastèque, \n 5. cerise, \n 6. banane, \n 7. jujube. \n Tapez un chiffre entre 1 et 7.\n")
        match fruit1:
            case "1":
                fruit1= "pommes"
            case "2":
                fruit1= "poires"
            case "3":
                fruit1= "pêches"
            case "4":
                fruit1= "pastèques"
            case "5":
                fruit1= "prunes"
            case "6":
                fruit1= "bananes"
            case "7":
                fruit1= "jujubes"
            case "8":
                fruit1= "cerises"
        print(fruit1)

        mois1 = input(f"Quand plante-t-on les {fruit1}. \n Vous avez le choix entre : \n 1. Janvier, \n 2. Février, \n 3. Mars, \n 5. Mai, \n 7. Juillet, \n 8. Août \n 9. Septembre \n 11. Novembre \n 12. Dêcembre \n Tapez un chiffre entre 1, 2, 3, 5, 7, 8, 9, 11 ou 12 (les mois 4, 6 et 10 ne sont pas disponibles pour le moment).\n")
        match mois1:
            case "1":
                mois1= "janvier"
            case "2":
                mois1= "février"
            case "3":
                mois1= "mars"
            case "5":
                mois1= "mai"
            case "7":
                mois1= "juillet"
            case "8":
                mois1= "août"
            case "9":
                mois1= "septembre"
            case "11": 
                mois1 = "novembre"
            case "12": 
                mois1 = "dêcembre"
        print(mois1)

        fruit2 = input(f"Quel fruit voulez vous plantez maintenant? \n Vous avez le choix entre : \n 1. pomme, \n 2. poire, \n 3. pêche, \n 4. pastèque, \n 5. cerise, \n 6. banane, \n 7. jujube.\n Tapez un chiffre entre 1 et 7.\n")
        match fruit2:
            case "1":
                fruit2= "pommes"
            case "2":
                fruit2= "poires"
            case "3":
                fruit2= "pêches"
            case "4":
                fruit2= "pastèques"
            case "5":
                fruit2= "cerises"
            case "6":
                fruit2= "bananes"
            case "7":
                fruit2= "jujubes"

        mois2 = input(f"Quand plante-t-on les {fruit2}. \n Vous avez le choix entre : \n 1. Janvier, \n 2. Février, \n 3. Mars, \n 5. Mai, \n 7. Juillet, \n 8. Août \n 9. Septembre \n 11. Novembre \n 12. Dêcembre \n Tapez entre 1 , 2 , 3 , 5 , 7 , 8 , 9 , 11 , 12 (les mois 4, 6 et 10 ne sont pas disponibles pour le moment).\n")
        match mois2:
            case "1":
                mois2= "janvier"
            case "2":
                mois2= "février"
            case "3":
                mois2= "mars"
            case "5":
                mois2= "mai"
            case "7":
                mois2= "juillet"
            case "8":
                mois2= "août"
            case "9":
                mois2= "septembre"
            case "11": 
                mois2 = "novembre"
            case "12": 
                mois2 = "dêcembre"
        phrase = f"On plante les {fruit1} en {mois1} et les {fruit2} en {mois2} ."
        print(phrase)

    elif forme == "3":
        famille = input("Quelle membre de votre famille avait des fruits dans son jardin? \n 1. mère, \n 2. père, \n 3. grand-mère, \n 4. grand-père, \n 5. soeur.\n Tapez le chiffre correspondant au membre de la famille.\n ")
        match famille:
            case "1":
                famille= "ma mère"
            case "2":
                famille= "mon père"
            case "3":
                famille= "ma grand-mère"
            case "4":
                famille= "mon grand-père"
            case "5":
                famille= "ma soeur"
        
        fruit1 = input("Maintenant choisissez un fruit qui poussait dans son jardin. \n Vous avez le choix entre : \n 1. pomme, \n 2. poire, \n 3. pêche, \n 4. pastèque, \n 5. cerise, \n 6. banane, \n 7. jujube.\n Tapez un chiffre entre 1 et 7.\n")
        match fruit1:
            case "1":
                fruit1= "pommes"
            case "2":
                fruit1= "poires"
            case "3":
                fruit1= "pêches"
            case "4":
                fruit1= "pastèques"
            case "5":
                fruit1= "cerises"
            case "6":
                fruit1= "bananes"
            case "7":
                fruit1= "jujubes"
        print(fruit1)
        
        fruit2 = input(f"Quel fruit y avait-il d'autres dans ce jardin? \n Vous avez le choix entre : \n 1. pomme, \n 2. poire, \n 3. pêche, \n 4. pastèque, \n 5. cerise, \n 6. banane, \n 7. jujube.\n Tapez un chiffre entre 1 et 7.\n")
        match fruit2:
            case "1":
                fruit2= "pommes"
            case "2":
                fruit2= "poires"
            case "3":
                fruit2= "pêches"
            case "4":
                fruit2= "pastèques"
            case "5":
                fruit2= "cerises"
            case "6":
                fruit2= "bananes"
            case "7":
                fruit2= "jujubes"
        phrase = f"{famille} avait des {fruit1} et des {fruit2} dans son jardin ."
        print(phrase)

    elif forme == "4":
        genre = input ("Voulez vous accorder cette phrase au masculin ou au féminin ? \nTapez F ou M ?\n")
        mois1 = input(f"En quel mois êtes-vous né?. \n Vous avez le choix entre : \n 1. Janvier, \n 2. Février, \n 3. Mars, \n 5. Mai, \n 7. Juillet, \n 8. Août \n 9. Septembre \n 11. Novembre \n 12. Dêcembre \n Tapez un chiffre entre 1, 2, 3, 5, 7, 8, 9, 11 ou 12 (les mois 4, 6 et 10 ne sont pas disponibles pour le moment).\n")
        match mois1:
            case "1":
                mois1= "janvier"
            case "2":
                mois1= "février"
            case "3":
                mois1= "mars"
            case "5":
                mois1= "mai"
            case "7":
                mois1= "juillet"
            case "8":
                mois1= "août"
            case "9":
                mois1= "septembre"
            case "11": 
                mois1 = "novembre"
            case "12": 
                mois1 = "dêcembre"
        print(mois1)
        
        famille = input("Quel membre de votre famille voulez-vous utiliser ? \n 1. mère, \n 2. père, \n 3. grand-mère, \n 4. grand-père, \n 5. soeur. Tapez le chiffre correspondant au membre de la famille.\n")
        match famille:
            case "1":
                famille= "ma mère"
            case "2":
                famille= "mon père"
            case "3":
                famille= "ma grand-mère"
            case "4":
                famille= "mon grand-père"
            case "5":
                famille= "ma soeur"
        
        mois2 = input(f"Quand est né {famille}?\n Vous avez le choix entre : \n 1. Janvier, \n 2. Février, \n 3. Mars, \n 5. Mai, \n 7. Juillet, \n 8. Août \n 9. Septembre \n 11. Novembre \n 12. Dêcembre \n Tapez entre 1 , 2 , 3 , 5 , 7 , 8 , 9 , 11 , 12 (les mois 4, 6 et 10 ne sont pas disponibles pour le moment).\n")
        match mois2:
            case "1":
                mois2= "janvier"
            case "2":
                mois2= "février"
            case "3":
                mois2= "mars"
            case "5":
                mois2= "mai"
            case "7":
                mois2= "juillet"
            case "8":
                mois2= "août"
            case "9":
                mois2= "septembre"
            case "11": 
                mois2 = "novembre"
            case "12": 
                mois2 = "dêcembre"
        if genre == "F": 
            print(f"Je suis née en {mois1} et {famille} en {mois2}.")
        else: 
            print(f"Je suis né en {mois1} et {famille} en {mois2}.")
        phrase = f"Je suis née en {mois1} et {famille} en {mois2} ."

    elif forme == "5":
        fruit1 = input("Pour la recette, quel fruit utilisez-vous? \n Vous avez le choix entre : \n 1. pomme, \n 2. poire, \n 3. pêche, \n 4. pastèque, \n 5. cerise, \n 6. banane, \n 7. jujube.\n Tapez un chiffre entre 1 et 7.\n")
        match fruit1:
            case "1":
                fruit1= "pommes"
            case "2":
                fruit1= "poires"
            case "3":
                fruit1= "pêches"
            case "4":
                fruit1= "pastèques"
            case "5":
                fruit1= "cerise"
            case "6":
                fruit1= "bananes"
            case "7":
                fruit1= "jujubes"
        print(fruit1)

        fruit2 = input(f"Pour la recette, quel autre fruit utilisez-vous? \n Vous avez le choix entre : \n 1. pomme, \n 2. poire, \n 3. pêche, \n 4. pastèque, \n 5. cerise, \n 6. banane, \n 7. jujube.\n Tapez un chiffre entre 1 et 7.\n")
        match fruit2:
            case "1":
                fruit2= "pommes"
            case "2":
                fruit2= "poires"
            case "3":
                fruit2= "pêches"
            case "4":
                fruit2= "pastèques"
            case "5":
                fruit2= "cerises"
            case "6":
                fruit2= "bananes"
            case "7":
                fruit2= "jujubes"
        phrase = f"Pour la recette , il faut mettre les {fruit1} puis les {fruit2} ."
        print(phrase)
    return phrase
    
def verif_phrase(phrase):
    with open('phrases_possibles.txt', 'r') as file:
        for line in file:
            if phrase in line:
                return line.strip()
    return None


def trouver_VERB (phrase):
    nlp = spacy.load('fr_core_news_sm')
    doc = nlp(phrase)
    for mot in doc: 
        if mot.pos_ == "VERB" or mot.pos_ == "AUX":
            return mot   

def remove_punctuation(liste_mot_phrase):
    #global phrase_sans_ponct
    punctuation = [",", ".", "!", "?", ";"]
    phrase_sans_ponct = []
    for item in liste_mot_phrase:
        if item not in punctuation:
            phrase_sans_ponct.append(item)
    return phrase_sans_ponct

def transformation_phon(phrase_sans_ponct):
#fonction transformation de phrase en phonetique
   #phrase = input("Quelle phrase voulez-vous prononcer?")
    phrase_phon = []
    #création d'une liste vide pour ajouter les transcription phon 
    for mot in phrase_sans_ponct:
        #ajout des liaisons
        if mot == "août":
            phrase_phon.append("n"+(dico[mot]))
        else:
            phrase_phon.append(dico[mot])
    phrase_phon = "".join(phrase_phon)
    phrase_phon = "_"+phrase_phon+"_"
    #print(phrase_phon)
    return phrase_phon


def manip_pitch(extrait, mod_pi):
    #manipulation des points de pitch (F-0)
    manipulation = call(extrait, "To Manipulation", 0.01, 75, 600)

    #pitch = call(sound, "To Pitch", 0.0, f0min, f0max) #create a praat pitch object
    pitch_tier = call(manipulation, "Extract pitch tier")
    call(pitch_tier, "Remove points between", 0, extrait.duration)
    call(pitch_tier, "Add point", 0.01, mod_pi)
    #call(pitch_tier, "Multiply frequencies", sound.xmin, sound.xmax, mod_pi) #changer mod_pi en un pourcentage 
    #trouve que ça sonne moins bien 
    call([pitch_tier, manipulation], "Replace pitch tier")
    extrait= call(manipulation, "Get resynthesis (overlap-add)")
    return extrait

def manip_duree(extrait, allongement):
    #manip = To Manipulation: 0.01, 75, 600 #en PRAAT 
    manipulation = call (extrait, "To Manipulation", 0.001, 75, 600)

    duration_tier = call(manipulation,"Extract duration tier")
    call(duration_tier, "Remove points between", 0, extrait.duration)
    call(duration_tier, "Add point", extrait.duration/2, allongement)
    call([duration_tier, manipulation], "Replace duration tier")
    extrait = call(manipulation, "Get resynthesis (overlap-add)")


def extraction_diphone():
    diphones = segmentation['diphones']
    #diphones = nom ligne d'annotation dans TextGrid// diphones
    global son_synthese
    son_synthese = sound.extract_part(0, 0.01, pm.WindowShape.RECTANGULAR,1,False)
    for i in range(len(phrase_phonetique)-1):
        i2 = i+2
        diphone = phrase_phonetique[i:i2]
        phoneme_a = diphone[0]
        phoneme_a2 = diphone[1]
        #print(phoneme_a , phoneme_a2)
        #boucle sur la longueur de la phrase en phono et attribu à diphone phone1 et phone2 
        for phoneme1 in range(len(diphones)):
            phoneme2 = phoneme1 + 1
            global extrait
            if diphones[phoneme1].text == phoneme_a and diphones[phoneme2].text == phoneme_a2:
                milieu_phoneme1 = diphones[phoneme1].xmin + (diphones[phoneme1].xmax - diphones[phoneme1].xmin)/2
                milieu_phoneme1 = sound.get_nearest_zero_crossing(milieu_phoneme1,1)

                milieu_phoneme2 = diphones[phoneme2].xmin + (diphones[phoneme2].xmax - diphones[phoneme2].xmin)/2
                milieu_phoneme2 = sound.get_nearest_zero_crossing(milieu_phoneme2,1)

                extrait = sound.extract_part(milieu_phoneme1, milieu_phoneme2, pm.WindowShape.RECTANGULAR, 1, False)
                
                if choix_prosodie == "1":
                    #allongement des phonemes 
                    if diphone in à_allonger: 
                        manip_duree(extrait, 1.3)
                        print(diphone)
                    else: 
                        manip_duree(extrait, 1)
                    #modif pitch 
                    if diphone in pitch_haut:
                        extrait = manip_pitch(extrait, 260)
                    elif diphone in pitch_bas:
                        extrait = manip_pitch(extrait, 200)
                    else:
                        extrait = manip_pitch(extrait, 230)

                son_synthese = son_synthese.concatenate([son_synthese,extrait])
                #son_synthese = sound.concatenate([son_synthese,extrait], 0.005)
                break #nécéssaire ? 
                
    son_synthese.save(synthese, pm.SoundFileFormat.WAV)
                      

def oscillogramme():
    plt.figure()
    plt.plot(sound.xs(), sound.values.T)
    plt.xlabel('time')
    plt.ylabel('amplitude')
    plt.show()


if __name__ == "__main__":
    main()
