#!/usr/bin/env python3
# s26VideoPlayer.py - IMPROVED
import threading
import os
import sys

# Suppress Qt backend issues with OpenCV
#os.environ['QT_QPA_PLATFORM'] = 'offscreen'

import ExtractFrames
import ConvertToGrayscale
import DisplayFrames
import s26Buffer

outputDir    = 'frames'
clipFileName = 'clip.mp4'

if __name__ == '__main__':
    try:
        extract_buffer = s26Buffer.Buffer(max_size=10)
        grayscale_buffer = s26Buffer.Buffer(max_size=10)
        
        t1 = threading.Thread(
            target=ExtractFrames.extractFrames,
            args=(clipFileName, extract_buffer),
            name='ExtractorThread'
        )
        t2 = threading.Thread(
            target=ConvertToGrayscale.convertFrame2Grayscale,
            args=(extract_buffer, grayscale_buffer),
            name='ConverterThread'
        )
        t3 = threading.Thread(
            target=DisplayFrames.displayFrames,
            args=(grayscale_buffer, 42),
            name='DisplayThread'
        )
        
        print('Starting threads...')
        t1.start()
        t2.start()
        t3.start()
        
        t1.join()
        t2.join()
        t3.join()
        
    except Exception as e:
        print(f'Error occurred: {e}', file=sys.stderr)
    finally:
        print('All threads completed')
