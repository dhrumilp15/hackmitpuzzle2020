import os

order = open('order.txt', 'r')
lines = order.readlines()

number = 4
for line in lines:
    source = 'uyxela_b6f561_video_track{}_[und]_DELAY -709ms.wav'.format(number);
    destination = '{}.wav'.format(line[:-1]);
    os.rename(source,destination)
    number += 1