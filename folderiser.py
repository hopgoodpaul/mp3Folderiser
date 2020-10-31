from mutagen.id3 import ID3, ID3NoHeaderError
import os
import shutil

def getAlbumName(folder):
	for file in os.listdir(folder):
		if file.endswith(".mp3"):
			musicPath = os.path.join(folder, file)
			print("checking:", musicPath)
			try:
				audio = ID3(musicPath)
				if 'TALB' in audio:
					print(audio['TALB'].text[0])
					newPath = os.path.join(folder,audio['TALB'].text[0])
					if os.path.exists(newPath):
						shutil.move(musicPath,newPath)
					else:
						try:
							os.mkdir(newPath)
						except OSError:
							print ("Creation of the directory %s failed" % newPath)
						else:
							print ("Successfully created the directory %s " % newPath)
							shutil.move(musicPath, newPath)
							print("Moved file")
			except ID3NoHeaderError:
				print("No tags available. Can't sort this one")
#			for info in audio:
#				print(audio[info].text[0])
#				print(info)

getAlbumName('/media/Volume5/Music from Google Play Music/')
