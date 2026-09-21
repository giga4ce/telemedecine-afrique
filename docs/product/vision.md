# Synthèse du dossier de projet

Le document source complet historique est dans `../sources/dossier-projet-original.md`. Cette synthèse conserve la vision stratégique du projet.

## Note de cadrage actuelle

Le dossier historique envisage un pilote couvrant le Tchad, la Côte d'Ivoire et le Cameroun. L'exécution actuelle est séquencée : le POC technique de téléradiologie se concentre sur la chaîne Orthanc, DICOMweb et OHIF, avec le Tchad comme premier terrain de validation.

Cette priorisation ne remet pas en cause la vision multi-pays. Elle évite de faire dépendre le POC technique d'une plateforme opérationnelle multi-pays.

Le POC technique actuel constitue une **première tranche** de la « Phase 1 » décrite dans le dossier historique, et non son équivalent complet : les comptes rendus médicaux, la deuxième lecture, les RCP, la gestion des vacations et le déploiement multi-pays restent **hors du périmètre du POC actuel** (voir `../poc/scope.md`).

## Résumé

Réseau francophone de télémédecine pour l'Afrique. Phase 1 : plateforme de téléradiologie (comptes rendus, deuxième lecture, avis spécialisés, RCP à distance) connectant des établissements de santé à des radiologues experts francophones.

## Modèle économique clé

Mutualisation des flux d'examens de plusieurs établissements par vacation pour atteindre un volume rentable. Revenus à l'acte (téléradiologie, avis, deuxième lecture, RCP) + revenus récurrents (abonnements, formation, accompagnement qualité).

## Pays pilotes

Tchad, Côte d'Ivoire, Cameroun. Cible : 5 vacations/semaine, ~25 examens/vacation, ~125 examens/semaine en régime de croisière du pilote.

## Segments clients

Hôpitaux publics, cliniques privées, centres d'imagerie, cabinets médicaux.

## Contraintes terrain à intégrer techniquement

- Connectivité internet souvent limitée ou instable.
- Coupures électriques fréquentes.
- Nécessité d'un mode dégradé / offline-first pour la transmission d'examens.

## Statut réglementaire et organisationnel

Voir `../domain/legal-reserves-by-country.md` pour le détail. Résumé : dans les 3 pays, une autorisation préalable de l'Ordre des médecins et du Ministère de la Santé est nécessaire, ainsi que des partenariats hospitaliers signés, avant toute mise en production. Workflow prévu :
- Un médecin spécialiste s'inscrit sur la plateforme → validation par un administrateur avant de pouvoir exercer.
- Un établissement signe un partenariat → l'administrateur de la plateforme crée les accès pour les personnes habilitées à envoyer des examens.

## Fonctions IA futures du produit

Voir `../target-platform/ai-functional-agents/` pour les fiches détaillées. Ces documents décrivent des fonctions futures du produit, pas des outils de développement.
