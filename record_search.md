# Vinyl Search App

##### Since most vintage records don't have a UPC code.  You can take a photo of a record cover and find it online(Discogs)

### Specific Fuctionality:

    - Take a photo of an album cover
        - On the phone version I would like to have the app turn on the camera and
          and take photo from the app then automatically search.
    - Open the app
    - import the photo, or have the user select the photo.
    - Have the app use google image search to find info on the album.
        -  The search will look for info on Discogs.com
    - Pull up info from Discogs, or take the user to the Discogs site to see if
       the user has it in their collection, check pricing, or add it to their wishlist.

### Data Model

    - Flexbox page layout.
    - Add a way to upload an image
        - On the phone it will need to turn on the camera and save the photo.
    - Automate a google image search(using selenium)
    - parse the google search results to populate a search of Discogs
    -Imgur API to create a url to search for.
    - Discogs API. to provide album info
    - Display album info and a link to go to the Discogs page for the album.

### Techincal Components

    - Use markdown to
    - Use CSS, HTML, JS, to create a web page
    - Import dropzone.js to collect the images with JavaScript
    - Use google image search API
    - Use python to parse the image results
    - Use Discogs API to return album info and display on page along with
      link to Discogs


### Schedule

    - Work hard to finish in time.

### Further Work

    - Create mobile app
    - Work on creating a larger database with my own image search system
