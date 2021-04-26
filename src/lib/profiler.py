import re
import lib.mathlib as ml

class Profiler():
    def __init__(self,data):
    
        self.numbers = []
        self.sum = 0
        self.arith_avg = None
        self.number_of_elements = None
        self.parse_numbers(data)
        
    def parse_numbers(self,data):
        parsed_data = []
        for line in data:
            parsed_data.append(re.split("\s+",line))
            
        for line in parsed_data:
            for element in line:
                if element.isdigit():
                    self.numbers.append(float(element))
        self.start_profiling()
    
    def start_profiling(self):
        # Calc N
        self.number_of_elements = len(self.numbers)
        # Calc sum of all numbers
        for i in range(0,len(self.numbers) - 1,2):
            self.sum += ml.add(self.numbers[i],self.numbers[i+1])
        
        # Calc ar. average
        self.arith_avg = self.sum / self.number_of_elements
        # TODO: idem spinkat
        
            