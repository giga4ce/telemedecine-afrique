# POC — Infrastructure technique

Ce dossier contient le squelette Docker du POC de téléradiologie.

## Statut actuel

| Élément | Statut | Commentaire |
|---|---|---|
| Docker Compose | Implemented | `docker-compose.yml` existe et déclare Orthanc + OHIF. |
| Orthanc | Implemented | Service exposé sur `localhost:8042`. |
| DICOMweb | Partial | Activé côté Orthanc. |
| OHIF Viewer | Partial | Service exposé sur `localhost:3000`, mais la configuration vers Orthanc reste à finaliser. |
| Import DICOM de test | Planned | Aucun jeu DICOM anonymisé ou synthétique n'est versionné. |
| Démonstration bout-en-bout | Planned | À valider après configuration OHIF et chargement de données de test. |

## Commandes locales

Le Compose peut être lancé pour travailler sur la configuration :

```bash
docker compose up -d
```

URLs attendues après lancement :

- Orthanc : http://localhost:8042
- OHIF Viewer : http://localhost:3000

Ces URLs ne signifient pas encore que la chaîne Orthanc -> DICOMweb -> OHIF est fonctionnelle.

## À faire avant une démonstration

- [ ] Compléter la configuration OHIF pour pointer vers Orthanc en DICOMweb.
- [ ] Ajouter une authentification basique sur Orthanc avant toute démo partagée.
- [ ] Charger un jeu de données DICOM anonymisées ou synthétiques dans `../data/`.
- [ ] Tester l'import et la consultation d'un examen de bout en bout.
- [ ] Documenter un test de réseau lent, coupure et reprise.

Aucune donnée patient réelle ne doit être utilisée.
