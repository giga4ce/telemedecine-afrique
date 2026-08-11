# POC — Infrastructure technique

Squelette de départ. Voir `docs/cahier-des-charges-poc.md` pour le périmètre complet et les critères de réussite.

## Démarrage rapide (une fois le docker-compose.yml complété)

```bash
docker compose up -d
```

- Orthanc : http://localhost:8042
- OHIF Viewer : http://localhost:3000

## À faire avant le premier lancement

- [ ] Compléter la configuration OHIF pour pointer vers Orthanc en DICOMweb.
- [ ] Ajouter une authentification basique sur Orthanc.
- [ ] Charger un jeu de données DICOM anonymisées/synthétiques dans `../data/`.
- [ ] Tester l'import d'un examen de bout en bout.

Rappel absolu : aucune donnée patient réelle, à aucun stade (voir `../CLAUDE.md`).
