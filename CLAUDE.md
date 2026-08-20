# CLAUDE.md — Contexte permanent du projet

Ce fichier est chargé automatiquement par Claude Code au démarrage de chaque session dans ce dossier. Il définit le contexte, les règles et les priorités du projet. Ne pas le laisser devenir un simple journal : chaque ligne doit changer le comportement de l'agent.

## Projet

Réseau francophone de télémédecine — Phase 1 : téléradiologie. Le POC technique actuel valide Orthanc, DICOMweb et OHIF avec le Tchad comme premier terrain de validation. La Côte d'Ivoire et le Cameroun restent dans la vision multi-pays, mais ils ne conditionnent pas le POC.

Document de vision : `docs/product/vision.md`

## Où en est le projet (à tenir à jour)

- Phase actuelle : **POC technique** (pas de production, pas de données patient réelles).
- Stack cible du POC : **Orthanc** (serveur DICOM) + **OHIF Viewer** (visualiseur web), conteneurisés avec Docker, développés en local puis déployés sur **OVHcloud**.
- Premier terrain de validation : **Tchad**.
- Statut réglementaire : autorisation préalable de l'Ordre des médecins et du Ministère de la Santé requise avant toute mise en production. Voir `docs/domain/legal-reserves-by-country.md`.
- Cahier des charges du POC : `docs/poc/scope.md`.

## Règles absolues (non négociables)

1. **Aucune donnée patient réelle, jamais**, y compris en local, en test, en démo. Utiliser exclusivement des jeux de données DICOM anonymisés ou synthétiques.
2. Ne pas coder de logique métier qui suppose une autorisation réglementaire acquise dans un pays tant que ce n'est pas confirmé dans `docs/domain/legal-reserves-by-country.md`.
3. Toute fonctionnalité touchant à un diagnostic assisté par IA doit rester clairement distincte du compte rendu médical officiel et nécessite une validation humaine — ne jamais faire produire à un agent IA une sortie présentée comme un diagnostic définitif.
4. Concevoir en priorité pour des conditions de connectivité faible/instable et des coupures électriques (reprise sur erreur, pas de perte de données, mode file d'attente).
5. Documentation et code commentés en français, sauf conventions techniques universelles (noms de variables, etc.).

## Stack technique

Backend : Symfony + API Platform. Frontend : React. Voir `.claude/skills/api-platform-conventions/` et `.claude/skills/react-conventions/` pour les conventions du projet.

## Structure du dossier

- `docs/product/` — vision, roadmap et glossaire.
- `docs/poc/` — périmètre et architecture du POC technique.
- `docs/domain/` — réserves juridiques par pays.
- `docs/sources/` — documents sources historiques.
- `docs/tooling/` — documents de tooling à extraire plus tard vers le AI Harness.
- `poc/` — infrastructure Docker du POC (Orthanc + OHIF).
- `docs/target-platform/ai-functional-agents/` — spécifications des **fonctions IA futures du produit** — une fiche par fonction.
- `.claude/agents/` — **agents techniques** (sous-agents Claude Code qui aident à construire le projet : backend-symfony, frontend-react, tests-qualite, devops-infra, securite-conformite, dicom-integration).
- `.claude/skills/` — conventions et checklists chargées automatiquement selon la tâche en cours.
- `data/` — jeux de test uniquement (anonymisés/synthétiques). Ne jamais y placer de vraies données.

Ne pas confondre les deux familles : les fiches de `docs/target-platform/ai-functional-agents/` décrivent des fonctionnalités produit futures ; les fichiers de `.claude/agents/` sont des outils de développement qui n'existent pas dans le produit livré.

## Conventions de travail

- Avant de modifier l'architecture du POC, relire `docs/poc/scope.md` et `docs/poc/architecture.md`.
- Avant de spécifier ou coder une fonction IA produit, relire la fiche correspondante dans `docs/target-platform/ai-functional-agents/`.
- Toute hypothèse réglementaire non confirmée doit être signalée comme telle dans le code ou la documentation produite (commentaire `# À valider juridiquement`).
