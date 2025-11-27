# Create a custom iterator called EvenRange that yields even numbers between a start and end.

class EvenRange:
    def __init__(self, start, end):
        self.value = start if start % 2 == 0 else start + 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration  

        current = self.value
        self.value += 2
        return current
                
          
    
evens = EvenRange(0, 10)  
for num in evens:
    print(num)