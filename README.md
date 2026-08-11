# Réseau francophone de télémédecine — Écosystème technique

Dossier de travail pour le développement du POC de téléradiologie et des agents IA associés, destiné à être ouvert avec **Claude Code** et/ou **Codex**.

## Démarrage

1. Ouvrir un terminal dans ce dossier.
2. Lancer `claude` (Claude Code) ou `codex` selon l'outil utilisé — le contexte est chargé automatiquement via `CLAUDE.md` / `AGENTS.md`.
3. Le contexte projet, les règles absolues et l'état d'avancement sont dans `CLAUDE.md` (Claude Code) et `AGENTS.md` (Codex) — contenu équivalent, à garder synchronisé si l'un des deux est modifié.

## Structure

```
teleradiologie-afrique/
├── CLAUDE.md                  # Contexte pour Claude Code
├── AGENTS.md                  # Contexte pour Codex
├── README.md                  # Ce fichier
├── docs/
│   ├── dossier-projet.md              # Synthèse du dossier de projet
│   ├── dossier-projet-original.docx   # Document source complet
│   ├── reserves-juridiques-pays.md    # État des lieux juridique par pays
│   └── cahier-des-charges-poc.md      # Spécifications techniques du POC
├── poc/
│   ├── docker-compose.yml     # Squelette Orthanc + OHIF (à compléter)
│   └── README.md
├── agents-ia/
│   ├── README.md              # Vue d'ensemble des 8 agents prévus
│   └── 01-...08-...md         # Une fiche de spécification par agent
└── data/                      # Données de test UNIQUEMENT (anonymisées/synthétiques)
```

## Règle absolue à ne jamais perdre de vue

Aucune donnée patient réelle ne doit jamais transiter par ce dépôt, à quelque stade que ce soit. Voir `CLAUDE.md` pour la liste complète des règles non négociables.
