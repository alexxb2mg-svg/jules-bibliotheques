"""Controle des bibliotheques de fiches VISUELLES (type `fiches-visuelles`) par le code de Jules.

Usage : python outils/verifier_visuelles.py --jules CHEMIN_DU_DEPOT_JULES fiches-visuelles-*
Sortie : une ligne par fiche ecartee avec son motif, un bilan par bibliotheque, code 1 si une fiche
est ecartee ou si une bibliotheque est vide. Le validateur est celui qui sert les fiches a l'eleve
(`jules.fiches_visuelles.lire_fiche_visuelle`) : ce qui passe ici est exactement ce qui s'affiche.
Les gabarits de figures viennent des extensions actives de `config.yaml` du depot jules.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def main() -> int:
    analyseur = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    analyseur.add_argument("--jules", required=True, help="dossier du depot jules (code + referentiel)")
    analyseur.add_argument("bibliotheques", nargs="+", help="dossiers de bibliotheques fiches-visuelles")
    args = analyseur.parse_args()

    racine_jules = Path(args.jules).resolve()
    sys.path.insert(0, str(racine_jules))
    import yaml

    from jules.bibliotheques import ErreurBibliotheque, charger_catalogue, lire_identite
    from jules.extensions import charger_extensions, figures_fournies
    from jules.fiches_visuelles import ErreurFicheVisuelle, lire_fiche_visuelle

    config = yaml.safe_load((racine_jules / "config.yaml").read_text(encoding="utf-8")) or {}
    extensions = charger_extensions(racine_jules / "extensions", config.get("extensions") or [])
    gabarits = frozenset(figures_fournies(extensions))

    total_ok = 0
    total_ko = 0
    for chemin in args.bibliotheques:
        dossier = Path(chemin).resolve()
        if not (dossier / "bibliotheque.yaml").is_file():
            print(f"{dossier.name} : pas une bibliotheque (bibliotheque.yaml manquant)")
            total_ko += 1
            continue
        try:
            biblio = lire_identite(dossier)
        except ErreurBibliotheque as err:
            print(f"ECARTEE {err}")
            total_ko += 1
            continue
        if biblio.type != "fiches-visuelles":
            print(f"{dossier.name} : type {biblio.type!r}, attendu 'fiches-visuelles'")
            total_ko += 1
            continue
        catalogue = charger_catalogue([racine_jules / "bibliotheque", dossier.parent], ["programme"], None)
        ok = 0
        ecartees: list[str] = []
        for fiche in sorted((dossier / "fiches").rglob("*.yaml")):
            try:
                lire_fiche_visuelle(fiche, catalogue.notions, biblio, gabarits)
                ok += 1
            except (ErreurFicheVisuelle, OSError) as err:
                ecartees.append(f"{fiche.relative_to(dossier)} : {err}")
        for motif in ecartees:
            print(f"ECARTEE {dossier.name}/{motif}")
        if ok == 0 and not ecartees:
            print(f"{dossier.name} : aucune fiche")
            total_ko += 1
        print(f"{dossier.name} : {ok} conforme(s), {len(ecartees)} ecartee(s)")
        total_ok += ok
        total_ko += len(ecartees)

    print(f"Total : {total_ok} conforme(s), {total_ko} ecartee(s)")
    return 1 if total_ko else 0


if __name__ == "__main__":
    sys.exit(main())
