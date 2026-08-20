# Fonction IA 1 — Pré-tri et priorisation des examens

**Horizon** : pilote opérationnel post-POC

## Objectif
Analyser les métadonnées d'un examen reçu (type, urgence relative, sur-spécialité requise) et proposer un ordre de traitement ainsi qu'une affectation suggérée à l'expert le plus pertinent selon compétence et disponibilité.

## Entrées
- Métadonnées DICOM de l'examen (type d'examen, établissement d'origine, date/heure de réception).
- Annuaire des experts disponibles (sur-spécialité, disponibilité déclarée, charge en cours).

## Sorties
- Une proposition d'ordre de traitement de la file d'attente.
- Une suggestion d'affectation expert ↔ examen, avec justification courte.

## Garde-fous
- L'affectation reste une **suggestion** : la coordination humaine valide ou modifie.
- Aucune priorisation basée sur des critères autres que le type d'examen et la disponibilité (pas de tri implicite par établissement ou pays).

## Statut
Spécification — non développé.
