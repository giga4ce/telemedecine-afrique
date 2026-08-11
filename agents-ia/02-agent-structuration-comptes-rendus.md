# Agent 2 — Assistant de structuration des comptes rendus

**Horizon** : phase pilote

## Objectif
Aider le radiologue à rédiger un compte rendu structuré : proposer un modèle adapté au type d'examen, harmoniser la terminologie, signaler les incohérences avant validation.

## Entrées
- Type d'examen et sur-spécialité concernée.
- Notes ou dictée du radiologue (texte libre).

## Sorties
- Un compte rendu structuré en brouillon, avec sections standard (technique, résultats, conclusion).
- Signalements de cohérence (ex. terme ambigu, section manquante) — jamais de correction silencieuse du contenu médical.

## Garde-fous
- Le radiologue reste seul signataire et responsable du compte rendu final.
- L'agent ne doit jamais ajouter de constat médical non fourni par le radiologue.
- Toute suggestion de contenu doit être visuellement distincte du texte du radiologue jusqu'à validation explicite.

## Statut
Spécification — non développé.
