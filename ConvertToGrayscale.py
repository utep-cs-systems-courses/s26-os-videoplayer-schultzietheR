#!/usr/bin/env python3
# ConvertToGrayscale.py
import cv2

def convertFrame2Grayscale(input_buffer, output_buffer):
    """
    Consumer/Producer: Get frames from input buffer, convert to grayscale,
    put converted frames in output buffer.
    Stops when None is received (end-of-stream signal).
    """
    count = 0
    
    while True:
        # Get frame from input buffer (blocks if empty)
        item = input_buffer.get()
        
        # Check for end-of-stream signal
        if item is None:
            output_buffer.put(None)
            break
        
        frame_num, frame = item
        print(f'Converting frame {count}')
        
        # Convert to grayscale
        grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Put converted frame in output buffer (blocks if full)
        output_buffer.put((frame_num, grayscale_frame))
        count += 1
    
    print('Grayscale conversion complete')
