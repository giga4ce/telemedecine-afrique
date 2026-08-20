---
name: donnees-sante-conformite
description: Checklist de conformité à appliquer à toute tâche touchant des données de santé (stockage, transmission, affichage, logs, fixtures). À consulter avant tout développement touchant une entité médicale.
---

# Conformité données de santé — checklist

Avant de considérer une tâche terminée, vérifier :

1. Aucune donnée patient réelle introduite (code, fixtures, jeux de test, captures d'écran de démonstration).
2. Chiffrement en transit (HTTPS/TLS) et, pour le stockage, au repos.
3. Contrôle d'accès basé sur les rôles vérifié à chaque nouvel endpoint exposant une donnée médicale.
4. Aucun log applicatif ne contient de donnée médicale ou d'identité patient en clair.
5. Toute hypothèse réglementaire non confirmée (voir `docs/domain/legal-reserves-by-country.md`) est signalée dans le code par un commentaire explicite, pas silencieusement supposée acquise.

En cas de doute sur un point de cette liste, déléguer une revue à l'agent `securite-conformite` plutôt que de trancher seul.
