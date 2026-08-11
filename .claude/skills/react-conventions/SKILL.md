---
name: react-conventions
description: Conventions de structuration des composants React et d'appel à l'API pour ce projet. À consulter avant de créer un composant ou un hook d'appel API.
---

# Conventions React — projet téléradiologie

- Un client API centralisé (ex. `apiClient.ts`) : aucun `fetch`/`axios` direct dispersé dans les composants.
- Composants organisés par domaine métier (`etablissements/`, `examens/`, `experts/`, `vacations/`) plutôt que par type technique.
- Tout composant affichant une donnée médicale ou un statut d'examen gère explicitement trois états : chargement, erreur réseau, succès — pas d'état implicite.
- Les suggestions produites par un agent IA fonctionnel (ex. second regard IA) sont affichées dans un composant visuellement distinct (bordure, étiquette "Suggestion IA — à valider"), jamais fondues dans le contenu validé.
