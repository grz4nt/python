import tkinter as tk
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
from urllib.parse import urlparse

class WebTagAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Znaczniki HTML")
        self.root.geometry("640x480")
        
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(main_frame, text="Wprowadź adres strony:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.url_entry = ttk.Entry(main_frame, width=50)
        self.url_entry.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(main_frame, text="Wybierz znacznik HTML:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.tag_var = tk.StringVar()
        self.tags = ['h1', 'h2', 'h3', 'p', 'ol', 'ul', 'li', 'div', 'span']
        self.tag_combo = ttk.Combobox(main_frame, textvariable=self.tag_var, values=self.tags, state='readonly')
        self.tag_combo.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=5)
        self.tag_combo.set(self.tags[0])
        
        ttk.Button(main_frame, text="Analizuj", command=self.analyze_page).grid(row=4, column=0, pady=20)
        
        ttk.Label(main_frame, text="Wyniki analizy:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.result_text = tk.Text(main_frame, height=10, width=60, wrap=tk.WORD)
        self.result_text.grid(row=6, column=0, columnspan=2, pady=5)
        
    def normalize_url(self, url):
        if not url:
            raise ValueError("Adres nie może być pusty")
            
        url = url.strip()
        
        if not any(url.startswith(prefix) for prefix in ['http://', 'https://']):
            url = 'http://' + url
            
        try:
            result = urlparse(url)
            if not result.netloc:
                raise ValueError("Nieprawidłowy format adresu")
            return url
        except Exception as e:
            raise ValueError(f"Nieprawidłowy adres: {str(e)}")

    def get_most_common_word(self, text):
        words = re.findall(r'\w+', text.lower())
        words = [word for word in words if len(word) > 2]
        if not words:
            return None
        return Counter(words).most_common(1)[0]

    def analyze_page(self):
        self.result_text.delete(1.0, tk.END)
        
        try:
            url = self.normalize_url(self.url_entry.get())
            selected_tag = self.tag_var.get()
            
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            elements = soup.find_all(selected_tag)
            
            if not elements:
                self.result_text.insert(tk.END, f"Nie znaleziono znaczników <{selected_tag}> na podanej stronie.")
                return
                
            all_text = ' '.join(element.get_text() for element in elements)
            result = self.get_most_common_word(all_text)
            
            if result:
                word, count = result
                self.result_text.insert(tk.END, 
                    f"Przeanalizowano {len(elements)} znaczników <{selected_tag}>\n\n"
                    f"Najczęściej występujące słowo: '{word}'\n"
                    f"Liczba wystąpień: {count}")
            else:
                self.result_text.insert(tk.END, "Nie znaleziono żadnych słów do analizy.")
                
        except ValueError as e:
            messagebox.showerror("Błąd", str(e))
        except requests.RequestException as e:
            messagebox.showerror("Błąd połączenia", f"Nie udało się pobrać strony: {str(e)}")
        except Exception as e:
            messagebox.showerror(f"Wystąpił nieoczekiwany błąd: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WebTagAnalyzer(root)
    root.mainloop()