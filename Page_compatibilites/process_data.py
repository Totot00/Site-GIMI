import pandas as pd
import sys


drug1 = sys.argv[1]
drug2 = sys.argv[2]


incomp_file_path = "C:/xampp/htdocs/proj - Copie/Donnée-imcompatibilitées (1).csv"
incomp = pd.read_csv(incomp_file_path, encoding='latin1')


#symetrisation du DataFrame
Medic = incomp.columns.tolist()
n = len(Medic)-2
for k in range(1, n+1):
    for i in range(k, n-1):
        incomp.iloc[k-1,i+1]=incomp.iloc[i,k]

Additionnal_medic = ["TPN_avec_lipides_ternaire", "TPN_sans_lipides_binaire", "RINGER-LACTATE", "GLUCOSALIN", "GLUCOSE_5%_et_10%", "NaCl_0.9%"]
for medicAdd in Additionnal_medic:
    Medic.append(medicAdd)

def fct(drug1, drug2):
    assert drug1 in Medic
    objet = incomp.loc[(incomp.Medicaments == drug2), drug1]
    index_objet = objet.index[0]
    reponse = objet[index_objet]
    if reponse == "I":
        return "{} est incompatible avec {} pour une injection en Y".format(drug1, drug2)
    if reponse == "C":
        return "{} est compatible avec {} pour une injection en Y".format(drug1, drug2)
    if reponse == "nan":
        return "Nous n'avons pas d'information sur l'interaction de ces médicaments"
    else:
        return "Se référer au code {} dans la documentation".format(reponse)
    

# Votre logique pour vérifier la compatibilité. Pour cet exemple, je suppose une compatibilité par défaut de 10.
compatibility = fct(drug1, drug2)

# Imprimez le résultat pour le renvoyer au script PHP
print(compatibility)

