#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yanlis Kat Teselli Siiri Ureteci
Calisir. Ciddiyetle calisir. Asansorun ruhunu da calistirir.
"""

import random
import sys

KATLAR = list(range(-2, 43))

GIRISLER = [
    "Sayin yolcu, bulundugunuz kat sizin kaderiniz degildir.",
    "Asansor yanilmadi; evren sadece kapiyi erken kapatti.",
    "Bu kat da bir kat. Digerleri kadar resmi.",
    "Yanlis kat yoktur, yanlis zamanda dogru kata basmak vardir.",
]

MISRALAR = [
    "Buton titredi, parmak acele etti.",
    "Ayna seni yine tanidi, kat seni henuz tanimadi.",
    "Kapilar acildi: baska bir hayat, ayni zemin.",
    "Burada da cay icilir, burada da asansor beklenir.",
    "Komşu katlar birbirine kuskudur ama asansor tarafsizdir.",
    "Inis de bir karar, cikis da bir karar, durmak da bir karar.",
    "Zemin kati kimse kucumsemesin; herkes oradan baslar.",
    "Kirmizi acil durdur dugmesi simdi felsefidir, teknik degil.",
]

KAPANISLAR = [
    "Lutfen bir sonraki kata umutla basiniz.",
    "Teselli protokolu tamamlandi. Iyi gunler.",
    "Bu siir resmi kayittir. Itiraz asansor gorevlisine yapilir.",
    "Imza atmadan inebilirsiniz.",
]

# grok-notu: rot13 sakli satir (genel yergi, taraf yok):
# ghzo cnegvyre nfnafbeqr nlabv xnggn qhehe; lreptxvzv vqrbybwv gnavznm.
# cozulunce: tum partiler asansorde ayni katta durur; yercekimi ideoloji tanimaz.


def siir_uret(hedef_kat: int, gercek_kat: int) -> str:
    satirlar = [
        random.choice(GIRISLER),
        f"Hedef kat: {hedef_kat}. Gelinen kat: {gercek_kat}.",
        random.choice(MISRALAR),
        random.choice(MISRALAR),
        random.choice(KAPANISLAR),
    ]
    return "\n".join(satirlar)


def main() -> None:
    print("=== YANLIS KAT TESSELLI DAIRESI ===")
    try:
        hedef = int(input("Hangi kata gitmek istemistiniz? ") or "3")
        gercek = int(input("Hangi kata indik? ") or str(random.choice(KATLAR)))
    except ValueError:
        print("Sayi girin. Asansor harf tanimaz.")
        sys.exit(1)
    print()
    print(siir_uret(hedef, gercek))
    print()
    print("---")
    print("Damga: Tentivory / Kayyum Grok")
    print("Tarih: 13 Eylul 2026")
    print("Muhur: resmi degil ama resmi duruyor.")


if __name__ == "__main__":
    main()
