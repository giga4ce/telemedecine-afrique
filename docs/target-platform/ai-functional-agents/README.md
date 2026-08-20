# Fonctions IA futures du produit — vue d'ensemble

Ce dossier décrit des fonctions IA futures du produit de télémédecine. Il ne décrit pas Codex, Claude, des skills de développement ou le futur AI Harness.

Une fiche par fonction est classée par horizon de mise en œuvre. Chaque fiche suit le même format : objectif, entrées, sorties, garde-fous, statut.

**Règle transversale** : aucune fonction IA ne produit de diagnostic final opposable. Toute sortie touchant à l'interprétation d'image ou à la décision clinique est une suggestion soumise à validation humaine par un radiologue.

## Pilote opérationnel post-POC

1. `01-agent-pretri-priorisation.md`
2. `02-agent-structuration-comptes-rendus.md`
3. `03-agent-coordination-plannings.md`
4. `04-agent-support-etablissements.md`

## Phase de consolidation — valeur qualité

5. `05-agent-second-regard-ia.md`
6. `06-agent-controle-qualite.md`
7. `07-agent-synthese-rcp.md`
8. `08-agent-veille-reglementaire.md`

## Statut

Toutes les fiches sont au stade **spécification** — aucun développement n'a encore démarré. À utiliser comme point de départ pour cadrer chaque fonction avant implémentation.

Ces fonctions sont postérieures au POC technique actuel, qui se limite à Orthanc, DICOMweb, OHIF, Docker Compose, données DICOM anonymisées ou synthétiques, et simulations minimales d'accès.
