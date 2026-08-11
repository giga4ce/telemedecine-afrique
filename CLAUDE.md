# CLAUDE.md — Contexte permanent du projet

Ce fichier est chargé automatiquement par Claude Code au démarrage de chaque session dans ce dossier. Il définit le contexte, les règles et les priorités du projet. Ne pas le laisser devenir un simple journal : chaque ligne doit changer le comportement de l'agent.

## Projet

Réseau francophone de télémédecine — Phase 1 : plateforme de téléradiologie connectant des établissements de santé du Tchad, de la Côte d'Ivoire et du Cameroun à un réseau d'experts radiologues francophones. Modèle économique basé sur la mutualisation des volumes d'examens par vacation.

Document de référence complet : `docs/dossier-projet.md`

## Où en est le projet (à tenir à jour)

- Phase actuelle : **POC technique** (pas de production, pas de données patient réelles).
- Stack cible du POC : **Orthanc** (serveur DICOM) + **OHIF Viewer** (visualiseur web), conteneurisés avec Docker, développés en local puis déployés sur **OVHcloud**.
- Statut réglementaire : autorisation préalable de l'Ordre des médecins et du Ministère de la Santé requise dans les 3 pays avant toute mise en production. Voir `docs/reserves-juridiques-pays.md`.
- Cahier des charges du POC : `docs/cahier-des-charges-poc.md`.

## Règles absolues (non négociables)

1. **Aucune donnée patient réelle, jamais**, y compris en local, en test, en démo. Utiliser exclusivement des jeux de données DICOM anonymisés ou synthétiques.
2. Ne pas coder de logique métier qui suppose une autorisation réglementaire acquise dans un pays tant que ce n'est pas confirmé dans `docs/reserves-juridiques-pays.md`.
3. Toute fonctionnalité touchant à un diagnostic assisté par IA doit rester clairement distincte du compte rendu médical officiel et nécessite une validation humaine — ne jamais faire produire à un agent IA une sortie présentée comme un diagnostic définitif.
4. Concevoir en priorité pour des conditions de connectivité faible/instable et des coupures électriques (reprise sur erreur, pas de perte de données, mode file d'attente).
5. Documentation et code commentés en français, sauf conventions techniques universelles (noms de variables, etc.).

## Stack technique

Backend : Symfony + API Platform. Frontend : React. Voir `.claude/skills/api-platform-conventions/` et `.claude/skills/react-conventions/` pour les conventions du projet.

## Structure du dossier

- `docs/` — dossier de projet, réserves juridiques par pays, cahier des charges POC, connecteurs MCP recommandés.
- `poc/` — infrastructure Docker du POC (Orthanc + OHIF).
- `agents-ia/` — spécifications des **agents fonctionnels** (métier, tournent dans le produit final) — une fiche par agent.
- `.claude/agents/` — **agents techniques** (sous-agents Claude Code qui aident à construire le projet : backend-symfony, frontend-react, tests-qualite, devops-infra, securite-conformite, dicom-integration).
- `.claude/skills/` — conventions et checklists chargées automatiquement selon la tâche en cours.
- `data/` — jeux de test uniquement (anonymisés/synthétiques). Ne jamais y placer de vraies données.

Ne pas confondre les deux familles d'agents : ceux de `agents-ia/` sont des spécifications de fonctionnalités produit ; ceux de `.claude/agents/` sont des outils de développement qui n'existent pas dans le produit livré.

## Conventions de travail

- Avant de modifier l'architecture du POC, relire `docs/cahier-des-charges-poc.md`.
- Avant de spécifier ou coder un agent IA, relire la fiche correspondante dans `agents-ia/`.
- Toute hypothèse réglementaire non confirmée doit être signalée comme telle dans le code ou la documentation produite (commentaire `# À valider juridiquement`).
