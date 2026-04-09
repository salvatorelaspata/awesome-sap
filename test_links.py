import re
import requests

def find_links(file_path):
    # Questa regex cattura tutto ciò che inizia con http/https 
    # ma si ferma appena incontra uno spazio, una parentesi tonda chiusa, 
    # una quadra chiusa o una virgola seguita da spazio.
    url_pattern = r'https?://[^\s)\]]+'
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        links = re.findall(url_pattern, content)
        
        # Pulizia extra per casi limite (rimuove punteggiatura finale rimasta)
        cleaned_links = [link.rstrip('.,') for link in links]
        
        # Elimina i duplicati e restituisce la lista
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
            if response.status_code in [403, 405, 500, 503, 401]:
                response = requests.get(link, headers=headers, allow_redirects=True, timeout=10, stream=True)

            if response.status_code >= 400:
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