# Déploiement de l'Application Flask avec PostgreSQL sur Kubernetes

## **1. Création du namespace `database`**
Le namespace `database` est utilisé pour isoler les ressources liées à PostgreSQL.

```bash
kubectl create namespace database
```
## **2. Lancement du Pod de la DB**
Le fichier postgres-deployment.yaml contient :

* Un ConfigMap pour la configuration.
* Un Secret pour le mot de passe.
* Le Deployment pour PostgreSQL.
* Un Service pour l'accès au Pod.
* Un PersistentVolumeClaim pour la persistance des données.

```bash
kubectl apply -f ./k8s/postgres-deployment.yaml
```
## **3. Lancement du pod de l'application Flask**
Dans un premier temps on génère l'image de l'application :
```bash
docker build -t simple-app-crud-psql-application:latest .
```
Le fichier web-logs-deployment.yaml contient :

* Un Pod avec deux conteneurs :
* flask-app (application Flask).
* log-collector (collecteur de logs simple).
* Un Service de type LoadBalancer pour exposer l'application.
```bash
kubectl apply -f ./k8s/web-logs-deployment.yaml
```
## **4. Obtenir les logs**
```bash
kubectl logs <nom du pod> -c flask-app
```
