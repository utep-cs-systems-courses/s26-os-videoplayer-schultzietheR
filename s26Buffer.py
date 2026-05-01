#!/usr/bin/env python3
# s26Buffer.py
import threading

class Buffer:
    """
    A thread-safe bounded buffer for producer-consumer patterns.
    Uses locks and condition variables for synchronization.
    """
    
    def __init__(self, max_size):
        self.max_size = max_size
        self.buffer = []
        self.lock = threading.Lock()
        self.not_empty = threading.Condition(self.lock)
        self.not_full = threading.Condition(self.lock)
    
    def put(self, item):
        """
        Producer: Add item to buffer.
        Blocks if buffer is full until consumer removes an item.
        """
        with self.not_full:
            # Wait until buffer is not full
            while len(self.buffer) >= self.max_size:
                self.not_full.wait()
            
            # Add item
            self.buffer.append(item)
            print(f'  Buffer: put item (size now {len(self.buffer)}/{self.max_size})')
            
            # Signal consumer that buffer is not empty
            self.not_empty.notify()
    
    def get(self):
        """
        Consumer: Remove and return item from buffer.
        Blocks if buffer is empty until producer adds an item.
        """
        with self.not_empty:
            # Wait until buffer is not empty
            while len(self.buffer) == 0:
                self.not_empty.wait()
            
            # Remove and return item
            item = self.buffer.pop(0)
            print(f'  Buffer: got item (size now {len(self.buffer)}/{self.max_size})')
            
            # Signal producer that buffer is not full
            self.not_full.notify()
            
            return item
