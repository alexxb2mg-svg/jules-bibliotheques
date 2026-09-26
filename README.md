# Bibliothèques de Jules

**Les fiches d'exercices de [Jules](https://github.com/alexxb2mg-svg/jules), le tuteur libre qui guide l'élève sans jamais donner la réponse. Écrites par la communauté, vérifiées par le code, relues par des enseignants.**

Jules a besoin d'une fiche pour chacune des **683 notions** de son référentiel (CM1, 5e, 4e, 3e). Une fiche v2 contient l'essentiel du cours, la méthode, les erreurs fréquentes et des exercices que le programme **corrige lui-même**, avec trois indices gradués et des pièges. Jules peut ainsi aider un élève sans aucune IA, gratuitement, pour tout le monde.

## Appel à contributions

C'est un chantier de bénévoles. Chacun peut donner un peu de temps et les crédits de son abonnement à une IA :

1. **Choisir** une ou plusieurs notions « à faire » dans le tableau de bord [CHANTIER.md](CHANTIER.md).
2. **Réserver** avec un ticket [« Je réserve des notions »](../../issues/new?template=reservation.yml).
3. **Générer** : `jules chantier paquet <notion>` donne un texte à coller dans l'IA de votre choix (Claude, Mistral, ChatGPT, Albert...).
4. **Vérifier** : `jules fiches verifier` dit ce qui manque ; on corrige jusqu'à « Conforme. ».
5. **Proposer** : une pull request. Un enseignant relira ensuite.

Le pas à pas est dans [CONTRIBUER.md](CONTRIBUER.md). Pas besoin d'être enseignant pour générer une fiche. Les **enseignants** sont très attendus pour **relire** (voir la section « Relire » de CONTRIBUER.md).

Une notion déjà prise peut recevoir d'autres générations, comme **propositions** : un relecteur choisira la meilleure ou les fusionnera.

## Contenu

| Dossier | Niveau | Notions |
|---|---|---:|
| `fiches-v2-cm1/` | CM1 | 158 |
| `fiches-v2-5e/` | 5e | 132 |
| `fiches-v2-4e/` | 4e | 141 |
| `fiches-v2-3e/` | 3e | 252 |

Chaque dossier est une bibliothèque au sens de Jules ([format](https://github.com/alexxb2mg-svg/jules/blob/main/bibliotheque/README.md), [contrat des fiches v2](https://github.com/alexxb2mg-svg/jules/blob/main/docs/FICHES-V2.md)) :

```
fiches-v2-3e/
  bibliotheque.yaml
  fiches/<matiere>/<notion>.yaml                    # la fiche servie par Jules
  propositions/<matiere>/<notion>/<pseudo>.yaml     # d'autres générations, jamais servies, en attente de choix
```

## Utiliser ces fiches avec Jules

```bash
git clone https://github.com/alexxb2mg-svg/jules-bibliotheques   # à côté du dossier de Jules
```

puis, dans `config.local.yaml` de Jules : `bibliotheques_externes: ["../jules-bibliotheques"]`. Voir [docs/CHANTIER.md](https://github.com/alexxb2mg-svg/jules/blob/main/docs/CHANTIER.md).

## Avertissement

Contenu **expérimental**. Chaque fiche est vérifiée par le code, mais tant que `relecture.statut` n'est pas `relue`, aucun enseignant ne l'a relue. Le cours de l'élève et la parole de son professeur font toujours foi.

## Licence

Les fiches sont sous [CC BY-SA 4.0](LICENCE.md). Chacune cite ses sources, qui doivent être libres ([SOURCES.md](SOURCES.md)). Le code de Jules est sous MIT, dans [son propre dépôt](https://github.com/alexxb2mg-svg/jules).
