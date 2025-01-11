import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import requests
from typing import Dict, Any
import threading

class WeatherAPIError(Exception):
    pass

class WeatherAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"
    
    def search_city(self, query: str) -> list:
        try:
            url = f"http://api.openweathermap.org/geo/1.0/direct"
            params = {
                "q": query,
                "limit": 5,
                "appid": self.api_key
            }
            response = requests.get(url, params=params, timeout=10)
            return response.json()
            
        except requests.Timeout:
            raise WeatherAPIError("Timeout podczas połączenia z serwerem")
        except requests.RequestException as e:
            raise WeatherAPIError(f"Błąd połączenia: {str(e)}")
    
    def get_weather(self, lat: float, lon: float) -> Dict[str, Any]:
        try:
            url = f"{self.base_url}/weather"
            params = {
                "lat": lat,
                "lon": lon,
                "appid": self.api_key,
                "units": "metric",
                "lang": "pl"
            }
            
            response = requests.get(url, params=params, timeout=10)
            return response.json()
            
        except requests.Timeout:
            raise WeatherAPIError("Timeout podczas pobierania danych pogodowych")
        except requests.RequestException as e:
            raise WeatherAPIError(f"Błąd połączenia: {str(e)}")

class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Aplikacja Pogodowa")
        self.geometry("900x700")
        self.resizable(False, False)
        self.configure(bg='#f0f0f0')
        
        self.style = ttk.Style()
        self.style.configure('Modern.TFrame', background='#f0f0f0')
        self.style.configure('Modern.TButton',
                           padding=10,
                           font=('Helvetica', 10))
        self.style.configure('Modern.TEntry',
                           padding=10,
                           font=('Helvetica', 10))
        
        self.api = WeatherAPI("6e5375298ffc9439f733c45d74302675")
        
        self._create_widgets()
    
    def _create_widgets(self):
        main_frame = ttk.Frame(self, style='Modern.TFrame')
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        top_frame = ttk.Frame(main_frame, style='Modern.TFrame')
        top_frame.pack(fill="x", pady=(0, 20))
        
        search_frame = ttk.Frame(top_frame, style='Modern.TFrame')
        search_frame.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=('Helvetica', 12),
            width=40
        )
        self.search_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.search_entry.bind('<Return>', lambda e: self._handle_search())
        
        self.date_var = tk.StringVar()
        dates = [
            (datetime.now() + timedelta(days=i)).strftime("%d.%m.%Y")
            for i in range(5)
        ]
        self.date_combo = ttk.Combobox(
            top_frame,
            textvariable=self.date_var,
            values=dates,
            state="readonly",
            font=('Helvetica', 12),
            width=15
        )
        self.date_combo.set(dates[0])
        self.date_combo.pack(side="left", padx=(0, 10))
        
        search_btn = ttk.Button(
            top_frame,
            text="Szukaj",
            command=self._handle_search,
            style='Modern.TButton'
        )
        search_btn.pack(side="left")
        
        self.status_var = tk.StringVar()
        self.status_label = ttk.Label(
            main_frame,
            textvariable=self.status_var,
            font=('Helvetica', 10),
            foreground='#666666'
        )
        self.status_label.pack(fill="x", pady=(0, 10))
        
        self.results_text = tk.Text(
            main_frame,
            height=25,
            wrap="word",
            font=('Helvetica', 12),
            bg='#ffffff',
            fg='#333333',
            padx=10,
            pady=10
        )
        self.results_text.pack(fill="both", expand=True)
    
    def _update_status(self, message: str, is_error: bool = False):
        self.status_var.set(message)
        self.status_label.configure(foreground='#ff0000' if is_error else '#666666')
        
    def _handle_search(self):
        query = self.search_var.get().strip()
        
        if not query:
            self._update_status("Wpisz nazwę miasta", True)
            return
            
        self.results_text.delete(1.0, tk.END)
        self._update_status("Wyszukiwanie...")
        
        def search_thread():
            try:
                cities = self.api.search_city(query)
                if cities:
                    city = cities[0]
                    weather = self.api.get_weather(city["lat"], city["lon"])
                    
                    self.results_text.delete(1.0, tk.END)
                    self.results_text.insert(tk.END, f"Pogoda dla {city['name']}, {city.get('country', '')}\n\n")
                    self.results_text.insert(tk.END, f"Temperatura: {weather['main']['temp']}°C\n")
                    self.results_text.insert(tk.END, f"Temp. odczuwalna: {weather['main']['feels_like']}°C\n")
                    self.results_text.insert(tk.END, f"Wilgotność: {weather['main']['humidity']}%\n")
                    self.results_text.insert(tk.END, f"Warunki: {weather['weather'][0]['description']}\n")
                    
                    self._update_status("Dane zostały pobrane pomyślnie")
                    
            except WeatherAPIError as e:
                self._update_status(str(e), True)

        threading.Thread(target=search_thread, daemon=True).start()

if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()