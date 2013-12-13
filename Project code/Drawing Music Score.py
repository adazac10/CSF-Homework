import cairo
from realbook import MusicScore

# Create a new MusicScore
score = MusicScore()
score.title = 'Title'
score.author = 'Author'
score.tempo = 'Swing'
s = score.add_staff()
m = s.add_measure(section='A', stop_barline='final')
m.add_chord(0, 'C')
# print to pdf
w, h = (8.27*100, 11.69*100)
surface = cairo.PDFSurface('score.pdf', w, h)
cr = cairo.Context(surface)
score.draw(cr, w, h)
cr.show_page()



'''
use cairo in order to get it to work, this is the best
module ever! we just need to add sound bits to it
so much better than the face I made earlier
'''