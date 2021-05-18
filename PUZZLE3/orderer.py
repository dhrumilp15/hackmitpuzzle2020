import json
import wave
from os import listdir

data = "genres trapped recommission letitia sylvain slave website divided according either mirror netflix february reporter censorship sameer subsequent sequence received desperate interviews humanitys milioti jesse emotional quite foster september anthem trippy another developing place referring overtly effect zombiebased imagination avail editing endemol picture reusing opted prime monahan bear cameron piece wright"

with open('final.json', 'r') as f:
    word_dict = json.load(f)

print(word_dict)

dat = [-1] * len(word_dict)
outfile = "combined.wav"

for word in data.split(" "):
    num = word_dict[word]
    audiofile = wave.open(f"./info/dhrumilp15_61090d_video_track{num}_[und]_DELAY -709ms.wav", "rb")
    dat[num - 4] = [audiofile.getparams(), audiofile.readframes(audiofile.getnframes())]
    audiofile.close()

output = wave.open(outfile, 'wb')
output.setparams(dat[0][0])
for seg in dat:
    output.writeframes(seg[1])
output.close()