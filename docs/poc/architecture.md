# Architecture du POC technique

## Objectif

Le POC doit valider une chaîne simple de téléradiologie :

```text
Établissement fictif
-> import DICOM anonymisé ou synthétique
-> Orthanc
-> DICOMweb
-> OHIF Viewer
-> consultation par un expert
```

## Composants actuels

| Composant | Statut | Commentaire |
|---|---|---|
| Orthanc | Implemented | Service Docker présent dans `poc/docker-compose.yml`. |
| DICOMweb | Partial | Activé côté Orthanc. La consommation par OHIF reste à finaliser. |
| OHIF Viewer | Partial | Service Docker présent. Configuration vers Orthanc à compléter. |
| Données DICOM de test | Planned | Aucune donnée versionnée à ce stade. |
| Maquette accès médecin/établissement | Planned | Aucun backend ou frontend produit n'est encore implémenté. |
| Résilience réseau | Planned | Tests à définir et documenter. |
| OVHcloud | Planned | Le POC doit rester redéployable, mais aucun déploiement cloud n'est configuré. |

## Contraintes

- Ne pas utiliser de données patient réelles.
- Ne pas introduire d'architecture multi-pays pour le POC.
- Ne pas implémenter de workflow médical de production.
- Garder la configuration portable entre local et redéploiement OVHcloud.
