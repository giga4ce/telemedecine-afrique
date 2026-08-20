# Télémédecine Afrique

## Vision

Le projet vise à construire progressivement un réseau francophone de télémédecine et d'expertise médicale pour l'Afrique.

La première brique produit est la téléradiologie. Les services plus larges, comme les comptes rendus médicaux, la deuxième lecture, les RCP, la gestion des vacations, la facturation et l'extension multi-pays, relèvent de la plateforme cible.

## Phase actuelle

Le repository est au stade **POC technique de téléradiologie**.

Le premier terrain de validation est le **Tchad**. La Côte d'Ivoire et le Cameroun restent dans la vision historique et la roadmap, mais le POC technique actuel ne dépend pas d'une architecture multi-pays.

Objectif technique du POC :

```text
DICOM
-> Orthanc
-> DICOMweb
-> OHIF Viewer
```

## État du repository

- `poc/docker-compose.yml` existe.
- Orthanc est présent dans Docker Compose.
- Le plugin DICOMweb d'Orthanc est activé.
- OHIF Viewer est présent dans Docker Compose.
- L'intégration OHIF -> Orthanc via DICOMweb reste à finaliser.
- Aucun backend produit complet n'est implémenté.
- Aucun frontend produit complet n'est implémenté.
- Aucun jeu DICOM de démonstration n'est versionné.

## Documentation

- Vision produit : [`docs/product/vision.md`](docs/product/vision.md)
- Roadmap : [`docs/product/roadmap.md`](docs/product/roadmap.md)
- Glossaire : [`docs/product/glossary.md`](docs/product/glossary.md)
- Périmètre du POC : [`docs/poc/scope.md`](docs/poc/scope.md)
- Architecture du POC : [`docs/poc/architecture.md`](docs/poc/architecture.md)
- Réserves juridiques par pays : [`docs/domain/legal-reserves-by-country.md`](docs/domain/legal-reserves-by-country.md)
- Fonctions IA futures du produit : [`docs/target-platform/ai-functional-agents/`](docs/target-platform/ai-functional-agents/)
- Documents sources historiques : [`docs/sources/`](docs/sources/)

## Données médicales

Aucune donnée patient réelle ne doit être utilisée dans ce POC.

Le dossier [`data/`](data/) accepte uniquement des données DICOM anonymisées ou synthétiques. Les données de test ne doivent pas contenir d'identité réelle, même partielle.
