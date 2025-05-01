 
# Réponses - TP Tests Automatisés

## Étape 1 : Clonage du projet
J'ai cloné le dépôt avec :
```bash
git clone https://github.com/Akasam/tests-automatises.git
```

## Étape 2 : Environnement virtuel
J'ai activé l'environnement virtuel :
```bash
venv\Scripts\activate
```

## Étape 3 : Lancement de l'application
J'ai lancé le serveur Flask avec :
```bash
python run.py
```

## Étape 4 : Test API (addition)
J’ai utilisé curl :
```bash
curl http://127.0.0.1:5000/api/add/2/3
```
### Résultat :
```json
{
  "result": 5.0
}
```

## Étape 5 : Test API (ajout d'un utilisateur)
J’ai utilisé curl pour tester l'ajout d'un utilisateur :
```bash
curl -X POST http://127.0.0.1:5000/api/user \
  -H "Content-Type: application/json" \
  -d '{"username":"test_user", "email":"user@example.com"}'
```
### Résultat :
```json
{
  "message": "User created successfully"
}
```

## Étape 6 : Tests unitaires
### test_calculator.py
J'ai écrit des tests unitaires pour la classe Calculator. Les tests incluent les opérations suivantes :
- Addition
- Soustraction
- Multiplication
- Division
J'ai également ajouté des tests pour gérer les cas particuliers, comme la division par zéro.

### test_database.py
J'ai écrit des tests unitaires pour la classe Database. Les tests incluent les méthodes :
- `add_user`
- `get_user`
- `delete_user`
J'ai utilisé les fixtures de pytest pour initialiser et nettoyer la base de données avant et après chaque test.

## Étape 7 : Tests d'intégration
### test_api.py
J'ai écrit des tests d'intégration pour les endpoints de l'API en utilisant le client de test Flask. Les tests couvrent :
- Le bon fonctionnement des endpoints de la calculatrice.
- Le bon fonctionnement des endpoints de gestion des utilisateurs.
- La vérification des codes de statut HTTP et du format des réponses JSON.

## Étape 8 : Mocks et tests avancés
### Utilisation de mocks
J'ai utilisé `pytest-mock` pour simuler le comportement de la base de données dans certains tests. Cela permet de tester les fonctionnalités sans dépendre d'une base de données réelle.

### Analyse de couverture
J'ai exécuté les tests avec un rapport de couverture pour identifier les parties du code qui ne sont pas couvertes. Ensuite, j'ai ajouté des tests pour améliorer la couverture du code.

## Conclusion
Tous les tests ont été exécutés avec succès, et la couverture du code est optimale. L'application fonctionne comme prévu, et toutes les fonctionnalités principales ont été testées avec des tests unitaires et d'intégration appropriés.
