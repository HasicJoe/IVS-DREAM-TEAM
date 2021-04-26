import re
import lib.mathlib as ml

class Profiler():
    def __init__(self,data):
        self.numbers = []
        self.sum = 0
        self.arith_avg = 0
        self.in_br = 0
        self.before_br = 0
        self.std_dev = 0
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
        # Calc sum of all numbers
        for i in range(0,len(self.numbers) - 1,2):
            self.sum += ml.add(self.numbers[i],self.numbers[i+1])
            
        if len(self.numbers) % 2 == 1:
            self.sum += self.numbers[len(self.numbers)-1]
        
        # Calc arithmetic. average
        self.arith_avg = ml.arith_average(self.sum,self.numbers)
        
        for i in self.numbers:
            self.in_br += ml.exp(i,2)
        
        self.in_br -= ml.list_len(self.numbers) * ml.exp(self.arith_avg,2)
        self.before_br = ml.divide(1,ml.list_len(self.numbers)-1)
        self.std_dev = ml.root(ml.multiply(self.before_br,self.in_br),2)
        print(self.std_dev)