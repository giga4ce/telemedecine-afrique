# Fonction IA 5 — Second regard IA sur l'image

**Horizon** : phase de consolidation (post-pilote)

## Objectif
Fournir une assistance à la détection (ex. nodules pulmonaires, fractures) en complément — jamais en remplacement — de la lecture experte, en s'appuyant sur des outils déjà validés cliniquement.

## Entrées
- Image DICOM de l'examen.
- Type d'examen et région anatomique.

## Sorties
- Suggestions de zones d'intérêt ou d'anomalies potentielles, avec niveau de confiance.
- Trace explicite de la suggestion IA, distincte du compte rendu médical.

## Garde-fous
- Ne remplace jamais la lecture du radiologue ; n'apparaît jamais comme un diagnostic.
- Utilisation d'outils déjà validés cliniquement uniquement — pas de modèle expérimental non validé sur ce périmètre.
- Traçabilité complète : chaque suggestion horodatée et associée à la version du modèle utilisé.
- Validation par le comité médical de pilotage avant tout déploiement (voir dossier de projet, gouvernance qualité).

## Statut
Spécification — non développé. Prérequis : validation clinique des outils envisagés.
