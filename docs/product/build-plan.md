# Plan de construction — POC de téléradiologie

**Statut :** décisions d'architecture actées ; 19 tickets créés de KAN-4 à KAN-22 ; prêt pour le démarrage du code sur KAN-5.
**Périmètre :** inventaire documentaire, synthèse du produit attendu, specs actionnables et ordre de réalisation.  
**Source canonique du POC :** `docs/poc/scope.md`. Les documents de vision et de plateforme cible ne l'étendent pas.

## 1. Inventaire documentaire

### 1.1 Arborescence complète de `docs/`

```text
docs/
├── README.md
├── domain/
│   └── legal-reserves-by-country.md
├── poc/
│   ├── architecture.md
│   └── scope.md
├── product/
│   ├── build-plan.md
│   ├── glossary.md
│   ├── roadmap.md
│   └── vision.md
├── sources/
│   ├── README.md
│   └── dossier-projet-original.md
└── target-platform/
    └── ai-functional-agents/
        ├── README.md
        ├── 01-agent-pretri-priorisation.md
        ├── 02-agent-structuration-comptes-rendus.md
        ├── 03-agent-coordination-plannings.md
        ├── 04-agent-support-etablissements.md
        ├── 05-agent-second-regard-ia.md
        ├── 06-agent-controle-qualite.md
        ├── 07-agent-synthese-rcp.md
        └── 08-agent-veille-reglementaire.md
```

`docs/product/build-plan.md` est le présent document.

### 1.2 Documents lus

L'ordre suivi est celui de `.claude/context/reading-order.md`, puis les autres documents :

1. `README.md`
2. `docs/README.md`
3. `docs/poc/scope.md`
4. `docs/poc/architecture.md`
5. `docs/product/roadmap.md`
6. `docs/domain/legal-reserves-by-country.md`
7. `docs/product/vision.md`, `docs/product/glossary.md`
8. `docs/target-platform/ai-functional-agents/README.md` et les huit fiches
9. `docs/sources/README.md`, `docs/sources/dossier-projet-original.md`
10. `.claude/context/project-rules.md`, `poc-boundaries.md`, `workflow.md`, `repository-map.md`, ainsi que `reading-order.md` et `jira.md`
11. Les six fiches d'agents techniques sous `.claude/agents/`
12. Les autres documents du dépôt utiles au constat : `poc/README.md`, `data/README.md` et `poc/docker-compose.yml`

Le dossier historique `agents-ia/` n'existe plus. Ses huit fiches d'agents **fonctionnels** ont été déplacées sous `docs/target-platform/ai-functional-agents/`. Elles ne doivent pas être confondues avec les agents **techniques** de développement sous `.claude/agents/`.

### 1.3 État documenté et constaté du dépôt

| Élément | État |
|---|---|
| Orthanc | Présent dans `poc/docker-compose.yml` |
| DICOMweb | Activé côté Orthanc ; consommation OHIF à finaliser |
| OHIF Viewer | Présent dans le Compose ; configuration Orthanc manquante |
| Backend FastAPI | Service déclaré comme squelette dans le Compose ; dossier `backend/` vide |
| Frontend React produit | Dossier `frontend/` vide ; OHIF est le seul frontend actuellement déclaré |
| Base relationnelle | Aucun moteur ni service déclaré |
| Données DICOM de démonstration | Aucune donnée versionnée |
| Résilience réseau | Tests à définir et documenter |
| OVHcloud | Aucun déploiement configuré |

### 1.4 Incohérences, tensions et ambiguïtés relevées — statut de résolution

| # | Sujet | Constat contradictoire ou ambigu | Sources |
|---|---|---|---|
| C1 | Portée de FastAPI | FastAPI est présenté comme stack cible non initialisée et non indispensable à la chaîne POC, mais un service `backend` obligatoire est déjà déclaré dans le Compose. | `README.md`, `docs/poc/architecture.md`, `poc/docker-compose.yml` |
| C2 | Persistance | SQLAlchemy/Alembic sont annoncés comme stack cible, mais aucun moteur de base n'est choisi ou déclaré. Les parcours d'accès impliquent pourtant de conserver comptes, statuts et habilitations. | `README.md`, `docs/poc/scope.md`, Compose |
| C3 | Portée de React | La demande vise React et le README le désigne comme stack cible ; le cahier du POC demande seulement une « application web légère » à définir et n'impose pas React. | `README.md`, `docs/poc/scope.md` |
| C4 | Backend et examens | Le POC exige qu'un examen soit retrouvable par établissement, type et date, mais ne dit pas si cette recherche relève directement d'OHIF/Orthanc ou d'une API FastAPI avec index local. | `docs/poc/scope.md` |
| C5 | Déploiement OVH | Résolu : `scope.md` et `roadmap.md` incluent désormais l'exécution du redéploiement OVH dans le POC. | `docs/poc/scope.md`, `docs/product/roadmap.md` |
| C6 | Reprise réseau | Le POC exige qu'une transmission reprenne sans renvoi complet après coupure, mais aucun protocole ou mécanisme de reprise n'est défini. La vision parle plus largement d'« offline-first ». | `docs/poc/scope.md`, `docs/product/vision.md` |
| C7 | Pays prioritaire | Le Tchad est le premier terrain d'exécution actuel ; le document juridique qualifie la Côte d'Ivoire de candidat naturel au premier lancement, et le dossier historique prévoit trois pays simultanément. | `scope.md`, `roadmap.md`, `legal-reserves-by-country.md`, dossier historique |
| C8 | Ordre de lecture | `.claude/context/reading-order.md` commence par le README et le scope ; `docs/README.md` recommande de commencer par la vision puis la roadmap. | Les deux fichiers cités |
| C9 | POC et plateforme cible | Le dossier historique appelle « phase 1 » une plateforme opérationnelle comprenant comptes rendus, vacations, RCP et trois pays ; le POC actuel exclut explicitement ces fonctions. | Dossier historique, `docs/product/vision.md`, `docs/poc/scope.md` |
| C10 | Sécurité | Le POC exclut la sécurité de niveau production, mais les fiches techniques demandent contrôle d'accès, traçabilité et parfois chiffrement pour les examens. Le niveau minimal exact de la maquette n'est pas spécifié. | `scope.md`, `.claude/agents/*` |

Les « vacations » et « comptes rendus » suggérés comme exemples de modèle de données dans la demande sont explicitement hors POC. Ils ne figurent donc pas dans les specs POC ci-dessous.

**Résolution (2026-09-22)** : C1–C7 et C10 sont tranchées dans **SPEC-01**. C9 est clarifiée dans `docs/product/vision.md` et C7 dans `docs/product/roadmap.md`. C8 (ordre de lecture) est **sans impact pratique** — les deux fichiers couvrent le même corpus, seul l'ordre d'entrée diffère ; aucune modification de `reading-order.md`/`docs/README.md` n'est faite.

## 2. Synthèse du périmètre à construire

### 2.1 Backend FastAPI

La documentation fixe FastAPI async, SQLAlchemy 2.0 et Alembic comme stack cible, mais ne définit pas encore son contrat détaillé. Pour servir le POC documenté, le backend doit rester une couche minimale :

- démarrer dans Docker Compose avec une configuration externalisée ;
- fournir le support persistant de la maquette d'accès : demandes médecins, statut en attente/validé/refusé, établissements fictifs et accès créés par un administrateur ;
- garantir qu'un médecin non validé ne peut pas agir et qu'un établissement ne s'auto-active pas ;
- permettre à la maquette d'administration de consulter et modifier ces statuts ;
- conformément à la décision 4 de SPEC-01, interroger Orthanc/DICOMweb via FastAPI pour retrouver les examens par établissement, type et date, sans dupliquer les images ;
- ne jamais utiliser ni journaliser de donnée patient réelle.

Ne font pas partie du backend POC : comptes rendus, vacations, facturation, RCP, réseau complet d'experts, PACS/RIS réel, multi-pays, IA médicale et sécurité/conformité de production.

### 2.2 Frontend React et OHIF

La documentation distingue deux surfaces :

- **OHIF Viewer**, cœur visuel du POC, configuré sur DICOMweb pour afficher dans un navigateur les examens de test et permettre zoom, contraste et défilement ;
- **maquette de gestion des accès**, réalisée avec React comme acté en SPEC-01 : demande d'inscription médecin, statut « en attente », validation/refus administrateur, établissement fictif et création administrative des accès.

Le frontend doit expliciter les erreurs et états réseau. Il ne doit pas afficher de véritable identité patient. Une intégration native d'OHIF dans React n'est pas imposée : une navigation vers le viewer suffit tant qu'aucune décision contraire n'est prise.

Ne font pas partie du frontend POC : saisie/validation de comptes rendus, planning de vacations, facturation, RCP/visioconférence, tableaux de bord de production et écrans IA.

### 2.3 Chaîne transverse indispensable au POC

- import d'examens DICOM strictement anonymisés ou synthétiques, avec au moins deux types d'examens ;
- stockage dans Orthanc, exposition DICOMweb et consultation OHIF ;
- simulation d'un envoi depuis un établissement fictif ;
- tests en bande passante réduite, coupure et reprise, avec conditions et résultats documentés ;
- portabilité du même Compose et des mêmes variables entre local et OVHcloud ;
- authentification basique Orthanc avant toute démonstration partagée.

## 3. Découpage en specs actionnables

Les dépendances référencent les identifiants ci-dessous. Un agent principal est indiqué pour chaque spec ; les agents de revue ou d'appui sont mentionnés séparément.

### Domaine A — Cadrage et fondations

#### SPEC-01 — Décisions d'architecture actées

- **Objectif :** figer les décisions qui conditionnent l'implémentation, sans élargir le périmètre du POC.
- **Statut :** décidé le 2026-09-22. Les points C1 à C7 et C10 sont tranchés ci-dessous ; ces décisions remplacent les questions ouvertes de la §5.

| # | Décision actée | Motif résumé | Specs impactées | Lève |
|---|---|---|---|---|
| 1 | FastAPI est **dans le périmètre exécutable** du POC. | Le service `backend` est déjà déclaré dans le Compose ; la maquette d'accès a besoin d'une API. | SPEC-02, SPEC-03 | C1 |
| 2 | React est **confirmé** pour la maquette d'accès. | Stack cible du produit ; aligne la maquette sur le frontend visé. | SPEC-13, SPEC-14, SPEC-15, SPEC-16 | C3 |
| 3 | Base relationnelle = **PostgreSQL**. | Compatible SQLAlchemy 2.0/Alembic, portable local↔OVH. | SPEC-04, SPEC-10 | C2 |
| 4 | La recherche d'examens (établissement/type/date) est **médiée par FastAPI**, qui interroge Orthanc côté serveur. | Centralise l'accès, évite d'exposer Orthanc au client, sans dupliquer les pixels. | SPEC-08 | C4 |
| 5 | Reprise réseau = **upload DICOM instance par instance** ; en cas de coupure, seules les instances non confirmées sont retransmises. | Rend le critère « reprise sans renvoi complet » concret et testable. | SPEC-08, SPEC-09 | C6 |
| 6 | OVHcloud est **exécuté dans le POC** (SPEC-18 reste dans le lot). | Conforme à `scope.md` §6 (bascule local→OVH = critère de réussite). | SPEC-18 | C5 |
| 7 | Authentification minimale : **basique sur Orthanc** + **token/session simple** sur les endpoints admin FastAPI, explicitement **non-production**. | Protège la démo partagée sans introduire une sécurité de niveau production, hors périmètre. | SPEC-05, SPEC-11, SPEC-12, SPEC-16 | C10 |

- **Exclus :** architecture de production, multi-pays, HDS, choix des fonctions post-POC.
- **Note post-POC :** SPEC-19 (agent pré-tri) reste documentée comme jalon post-POC mais **hors du lot de tickets actif**.
- **Dépendances :** aucune.
- **Terminé si :** chaque décision est consignée avec son motif et ses specs impactées — atteint.
- **Agent technique principal :** `devops-infra` ; revue `backend-fastapi`, `frontend-react`, `dicom-integration`, `securite-conformite`.

#### SPEC-02 — Socle Compose local portable

- **Objectif :** disposer d'un environnement local reproductible et transposable sur OVH.
- **Inclus :** services Orthanc, OHIF, backend FastAPI, frontend React et base PostgreSQL (actés en SPEC-01) ; variables externalisées ; healthchecks de conteneurs ; persistance Orthanc/base ; aucun secret committé.
- **Exclus :** CI/CD, haute disponibilité, infrastructure HDS et exploitation production.
- **Dépendances :** SPEC-01.
- **Terminé si :** le contrat Compose complet est livré avec réseau, service PostgreSQL, volumes persistants, variables externalisées, noms de services stables, versions d'images figées et healthchecks ; une commande documentée démarre tous les services localement sans secret versionné ; le squelette backend dispose d'un `Dockerfile` minimal qui démarre FastAPI et répond `200` sur `/health`, sans logique métier ; le squelette frontend dispose d'un `Dockerfile` minimal qui sert une page statique.
- **Répartition avec les specs suivantes :** SPEC-02 livre uniquement ces squelettes exécutables et leur intégration Compose ; SPEC-03 enrichit ensuite le backend FastAPI, et SPEC-13 enrichit ensuite le frontend React.
- **Agent technique principal :** `devops-infra`.

#### SPEC-03 — Fondations FastAPI

- **Objectif :** initialiser une API FastAPI async minimale, testable et conteneurisée.
- **Inclus :** structure applicative, configuration par environnement, route de santé, gestion d'erreurs minimale, tests du démarrage et du healthcheck.
- **Exclus :** modèles métier, DICOM, authentification de production.
- **Dépendances :** SPEC-01 ; intégration Compose via SPEC-02.
- **Terminé si :** l'API démarre dans le Compose, répond au healthcheck et ses tests ciblés passent.
- **Agent technique principal :** `backend-fastapi` ; appui `tests-qualite`.

#### SPEC-04 — Persistance SQLAlchemy/Alembic

- **Objectif :** rendre la base choisie accessible à FastAPI avec des migrations réversibles.
- **Inclus :** connexion async, gestion de session, configuration Alembic, migration initiale technique, contrôle de disponibilité de la base.
- **Exclus :** tables métier et données de démonstration.
- **Dépendances :** SPEC-01, SPEC-02, SPEC-03.
- **Terminé si :** une base vierge peut être montée puis migrée en avant et en arrière par les commandes documentées.
- **Agent technique principal :** `backend-fastapi` ; appui `devops-infra`.

### Domaine B — DICOM, viewer et robustesse

#### SPEC-05 — Orthanc sécurisé pour la démonstration

- **Objectif :** rendre Orthanc utilisable dans une démonstration partagée sans accès anonyme.
- **Inclus :** configuration DICOMweb vérifiée, authentification basique externalisée, volume persistant, contrôle des endpoints exposés.
- **Exclus :** sécurité/HDS de production, PACS/RIS réel.
- **Dépendances :** SPEC-02.
- **Décision différée :** avant l'implémentation de SPEC-16, trancher la stratégie d'authentification entre OHIF, Orthanc et FastAPI : reverse proxy, relais DICOMweb côté serveur ou authentification portée par un proxy.
- **Terminé si :** Orthanc refuse un accès non authentifié, accepte les identifiants injectés hors Git et expose DICOMweb aux composants autorisés.
- **Agent technique principal :** `dicom-integration` ; revue lecture seule `securite-conformite`.

#### SPEC-06 — Jeu DICOM de démonstration

- **Objectif :** constituer un jeu sûr couvrant au moins deux types d'examens.
- **Inclus :** données synthétiques ou anonymisées, preuve documentée de leur origine/statut, contrôle de l'absence d'identité réelle, procédure reproductible d'import.
- **Exclus :** toute donnée patient réelle, constitution d'un dataset clinique.
- **Dépendances :** SPEC-05.
- **Terminé si :** au moins deux examens de types distincts sont importables et contrôlés comme synthétiques/anonymisés, sans identité réelle même partielle.
- **Agent technique principal :** `dicom-integration` ; revue lecture seule `securite-conformite`.

#### SPEC-07 — OHIF connecté à DICOMweb

- **Objectif :** rendre la chaîne Orthanc → DICOMweb → OHIF consultable dans un navigateur.
- **Inclus :** configuration OHIF externalisée/montée, accès aux études de test, zoom, contraste et défilement.
- **Exclus :** personnalisation avancée d'OHIF et intégration React native.
- **Dépendances :** SPEC-05, SPEC-06.
- **Terminé si :** chacun des deux types d'examens s'ouvre dans OHIF et les trois manipulations attendues sont vérifiées dans un navigateur standard.
- **Agent technique principal :** `dicom-integration`.

#### SPEC-08 — Envoi fictif et recherche d'examens

- **Objectif :** démontrer qu'un établissement fictif transmet un examen qui reste retrouvable par établissement, type et date.
- **Inclus :** import DICOM **instance par instance** (décision 5 de SPEC-01, base de la reprise réseau) ; recherche **médiée par FastAPI** interrogeant Orthanc (décision 4) ; métadonnées strictement nécessaires ; filtres documentés.
- **Exclus :** PACS/RIS réel, dossier patient, compte rendu, duplication des pixels en base applicative.
- **Dépendances :** SPEC-01, SPEC-03 (FastAPI porte la recherche), SPEC-05, SPEC-06.
- **Décision différée :** avant l'implémentation, formaliser le protocole de reprise DICOM : identifiant d'idempotence (probablement le SOP Instance UID), définition d'une confirmation et gestion des doublons.
- **Terminé si :** un examen envoyé par le parcours fictif est stocké puis retrouvé via FastAPI avec chacun des trois critères, sans donnée réelle.
- **Agent technique principal :** `dicom-integration` ; appui `backend-fastapi` (API de recherche).

#### SPEC-09 — Résilience réseau mesurée

- **Objectif :** vérifier l'envoi et la consultation sous réseau lent, instable et interrompu.
- **Inclus :** protocole de test reproductible, conditions mesurées, coupure/reprise, observation de perte ou corruption, vérification du critère de reprise arrêté en SPEC-01.
- **Exclus :** garantie SLA, optimisation mondiale, mode offline complet non spécifié.
- **Dépendances :** SPEC-07, SPEC-08.
- **Décision différée :** avant l'implémentation, formaliser avec SPEC-08 le protocole de reprise DICOM : identifiant d'idempotence (probablement le SOP Instance UID), définition d'une confirmation et gestion des doublons.
- **Terminé si :** les scénarios lent/coupure/reprise sont exécutés et documentés, et le critère canonique « sans renvoi complet » est démontré ou l'écart est explicitement signalé.
- **Agent technique principal :** `tests-qualite` ; appui `dicom-integration`, `devops-infra`.

### Domaine C — Accès et administration

#### SPEC-10 — Modèle minimal d'accès

- **Objectif :** persister uniquement les acteurs et états nécessaires aux deux parcours de maquette.
- **Inclus :** médecin/demande d'inscription, statut en attente-validé-refusé, établissement fictif/partenariat, personnes habilitées et accès créés par admin ; contraintes et migration réversible.
- **Exclus :** examen clinique local, patient, expert avancé, vacation, compte rendu, facturation et pays.
- **Dépendances :** SPEC-04.
- **Terminé si :** la migration crée seulement le modèle minimal, ses contraintes interdisent les transitions incohérentes et les tests de persistance passent.
- **Agent technique principal :** `backend-fastapi` ; appui `tests-qualite`.

#### SPEC-11 — API du parcours médecin

- **Objectif :** permettre une demande d'inscription puis sa validation ou son refus administratif.
- **Inclus :** schémas lecture/écriture distincts, création en attente, liste administrative, actions valider/refuser, garde interdisant l'action avant validation.
- **Exclus :** vérification réglementaire réelle des qualifications, authentification forte de production.
- **Dépendances :** SPEC-10 et décision d'identification de SPEC-01.
- **Terminé si :** les tests démontrent qu'une demande naît en attente, qu'un non-admin ne décide pas, qu'un refusé reste bloqué et qu'un validé peut effectuer l'action témoin définie.
- **Agent technique principal :** `backend-fastapi` ; revue `securite-conformite`, appui `tests-qualite`.

#### SPEC-12 — API du parcours établissement

- **Objectif :** enregistrer un partenariat fictif et réserver la création des accès à l'administrateur.
- **Inclus :** établissement/partenariat fictif, liste administrative, création/révocation d'accès pour personnes habilitées, absence d'auto-activation.
- **Exclus :** contrat réel, onboarding opérationnel, gestion multi-pays.
- **Dépendances :** SPEC-10 et décision d'identification de SPEC-01.
- **Terminé si :** les tests prouvent qu'aucun établissement ne s'active seul et que seul l'administrateur peut créer ou révoquer un accès.
- **Agent technique principal :** `backend-fastapi` ; revue `securite-conformite`, appui `tests-qualite`.

#### SPEC-13 — Fondations React

- **Objectif :** initialiser la maquette React et sa communication robuste avec l'API.
- **Inclus :** structure, routage minimal, client API configuré par environnement, états chargement/erreur réseau, test de build et de navigation.
- **Exclus :** design system complet, rendu médical, intégration native OHIF.
- **Dépendances :** confirmation React en SPEC-01, SPEC-02, SPEC-03.
- **Terminé si :** l'application se construit, est servie par le Compose, joint le healthcheck et rend correctement succès et indisponibilité API.
- **Agent technique principal :** `frontend-react` ; appui `tests-qualite`.

#### SPEC-14 — Écrans médecin et administration

- **Objectif :** rendre visible et manipulable le parcours médecin documenté.
- **Inclus :** formulaire de demande, statut « en attente » clairement visible, liste admin, validation/refus, messages d'erreur et de confirmation.
- **Exclus :** dossier médical, profil expert complet, workflow de production.
- **Dépendances :** SPEC-11, SPEC-13.
- **Terminé si :** un scénario navigateur couvre demande → attente → validation et demande → refus, avec blocage avant validation.
- **Agent technique principal :** `frontend-react` ; appui `tests-qualite`.

#### SPEC-15 — Écrans établissement et accès

- **Objectif :** rendre manipulable le parcours établissement sans auto-activation.
- **Inclus :** liste/fiche d'établissement fictif, état du partenariat, liste des personnes habilitées, création/révocation administrative d'accès.
- **Exclus :** signature électronique, contrats réels, self-service établissement.
- **Dépendances :** SPEC-12, SPEC-13.
- **Terminé si :** un scénario navigateur montre qu'un admin crée puis révoque un accès et qu'aucune action d'auto-activation n'est exposée.
- **Agent technique principal :** `frontend-react` ; appui `tests-qualite`.

#### SPEC-16 — Accès au viewer depuis la maquette

- **Objectif :** relier la surface de gestion au viewer sans réimplémenter OHIF.
- **Inclus :** navigation vers OHIF pour l'examen de test autorisé, gestion des erreurs d'accès, méthode d'intégration minimale décidée (lien/redirect/iframe).
- **Exclus :** viewer DICOM React maison, intégration OHIF native non nécessaire au POC.
- **Dépendances :** SPEC-07, SPEC-08, SPEC-13 et règles d'accès de SPEC-01.
- **Décision préalable :** avant l'implémentation de cette spec, trancher la stratégie d'authentification entre OHIF, Orthanc et FastAPI : reverse proxy, relais DICOMweb côté serveur ou authentification portée par un proxy.
- **Terminé si :** depuis la maquette, le scénario autorisé ouvre l'examen dans OHIF et le scénario non autorisé est bloqué.
- **Agent technique principal :** `frontend-react` ; appui `dicom-integration`, revue `securite-conformite`.

### Domaine D — Validation et déploiement

#### SPEC-17 — Recette POC locale de bout en bout

- **Objectif :** vérifier l'ensemble des critères du cahier des charges sur un poste local.
- **Inclus :** import, stockage, recherche, lecture OHIF, parcours médecin, parcours établissement, absence de données réelles, résultats de résilience.
- **Exclus :** homologation production, audit HDS.
- **Dépendances :** SPEC-09, SPEC-14, SPEC-15, SPEC-16.
- **Terminé si :** une checklist traçable couvre chaque critère de réussite de `scope.md`, avec preuve de réussite ou écart nommé.
- **Agent technique principal :** `tests-qualite` ; revue `securite-conformite`.

#### SPEC-18 — Redéploiement OVHcloud du POC

- **Objectif :** vérifier la portabilité local → OVH avec la même définition Compose.
- **Inclus :** redéploiement sur instance standard POC, variables propres à l'environnement, répétition des tests clés et consignation des écarts.
- **Exclus :** mise en production, données réelles, offre HDS, haute disponibilité, CI/CD complet.
- **Dépendances :** SPEC-17 (décision 6 de SPEC-01 : OVH exécuté dans le POC).
- **Terminé si :** le même Compose est redéployé sur OVH sans réécriture et les scénarios import/lecture/accès y passent.
- **Agent technique principal :** `devops-infra` ; appui `tests-qualite`, revue `securite-conformite`.

### Domaine E — Première fonction IA, après le POC

#### SPEC-19 — Pré-tri et priorisation (post-POC)

- **Objectif :** préparer la première fonction d'assistance : ordre proposé des examens et suggestion d'affectation à un expert.
- **Pourquoi cette fonction :** parmi les huit fiches, `01-agent-pretri-priorisation` a les dépendances les plus proches du POC (métadonnées DICOM) et peut commencer par des règles explicites ; elle n'exige ni analyse d'image, ni compte rendu, ni RCP, ni sources réglementaires externes. Ce choix reste une appréciation technique à valider, pas une priorité imposée par la documentation.
- **Inclus :** métadonnées documentées, annuaire minimal d'experts (sur-spécialité, disponibilité, charge), ordre proposé, suggestion justifiée, validation humaine obligatoire.
- **Exclus :** diagnostic, analyse des pixels, affectation automatique, tri selon établissement/pays, lancement pendant le POC.
- **Dépendances :** POC validé ; modèle opérationnel et annuaire d'experts spécifiés après POC ; réutilisation possible de SPEC-08.
- **Terminé si :** sur données entièrement fictives, la fonction propose un ordre et une affectation justifiée, clairement étiquetés comme suggestions modifiables par un humain.
- **Agent technique principal :** `backend-fastapi` ; appui `dicom-integration`, revue `securite-conformite`, `tests-qualite`.

## 4. Ordre de réalisation et blocages

```text
SPEC-01 Décisions
   ├── SPEC-02 Compose ──┬── SPEC-03 FastAPI ── SPEC-04 Persistance ── SPEC-10 Modèle
   │                     │                                      ├── SPEC-11 API médecin
   │                     │                                      └── SPEC-12 API établissement
   │                     ├── SPEC-05 Orthanc ── SPEC-06 Données ── SPEC-07 OHIF
   │                     │                         └────────────── SPEC-08 Envoi/recherche
   │                     └── SPEC-13 React
   │                                            SPEC-11 + SPEC-13 ── SPEC-14 UI médecin
   │                                            SPEC-12 + SPEC-13 ── SPEC-15 UI établissement
   │                           SPEC-07 + SPEC-08 + SPEC-13 ───────── SPEC-16 Accès viewer
   └────────────────────────── SPEC-07 + SPEC-08 ── SPEC-09 Résilience

SPEC-09 + SPEC-14 + SPEC-15 + SPEC-16 ── SPEC-17 Recette locale ── SPEC-18 OVH
POC validé + prérequis pilote ──────────────────────────────────── SPEC-19 IA post-POC
```

Ordre recommandé :

1. **SPEC-01** est le verrou initial : elle évite de coder sur des hypothèses non documentées.
2. **SPEC-02**, puis **SPEC-03** et **SPEC-05** peuvent avancer comme fondations.
3. La chaîne visuelle prioritaire est **SPEC-05 → SPEC-06 → SPEC-07**.
4. La chaîne backend est **SPEC-03 → SPEC-04 → SPEC-10 → SPEC-11/SPEC-12**.
5. **SPEC-08** suit le choix de responsabilité DICOM ; **SPEC-09** attend une chaîne complète.
6. **SPEC-13** peut avancer après le contrat API minimal ; **SPEC-14** et **SPEC-15** attendent leurs APIs.
7. **SPEC-16** assemble la maquette et OHIF sans imposer une intégration complexe.
8. **SPEC-17** clôt le POC local ; **SPEC-18** (OVH) est dans le lot, décision 6 de SPEC-01.
9. **SPEC-19** reste bloquée jusqu'à validation du POC et cadrage du pilote opérationnel.

Chemins critiques :

- démonstration DICOM : **SPEC-01 → SPEC-02 → SPEC-05 → SPEC-06 → SPEC-07 → SPEC-08 → SPEC-09** ;
- maquette d'accès : **SPEC-01 → SPEC-02 → SPEC-03 → SPEC-04 → SPEC-10 → SPEC-11/SPEC-12 → SPEC-14/SPEC-15** ;
- recette : convergence des deux chemins dans **SPEC-17**.

## 5. Décisions de cadrage — actées le 2026-09-22

Les questions d'architecture qui bloquaient l'amorçage sont tranchées dans **SPEC-01** :

1. FastAPI dans le périmètre exécutable du POC — **oui**.
2. React confirmé pour la maquette d'accès — **oui**.
3. Base relationnelle — **PostgreSQL**.
4. Recherche établissement/type/date — **médiée par FastAPI** interrogeant Orthanc.
5. Reprise d'envoi — **upload instance par instance**, retransmission des seules instances non confirmées.
6. Redéploiement OVH — **exécuté dans le POC** (SPEC-18 dans le lot).
7. Identification/rôles de la maquette — **auth basique Orthanc + token/session simple** côté admin FastAPI, non-production.
8. SPEC-19 (pré-tri post-POC) — **documentée, mais hors du lot de tickets POC actif**.

**Prochaine étape :** démarrer l'implémentation sur KAN-5 (SPEC-02), selon le contrat Compose et la répartition avec SPEC-03 et SPEC-13 définis ci-dessus.
