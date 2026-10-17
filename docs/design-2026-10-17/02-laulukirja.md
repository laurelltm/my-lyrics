# 2. Laulukirja — toimitettu julkaisu

[Vertailuun](README.md) · **Käyttäjän valitsema ja toteutettu suunta · 17.10.2026**

![2. Laulukirja — toimitettu julkaisu — etusivu, web-demo, ohje ja tietosuoja](images/02-laulukirja.png)

[Avaa kuva täysikokoisena](images/02-laulukirja.png) · [Vertaa kuvia GitHub Pagesissa](https://laurelltm.github.io/my-lyrics/design-previews/)

## Toteutus

[Kuvallinen toteutusvertailu Markdownina](toteutusvertailu.md)

[Avaa toteutettu sivusto](https://laurelltm.github.io/my-lyrics/) · [Luonnos ja toteutus kuvina rinnakkain](https://laurelltm.github.io/my-lyrics/design-comparison/)

Hyväksytty kuva on toteutuksen visuaalinen auktoriteetti. Alla oleva alkuperäinen tekstiehdotus on suunnitteluhistoriaa; lopullinen järjestelmä on kirjattu projektin DESIGN.md-tiedostoon. Tietosuojateksti on säilytetty kokonaisena ja ohje on laajennettu kymmeneen lukuun.

## Idea

Sivusto rakentuu hyvän painetun laulukirjan tavoin: kansi, sisällys ja selkeät luvut. Suuri typografia ja harkittu tyhjä tila korvaavat tuotekortit. Jokaisen sivun yläreunassa on pieni luvun tunnus, kuten “02 / Kokeile”. Tämä numerointi kuuluu sivuston rakenteeseen eikä muuta laulujen numeroita sovelluksessa.

**Oletettu ensisijainen käyttäjä:** ohjeita etsivä laulaja, jolle tekninen esittely tuntuu vieraalta. Päätoiminto on “Avaa web-versio”, mutta sisällys on heti sen rinnalla.

## Visuaalinen kieli

| Rooli | Ehdotus |
|---|---|
| Tausta / lukupinta | Paperi `#F5F0E6` / `#FFFCF6` |
| Pääteksti / tukiteksti | `#28251F` / `#655D50` |
| Korostus | Metsänvihreä `#345A45`, tärkeän napin teksti `#FFFFFF` |
| Erottimet | `#CFC5B4` |
| Typografia | Otsikot Source Serif 4, käyttöliittymä ja leipäteksti Source Sans 3; fontit itse tarjottavia |
| Muoto | Avoin palsta, ohuet vaakaviivat, 24 px pyöristetyt napit; ei paperitekstuurin kuvaa |

Tunnistettava yksityiskohta: leveä sisällysrivi, jossa luvun nimi vasemmalla ja pieni sivun/lukutyypin tunnus oikealla. Kirjallinen ilme syntyy typografiasta, ei keinotekoisista sivunkäännösanimaatioista.

## Etusivu — kansi ja sisällys

Ensimmäinen näkymä on pystysuuntainen: pieni sovelluksen logo, suuri “My Lyrics”, yhden virkkeen tuotekuvaus, päätoiminto. Alareunasta alkaa sisällys, joka tekee sivuston sisällön näkyväksi heti. Leveällä näytöllä oikealla on yksi esimerkkikirjan kuva, joka katkaisee palstan hillitysti.

```text
My Lyrics                                     Ohjeet  Kieli
──────────────────────────────────────────────────────────
MY LYRICS
Omat laulut ja kirjat mukana.
[Avaa web-versio]       Tutustu sovellukseen ↓

SISÄLLYS
01  Aloittaminen                                      →
02  Kokeile selaimessa                                →
03  Kirjat, kokoelmat ja tiedostot                     →
04  Tietosuoja ja tuki                                →
```

Etusivun alempi osa näyttää kolme toimitettua esimerkkiä kuvateksteineen: kirjan avaaminen, kokoelman ohjelma ja laulun muokkaaminen. Kaikki kuvat ovat oikeasta esimerkkikirjasta. Puhelimessa sisällysrivit ovat täysleveitä ja vähintään 56 px korkeita.

## Web-demon esittely — avoin kirja ja sen työväline

Yläosa on lyhyt: “02 / Kokeile”, otsikko ja kaksi lausetta. Työpöydällä sivu jakautuu kuin kirjan aukeama: vasen palsta kertoo mitä kokeilla, oikealla sovellus omalla suoralla pinnallaan. Kehys on 1 px viiva ja pieni My Lyrics -otsake, ei puhelimen metallia.

“Lue ohje” ei keskeytä demoa: avaa saman sivun ohjealueen tai uuden dokumenttisivun tavallisen linkin tavoin. “Avaa suurempana” avaa täysleveän sovelluksen. Kokeilun jälkeen “Seuraavaksi: omien kirjojen tuonti” vie ohjeeseen.

Puhelimessa vaihtoehdot ovat “Avaa demo” ja “Lue pikaohje”. Sovellus ei käynnisty tai lukitse sivun scrollia ennen käyttäjän valintaa. Lataus ja virhe näkyvät asiallisena tekstinä samassa demoalueessa; koristeellinen animaatio ei ole välttämätön.

## Ohjeet ja tiedostomuodot — kirjan luvut

Mode: Read. Leveä vasen marginaali ja keskellä 66 merkin palsta. Luvun alussa: otsikko, yhden virkkeen tavoite ja tarvittavat lähtötiedot. Numeroitu toimintaohje käyttää yhtä oikeaa kuvaa vaihetta kohden vain, jos kuva selventää toimintoa.

Tiedostomuodon esittely on “resepti”: valmis esimerkki → tarvittavat kentät → koko kirjan rakenne → lataus ja avaaminen. Tekniset lisätiedot siirretään erilliseen alalukuun. JSON on neutraalilla tummemmalla paperipinnalla, rivit eivät katkea arvaamattomasti. Koodin vaakascroll ei liikuta otsikkoa tai koko sivua.

Jokaisen luvun lopussa on “Edellinen / Seuraava”. Puhelimessa sisällys on aina saatavilla ylhäällä nimetystä napista; sivun lopussa ei tarvitse palata ensin alkuun.

## Tietosuoja — lyhyt, toimitettu asiakirja

Sivun rakenne näyttää dokumentilta: otsikko, voimassaolopäivä, sisällys ja koko teksti. Sama paperipinta, mutta ei kuvia tai koristeellisia nostolauseita. Pitkät URL-osoitteet rivittyvät. Yhteystieto on asiakirjan lopussa ja footerissa. Tietosuojan sisältö pysyy sellaisenaan, kunnes sen muuttamisesta erikseen sovitaan.

## Ero, riski ja toteutus

Tämä on toimitettu dokumentaatio, jossa eteneminen tapahtuu lukujen kautta. Se eroaa vaihtoehdosta 1 myös rakenteeltaan: sisällys on etusivun selkäranka, ei tuotehero. Riski on hitaaksi koettu tai vanhanaikainen ensivaikutelma. Siksi demo avautuu suoraan ensimmäisestä näkymästä ja fonttien lataus ei saa piilottaa tekstiä.

Staattinen toteutus, yhteinen luku- ja ohjesivupohja, hyvä tulostustyyli. Kaikkia sovelluksen teemoja ei siirretä verkkosivun teemoiksi.
