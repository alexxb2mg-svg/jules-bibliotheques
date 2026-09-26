# Sources admises

Une fiche cite **toutes** ses sources dans `sources`, chacune avec sa licence et un lien `https://` vers la
version consultée. Le vérificateur refuse une licence non libre ; le relecteur ouvre chaque lien.

## Admises

| Source | Licence à indiquer | Comment la citer |
|---|---|---|
| Programmes officiels, attendus de fin d'année, repères de progression, ressources d'accompagnement publiés sur education.gouv.fr ou eduscol.education.gouv.fr | `etalab-2.0` | l'URL du texte ; le paquet de génération les fournit pour chaque notion |
| Wikiversité, Wikipédia, Wikilivres | `CC-BY-SA-4.0` | le lien vers la **révision** consultée (`...index.php?title=...&oldid=...`) |
| Ressources explicitement sous CC0, CC BY, CC BY-SA ou domaine public | l'identifiant exact (`CC-BY-4.0`...) | le lien vers la page qui porte la mention de licence |

## Refusées

- Manuels scolaires, même en accès gratuit ; sites d'enseignants ou d'éditeurs sans licence libre affichée.
- Licences NC (pas d'usage commercial) ou ND (pas de modification) ; « droits réservés » ; « usage en classe ».
- Ressources éduscol marquées © Réseau Canopé ou éditées par un tiers privé.
- **Une autre fiche générée**, ici ou ailleurs : on génère à partir des attendus et des sources, jamais d'une
  fiche d'IA, pour que les erreurs ne s'accumulent pas.
- **Une source inventée.** Une IA sans accès au web invente volontiers des liens plausibles. Sans web, on
  cite seulement les textes officiels fournis par le paquet, avec `usage: "rédigé à partir des attendus
  officiels"`.
