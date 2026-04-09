import re
import requests

def find_links(file_path):
    # Regex per catturare URL standard (http/https)
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        return re.findall(url_pattern, content)

def test_links(links):
    broken_links = []
    print(f"🧐 Trovati {len(links)} link. Inizio scansione...\n")

    for link in links:
        # Rimuoviamo eventuali parentesi finali catturate dalla regex se il link è in Markdown (es: [test](url))
        clean_url = link.rstrip(')')
        
        try:
            # Usiamo HEAD invece di GET per essere più veloci (scarica solo l'header, non il contenuto)
            response = requests.head(clean_url, allow_redirects=True, timeout=10)
            
            if response.status_code >= 400:
                print(f"❌ Errore {response.status_code}: {clean_url}")
                broken_links.append((clean_url, response.status_code))
            else:
                print(f"✅ OK: {clean_url}")
        
        except requests.exceptions.RequestException as e:
            print(f"🚫 Fallito: {clean_url} (Errore di connessione)")
            broken_links.append((clean_url, "Connection Error"))

    return broken_links

if __name__ == "__main__":
    readme_path = "README.md"  # Assicurati che il file sia nella stessa cartella
    links_to_test = find_links(readme_path)
    
    errors = test_links(links_to_test)

    print("\n--- Risultato Finale ---")
    if not errors:
        print("🎉 Tutti i link funzionano perfettamente!")
    else:
        print(f"⚠️ Trovati {len(errors)} link non validi.")
        exit(1) # Utile per far fallire una CI/CD se ci sono errori