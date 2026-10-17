# 5. Selkeä polku — kevyt tukipalvelu

[Vertailuun](README.md) · Helpoin ylläpitää · Ei toteutettu

## Idea

Sivusto vastaa ensin kysymykseen “Mitä haluat tehdä?”. Jokaiselle tehtävälle on selkeä nimetty reitti. Valkoinen pinta, jämäkkä typografia ja harvat värikorostukset tekevät siitä modernin tukipalvelun ilman korttimeren tai teknisen portaalin tuntua.

**Oletettu ensisijainen käyttäjä:** kuka tahansa, joka haluaa päästä eteenpäin nopeasti. Päätoiminto vaihtelee tehtävän mukaan, mutta etusivulla “Kokeile selaimessa” saa suurimman painon.

## Visuaalinen kieli

| Rooli | Ehdotus |
|---|---|
| Tausta / toissijainen pinta | `#FFFFFF` / `#F2F5F7` |
| Pääteksti / tukiteksti | `#142E3A` / `#536872` |
| Päätoiminto | Merensininen `#125A75`, valkoinen teksti |
| Pieni tunnuskorostus | Kupari `#A24732`, ei pitkän tekstin väri |
| Erottimet | `#D6E0E5` |
| Typografia | Atkinson Hyperlegible Next; itse tarjottava, järjestelmäfontti fallbackina |
| Muoto | Vahvat listat ja erottimet, 999 px pillerinapit, hyvin vähän varjoja |

Tunnistettava yksityiskohta: suuret tehtävärivit, joissa on lyhyt selitys vasemmalla ja suuntaa näyttävä nuoli oikealla. Koko rivi on linkki. Nuoli tarkoittaa siirtymää, ei koristeellista lisäikonia jokaiseen toimintoon.

## Etusivu — valitse tehtävä

Ensimmäinen näkymä on kahden palstan tehtävävalinta. Vasemmalla nimi, yksi tuotekuvaus ja päätoiminto. Oikealla kolme suurta linkkiriviä: “Tarvitsen käyttöohjeen”, “Haluan tuoda tai tehdä kirjan”, “Etsin tietosuojaa tai tukea”. Alempana pieni todellinen sovelluskuvien sarja.

```text
My Lyrics                   Kokeile  Ohjeet  Tietosuoja  Kieli
────────────────────────────────────────────────────────────
Laulut kätevästi mukana.        Tarvitsen käyttöohjeen      →
Kirjat, kokoelmat ja muokkaus.  Haluan tuoda tai tehdä kirjan →
[Kokeile selaimessa]            Tietosuoja ja tuki           →
────────────────────────────────────────────────────────────
[oikea kuva]   [oikea kuva]   [oikea kuva]
Kirjasto       Kokoelmat      Laulueditori
```

Puhelimessa otsikko ja päätoiminto näkyvät ensin, tehtävälista heti perässä. Sovelluskuvat tulevat vasta tehtävävalinnan jälkeen. Mikään tehtävä ei edellytä karusellin selaamista.

## Web-demon esittely — selkeä aloituspolku

Lyhyt otsikko “Kokeile selaimessa”. Sen alla kaksi selvää vaihtoehtoa: täytetty “Avaa My Lyrics” ja tekstilinkki “Lue pikaohje”. Työpöydällä pieni esikatselu oikealla; käynnistys vaihtaa sen toimivaksi demoksi ja tarjoaa koko ruudun avauksen.

Kolme hyvin lyhyttä tietoa: oma esimerkkikirja käytössä, kirjaston tiedot säilyvät tässä selaimessa alustakohtaisten ehtojen mukaan, puhelinsovelluksen pilvipalvelut voivat poiketa webistä. Lopulliset sanamuodot tarkistetaan käytännössä ennen julkaisua.

Puhelimessa “Avaa” vie suoraan täysleveään sovellukseen. Upotettua demoa ei pakoteta sivulle. Lataus, virhe ja uusintanappi ovat näkyviä HTML-tiloja; esittelyteksti ei katoa latauksen mukana.

## Ohjeet ja tiedostomuodot — tehtäväkohtaiset sivut

Ohjekeskuksessa isot tekstilinkit: aloittaminen, laulujen lukeminen, kokoelmat, muokkaaminen, jakaminen, ulkoasu, varmuuskopiot. Jokaisen ohjesivun alussa “Tällä ohjeella voit…” ja lopussa seuraava luonteva tehtävä.

Tiedostomuodot erotetaan kahteen tasoon: tavallisen käyttäjän “Avaa saamasi tiedosto” ja tekijän “Kirjatiedoston rakenne”. Minimaalinen JSON tulee vasta tekijän sivulla, ei jokaisen käyttäjän aloituspolulle. Ladattavalla esimerkillä on selvä tiedostonimi ja tyyppi.

Desktopilla lukuhakemisto on sivupalkissa; puhelimessa sama sisältö on sivun alussa avattavana listana. Ohjeissa ei tarvita kuvia joka kappaleeseen. Oikea kuva käytetään, kun se auttaa tunnistamaan napin tai näkymän.

## Tietosuoja — helposti löydettävä

Yksi palsta, selkeä pääotsikko ja päivämäärä. Otsikoista muodostettu sisällys alussa; koko asiakirja pysyy näkyvissä. Yhteinen header ja footer tarjoavat ulospääsyn, mutta sivua ei kuormiteta demolla, kauppamerkeillä tai ominaisuuslistoilla.

## Ero, riski ja toteutus

Tämä on tehtäviin perustuva tukisivusto. Se eroaa muista ennen kaikkea informaation järjestyksellä: kävijä valitsee tarpeensa ennen pitkää tuote-esittelyä. Vahvuudet ovat selkeys, nopea lataus ja pieni ylläpitokuorma. Riski on geneerinen yleisilme; sitä torjutaan oikealla logolla, tunnistettavalla typografialla ja todellisilla esimerkkikirjan kuvilla.

Sopii pienimpään ensimmäiseen toteutukseen. Staattiset sivut ja yhteinen tyyli riittävät; ei pakollista hakupalvelua, sisältöjärjestelmää tai JavaScript-kehystä.
