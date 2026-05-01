#!/usr/bin/env python3
# DisplayFrames.py
import cv2

def displayFrames(input_buffer, frame_delay=42):
    expected_frame_num = 0
    
    while True:
        item = input_buffer.get()
        if item is None:
            break
        
        frame_num, frame = item
        
        # Verify ordering
        if frame_num != expected_frame_num:
            print(f'ERROR: Expected frame {expected_frame_num}, got {frame_num}')
        
        print(f'Displaying frame {frame_num}')
        cv2.imshow('Video', frame)
        
        if cv2.waitKey(frame_delay) & 0xFF == ord('q'):
            break
        
        expected_frame_num += 1
    
    print('Finished displaying all frames')
    cv2.destroyAllWindows()
