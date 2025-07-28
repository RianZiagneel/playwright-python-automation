import os
from bs4 import BeautifulSoup

def embed_screenshots_in_report(report_path, screenshot_dir):
    with open(report_path, "r") as file:
        soup = BeautifulSoup(file, "html.parser")

    for test in soup.find_all("tr", class_=["pass", "fail"]):
        test_name = test.find("td", class_="col-name").text.strip()
        screenshot_path = os.path.join(screenshot_dir, f"{test_name}.png")

        if os.path.exists(screenshot_path):
            img_tag = soup.new_tag("img", src=screenshot_path, width="300")
            test.find("td", class_="col-links").append(img_tag)

    with open(report_path, "w") as file:
        file.write(str(soup))

# Call this function after generating the report
embed_screenshots_in_report("report.html", "screenshots")