# Cahier des charges technique — POC Plateforme de téléradiologie francophone

**Projet :** Réseau francophone de télémédecine — Phase 1 Téléradiologie (Tchad, Côte d'Ivoire, Cameroun)
**Objet du document :** Spécifications techniques du Proof of Concept (POC), à l'attention d'un développeur ou d'un prestataire
**Version :** 1.0

---

## Note de cadrage actuelle

Le périmètre historique mentionne le Tchad, la Côte d'Ivoire et le Cameroun comme pays pilotes de la vision produit. Le POC technique actuel est indépendant d'un déploiement simultané dans trois pays.

L'exécution démarre par le Tchad comme premier terrain de validation. Le code du POC doit rester simple : il valide Orthanc, DICOMweb, OHIF et les simulations minimales d'accès, sans architecture multi-pays.

## 1. Contexte et objectif du POC

Le projet vise à connecter des établissements de santé d'Afrique francophone à un réseau d'experts radiologues francophones, via une plateforme de téléradiologie sécurisée. Avant tout déploiement réel (qui nécessite l'autorisation préalable des Ordres des médecins et des Ministères de la Santé des pays pilotes, ainsi que des partenariats hospitaliers signés), un **POC technique** doit démontrer la faisabilité de la chaîne technologique de bout en bout, dans des conditions représentatives du terrain (connectivité limitée, coupures d'électricité).

**Le POC n'a pas vocation à être mis en production.** Il sert à :
- Valider la faisabilité technique de la chaîne réception → stockage → lecture d'images DICOM.
- Tester le comportement du système dans des conditions réseau dégradées.
- Maquetter le parcours d'inscription et de validation des utilisateurs (médecins, établissements).
- Servir de support de démonstration auprès de la porteuse de projet, de futurs partenaires et d'un bailleur.

## 2. Périmètre

### Inclus dans le POC
- Déploiement d'un serveur DICOM (Orthanc) et d'un visualiseur web (OHIF Viewer).
- Import et affichage d'images DICOM **anonymisées ou synthétiques uniquement**.
- Simulation d'un envoi d'examen depuis un établissement fictif.
- Simulation du parcours d'inscription d'un médecin avec validation par un administrateur.
- Simulation de la création d'accès pour un établissement après un « partenariat » fictif.
- Test du comportement en connexion lente/instable.
- Déploiement en deux temps : environnement local, puis bascule sur une instance cloud OVHcloud.

### Explicitement hors périmètre
- Toute donnée patient réelle, sous quelque forme que ce soit.
- Authentification et sécurité de niveau production (chiffrement bout-en-bout complet, conformité HDS, audit de sécurité).
- Intégration avec un PACS/RIS hospitalier réel.
- Rédaction de comptes rendus médicaux (structuration, validation médicale).
- Visioconférence / RCP à distance.
- Facturation, gestion des plannings de vacations.
- Réseau complet d'experts.
- Plateforme opérationnelle multi-pays.
- Automatisation médicale par IA.

## 3. Architecture technique

### 3.1 Composants principaux

| Composant | Rôle | Technologie |
|---|---|---|
| Serveur DICOM | Réception, stockage, routage des images | Orthanc (open source) |
| Visualiseur | Affichage web des examens (zoom, contraste, défilement) | OHIF Viewer (open source), via protocole DICOMweb |
| Conteneurisation | Portabilité entre local et cloud | Docker + Docker Compose |
| Interface de gestion des accès (maquette) | Simulation du workflow inscription/validation | Développement simple à définir avec le prestataire (ex. application web légère) |

### 3.2 Schéma de principe

```
[Établissement fictif] → upload DICOM → [Orthanc] → DICOMweb → [OHIF Viewer] → [Expert radiologue]
                                              ↑
                                   [Interface admin : validation
                                    médecins / accès établissements]
```

### 3.3 Environnement d'exécution

- **Phase locale** : Docker Desktop (Windows/Mac) ou Docker Engine (Linux), poste avec 8 Go de RAM minimum recommandés.
- **Phase cloud** : instance OVHcloud (offre standard pour le POC ; bascule possible vers une offre certifiée HDS lors du passage en production).
- Même fichier `docker-compose.yml` et mêmes variables d'environnement utilisés dans les deux phases, pour garantir une bascule sans reconstruction.

## 4. Jeu de données de test

- Utilisation exclusive de **données DICOM anonymisées ou synthétiques** (jeux de données publics de test ou générateur de données factices).
- Aucune donnée patient réelle, à aucun moment du POC, y compris en environnement local.
- Le jeu de données doit couvrir au moins deux types d'examens (ex. scanner et IRM) pour tester la variabilité de taille de fichiers.

## 5. Spécifications fonctionnelles à démontrer

1. **Réception d'un examen** : un établissement fictif transmet un examen DICOM à la plateforme.
2. **Stockage et organisation** : l'examen est stocké et retrouvable (par établissement, type d'examen, date).
3. **Lecture à distance** : un expert accède à l'examen via le visualiseur web, sans installation locale (zero-footprint).
4. **Résilience réseau** : test de l'envoi et de la consultation en conditions de bande passante réduite et de coupure/reprise de connexion.
5. **Parcours d'inscription médecin** : un médecin soumet une demande d'inscription ; un administrateur valide ou refuse ; le médecin ne peut agir qu'après validation.
6. **Parcours établissement** : un partenariat fictif est enregistré ; l'administrateur crée les accès pour les personnes habilitées côté établissement.

## 6. Plan de déploiement

| Étape | Environnement | Contenu | Durée indicative |
|---|---|---|---|
| 1 | Local | Déploiement Docker d'Orthanc + OHIF, import des données de test | Semaine 1 |
| 2 | Local | Tests de connectivité dégradée, coupure/reprise | Semaine 2 |
| 3 | Local | Maquette des parcours d'inscription/validation | Semaine 3 |
| 4 | OVHcloud | Bascule des mêmes conteneurs vers une instance OVH | Fin semaine 3 / début semaine 4 |
| 5 | OVHcloud | Répétition des tests clés en environnement cloud, préparation de la démonstration | Semaine 4 |

## 7. Critères de réussite du POC

- Un examen DICOM de test peut être transmis, stocké et affiché de bout en bout, en local puis sur OVH, sans perte de données.
- Le visualiseur permet une lecture confortable (zoom, contraste, défilement des coupes) directement dans un navigateur standard.
- Le système résiste à une simulation de coupure réseau : la transmission reprend sans nécessiter un renvoi complet du fichier.
- Le parcours d'inscription médecin et le parcours établissement sont fonctionnels dans leur logique (même en version simplifiée), avec un statut « en attente de validation » clairement visible.
- La bascule local → OVH ne nécessite pas de réécriture de la configuration, seulement un redéploiement.

## 8. Points de vigilance pour le prestataire

- Aucune donnée patient réelle ne doit transiter par le POC, à aucun stade.
- Le POC est un démonstrateur technique : la sécurité de niveau production (chiffrement complet, conformité réglementaire par pays, audit) sera spécifiée séparément lors du passage en production, une fois les autorisations obtenues.
- Privilégier la simplicité et la rapidité de mise en œuvre plutôt que l'exhaustivité fonctionnelle — l'objectif est de démontrer la faisabilité, pas de livrer un produit fini.

## 9. Suite après le POC

- Présentation de la démonstration à la porteuse de projet et aux interlocuteurs pertinents (Ordres des médecins, Ministères de la Santé, futurs établissements partenaires, bailleur).
- En parallèle du POC, poursuite du travail administratif : demandes d'autorisation auprès des Ordres et Ministères, négociation des premiers partenariats hospitaliers.
- Une fois les autorisations obtenues dans le premier pays retenu pour le pilote opérationnel, spécification détaillée de la plateforme de production sur la base des enseignements du POC.
