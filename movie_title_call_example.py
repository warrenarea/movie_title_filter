import movie_title_filter

Movie_Tests = [
  "Bad.S03E01.HDTV.x264-TLA[rarTV]",
  "army.wives.s04e02.720p.hdtv-red",
  "The Grand Tour S01E06 WEBRip X264-FUM[ettv]",
  "Bad Santa 2 2016 READNFO HDRip XviD AC3-EVO",
  "Nocturnal Animals 2016 HC HDRip XViD AC3-ETRG",
  "tvN 도깨비 E08 161224 720p NEXT",
  "Trolls 2016 720p WEBRip x264 AAC-ETRG",
  "The Accountant (2016) 1080p YTS AG",
  "The Accountant 2016 720p BRRip x264 AAC-ETRG",
  "Assassins Creed 2016 HDCAM NAKRO",
  "Warriors.Gate.2016.DVDRip.XviD.AC3-EVO",
  "The Accountant 2016 BRRip XviD-ETRG",
  "Inferno 2016 720p WEBRip x264 AAC-ETRG",
  "Spectral.2016.FRENCH.WEBRip.XviD-EXTREME",
  "Dangal (2016) 1CD Desi pDVD x264 -DDR",
  "The Accountant 2016 1080p BRRip x264 AAC-ETRG",
  "The Accountant (2016) YTS AG",
  "The Trust 2016 TRUEFRENCH BDRip XviD-EXTREME",
  "Doctor Who 2005 S10E00 The Return of Doctor Mysterio HDTV x264-DEADPOOL[ettv]",
  "Office Christmas Party 2016 HDCAM x264 UnKnOwN",
  "Dangal (2016) Hindi 1CD Desi Pre-DvDRip x264 AAC - Downloadhub",
  "Lone.Star.1996.1080p.AMZN.WEB-DL.DD+2.0.x264-AJP69"
]

for Test in Movie_Tests:
    movie_title, release_year = movie_title_filter.request_title(Test)
    print(f"\r\n Title: {movie_title} {release_year} ") 
