import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on " + time.ctime())

while(break_count<total_breaks):
    time.sleep(2*60*60)
    webbrowser.open('http://v.youku.com/v_show/id_XMTc3MTg1ODg4MA==.html?spm=a2hms.20021793.m_213513.5~5!2~5~5~8~A')
    break_count = break_count +1
