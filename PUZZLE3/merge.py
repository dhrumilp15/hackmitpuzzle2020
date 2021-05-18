import wave

file_list = "another completed realised dramas sense messages zeppotron waldo quite exists important establishes reached opener bear done first ended enjoying unexpected referring unanticipated former colours living earning lacked addiction brookers complex format donald moving rather recommission endemol andrea international hand manifestly mackenzie trapped yorkie sameer experimental prime million newspaper interviews window"
infiles = file_list.split(' ')
outfile = "audio.wav"

data = []
for infile in infiles:
    file_name = '{}.wav'.format(infile)
    w = wave.open(file_name, 'rb')
    data.append( [w.getparams(), w.readframes(w.getnframes())] )
    w.close()

output = wave.open(outfile, 'wb')
output.setparams(data[0][0])
for i in range(len(data)):
    output.writeframes(data[i][1])
output.close()