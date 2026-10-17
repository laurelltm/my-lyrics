# 1. Sävel — sovelluksen sisarsivusto

[Vertailuun](README.md) · Suositeltu kokonaisuus · Ei toteutettu

## Idea

Sivusto tuntuu My Lyricsin luonnolliselta jatkeelta. Syvä tumma pohja, laventeli toimintaväri ja oikea sovelluskuva yhdistävät sen puhelimeen. Etusivu auttaa tutustumaan, demo auttaa kokeilemaan ja ohjeet auttavat tekemään. Sama tumma ilme ei tarkoita, että jokainen tekstialue suljetaan laatikkoon.

**Oletettu ensisijainen käyttäjä:** sovellukseen tutustuva laulaja tai olemassa oleva käyttäjä, joka tarvitsee ohjetta. Päätoiminto on “Kokeile selaimessa”.

## Visuaalinen kieli

| Rooli | Ehdotus |
|---|---|
| Sivun tausta | Lähes musta luumu `#100F14` |
| Toissijainen pinta | `#1B1822` |
| Pääteksti / tukiteksti | `#F6F2FA` / `#BDB5C8` |
| Toimintaväri / sen teksti | Laventeli `#C7ABEF` / `#241632` |
| Rajat | `#39323F`, yhden pikselin erottimet |
| Typografia | Itse tarjottava Manrope 500–750; pitkään ohjetekstiin system-ui |
| Muoto | Pillerin muotoiset tärkeät napit, avoimet sisältöalueet, vain tarpeelliset pinnat |

Tunnistettava yksityiskohta: pystysuora laventeli sivumerkki osoittaa ohjeen nykyisen luvun. Sovelluksen oikea logo näkyy pienenä navigaatiossa; sitä ei korvata geneerisellä nuotilla.

## Etusivu — tutustu

Työpöydän ensimmäinen näkymä: ylhäällä logo ja neljä selkeää linkkiä. Alla vasemmalla “Laulut mukana. Kirjat järjestyksessä.”, lyhyt kuvaus ja yksi täytetty “Kokeile selaimessa” -nappi. Oikealla oikea esimerkkikirjan sovelluskuva ilman suurta keinotekoista puhelinkehystä. Kuvaa ei saa erehtyä luulemaan jo toimivaksi sovellukseksi: kuvateksti “Esimerkkikirja My Lyricsissä”.

Seuraava rytmi: kolme tekstiriviä todellisista tehtävistä — “Löydä laulu”, “Kokoa oma ohjelma”, “Muokkaa ja jaa”. Kutakin tukee yksi oikea, rajattu näkymä. Lopuksi linkit ohjeisiin, sovelluskauppoihin ja tukeen. Kauppamerkit ovat toissijaisia suhteessa web-kokeiluun.

```text
Logo My Lyrics             Kokeile  Ohjeet  Tietosuoja  Kieli
──────────────────────────────────────────────────────────
Laulut mukana.             [oikea esimerkkikirjan kuva]
Kirjat järjestyksessä.
Lyhyt kuvaus.
[Kokeile selaimessa]  Ohjeet →
──────────────────────────────────────────────────────────
Löydä laulu       Kokoa oma ohjelma       Muokkaa ja jaa
```

Puhelimessa järjestys on otsikko → kuvaus → päätoiminto → esimerkkikuva. Navigaatio tiivistyy logoihin ja nimettyyn “Valikko”-painikkeeseen. Ei pelkkää ikoniriviä. Kuvan jälkeen tulee sisältö, ei uutta pitkää hero-aluetta.

## Web-demon esittely — kokeile

Mode: Operate. Lyhyt otsikko “Kokeile My Lyricsiä” ja selitys selaimeen tallentuvista tiedoista. Työpöydällä keskellä toimiva sovellus noin 420 × 780 px alueella ja vasemmalla kolme lyhyttä kokeilutehtävää: avaa esimerkkikirja, hae laulu, kokoa oma kokoelma. Tehtävät ovat tavallisia ohjeita; ne eivät esitä sovelluksen sisäistä automaatiota, jota ei ole toteutettu.

Yläreunassa “Avaa koko ruudulle” sekä paluu ohjeeseen. Sovellus käynnistyy “Käynnistä demo” -painalluksella. Latauksen aikana sovelluksen kokoinen vakaa alue ja teksti “My Lyrics käynnistyy”. Hitaan latauksen jälkeen koko ruudun suora linkki ja “Yritä uudelleen”.

Puhelimessa päätoiminto avaa suoraan `/web-demo/app/`-näkymän. Upotus on toissijainen, jotta käyttäjän ei tarvitse käyttää puhelinta puhelimen sisällä. Selaimen navigaatio ja paluu toimivat normaalisti.

## Ohjeet ja tiedostomuodot — ymmärrä ja tee

Mode: Read. Vasemmalla lukuvalikko, keskellä enintään 70 merkin tekstipalsta, oikealla vain pitkällä sivulla “Tällä sivulla” -ankkurit. Alkuun lyhyt valinta “Haluan käyttää sovellusta / Haluan tehdä kirjatiedoston”.

Käyttöohje etenee aloittamisesta selaamiseen, kokoelmiin, muokkaukseen, jakoon ja varmuuskopiointiin. Tiedostomuodoilla on oma sivu: tuettu tiedosto → minimaalinen JSON → kenttäkohtaiset selitykset → valmis ladattava esimerkki → yleiset virheet. `.books`, `.mylyrics` ja kokoelmien tiedostomuoto dokumentoidaan nykyisen parserin mukaan.

Koodilaatikon “Kopioi” antaa tekstipalautteen “Kopioitu”. Esimerkki ja kenttäselitys ovat vierekkäin vain leveällä näytöllä. Puhelimessa lukuhakemisto avautuu “Ohjeen sisältö” -napista; sitä ei jätetä pieneksi sivupalkiksi.

## Tietosuoja — luota ja tarkista

Sama navigaatio, rauhallinen yksipalstainen teksti, voimassaolopäivä heti otsikon alla. Ei hero-kuvaa, myyntinappeja tekstin välissä tai suljettuja haitareita. Lyhyt lukuhakemisto auttaa löytämään kohdan, mutta varsinainen teksti pysyy näkyvissä. Tulostuksessa valkoinen tausta ja tumma teksti.

## Ero, riski ja toteutus

Tämän suunnan vahvuus on jatkuvuus puhelinsovelluksen kanssa ilman, että ohjesivusta tehdään sovelluksen kopio. Riski on liian matalakontrastinen tumma teksti; tukitekstin sävyä ei himmennetä koristeellisuuden vuoksi. Kevyt vaalea ohjeversio voidaan tarjota käyttäjän asetuksella, mutta sen ei tarvitse olla ensimmäisen toteutuksen lisäominaisuus.

Toteutus säilyy staattisena HTML/CSS-sivustona. Yhteinen navigaatio, tyyli ja ohjesivupohja riittävät; uutta sovelluskehystä ei tarvita.
