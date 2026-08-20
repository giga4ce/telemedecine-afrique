# AGENTS.md — Contexte permanent du projet (Codex)

Ce fichier est l'équivalent de `CLAUDE.md` pour les agents Codex. Le contenu de fond est identique — se référer à `CLAUDE.md` en cas de doute sur une règle. Ce fichier reprend les mêmes informations pour garantir que tout outil IA lancé dans ce dossier parte du même contexte.

## Projet

Réseau francophone de télémédecine — Phase 1 : téléradiologie. Le POC technique actuel valide Orthanc, DICOMweb et OHIF avec le Tchad comme premier terrain de validation.

Document de vision : `docs/product/vision.md`

## État du projet

- Phase actuelle : POC technique, aucune donnée patient réelle.
- Stack : Orthanc (serveur DICOM) + OHIF Viewer, Docker, local puis OVHcloud.
- Premier terrain de validation : Tchad.
- Statut réglementaire par pays : voir `docs/domain/legal-reserves-by-country.md` — production bloquée tant que l'autorisation Ordre des médecins + Ministère de la Santé n'est pas obtenue.
- Spécifications POC : `docs/poc/scope.md`.

## Règles absolues

1. Aucune donnée patient réelle, à aucun stade, y compris en local. Utiliser uniquement des données DICOM anonymisées/synthétiques.
2. Ne pas implémenter de flux supposant une autorisation réglementaire acquise dans un pays non confirmé.
3. Toute sortie d'un agent IA touchant à l'interprétation d'image doit être marquée comme suggestion, jamais comme diagnostic final — validation humaine obligatoire.
4. Prioriser la résilience réseau (connexions faibles/instables) et la tolérance aux coupures électriques dans toute implémentation.
5. Documentation et commentaires de code en français.

## Commandes utiles (à compléter au fur et à mesure)

```bash
# Lancer le POC en local (une fois docker-compose.yml complété dans poc/)
cd poc && docker compose up -d

# Arrêter
cd poc && docker compose down
```

## Structure

- `docs/` — documentation de fond (dossier projet, réserves juridiques, cahier des charges).
- `poc/` — infrastructure Docker du POC.
- `docs/target-platform/ai-functional-agents/` — spécifications des fonctions IA futures du produit.
- `data/` — données de test uniquement, jamais de données réelles.
