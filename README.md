Cel projektu

Aplikacja pobiera w czasie rzeczywistym dane o jakości powietrza i warunkach pogodowych z serwisu OpenWeatherMap.
Umożliwia:

wyświetlanie bieżących danych PM2.5 dla wybranego miasta,

automatyczne odświeżanie wyników co 60 sekund,

symulację wpływu zmian temperatury, wilgotności i prędkości wiatru na prognozę jakości powietrza.

Projekt jest przykładem rozwiązania z zakresu Internetu Rzeczy (IoT), integrującym dane z czujników dostępnych online, wykorzystującym elementy RAG i Publishera.


Architektura procesowa

 [Źródła danych: API OpenWeatherMap] 
        │
        ▼
 [Publisher - pobranie danych]
        │
        ▼
 [Przetwarzanie i normalizacja - normalizer.py]
        │
        ▼
 [RAG - wykorzystanie danych historycznych i bieżących]
        │
        ▼
 [Model uproszczonej prognozy jakości powietrza - app.py]
        │
        ▼
 [Streamlit - prezentacja wyników]
        │
        ▼
 [Autorefresh - streamlit-autorefresh (60 sekund)]


Opis kroków:

Retrieve (R) – dane PM2.5 i pogodowe (temperatura, wilgotność, wiatr) są pobierane z API OpenWeatherMap.

Augment (A) – dane są przetwarzane, normalizowane i uzupełniane o kontekst historyczny (RAG).

Generate (G) – model ML oblicza prognozę jakości powietrza.

Publisher – Streamlit publikuje wynik w czasie rzeczywistym do użytkownika końcowego.

Autorefresh – dashboard automatycznie odświeża dane co 60 sekund.


Architektura technologiczna

[Pliki CSV / API OpenWeatherMap]
           │
           ▼
  [Publisher - requests do API]
           │
           ▼
  [normalizer.py - czyszczenie i standaryzacja danych]
           │
           ▼
  [app.py - logika prognozy, RAG, model ML]
           │
           ▼
  [Streamlit - interfejs webowy + API aplikacji]
           │
           ▼
  [streamlit-autorefresh - cykliczne odświeżanie dashboardu]


Struktura repozytorium

app.py – główny plik aplikacji Streamlit (pobieranie danych, prognoza jakości powietrza, wizualizacja).

normalizer.py – preprocessing: czyszczenie i standaryzacja danych pogodowych i jakości powietrza.

scenariusz.md – opis scenariusza użycia aplikacji i eksperymentów.

requirements.txt – lista bibliotek potrzebnych do uruchomienia projektu.

run_app.bat – skrypt do szybkiego uruchamiania aplikacji w Windows.

README.md – dokumentacja projektu (ten plik).

venv/ – wirtualne środowisko (automatycznie generowane, zawiera wszystkie zależności i interpretery Pythona).

Instalacja i uruchomienie

Zainstaluj wymagane biblioteki:

pip install -r requirements.txt
pip install streamlit-autorefresh

Uruchom aplikację:

streamlit run app.py


 
