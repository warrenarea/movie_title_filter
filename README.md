# Movie Title Filter
Filter out common torrent formatting from a video file. <br>
Returns a simplified output with a date, if it has one.


* First strips out all of the brackets.
* Searches through the title string, and looks for the "date".  <br>
  ie. a date between 1920 and 2050. <br>
  Function returns an array of the date(s) found and picks the last one.
* If a date was found, parse out the title left of the date.
* No date? Parses out codecs, video codecs, resolutions, and provide a result. 

<img src="./movie_title_filter_image_3.png" />

<img src="./movie_title_filter_image_4.png" />

<img src="./movie_title_filter_image_1.png" />

<img src="./movie_title_filter_image_2.png" />


