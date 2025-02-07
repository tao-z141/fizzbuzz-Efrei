# FizzBuzz avec Docker et Tests Unitaires

Ce projet implémente l'algorithme **FizzBuzz** en Python et inclut des **tests unitaires** avec `unittest`.  
J'ai utilisé **Docker** pour exécuter l'application et les tests, et **GitHub Actions** pour l'intégration continue avec un rapport de couverture de code.

## **Installation et Exécution en Local**

### **Cloner le projet**

git clone https://github.com/tao-z141/fizzbuzz-Efrei

cd fizzbuzz-docker

**Exécuter le programme**

python main.py

**Exécuter les tests**

python -m unittest Unit_test.py

#### ** Utilisation avec Docker**
**Construire l’image Docker**

docker build -t fizzbuzz-docker .

**Exécuter le programme avec Docker**

docker run --rm fizzbuzz-docker

**Exécuter les tests avec Docker**

docker run --rm fizzbuzz-docker python -m unittest Unit_test.py

**Exécuter les tests avec coverage**

docker run --rm fizzbuzz-docker sh -c "coverage run --source=main -m unittest Unit_test.py && coverage report"
