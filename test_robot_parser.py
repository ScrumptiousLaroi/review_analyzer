from urllib.parse import urlparse

from urllib.robotparser import RobotFileParser


rp = RobotFileParser()
rp.set_url("https://www.amazon.in/robots.txt")
rp.read()



test_url = "https://www.amazon.in/gp/cart"
user_agent = "Mozilla/5.0"  # Look at your scraper line 13!

allowed = rp.can_fetch(user_agent, test_url)
print(f"Am I allowed? {allowed}")