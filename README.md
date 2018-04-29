# llamallamallama

## Inspiration
This project was inspired by the magnificent camelcamelcamel.com, and also by our own desires to have a better understanding of seasonal pricing trends in retail. We hope that once completed, our extension will help users determine the pricing and restocking cycles of their most commonly visited retailers, and when the ideal time to buy is.

## What it does
In a nutshell, our project has a spider that will periodically crawl websites we support (we plan to continue adding more and more) and store any new products, price changes, and sales in a database. When users are shopping, they can click our chrome extension to view price statistics for the current item their viewing, which will request this information from our database. We hope in the future to add more analytics, to advise people when a good time to buy based on the retailer's history is rather than leaving them to determine his for themselves.

## How we built it
We used python to scrape a website and store the information of products and then collected last 6 months data from Wayback Machine. We stored all the information in a JSON file so that we can use Javascript to read the data and plot the price changes over the time. We used Javascript with the Chrome API to make the extension icon turn blue on supported websites. Javascript also allowed us to retrieve HTML elements from the current page and dynamically create the HTML for our extension's pop-up window. 

## Challenges we ran into
We were unable to read the JSON file locally so it may not be efficient enough to plot the graph. And since we were not familiar with the Chrome API, we cannot update the product information dynamically.

## Accomplishments that we're proud of
We scraped the target website successfully and got all the data we want. And the Chrome extensions we built and our data visualization let the user easy to use and clearly know the price trend.

## What we learned
A piece of advice I've read in books and have now learned that hard way firsthand is to carefully plan the project beforehand. It wastes a lot of time and effort to completely scrap code you've been working on for hours when you realize something else works better. In the future, this means putting more deliberation into the APIs and libraries we plan to use.

## What's next for llamallamallama
Our next steps are to set up a database and begin periodically crawling sites to fill it. We'd also like to make our extension's pop-up fully dynamic and have it provide more useful analytics to the user.
