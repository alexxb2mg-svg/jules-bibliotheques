# Contribuer : générer, vérifier, relire des fiches

Merci. Ce guide suffit pour contribuer, même sans être développeur.

Il y a deux façons d'aider :

- **générer** une ou plusieurs fiches avec une IA : c'est à la portée de tous, avec un peu de soin ;
- **relire** des fiches déjà vérifiées : c'est le rôle des enseignants (voir [Relire](#relire-enseignants)).

## Ce qu'il faut

- Python 3.10 ou plus récent, et git.
- Un accès à une IA conversationnelle récente : Claude, Mistral (Le Chat), ChatGPT, Albert (agents publics)...
  Préférez un modèle haut de gamme : il se trompe moins dans les calculs et respecte mieux le format.
- Un compte GitHub.

Installation, une seule fois :

```bash
git clone https://github.com/alexxb2mg-svg/jules
git clone https://github.com/alexxb2mg-svg/jules-bibliotheques
cd jules
python -m venv .venv
# Windows : .venv\Scripts\activate    macOS / Linux : source .venv/bin/activate
python -m pip install -e .
```

Les commandes ci-dessous se lancent depuis le dossier `jules`.

## 1. Choisir

Ouvrez [CHANTIER.md](CHANTIER.md), dépliez une matière, notez l'**identifiant** (entre `` ` ``) d'une ou
plusieurs notions **à faire**. Conseils :

- commencez par **une** notion, pour apprendre la boucle ; ensuite, 3 à 5 notions d'un même chapitre à la fois ;
- prenez une matière que vous connaissez : vous devrez relire ce que l'IA a écrit.

Une notion déjà réservée ou déjà faite peut quand même recevoir votre génération, comme **proposition**
(voir plus bas). Elle ne remplace rien : un relecteur choisira.

## 2. Réserver

Ouvrez un ticket [« Je réserve des notions »](../../issues/new?template=reservation.yml) et listez les
identifiants, **un par ligne**. Le tableau de bord affiche votre réservation à sa prochaine mise à jour.
Sans nouvelles de votre part (commit, commentaire) pendant **21 jours**, la réservation tombe : les notions
redeviennent « à faire ». Un commentaire sur le ticket suffit à la prolonger.

## 3. Générer

```bash
jules chantier paquet ratio fractions-irreductibles --par votre-pseudo --sortie paquet.md
```

Ouvrez `paquet.md`, copiez **tout** son contenu dans une nouvelle conversation avec l'IA, envoyez.
Le paquet contient les règles, le contrat du format, une fiche modèle et, pour chaque notion, les attendus
officiels. Ne le raccourcissez pas : c'est lui qui rend les contributions comparables.

L'IA rend un bloc YAML par notion, précédé de `Fichier : fiches/<matiere>/<notion>.yaml`. Enregistrez chaque
bloc dans la bibliothèque du bon niveau :

| Niveau de la notion | Dossier |
|---|---|
| CM1 | `jules-bibliotheques/fiches-v2-cm1/` |
| 5e | `jules-bibliotheques/fiches-v2-5e/` |
| 4e | `jules-bibliotheques/fiches-v2-4e/` |
| 3e | `jules-bibliotheques/fiches-v2-3e/` |

Exemple : `jules-bibliotheques/fiches-v2-3e/fiches/mathematiques/ratio.yaml`.

**Proposition** (la notion a déjà une fiche, ou elle est réservée par quelqu'un d'autre) : rangez le fichier
dans `propositions/<matiere>/<notion>/<votre-pseudo>.yaml` au lieu de `fiches/`.

Vérifiez que le champ `generation.modele` contient bien le nom de l'IA utilisée.

## 4. Vérifier, jusqu'à « Conforme. »

```bash
jules fiches verifier ../jules-bibliotheques/fiches-v2-3e
```

Chaque manquement est listé. Collez la sortie dans la même conversation avec l'IA, avec la phrase
« Corrige seulement ces manquements et rends la fiche entière. », remplacez le fichier, relancez. Deux ou
trois allers-retours sont normaux. Les manquements les plus fréquents :

| Message | Ce qu'il faut faire |
|---|---|
| `YAML illisible` | un texte contient « : » (un ratio 2 : 3, « Attention : ») : le mettre entre guillemets |
| `l'indice ... contient la reponse` | l'indice donne le résultat, même écrit autrement (« 1 800 ÷ 9 » quand la réponse est 800) : le reformuler |
| `la solution redigee n'aboutit pas a la reponse attendue` | la solution et la réponse ne concordent pas : **refaire le calcul à la main**, l'erreur peut être dans la réponse |
| `declencheur(s) invisible(s)` | un déclencheur fait de mots trop courts ou vides : le remplacer par une expression d'élève |
| `declencheur « ... » revendique par` | deux notions se disputent un mot : le rendre plus précis dans votre fiche |

Quand tout est conforme, scellez :

```bash
jules fiches signer ../jules-bibliotheques/fiches-v2-3e
```

La fiche passe `etat: verifiee` et reçoit son `empreinte`. Toute modification ultérieure demandera de
re-signer.

**Fiches visuelles** (`fiches-visuelles-<niveau>/`, format `bibliotheque/SCHEMA-FICHE-VISUELLE.md` du
dépôt jules) : `jules fiches verifier` ne les connaît pas. Le contrôle, avec le même validateur que celui
qui les affiche à l'élève :

```bash
python outils/verifier_visuelles.py --jules ../jules fiches-visuelles-3e
```

Chaque fiche écartée est listée avec son motif (bloc inconnu, champ trop long, gabarit absent, SVG refusé…).
La CI lance ce contrôle sur chaque pull request (« Contrat des fiches visuelles »). Pas de signature
pour les fiches visuelles : la relecture reste `a_relire` tant qu'un adulte n'a pas relu.

## 5. Relire soi-même avant de proposer

Le vérificateur contrôle la forme et la cohérence interne, pas la vérité. Avant de proposer, vérifiez :

- [ ] j'ai refait **chaque calcul** et chaque réponse attendue moi-même ;
- [ ] le contenu reste dans le niveau (rien au-delà des attendus du paquet) ;
- [ ] j'ai **ouvert chaque lien** de `sources` : il existe et dit bien ce qu'on lui fait dire ;
- [ ] rien n'est recopié d'un manuel ou d'un site non libre ([SOURCES.md](SOURCES.md)) ;
- [ ] les énoncés sont clairs pour un élève de ce niveau, sans prénom réel ni donnée personnelle.

## 6. Proposer

Créez une branche, committez vos fichiers, ouvrez une pull request et écrivez `Ferme #<numéro du ticket>`
dans sa description. La CI relance le vérificateur : une pull request rouge n'est pas fusionnée.
Sans git, vous pouvez aussi déposer les fichiers par l'interface web de GitHub (« Add file » puis
« Upload files ») : la CI vérifiera de la même façon.

## Relire (enseignants)

Une fiche `verifiee` est déjà servie par Jules, marquée expérimentale. Votre relecture la fait passer `relue`.

1. Choisissez une fiche `vérifiée` dans votre matière ([CHANTIER.md](CHANTIER.md)).
2. Lisez-la comme un élève puis comme un correcteur : exactitude, niveau, clarté, qualité des indices
   (ils doivent faire avancer sans donner la réponse), pertinence des pièges.
3. Corrigez directement ce qui doit l'être, puis relancez `jules fiches verifier` et `jules fiches signer`.
4. Renseignez la relecture et passez l'état à `relue` :

   ```yaml
   etat: relue
   relecture:
     statut: relue
     par: "professeur de mathématiques (collège)"   # une fonction suffit, pas besoin de votre nom
     le: "2026-10-01"
   ```

5. Ouvrez une pull request « Relecture : <notion> ».

**Propositions.** Si une notion a des propositions, comparez-les à la fiche servie. Vous pouvez déplacer la
meilleure dans `fiches/` (elle remplace l'ancienne), reprendre un exercice ou un piège d'une proposition dans
la fiche servie, puis supprimer les propositions traitées. Dites dans la pull request ce que vous avez gardé.

## Règles

- On ne génère jamais à partir d'une autre fiche générée : seulement les attendus du paquet et des sources.
- Pas de source inventée, pas de contenu non libre (voir [SOURCES.md](SOURCES.md)).
- Rien de personnel : pas de prénom réel d'élève, pas de photo, pas de donnée d'un enfant.
- Les fiches sont publiées sous [CC BY-SA 4.0](LICENCE.md).
- Code de conduite : celui du [projet Jules](https://github.com/alexxb2mg-svg/jules/blob/main/CODE_OF_CONDUCT.md).
