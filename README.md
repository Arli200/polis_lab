# # Detyra Kursi - Web Scraping, Enkriptimi dhe Integrimi API

Ky projekt përdor teknika të **web scraping**, **enkriptim** dhe **përdorim API** për të marrë dhe përpunuar të dhëna.

## Si të përdorni:

### 1. Web Scraping
- Ky skript përdor **BeautifulSoup** për të nxjerrë tituj artikujsh nga një faqe lajmesh (BBC News).
- Të dhënat ruhen në një skedar JSON (data.json).

### 2. Enkriptimi
- Ky skript përdor **PyCryptodome** për të enkriptuar titujt e artikujve në skedarin JSON me algoritmin **AES**.
- Të dhënat e enkriptuara ruhen në skedarin **encrypted_data.json**.

### 3. Integrimi API
- Ky skript përdor **OpenWeather API** për të marrë informacionin për motin për një qytet të caktuar.
- Të dhënat e motit ruhen në skedarin **weather_data.json**.

## Hapat për të ekzekutuar skriptin:
1. Instaloni bibliotekat e nevojshme:
   ```bash
   pip install requests beautifulsoup4 pycryptodome



   
