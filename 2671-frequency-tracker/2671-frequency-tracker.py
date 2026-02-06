class FrequencyTracker:

    def __init__(self):
        self.number_to_frequency = defaultdict(int)

        self.frequency_to_numbers = defaultdict(set)

    def add(self, number: int) -> None:
        frequency = self.number_to_frequency[number]
        if number in self.frequency_to_numbers[frequency]:
            self.frequency_to_numbers[frequency].remove(number)
        self.frequency_to_numbers[frequency + 1].add(number)
        self.number_to_frequency[number] += 1

    def deleteOne(self, number: int) -> None:
        frequency = self.number_to_frequency[number]
        if frequency > 0 and number in self.frequency_to_numbers[frequency]:
            self.frequency_to_numbers[frequency].remove(number)
            self.number_to_frequency[number] -= 1


        

    def hasFrequency(self, frequency: int) -> bool:

        if len(self.frequency_to_numbers[frequency]) != 0:
            return True
        return False
            
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)