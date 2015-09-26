import os
import eyed3
#put adress here
adress = ""     #give your own address here for the directory 
folder_list = os.listdir(adress)        #btw for the spelling of address, that's intentional


#album_name = i.split('-')[2]

for x in next(os.walk(adress))[1]:
    album_name = unicode(x.split('-')[2]).strip()
    album_year = unicode(x.split('-')[1]).strip()
    os.chdir(adress+x)
    for file_name in os.listdir(adress+x):
        title = unicode((((file_name.split('-')[1]).strip()).split('.'))[0])
        track_number = unicode((file_name.split('-')[0]).strip())
        if file_name.endswith('.mp3'):
            f = eyed3.load(file_name)
            f.tag.album = album_name
            f.tag.artist = u'Pink Floyd'    # change the setting according to your specifications
            f.tag.genre = u'Psychedelic Rock'   
            f.tag.album_artist = u'Pink Floyd'  
            f.tag.title = title
            f.tag.play_count = track_number
            f.tag.save(file_name, version=(1,None,None))
            f.tag.save(file_name, version=(2,3,0))
            #By default eyed3.load(pathtofile) loads ID3_V2_4 tags,
            #and Explorer and Windows Media Player use 1.x tag (X is
            #encoding; I don't know which

    for y in next(os.walk(adress+x))[1]:
        print adress+x+'\\'+y
        os.chdir(adress+x+'\\'+y)
        for file_name in os.listdir(adress+x+'\\'+y):
            title = unicode((((file_name.split('-')[1]).strip()).split('.'))[0])
            track_number = unicode((file_name.split('-')[0]).strip())
            if file_name.endswith('.mp3'):
                f = eyed3.load(file_name)
                f.tag.album = album_name
                f.tag.artist = u'Pink Floyd'
                f.tag.genre = u'Psychedelic Rock'
                f.tag.album_artist = u'Pink Floyd'
                f.tag.title = title
                f.tag.play_count = track_number
                f.tag.save(file_name, version=(1,None,None))
                f.tag.save(file_name, version=(2,3,0))
    
    #for x in next(os.walk(adress+i)):
        #dir2 = os.listdir(adress+i+"\\"+x)
        #print x[1]
