Readme du script VIENOT_synthese.py - Alix Sirven-Viénot 

Ce script synthétise des phrases dans un fichier son "ASV_resultat.wav"
Il a besoin d'être dans le même dossier que le fichier "phrases_possibles.txt" généré par le script "générateur_de_phrases.py", le fichier son contenant les logatomes "VIENOT.wav", la textgrid "VIENOT.TextGrid" et le dictionnaire "dico_UTF8.txt".


## Les formes de phrases
1. J'aime les X C et F les X C.
2. On plante les X en M et les X en M.
3. Membre_famille avait des X et des X dans son jardin.
4. Je suis né(e) en M et Membre_famille en M.
5. Pour la recette, il faut mettre les X puis les X.

Variables de formation de phrase: 
X = fruits = pomme, poire, pêche, pastèque, banane, jujube, cerise 
C = couleurs = rouge, verte
F = membres de la famille = mère, père, grand-mère, grand-père, soeur 
M = mois de l'année = janvier, fevrier, mars, mai, juillet, aout, septembre, novembre, dêcembre


- pas réussi à enregistrer le mot "prune"
- "avait" considéré comme un auxiliaire
- création d'un générateur de phrases 
- modification du pitch avec "Multiply frequencies" ne s'adaptait pas à toutes les phrases (utilisation de "Add points")