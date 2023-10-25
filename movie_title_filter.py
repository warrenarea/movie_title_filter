import sys,os      # Common imports, sys to get command-line arguments. os to exit back to terminal.

# Arrays of strings to parse out.
video_sources     = ["web","ahdtv","bd25","bd5","bd50","bd9","bdr","bdrip","bdscr","bluray","blueray","bluray","blurayrip","brrip","cam","cam(ts)","camrip","ddc","dhrip","dsr","dsrip","dsrrip","dth","dthrip","dtv","dvb","dvbrip","dvdfull","dvd5","dvd9","dvdr","dvdrip","dvdscr","dvdscreener","hdts","hdtv","hdcam","hdcamrip","hddvdrip","hdrip","hdts","hdtv","hdtvrip","hdtvrip","iptvrip","ldrip","mbluray","mdvdr","pdtv","pdtv","pdtvrip","pdtvrip","ppv","ppvwebdl","ppv.hdtv","ppvrip","r5line","satrip","satrip","scr","screener","sdtv","std","tc","telecine","telesync","ts","tvrip","tvrip","vcdrip","vhsrip","vhsscr","vodr","vodrip","wbbrip","webdl","webdlrip","webdl","webdldvdrip","webdlrip","webrip"]
video_codecs      = ["h264","3iv2","3ivd","advj","avc","avrn","div1","div2","div3","div4","div5","div6","divx","dm4v","dvdr","dx50","em2v","geox","h.264","hevc","hevc x265","lmp2","m4s2","mmes","mp4","mpeg 1 video","mpeg 2","mpeg 2 video","mpeg 4","nds","ndx","ntsc","pal","pim1","pvmm","rle","rpza","smc","sv10","svq","umdmovie","v mpeg4","vc 1","x264","x265","x265 hevc","xvid","xvix","zygo"]
audio_channels    = ["2.0","2ch","5.1","5.1ch","6ch"]
lang_codes        = ["NL", "nl","ENG", "en","CRO", "hr","JAP", "jp","RUS", "ru","SER", "sr","SLO", "sl","srbski", "sr","hrvatski", "hr","German", "de","ITALIAN", "it","Chinese", "cn","CZECH", "cz","RUSSIAN", "ru","FRENCH", "fr","TRUEFRENCH", "fr"]
release_groups    = ["0x539","420ripz","7sins","8ballrips","aaa","aaf","abd","adhd","aen","aeroholics","afg","afo","aggr0","aihd","alliance","amiable","an0nym0us","anihls","apl","arc","arigold","arrow","arthouse","avchd","avs720","axxo","band1d0s","belial","bestdivx","besthd","bff","bia","biq","blow","brmp","cbgb","ccat","cddhd","cfh","chd","cinefile","cocain","condition","counterfeit","cowry","crisc","crooks","crossbow","ctrlhd","ctu","cultxvid","cybermen","d-z0n3","d3si","daa","de(42)","debtxvid","decibel","definite","deity","dem","demented","depravity","deprived","deranged","devise","diamond","dimension","dioxide","dirty","document","domino","don","done","dot","dutchreleaseteam","dvf","dvl","dvsky","ea","ebp","eci","effect","episode","erodeluxe","esir","espise","ethos","ettv","eureka","evo","evolve","ewdp","exile","extacy","exvid","exvidint","failed","felony","ffm","fico","fihvid","filmhd","finale","flair","flaite","flawl3ss","form","fqm","fragment","framestor","fsihd","ftp","ftw-hd","fty","fum","fzhd","galt","geckos","gimchi","gxp","gzp","h264irmu","h@m","hab","haggis","haideaf","halcyon","handjob","hangover","hca","hd4u","hdc","hdclassics","hdclub","hddevils","hdencx","hdex","hdmaniacs","hdnordic","hidt","hls","hubris","hv","ibex","ifpd","ift","ignition","iguana","iht","ika","ilg","ill","illusion","ils","imbt","immerse","immortals","incite","ind","infamous","injection","intimid","invandraren","itch","japhson","jetset","jollyroger","kafferep","kaka","kebap","killers","kingben","kinobox","klaxxon","kwz","kyr","lap","larceny","lchd","leverage","line","lividity","lol","loung3d","lpd","ltrg","ltu","margin","maxhd","mchd","mcr","megusta","melite","meth","metis","mhd","mhq","moh","momentum","moovee","mrx","msd","multiply","mysilu","ndn","nedivx","neptune","newmov","ngb","nhanc3","nile","nodlabs","nordichd","noscreens","nox","ntv","obsidion","oem1080","osiris","otv","ouzo","parasite","particle","perfectionhd","pfa","phobos","postx","prime","prodji","progress","psychd","publichd","pukka","qcf","rarbg","rartv","rawnitro","rcdivx","reactor","red","redblade","refined","reveille","ritalin","ritalix","roundrobin","rovers","ruby","rude","rusted","saimorny","sam","santi","saphire","scared","scream","sector7","semtex","septic","ser","sinners","skitfiske","sml","smokey","sonido","sparks","splitsville","sprinter","sunspot","svinto","swaggerhd","sys","target","taste","tcm","tdf","tdm","thora","thugline","tide","timelords","titans","tla","tlf","trojan","trv","tusahd","twist","twizted","txf","ubm","ulla","undead","unit","untouchables","unveil","usi","utl","vamps","vcdvault","vedett","veto","vh-prod","vision","vista\u2122","vomit","w4f","walmart","waste","whiizz","whiskey","wide","wiki","wlm","wpi","wrd","wsp\u00ae","xander","xcz","xii","treem","sf"]
release_props     = ["BAD FPS","BAD IVTC","DiRFiX","NFOFiX","READNFO","REMASTER","REMASTERED","REPACK","RERIP","STV","vhsrip"]
video_resolutions = ["1080i","1080p","1440i","1440p","2160i","2160p","360i","360p","4320i","4320p","480i","480p","576i","576p","720i","720p","900i","900p"]


# Find a date between 1920 to 2070 and then return all array positions of the dates.
def sift_dates(title):
    title_grouping = title.split(".")
    
    date_entries = [0]
    for index, look_for_date in enumerate(title_grouping):
        for date_range in range(1920,2070):
            if str(date_range) in look_for_date:
                date_entries.append(index)
    
    return date_entries  # returns  [0, 1]  where 1 is 

# Removes brackets from title.            
def sift_brackets(title):
    title = title.replace("[","")
    title = title.replace("]","")
    title = title.replace("(","")
    title = title.replace(")","")
    title = title.replace("{","")
    title = title.replace("}","")
    return title

# Look for partial matches in the 'title' of the dictionary_grouping array.
def sift_through(title, dictionary_grouping):
    if not isinstance(title, list):
        title_grouping = title.split(".")
    else:
        title_grouping = title

    filtered_title_grouping = []

    for entry in title_grouping:
        found = False

        for dict_name in dictionary_grouping:
            if dict_name.lower() in entry.lower():
                found = True
                break

        if not found:
            filtered_title_grouping.append(entry)

    return filtered_title_grouping

# Remove excessive spaces and additional formatting.
def remove_excess_spaces(title):
    title      = title.replace("-"," ")
    title      = title.replace("+"," ")
        
    iteration = 0  
    while "  " in title and iteration < 100:
        iteration += 1  # Prevent a loop through very unlikely formatting.
        title      = title.replace("  "," ")
        title      = title.replace(". "," ")
        title      = title.replace("  "," ")
    title = title.replace(" ",".")
    return title


def request_title(title=None):
    if title == None:
        if len(sys.argv) > 1:
            title = sys.argv[1:]
            title = " ".join(title)
        else:    
            print("\r\n Usage: python.exe .\movie_title_filter.py The Movie Name (Year) And Excess Text. ")
            print(" " + ("_" * 50))
            print(" Formats excess text out of text. ")
            os._exit(0)
            
    title = remove_excess_spaces(title)   

    title      = sift_brackets(title)   # Remove brackets.
    last_date  = sift_dates(title)[-1]  # Get last date.

    if last_date == 0:
        title      = sift_through(title, video_codecs)
        title      = sift_through(title, video_resolutions)
        title      = sift_through(title, video_sources)
        title      = sift_through(title, audio_channels)
        title      = sift_through(title, release_props)
        title      = " ".join(title)
    else:   
        title_str   = title.replace("."," ")
        title_split = title_str.split(" ")
        

        title =  title_split[0 : int(last_date)]     
        title     = " ".join(title)

    if last_date != 0:
        date = "(" + title_split[last_date][:4] + ")"
    else:
        date = ""

    return title, date

movie_title, release_year = request_title()  # No title passed? Check command-line arguments.
#title, date = request_title("shining.time.station.2024.1080p.blueray.x264")  # or pass the title.

# Print out results.
print("Title: " + str(movie_title) + " " +  str(release_year))
