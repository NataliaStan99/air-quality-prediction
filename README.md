DOKUMENTACJA TECHNICZNA PROJEKTU  

1. Cel projektu 

Aplikacja pobiera w czasie rzeczywistym dane o jakości powietrza i warunkach pogodowych z serwisu OpenWeatherMap. Umożliwia: 

wyświetlanie bieżących danych PM2.5 dla wybranego miasta, 

automatyczne odświeżanie co 60 sekund, 

symulację wpływu zmian temperatury, wilgotności i prędkości wiatru na prognozę jakości powietrza. 

Projekt jest przykładem rozwiązania z zakresu Internetu Rzeczy (IoT), integrującym dane z czujników dostępnych online. 

 

2. Architektura rozwiązania 

Źródła danych (Retrieve): 

Air Pollution API (PM2.5), 

Weather API (temperatura, wilgotność, wiatr). 

Analiza i prognoza (Augment): 

Dane bieżące są przetwarzane, 

Użytkownik może zmienić parametry pogodowe i zobaczyć wpływ na jakość powietrza. 

Prezentacja danych (Generate + Publisher): 

Wyniki są publikowane w czasie rzeczywistym w aplikacji Streamlit, 

Dane odświeżają się automatycznie co 60 sekund, pełniąc rolę Publishera dla konsumenta końcowego (studenta/użytkownika). 

 

3. Instalacja i uruchomienie 

Instalacja bibliotek: 

pip install streamlit requests pandas 
 

Uruchomienie aplikacji: 

streamlit run app.py 
 

 

4. Ograniczenia 

API OpenWeatherMap w darmowej wersji udostępnia jedynie bieżące dane (historyczne i prognozowane są ograniczone). 

Predykcja oparta jest na uproszczonym modelu zależności atmosferycznych. 

Aplikacja nie stanowi naukowego narzędzia analizy jakości powietrza – to prototyp edukacyjny w ramach IoT. 

 

5. Zastosowanie 

Internet Rzeczy (IoT): demonstracja integracji danych z czujników online, 

RAG + Publisher: pobranie danych → przetworzenie → prezentacja w czasie rzeczywistym, 

Edukacja: zrozumienie zależności pomiędzy warunkami pogodowymi a jakością powietrza, 

Projekt studencki: przykładowy scenariusz wykorzystania otwartych danych w praktyce. 

 

 

 

 

 