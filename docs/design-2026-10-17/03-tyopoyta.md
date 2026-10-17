# 3. Työpöytä — ohjeet ja kokeilu rinnakkain

[Vertailuun](README.md) · Vahvin kirjojen tekijälle · Ei toteutettu

## Idea

Sivusto on käyttökelpoinen tukityöpöytä: navigaatio pysyy paikallaan, ohje on keskellä ja oikean reunan demo tekee esimerkin näkyväksi. Ensimmäinen näkymä sisältää oikeaa työtä, ei suurta markkinointiotsikkoa. Käyttäjä voi lukea kirjatiedoston rakenteesta ja nähdä saman esimerkkikirjan sovelluksessa.

**Oletettu ensisijainen käyttäjä:** omia kirjoja tai kokoelmia tekevä käyttäjä. Tämä painotus tarvitsee vahvistuksen ennen toteutusta; kaikkien käyttäjien ei pidä joutua lukemaan JSONia päästäkseen demoon.

## Visuaalinen kieli

| Rooli | Ehdotus |
|---|---|
| Pääpinta / sivupalkki | `#F8FAFC` / `#E9F1F1` |
| Pääteksti / tukiteksti | `#182C34` / `#4C636D` |
| Toimintaväri | Syvä petrooli `#075D67`, valkoinen nappiteksti |
| Valittu kohta | `#C7E5E3`, teksti `#123E45` |
| Koodi | `#15292E`, teksti `#E8F3F1` |
| Typografia | IBM Plex Sans ja IBM Plex Mono, itse tarjottuina |
| Muoto | 8–12 px pienet pinnat, 24 px nappipyöristys, selvä taulukko- ja listakieli |

Tunnistettava yksityiskohta: ohjeen ja demon välinen pystyerotin sekä nimetty paneeli “Esimerkki sovelluksessa”. Paneeli ei väitä synkronoivansa sisältöä reaaliaikaisesti.

## Etusivu — tehtävän aloitus

Kiinteä vasen navigaatio sisältää Aloitus, Kokeile, Käyttöohje, Tiedostomuodot, Tietosuoja ja Tuki. Keskellä tervetuloa-teksti ja kolme suurta tehtäväriviä: “Kokeile sovellusta”, “Tuo oma kirja”, “Tee kirjatiedosto”. Oikealla pieni esimerkkikuva ja sovelluskauppalinkit.

```text
My Lyrics        Aloita tästä                         Esimerkkikirja
──────────────────────────────────────────────────────────────────
Aloitus          My Lyrics selaimessa                [oikea kuva]
Kokeile          Valitse mitä haluat tehdä.
Käyttöohje       Kokeile sovellusta                 →
Tiedostomuodot   Tuo oma kirja                      →
Tietosuoja       Tee kirjatiedosto                 →
Tuki
```

Ei ylä- ja sivunavigaation tuplausta. Sivun otsikko kertoo aina sijainnin. Puhelimessa vasen palkki muuttuu “Ohjevalikko”-napiksi ja pääsisältö käyttää koko leveyden.

## Web-demon esittely — rinnakkainen työtila

Desktopilla kolme aluetta: navigaatio 220 px, pikaohje joustavana palstana, demo vähintään 360 px. Pikaohjeessa oikeat toimintovaiheet ja ladattava esimerkkitiedosto. Demoalueen työkalurivillä “Käynnistä”, “Avaa koko ruudulle” ja versiotieto.

Ohjeen vaihtaminen ei saa käynnistää demoa uudelleen. Tämä vaatii joko pysyvän demoalueen saman sivun sisällä tai erillisen selausikkunan; valittu ratkaisu dokumentoidaan toteutuksessa. Tiedoston muokkaus, validointi tai automaattinen siirto demoon eivät kuulu ensiversioon ilman erillistä toiminnallista tilausta.

Tabletilla valitaan “Ohje / Demo” oikeina tabeina. Puhelimessa demo avataan omaan täysleveään näkymään; kolme palstaa ei saa kutistua päällekkäisiksi kapeiksi laatikoiksi.

## Ohjeet ja tiedostomuodot — tarkka referenssi

Ohjeissa vasen pysyvä navigaatio, keskellä varsinainen sisältö ja oikealla sivun sisäiset ankkurit. Tiedostomuoto käyttää selkeää kenttätaulukkoa: kenttä, tyyppi, pakollisuus, merkitys ja esimerkki. Alussa näkyy sekä minimaalinen kelvollinen tiedosto että ladattava kokonainen esimerkki.

Käyttöohje ja tekninen referenssi erotetaan navigaatiossa toisistaan. Kehittäjän build-ohje ei ole kirjantuontiohjeen keskellä. Virhetilanteet selitetään käyttäjän sanoin: “Tiedostosta ei löytynyt kirjoja”, sitten mahdollinen tekninen syy.

Paikallinen ohjehaku voidaan lisätä myöhemmin, jos sisältömäärä sitä vaatii. Hakukenttää ei piirretä toimimattomana koristeena. Ensiversiossa selkeä sisällysluettelo riittää.

## Tietosuoja — dokumentti työtilan sisällä

Sivupalkki säilyy, mutta oikea demopaneeli poistuu. Keskellä leveydeltään rajattu koko teksti ja oikealla sisällysluettelo. Ei demonstraatiota tai uusia verkkopyyntöjä tietosuojasivulla. Tulostus poistaa sivupalkin.

## Ero, riski ja toteutus

Vahvuus on toistuvan käytön nopeus ja dokumentaation löydettävyys. Suurin riski on tekninen yleisilme, joka voi karkottaa pelkkää laulamista varten saapuvan. Etusivun kieli pidetään siksi tavallisena, ja “Kokeile” on ensimmäinen tehtävä.

Tämä on työläin vaihtoehto: pysyvän demopaneelin tila ja pienempien näyttöjen paneelinvaihto pitää ratkaista huolellisesti. Staattiset ohjeet säilyvät kuitenkin luettavina ilman JavaScriptiä.
