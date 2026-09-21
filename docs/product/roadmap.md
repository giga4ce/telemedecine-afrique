# Roadmap produit

Cette roadmap sépare le POC technique, le premier terrain de validation et la plateforme cible.

## 1. POC technique actuel

Objectif : valider la chaîne technique de téléradiologie avec des données DICOM anonymisées ou synthétiques.

Périmètre :
- Orthanc.
- DICOMweb.
- OHIF Viewer.
- Docker Compose.
- Import et consultation d'examens DICOM de test.
- Simulation minimale d'un établissement envoyant un examen.
- Simulation minimale du parcours médecin et de la validation administrative.
- Tests de réseau lent, instable, coupure et reprise.
- Fonctionnement local.
- Préparation d'un redéploiement ultérieur sur OVHcloud.

Le premier terrain de validation est le Tchad.

Le pays de la **démonstration et de l'exécution technique actuelle** (Tchad) ne préjuge pas du pays retenu pour le **premier lancement opérationnel réel** après obtention des autorisations : sur le plan réglementaire, la Côte d'Ivoire — dotée d'un décret télémédecine (2018) — reste le candidat le plus avancé (voir `../domain/legal-reserves-by-country.md`). Terrain de démonstration et pays de premier lancement sont deux questions distinctes.

## 2. Pilote opérationnel après POC

Objectif : transformer la preuve technique en pilote métier encadré.

Préconditions :
- Autorisations réglementaires obtenues pour le pays concerné.
- Partenariats établissements validés.
- Jeu de procédures médicales et opérationnelles approuvé.
- Sécurité adaptée au contexte de données réelles.

Les workflows de comptes rendus, deuxième lecture, vacations, support établissement et réseau d'experts relèvent de cette étape ou des suivantes.

## 3. Extension pays et services

Objectif : étendre le modèle à d'autres pays et services après validation du POC et du pilote opérationnel.

La Côte d'Ivoire et le Cameroun restent dans la vision historique. Leur intégration dépendra des validations réglementaires, des partenaires locaux et des résultats du premier terrain.

Services cibles :
- Comptes rendus médicaux.
- Deuxième lecture.
- Avis spécialisés.
- RCP à distance.
- Gestion des vacations.
- Facturation.
- Qualité et audit.
- Fonctions IA d'assistance, jamais de diagnostic autonome.
