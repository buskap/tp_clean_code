# API Clean Code TP Noté 
L'objectif de cette api met en place un système de clé permettant la validation de l'identifiant d'un client. 
Le projet à été développer en python avec le framework Flask.

## Arborescence du projet 
.
├── functions
│   └── functions.py
├── tests
│   └── tests.py
├── README.md
└── apy.py

## Procédure d'installation
### Venv
Installation et initialisation d'un venv
    python3 -m venv .env
    cd .env
    source bin/activate

cf. https://docs.python.org/3/library/venv.html en cas de difficulté

### Requirements 
Installation des dépendances
    pip install -r requirements.txt

## Run api 
    export FLASK_APP=api
    flask run

### Accès et utilisation de l'api
Le serveur ce lance sur le localhost au port 5000    
    127.0.0.1:5000

### Verification d'une clé 
Les clé doivent respecter la forme suivante : 
    cle = key + id 
    # cle -> (str)
    key = unique caractère majuscule (A-Z)
    id = suite de chiffre de longueur 9
    ex : "A123456789"

Requête :
    127.0.0.1:5000/client/cle/verification?id=A123456789

Réponse : 
    {"request":"J133486789","result":0,"status":"ok"}
    request : id testé
    result : 0 si id validé, 1 sinon
    status : état du traitement

