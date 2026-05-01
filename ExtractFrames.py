#!/usr/bin/env python3
# ExtractFrames.py
import cv2

def extractFrames(filename, output_queue, max_frames=9999):
    """
    Extract frames from video and put them in output queue.
    Signals completion by putting None in queue.
    """
    vidcap = cv2.VideoCapture(filename)
    count = 0
    
    success, image = vidcap.read()
    print(f'Reading frame {count}: {success}')
    
    while success and count < max_frames:
        # Put frame tuple (frame_number, image_data) in queue
        output_queue.put((count, image))
        
        success, image = vidcap.read()
        count += 1
        print(f'Reading frame {count}: {success}')
    
    # Signal end-of-stream
    output_queue.put(None)
    print('Frame extraction complete')
    vidcap.release()
