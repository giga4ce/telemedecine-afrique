# Synthèse du dossier de projet

Le document source complet (mise en page bailleur) est dans `dossier-projet-original.docx`. Cette synthèse est la version de référence pour un agent IA.

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

Voir `reserves-juridiques-pays.md` pour le détail. Résumé : dans les 3 pays, une autorisation préalable de l'Ordre des médecins et du Ministère de la Santé est nécessaire, ainsi que des partenariats hospitaliers signés, avant toute mise en production. Workflow prévu :
- Un médecin spécialiste s'inscrit sur la plateforme → validation par un administrateur avant de pouvoir exercer.
- Un établissement signe un partenariat → l'administrateur de la plateforme crée les accès pour les personnes habilitées à envoyer des examens.

## Roadmap agents IA (vision)

Voir le dossier `agents-ia/` pour les fiches détaillées. Priorité phase pilote : pré-tri des examens, aide à la structuration des comptes rendus, coordination des plannings, support établissements. Priorité phase de consolidation : second regard IA sur l'image, contrôle qualité rétrospectif, synthèse des RCP, veille réglementaire multi-pays.
