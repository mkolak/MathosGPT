from llama_index import StorageContext, load_index_from_storage
import openai

# Set up OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

kadrovi = {
    "name": "kadrovi",
    "index": load_index_from_storage(
        StorageContext.from_defaults(persist_dir="./indices/kadrovi/storage")
    ),
    "summary": """
        Sadrži podatke o svim zaposlenicima Fakulteta primjenjene matematike i informatike(Odjela za matematiku). To uključuje:
        Nastavnike, suradnike, bivše nastavnike, suradnike iz drugih institucija te administrativno i pomoćno osoblje.
        Za sve zaposlenike dostupne su osnovne informacije, a za nastavnike i suradnike dostupne su i detaljne informacije.
        Dostupne informacije uključuju:
        Titula
        Kontakt informacije - Email, Broj telefona, Lokacija ureda
        Research interests, istraživačka zanimanja
        Degrees, stupanj obrazovanja(diploma)
        Popis publikacija, knjiga, softwarea, itd.
        Projekti na kojima je zaposlenik sudjelovao
        Profesionalne aktivnosti
        Privatne informacije
        Popis kolegija koje profesor predaje
        Vrijeme konzultacija
        """,
    "query_top": 5,
}

studiji = {
    "name": "studiji",
    "index": load_index_from_storage(
        StorageContext.from_defaults(persist_dir="./indices/studiji/storage")
    ),
    "summary": """
        Sadrži popis i informacije o svim studijima koje studenti pohađaju na Fakultetu primjenjene matematike i informatike(Odjelu za matematiku).
        Informacije o studiju uključuju:
        Opće informacije, titulu, stupanj obrazovanja, trajanje, uvjete upisa, itd.
        Također, dostupni su i izvedbeni planovi za svaki studij koji uključuju:
        Popis kolegija koji se izvode na svakoj godini svakog studija uz osnovne informacije o svakom kolegiju.
        """,
    "query_top": 2,
}

kolegiji = {
    "name": "kolegiji",
    "index": load_index_from_storage(
        StorageContext.from_defaults(persist_dir="./indices/kolegiji/storage")
    ),
    "summary": """
        Sadrži detaljne informacije o svakom kolegiju koji se izvodi na Fakultetu primjenjene matematike i informatike(Odjelu za matematiku).
        Dostupne informacije uključuju:
        Naziv kolegija
        Sadržaj kolegija
        Imena voditelja, nastavnika, asistenta
        Popis osnovne i dodatne literaturu
        Raspored i termine predavanja i vježbi
        Pravila i upute o polaganju kolegija
        Primjere prijašnjih ispita i kolokvija
        """,
    "query_top": 2,
}

studenti = {
    "name": "studenti",
    "index": load_index_from_storage(
        StorageContext.from_defaults(persist_dir="./indices/studenti/storage")
    ),
    "summary": """
        Sadrži općenite informacije koje se odnose na studente Fakulteta primjenjene matematike i informatike(Odjela za matematiku). Teme koje su uključene:
        C++ klub, ERASMUS+, IAESTE, IT podrška, Knjižnica, Matematički/Alumni klub, MATHOS CUP, Natjecateljsko programiranje, Pretkolegij, Referada, Šahovska sekcija, Sigurni kanal, Srednjoškolska natjecanja iz informatike, Studentska natjecanaj iz matematike, Studentska unija, Studentski zbor
        """,
    "query_top": 2,
}

upisi = {
    "name": "upisi",
    "index": load_index_from_storage(
        StorageContext.from_defaults(persist_dir="./indices/upisi/storage")
    ),
    "summary": """
        Sadrži informacije o upisima na fakultet. Općenito o upisima na diplomske i preddiplomske studije.
        Uvjeti upisa, upisne kvote, termini, obrasci te potrebna dokumentacija
        """,
    "query_top": 2,
}

fakultet = {
    "name": "fakultet",
    "index": load_index_from_storage(
        StorageContext.from_defaults(persist_dir="./indices/fakultet/storage")
    ),
    "summary": """
        Sadrži općenite informacije o fakultetu. Adresa fakulteta, kontakt podaci fakulteta i pojedinih dijelova fakulteta.
        Neke od tema su:
        Pojavljivanje fakulteta u medijima
        Kvaliteta u visokom obrazovanju
        Reakreditacija
        Studentski izbori
        Izdanja fakulteta, tiskana izdanja, digitalna izdanja
        Diplomirani studenti
        """,
    "query_top": 2,
}

all = [kadrovi, kolegiji, studiji, studenti, upisi, fakultet]
