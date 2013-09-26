from datetime import datetime


class MorningRoutine(object):
    
    
    GREETING = 'Its {hour} AM.\n{msg}Time to do your morning routine.'
    LATE = 'You are late!\n'
    ONTIME = 'You are on time.\n'
    
    
    def __init__(self):
        self.time = datetime.now().hour
        
        
    def routine(self):
        """returns greeting to user. lets user now if late for routine"""
        if self.time > 9:
            return self.GREETING.format(hour=self.time, msg=self.late)
        else:
            return self.GREETING.format(hour=self.time, msg=self.late)
            
            
            
morning_routine = MorningRoutine()
print morning_routine.routine()

