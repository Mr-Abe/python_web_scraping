import requests
from bs4 import BeautifulSoup as bs

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = bs(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    """ print(title_element.text.strip(), end="\n"*2)
    print(company_element.text.strip(), end="\n"*2)
    print(location_element.text.strip(), end="\n"*2)
    print() """
    # print(job_element.prettify(), end="\n"*2)

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    """print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print(title_element) """

for job_element in python_job_elements:
    # -- snip --
    links = job_element.find_all("a")
    for link in links:
        link_url = job_element.find_all("a")[1]["href"]
        print(f"Apply here: {link_url}\n")