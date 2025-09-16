1. Tytuł projektu 

„Prognoza jakości powietrza (PM2.5) z uwzględnieniem temperatury, wilgotności i wiatru – RAG + Publisher” 

2. Cel 

Celem projektu jest monitorowanie jakości powietrza w wybranych miastach (Amsterdam, Porto, Wrocław, Paryż) i symulacja prognozy PM2.5 w oparciu o zmiany parametrów pogodowych. Projekt demonstruje zastosowanie danych IoT do podejmowania decyzji środowiskowych. 

3. Scenariusz użycia 

3.1. Opis krok po kroku 

Użytkownik wybiera miasto z listy rozwijanej w aplikacji. 

System pobiera bieżące dane jakości powietrza i parametry pogodowe z OpenWeatherMap API. 

Dane wyświetlane są w tabeli i aktualizowane co 60 sekund. 

Użytkownik może modyfikować parametry pogodowe (temperatura, wilgotność, wiatr). 

Na podstawie zmienionych parametrów obliczana jest prognoza PM2.5, prezentująca wpływ zmian warunków na jakość powietrza. 

Użytkownik obserwuje różnice między aktualnymi a prognozowanymi wartościami PM2.5. 

3.2. Przykładowy scenariusz eksperymentalny 

Cel: Zbadanie wpływu pogody na zanieczyszczenie powietrza w Wrocławiu. 

Etapy: 

System pobiera aktualne dane PM2.5 w Wrocławiu. 

Użytkownik zmienia temperaturę o +5°C, obserwując zmianę prognozy PM2.5. 

Analogicznie, modyfikuje wilgotność i prędkość wiatru. 

Analiza wyników pokazuje w jaki sposób warunki pogodowe wpływają na poziom zanieczyszczenia powietrza. 

3.3. Korzyści 

Interaktywny monitoring jakości powietrza. 

Możliwość symulacji różnych scenariuszy środowiskowych. 

Przydatne dla naukowców, władz miejskich i osób dbających o zdrowie. 