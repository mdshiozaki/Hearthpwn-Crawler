# Hearthpwn-Crawler
Software Design (SYDE 322) Final Project. Objective: use a web crawler combined with a front and back end to scrape data
and present it to the user.

Our project is based around deck building in the online card collecting game Hearthstone. The primary game mode of Hearthstone has each
player build a deck of 30 cards. With 10 classes and hundreds of cards to choose from, players can be overwhelmed with options. This tool
allows players to search for specific cards they already own and find suggestions for cards to place in a deck with it. Using data scraped
from https://hearthpwn.com, cards most often found in decks with the searched cards are displayed by most popular to the user. 

The scraped data was stored in a MySQL database, which was connected to a web server. The web server housed the API and webcrawler and 
HTTP calls to the REST API were used as client-server communication.

Activity Diagram: 
![alt text][adiagram]

[adiagram]: https://github.com/mdshiozaki/Hearthpwn-Crawler/blob/master/activity_diagram_crawler.png "Webcrawler Activity Diagram"

## Data Scraped
* Deck code
* Deck name
* Deck URL (from https://hearthpwn.com)

## Additional Components
Scrapy has MailSender, an email client, built in. This is configured to send text-only emails when crawl errors occur.

## Full Implementation
Frontend:
* Framework: Xamarin
* Language: C#

Web Server:
* Service: Amazon Elastic Cloud Compute (EC2)
* OS: Amazon Linux 2
* Access Framework: Django v2.2
* Security: Amazon Security Groups - Custom Access Settings

Database: 
* Service: Amazon Relational Database Service (RDS)
* Database: MySQL
* Security: Amazon Security Groups - Custom Access Settings


Subsystem Diagram: 

![alt text][sdiagram]

[sdiagram]: https://github.com/mdshiozaki/Hearthpwn-Crawler/blob/master/Crawler_subsystem_diagram.png "Webcrawler Subsystem Diagram"



