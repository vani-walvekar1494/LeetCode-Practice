class Solution(object):
    def convertTemperature(self, celsius):
        kelvin = round(celsius + 273.15, 2)
        fahrenheit = round(celsius * 1.80 + 32.00, 2)
        return [kelvin, fahrenheit]

def get_valid_celsius_input():
    while True:
        try:
            celsius = float(input("Please enter temperature in Celsius: "))
            if len(str(celsius).split('.')[-1]) > 2:
                print("Please enter a value with at most two decimal places.")
            else:
                return celsius
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

solution = Solution()
celsius = get_valid_celsius_input()
result = solution.convertTemperature(celsius)
print(result)
