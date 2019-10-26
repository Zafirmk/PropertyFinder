# Property Finder
![Sample Run](https://github.com/Zafirmk/PropertyFinder/blob/master/SampleRun.gif)  

**Project duration**: 1 day  
**IDE**: Pycharm 2019.2.1 (Community Edition)  
**Python Version**: Python 3.7  


## Description
A web scraping project that scrapes [Bayut](https://www.bayut.com/to-rent/property/dubai/). Returns a .csv file containg properites with all their attributes including: rent, area, location etc. Has the ability to sample through each page of the website on it's own and can potentially return upto 30,000 properties. 


## .csv Files Used  
* **properties.csv**: Contains each property with its attributes. 

## How it works
* Samples through every page available and for each page samples through every property available on that page. 


## Getting Started

1. Clone this repo using the following command  
```
$ git clone https://github.com/Zafirmk/PropertyFinder.git
$ cd PropertyFinder
```
2. Open the project in your preferred IDE  


### Prerequisites
Things you need to install before running:
*  [Python](https://www.python.org/)
*  [Regex](https://docs.python.org/3/library/re.html)
*  [Requests](https://realpython.com/python-requests/)
*  [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

#### Additional Notes
*  Check [PropertyAnalysis](https://github.com/Zafirmk/PropertyAnalysis) to see how the obtained data can be analyzed. 
