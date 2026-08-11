---
name: api-platform-conventions
description: Conventions de nommage et de structuration pour les ressources API Platform de ce projet (établissements, experts, examens, vacations, comptes rendus). À consulter avant de créer ou modifier une entité/ressource API.
---

# Conventions API Platform — projet téléradiologie

- Une ressource API par concept métier du dossier de projet : `Etablissement`, `Expert`, `Examen`, `Vacation`, `CompteRendu`, `AvisSpecialise`, `RCP`.
- Groupes de sérialisation systématiques : `{ressource}:read` et `{ressource}:write`, jamais d'exposition par défaut de tous les champs.
- Toute donnée médicale (examen, compte rendu) expose un champ `dateSuppressionPrevue` ou équivalent de traçabilité, cohérent avec les exigences de conformité du dossier de projet.
- Sécurité : un Voter dédié par ressource sensible, jamais une vérification de rôle inline dans le contrôleur.
- Pagination et filtres activés par défaut sur les collections volumineuses (liste des examens par établissement).
