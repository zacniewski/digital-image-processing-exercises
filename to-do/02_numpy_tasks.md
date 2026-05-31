# Zadania: Fundamenty NumPy

### Instrukcja oddawania zadań

- Każde rozwiązanie musi być zapisane w **osobnym pliku Pythona**.
- Nazwa pliku musi zawierać **Twoje nazwisko** (np. `01_nazwisko.py`).
- Umieszczamy komentarze dotyczące zastosowanego kodu.
- Tam, gdzie zadanie generuje wynik wizualny, wykonaj **zrzut ekranu** i zapisz go jako plik obrazu.
- Po realizacji wszystkich zadań należy je wysłać (wraz ze zrzutami ekranu) na **maila prowadzącego**.
- **Nie wysyłamy środowiska wirtualnego (`venv`)**.

______________________________________________________________________

Poniżej znajduje się 10 zadań dotyczących podstaw biblioteki NumPy w kontekście przetwarzania obrazów.

1. **Tworzenie pustego obrazu**

   - Zadanie: Utwórz czarną macierz o wymiarach 500x500 pikseli (3 kanały kolorów) typu `uint8`.
   - Podpowiedź: Użyj funkcji `np.zeros()` i określ `dtype='uint8'`.

1. **Tworzenie białego obrazu**

   - Zadanie: Utwórz białą macierz o wymiarach 200x200 pikseli (skala szarości).
   - Podpowiedź: Możesz użyć `np.ones()` i pomnożyć wynik przez 255 lub użyć `np.full()`.

1. **Sprawdzanie wymiarów i typu**

   - Zadanie: Stwórz dowolną macierz NumPy i wyświetl jej kształt (`shape`), rozmiar (`size`) oraz typ danych (`dtype`).
   - Podpowiedź: Atrybuty te są dostępne bezpośrednio na obiekcie tablicy (np. `arr.shape`).

1. **Wycinanie fragmentu (Slicing)**

   - Zadanie: Z macierzy 100x100 wycnij środkowy kwadrat o wymiarach 50x50.
   - Podpowiedź: Użyj notacji `macierz[start_y:end_y, start_x:end_x]`.

1. **Zmiana koloru fragmentu**

   - Zadanie: Stwórz czarny obraz 300x300 i zmień jego lewy górny kwadrat (100x100) na czerwony.
   - Podpowiedź: W OpenCV kolory są w formacie BGR, więc czerwony to `[0, 0, 255]`.

1. **Kanały kolorów**

   - Zadanie: Rozdziel obraz RGB na trzy osobne macierze odpowiadające kanałom R, G i B.
   - Podpowiedź: Możesz użyć indeksowania `obraz[:, :, 0]` dla kanału Blue (w OpenCV).

1. **Progowanie ręczne (NumPy)**

   - Zadanie: Masz macierz z losowymi wartościami od 0 do 255. Zamień wszystkie wartości powyżej 127 na 255, a resztę na 0.
   - Podpowiedź: Użyj maskowania logicznego: `macierz[macierz > 127] = 255`.

1. **Łączenie macierzy (Stacking)**

   - Zadanie: Utwórz dwie macierze 100x100 i połącz je poziomo.
   - Podpowiedź: Użyj funkcji `np.hstack()` lub `np.concatenate()`.

1. **Statystyki obrazu**

   - Zadanie: Znajdź wartość minimalną, maksymalną oraz średnią jasność w zadanej macierzy (obrazie).
   - Podpowiedź: Skorzystaj z metod `min()`, `max()` i `mean()`.

1. **Losowy szum**

   - Zadanie: Do macierzy reprezentującej obraz dodaj niewielką ilość losowego szumu (używając `np.random`).
   - Podpowiedź: Pamiętaj, aby po dodaniu szumu upewnić się, że wartości nadal mieszczą się w zakresie 0-255 (użyj `np.clip()`) i są typu `uint8`.
