from cProfile import label

from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QWidget


def verifier_contenu(champ_1: QLineEdit, label_1: QLabel):
    contenu = champ_1.text()

    # Vérifiez si le contenu est un nombre
    if not contenu.isdigit():  # Vérifie si le contenu est uniquement des chiffres
        label_1.setText("Veuillez entrer un nombre valide.")  # Message d'erreur
    else:
        label_1.setText("")  # Efface le message si c'est un
        float(contenu)




# -------------------------------------------------------------------------------------------------------

def verifier_contenu_2(champ_2: QLineEdit, label_2: QLabel):
    contenu = champ_2.text()
    # Vérifiez si le contenu est un nombre
    if not contenu.isdigit():  # Vérifie si le contenu est uniquement des chiffres
        label_2.setText("Veuillez entrer un nombre valide.")  # Message d'erreur
    else:
        label_2.setText("")  # Efface le message si c'est un nombre
        float(contenu)

# -------------------------------------------------------------------------------------------------------

def verifier_contenu_3(champ_3: QLineEdit, label_3: QLabel):
    contenu = champ_3.text()
    # Vérifiez si le contenu est un nombre
    if not contenu.isdigit():  # Vérifie si le contenu est uniquement des chiffres
        label_3.setText("Veuillez entrer un nombre valide.")  # Message d'erreur
    else:
        label_3.setText("")  # Efface le message si c'est un nombre
        float(contenu)


# -------------------------------------------------------------------------------------------------------

def verifier_contenu_4(champ_4: QLineEdit, label_4: QLabel):
    contenu = champ_4.text()
    # Vérifiez si le contenu est un nombre
    if not contenu.isdigit():  # Vérifie si le contenu est uniquement des chiffres
        label_4.setText("Veuillez entrer un nombre valide.")  # Message d'erreur
    else:
        label_4.setText("")  # Efface le message si c'est un nombre
        float(contenu)





# def champ_2_change (champ_1:QLineEdit, champ_2:QLineEdit):
#     try:
#         valure_1 = int(champ_1.text())
#         val_2 = valure_1+100
#         champ_2.setText(str(val_2))
#         return val_2
#     except ValueError:
#         champ_2.setText("")
#     return 0

# def calc_label (champ_2:QLineEdit,label_10:QLabel):
#     try:
#         val_2 = int(champ_2.text()) if champ_2.text().isdigit() else 0
#         val_3 = val_2 + 100
#         print(f"Valeur val : {val_3},valeur de val 2 {val_2}")  # Affiche la valeur calculée
#         label_10.setText(str(val_3))
#     except ValueError:
#         label_10.setText("ERR")
#

def calc_tri(champ_1,champ_2,champ_3,champ_4:QLineEdit,label_10:QLabel):
    val_1 =float(champ_1.text())
    val_2 =float(champ_2.text())
    val_3 =float(champ_3.text())
    val_4 =float(champ_4.text())
    try:
        if val_3 != 0 :
            val_4 = ((val_2*val_3)/val_1)
            print(f"val_4 est : {val_4}")
            champ_4.setText(str(val_4))
        # elif val_4 !=0:
        #     val_3 = ((val_2*val_4)/val_1)
        #     champ_3.setText(str(val_3))
        else:
            val_3 = ((val_1*val_4)/val_2)
            champ_3.setText(str(val_3))
    except ValueError:
        label_10.setText("Halim")







