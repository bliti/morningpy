#!/usr/bin/env python
from datetime import datetime


class MorningRoutine(object):
    
    
    GREETING = 'Its {hour} AM.\n{msg}Time to do your morning routine.'
    LATE = 'You are late.\n'
    ONTIME = 'You are on time.\n'
    
    
    def __init__(self):
        self.time = datetime.now().hour
        
    
    def routine(self):
        """greets user and tells if routine was done late"""
        if self.time > 9:
            return self.GREETING.format(hour=self.time, msg=self.LATE)
        else:
            self.GREETING.format(hour=self.time, msg=self.ONTIME)
            
            
def main():
    morning_routine = MorningRoutine()
    print morning_routine.routine()      


if __name__ == "__main__":
    main()