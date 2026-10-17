# 4. Avaa ja kokeile — demo pääosassa

[Vertailuun](README.md) · Nopein tie web-sovellukseen · Ei toteutettu

## Idea

Kävijä ymmärtää My Lyricsin kokeilemalla sitä. Etusivu on leveä sovelluksen näyttämö, jonka ympärillä on vain tarpeellinen esittely. Web-demon erillinen reitti säilyy, mutta etusivun “Avaa” vie samaan kokeiluun ilman uutta pitkää myyntisivua.

**Oletettu ensisijainen käyttäjä:** puhelimella tai tietokoneella nopeasti sovellusta kokeileva henkilö. Päätoiminto on “Avaa My Lyrics”.

## Visuaalinen kieli

| Rooli | Ehdotus |
|---|---|
| Ympäristö / sovellusalue | Musta `#08090B` / `#15151A` |
| Pääteksti / tukiteksti | `#FAF8FC` / `#B8B4C0` |
| Toimintaväri | Laventeli `#C4A6ED`, teksti `#21152F` |
| Oppaan pinta | Vaalea `#F5F3F8`, teksti `#25202D` |
| Typografia | Järjestelmäfontti 450–750, hyvin suuret mutta lyhyet otsikot |
| Muoto | Suuret avoimet sovelluspinnat, pyöreät painikkeet ja vähäinen ympäröivä chrome |

Tunnistettava yksityiskohta: esimerkkikirjan todellinen näyttö täyttää suuren osan ensimmäisestä näkymästä. Sivusto ei piilota sitä puhelimen kuvan sisään. Tumman esittelyn ja vaalean lukutilan vaihtuminen kertoo tehtävän vaihtumisesta.

## Etusivu — sovellus näyttämöllä

Ylhäällä My Lyrics ja vain kolme reittiä: Avaa, Ohjeet, Tietosuoja. Keskellä suuri oikea sovelluskuva tai käynnistyksen jälkeen oikea demo. Lyhyt otsikko “Laulukirjasi. Valmiina avattavaksi.” ja “Avaa My Lyrics” ovat kuvan yhteydessä, eivät pitkän sisältöjonon alussa.

```text
My Lyrics                              Avaa  Ohjeet  Kieli
──────────────────────────────────────────────────────────
Laulukirjasi. Valmiina avattavaksi.
[Käynnistä web-versio]      Näin aloitat →
┌────────────────────────────────────────────────────────┐
│             Oikea esimerkkikirjan sovellus              │
└────────────────────────────────────────────────────────┘
Kirjasto       Haku       Kokoelmat       Muokkaus
```

Alareunan neljä sisältölinkkiä avaavat ohjeet. Ne eivät jäljittele Flutterin bottombaria eikä niitä kutsuta sovelluksen tabeiksi. Näin ulomman sivuston ja sovelluksen navigaatio eivät sekoitu.

Puhelimessa alkuun lyhyt nimi ja yksi päätoiminto. “Avaa” käynnistää suoraan koko sivun sovelluksen. Markkinointisivun headeria ei jätetä sen päälle viemään tilaa.

## Web-demon esittely — lyhyt portti ja koko ruutu

`/web-demo/` toimii selkeänä porttina: mitä kokeilu tekee, missä tiedot säilyvät, “Käynnistä” ja vaihtoehtoinen “Lue ensin ohje”. Käynnistyksen jälkeen työpöydällä sovellus saa lähes koko näkymän, ja sivuston ohjeet avautuvat tarvittaessa erillisenä paneelina.

Valinnainen “Näytä pikaohje” pysyy sovelluksen ulkopuolisena. Sille ei anneta samoja ikoneita kuin laulun toiminnoille. Sulkeminen palauttaa porttisivulle, selaimen takaisin toimii normaalisti.

Latauksessa näkyy suuri selkeä edistymätön latausindikaattori ja teksti. Todellista prosenttia ei keksitä. Virheessä HTML-ympäristö säilyy käyttökelpoisena ja tarjoaa uusinnan sekä tuen. Tallennustilan ongelmasta ei luvata tietojen säilyvän, jos sitä ei voida todeta.

## Ohjeet ja tiedostomuodot — rauhallinen lukutila

Ohjelinkki siirtää vaaleaan asiakirjatilaan. Selkeä “Takaisin My Lyricsiin” -linkki on aina saatavilla. Alkuun pikaohje: avaa kirja → valitse laulu → vaihda laulua → tee kokoelma. Edistyneet toiminnot ovat omia lukujaan.

Tiedostomuodot ovat erillinen luettava referenssi, jossa on ladattava esimerkki ja kopioitava JSON. Ohjetekstin vieressä ei käynnistetä raskasta demoa uudelleen. Puhelimessa ankkurit ovat nimetyssä sisällysvalikossa, ja kappaleet ovat lyhyitä.

## Tietosuoja — itsenäinen asiakirja

Sama vaalea lukutila kuin ohjeessa. Voimassaolopäivä ja koko teksti ovat heti näkyvissä, ilman automaattisesti käynnistyvää sovellusta. “Palaa etusivulle” ja yhteystieto sulkevat sivun. Osoite säilyy muuttumattomana.

## Ero, riski ja toteutus

Tämä vaihtoehto vaihtaa koko sivuston painopisteen esittelystä käyttöön. Vahvuus on hyvin pieni askel web-sovellukseen. Riski on raskas ensilataus tai epäselvä raja demon ja käyttäjän oman kirjaston välillä. Ratkaisu on kevyt staattinen ensikuva, käyttäjän käynnistämä Flutter ja selkeä tieto tallennuksesta ennen avaamista.

Toinen riski on kaksi kilpailevaa navigaatiota. Täysruudussa ulompi sivustonavigaatio poistuu näkyvistä; sovelluksen oma navigaatio jää ennalleen. Tämä ei sisällä sovelluksen sisäisten näkymien uudistusta.
