# movie_title_filter
Filter out common text formatting from a movie file.  Returns a simplified output with a date, if it has one.

<img src="./movie_title_filter_image_1.png" />

<img src="./movie_title_filter_image_2.png" />

<img src="./movie_title_filter_image_3.png" />


* First strips out all of the brackets.
* Searches through the title string, and looks for the "date".  <br>
  ie. a date between 1920 and 2050. <br>
  Function returns an array of the date(s) found and picks the last one.
* If a date was found, parse out the title left of the date.
* No date? Parses out codecs, video codecs, resolutions, and provide a result. 
