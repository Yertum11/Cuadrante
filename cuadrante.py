import os

def get_values():
    try:
        x = int(input('Enter the value of x: '))
        y = int(input('Enter the value of y: '))
        return x, y
    except ValueError:
        print("Please enter numeric values.")
        return None, None

def determine_location(x, y):
    if x == 0 and y == 0:
        return 'Origin'
    elif x == 0:
        return 'Y-axis'
    elif y == 0:
        return 'X-axis'
    elif x > 0 and y > 0:
        return 'Quadrant I'
    elif x < 0 and y > 0:
        return 'Quadrant II'
    elif x < 0 and y < 0:
        return 'Quadrant III'
    elif x > 0 and y < 0:
        return 'Quadrant IV'

def main():
    x, y = get_values()

    if x is not None and y is not None:
        location = determine_location(x, y)
        print(f'Location: {location}')
    else:
        print('Error entering values.')

    os.system('pause')

if __name__ == "__main__":
    main()
