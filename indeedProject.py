from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pymysql

# ---------------- Database Function ----------------
def save_to_db(data):
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="Ashish@2212",
        database="jobDB",
        charset='utf8mb4'  # important for emojis/unicode
    )
    cur = db.cursor()

    query = """
    INSERT IGNORE INTO jobs (title, company, location, salary, link)
    VALUES (%s, %s, %s, %s, %s)
    """
    cur.executemany(query, data)
    db.commit()
    print("Inserted:", cur.rowcount)
    db.close()


# ---------------- Scraper Function ----------------
def scrape_jobs():
    url = "https://in.indeed.com/jobs?q=python+developer&l="

    # Open Chrome Browser via Selenium
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    # Wait for JavaScript to render jobs
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    job_cards = soup.select("div.job_seen_beacon")

    scraped_data = []

    for job in job_cards:
        # Title
        title_tag = job.select_one("h2.jobTitle span")
        title = title_tag.text.strip() if title_tag else "N/A"

        # Company
        company_tag = job.select_one("span.companyName")
        if not company_tag:
            company_tag = job.select_one("div[class*='company'] span")
        company = company_tag.text.strip() if company_tag else "N/A"

        # Location
        location_tag = job.select_one("div.companyLocation")
        if not location_tag:
            location_tag = job.select_one("span.location")
        location = location_tag.text.strip() if location_tag else "N/A"

        # Salary
        salary_tag = job.select_one("div.salary-snippet")
        if not salary_tag:
            salary_tag = job.select_one("span.salaryText")
        salary = salary_tag.text.strip() if salary_tag else "Not Mentioned"

        # Job Link
        link_tag = job.select_one("h2.jobTitle a")
        link = "https://in.indeed.com" + link_tag["href"] if link_tag else ""

        scraped_data.append((title, company, location, salary, link))

    print("Scraped:", len(scraped_data))
    print(scraped_data[:5])  # print first 5 jobs for verification

    save_to_db(scraped_data)
    print("Scraped & Saved Successfully!")


# ---------------- Main ----------------
if __name__ == "__main__":
    scrape_jobs()
