# Déploiement de l'Application Flask avec PostgreSQL sur Kubernetes

## **1. Création du namespace `database`**
Le namespace `database` est utilisé pour isoler les ressources liées à PostgreSQL.

```bash
kubectl create namespace database
```