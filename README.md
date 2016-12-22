# Vinyl Search

![alt text](https://raw.githubusercontent.com/enderst3/mycapstone/beb0a29815ec7180b8fd6c4eed4e0c3f85517cac/images/homepagecrop.png)
![alt text](https://github.com/enderst3/mycapstone/blob/master/images/search%20resultscrop2.png?raw=true)
This is a search app that will let you take a photo of an album cover, then it uses google to search(using the selenium webdriver) for the album info.  It returns results, you can click on the album cover to go to the corresponding Discogs page, where you can see the info, and maintain your album collection.

### Motivation

I wrote this to help me keep track of the Albums I own, and to keep me from buying duplicates while I am at a record store.  Since the majority of albums do not have a barcode, I wanted a quick and easy way to search for them.

The google image search api is deprecated, I had to use the Selenium webdriver.  It opens a web browser and manually fills in the google search, and clicks the buttons needed to automate the search.  It takes about 10 seconds to complete the search.

### Prerequisites

The app uses Python, Django, JavaScript, and api's from Discogs.com, and Imgur.com.
See requirements.txt to install all the requirements.

### Installation

Create a virtual environment, then pip install everything in the requirements.txt.
You will need get api's from Discogs.com, and Imgur.com.

### Tests

I have a few tests written, however they are not 100%.  I could use some help with that.  Next time I will write the tests as I write the program.

## Author

* **Todd Enders**

## Acknowledgments

* Thanks to  Kieran, Chris, and everyone at PDX Code Guild
