# blogisovellus
Linkkienjakosovellus kommenttikentillä ja vuorovaikutteisuudella käyttäjän kanssa
Blogisovellus johon pääkäyttäjä voi lisätä (muiden alustojen) videoita saatetekstillä ja muut käyttäjät pystyvät kirjautuneina käymään keskustelua jaetuista.
Konseptissa on keskiössä sisällönkuratointi ja sitä kautta mielenkiintoisen sisällön löytäminen.

Yksinkertainen malli
Yksi kuraattori, muut käyttäjät voivat kommentoida

Monimutkainen malli
Useita kuraattoreja, käyttäjät voivat valita keitä seuraavat

Molemmissa malleissa sovellus pitää kirjaa käyttäjien tykkäyksistä, kommenteista ja niiden järjestyksestä.
Käyttäjä voi kirjautua joko käyttäjätunnuksella tai sähköpostiosoitteella ja salasanalla.

# testaus
1. Aluksi kloonaa repositorio
    ```git clone https://github.com/Ogkarhu/blogisovellus.git```
2. Avaa kohdekansio (cd)

3. Testataksesi sovellusta sinun täytyy asentaa esivaatimukset
    ```pip install -r requirements.txt```

4. Rakenna virtuaaliympäristö
    ```python3 -m venv venv```

5. Avaa virtuaaliympäristö
    ```source venv/bin/activate```


6. Käynnistä paikallinen sovellus
    ```flask run```

7. Avaa tietokanta uuteen terminaali-ikkunaan 
    ```start-pg.sh```

8. Luo tietokanta ajamalla uudessa terminaali-ikkunassa schema.sql
    ```psql < schema.sql```

9. Voit avata sivuston selaimessa
    http://localhost:5000/

# sivuston käyttö
1. Tällä hetkellä sivusto aukeaa "blog template"-etusivulle
2. Sivustolla on otsikon lisäksi mahdollisuus lisätä uusi videoupotus 
joko youtube-videon osoitekentästä, tai jakolinkistä "new post"-napista
3. nämä postaukset ovat nähtävillä etusivulla



