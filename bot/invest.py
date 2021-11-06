import graph
import watermark
import os


# Updating all graphs.
def update_all():
    graph.correlation_xfl_spx_to_us10yt()
    graph.correlation_copper_gold_to_us10yt()
    print('log: all graphs has been updated')


def watermark_text_all():
    for imagename in os.listdir('images'):
        watermark.text('images/' + imagename, pos=(0, 0))
    print('log: all images has been watermakred(text)')

