 1. Project Overview
Target Website: [https://www.worldometers.info/world-population/population-by-country/]
Data Fields Extracted: ['#', 'Country (or dependency)', 'Population 2026', 'Yearly Change', 'Net Change', 'Density (P/KmÂ²)', 'Land Area (KmÂ²)', 'Migrants (net)', 'Fert. Rate', 'Median Age', 'Urban Pop %', 'World Share']
Tools Used: Python, [requests, pandas, BeautifulSoup]
 2. Setup Instructions
1. Clone this repo: git clone [https://github.com/roshanehrizwan-a11y/web-scraping-project.git]
2. Install dependencies: `pip install -r requirements.txt`
3. Run script: `python scraper.py`
 3. Challenges & Solutions
During the project, one key challenge was extracting the correct table structure from the webpage. Although the HTML content was successfully retrieved using the requests library, the dataset initially lacked column headers when converted into a DataFrame using pandas. This occurred because the scraping logic only extracted <td> elements, while the actual headers were defined using <th> tags in the first table row. To resolve this, the header row was separately extracted using the BeautifulSoup library and then assigned to the DataFrame, ensuring the dataset accurately reflected the original table without any modification.
Another challenge involved handling restricted and dynamically loaded websites. Initial attempts to scrape certain platforms resulted in 403 Forbidden errors, as these sites block automated requests. Although modifying request headers (such as the User-Agent) using the requests library helped mimic a browser, it was observed that some websites rely on JavaScript to load data dynamically. Since BeautifulSoup can only parse static HTML, it could not extract data from such sources. To overcome this, a static, table-based website was selected, ensuring reliable data extraction and consistency throughout the project.
These challenges enhanced understanding of HTML structures, server restrictions, and the importance of selecting appropriate data sources for efficient web scraping.

