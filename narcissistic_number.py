def narcissistic( value ):
    return value == sum(int(x)**len(str(value)) for x in str(value))

if __name__ == '__main__':
    print(narcissistic(153))