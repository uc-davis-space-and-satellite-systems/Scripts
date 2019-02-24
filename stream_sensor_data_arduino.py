import serial

if __name__ == "__main__":
    ser = serial.Serial("\\\\.\\COM8", baudrate=9600, timeout=0)

    f = open("data.csv", "w")

    while True:
        line = ser.read()
        if line:
            print(line)
            f.write(line.decode('utf-8'))
            f.flush()

    f.close()
