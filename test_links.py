import re
import requests

def find_links(file_path):
    # Si ferma se trova: spazi, virgolette (singole/doppie), 
    # parentesi (tonde/quadre/angolari)
    url_pattern = r'https?://[^\s"\'<>)\]]+'
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        links = re.findall(url_pattern, content)
        
        # Pulizia per punteggiatura rimasta attaccata alla fine (es. virgole o punti)
        cleaned_links = [link.rstrip('.,') for link in links]
        
        return list(set(cleaned_links))

def test_links(links):
    broken_links = []
    # Header che imita un browser moderno per evitare i 403
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    print(f"🧐 Test di {len(links)} link unici...\n")

    for link in links:
        try:
            # Primo tentativo con HEAD (veloce)
            response = requests.head(link, headers=headers, allow_redirects=True, timeout=10)
            
            # Se HEAD fallisce (403, 405 o 500), riproviamo con GET
            if response.status_code in [401, 403]:
                print(f"⚠️ Warning di autenticazione {response.status_code}: {link}")
            elif response.status_code >= 404:
                print(f"❌ Errore {response.status_code}: {link}")
                broken_links.append((link, response.status_code))
            else:
                print(f"✅ OK: {link}")
        
        except requests.exceptions.RequestException as e:
            print(f"🚫 Fallito: {link} (Errore connessione)")
            broken_links.append((link, "Conn Error"))

    return broken_links

if __name__ == "__main__":
    readme_path = "README.md"
    links_to_test = find_links(readme_path)
    errors = test_links(links_to_test)

    print("\n--- Report Finale ---")
    if not errors:
        print("🎉 Tutti i link sono validi!")
    else:
        print(f"⚠️ Trovati {len(errors)} link rotti.")
        # Se vuoi che la GitHub Action fallisca solo per i 404 reali (e non per i 403/401 ostici)
        # potresti filtrare la lista qui sotto.
        exit(1)