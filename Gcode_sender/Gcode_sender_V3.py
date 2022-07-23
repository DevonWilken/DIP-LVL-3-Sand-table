import time
import serial
list_of_lists = []

def check_boundry(f, list_of_lists):
    for line in f:
        l = line.strip() # Strip all EOL characters for consistency
        if l == "$H" or l == "" or l.find(";") != -1:
            pass
        else:
            striped_l = l.strip("G0 ") #remove speed function G0
            number_strings = striped_l.split() # Split the line on runs of whitespace
            list_of_lists.append(number_strings) #add to list

    for item in list_of_lists:
        for i in item:
            removed_x_y = i[1:]#remove first character X or Y
            if float(removed_x_y) > 370:#check boundry
                print("Gcode file exceeds boundry of 370mm please use files under 370mm")
                print("code will now exit")
                time.sleep(5)
                raise SystemExit
            else:
                pass

# Open grbl serial port
s = serial.Serial('COM4',115200)
# Open g-code file
f = open('Gcode_sender\Visualize gcode.gcode','r')
check_boundry(f, list_of_lists)

# Wake up grbl
s.write("\r\n\r\n".encode())
time.sleep(2)   # Wait for grbl to initialize 
s.flushInput()  # Flush startup text in serial input

# Stream g-code to grbl
for line in f:
    l = line.strip() # Strip all EOL characters for consistency
    print( 'Sending: ' + l)
    s.write((l + '\n').encode()) # Send g-code block to grbl
    grbl_out = s.readline() # Wait for grbl response with carriage return
    print( ' : ' + (grbl_out.strip()).decode())

# Wait here until grbl is finished to close serial port and file.
input("  Press <Enter> to exit and disable grbl.") 

# Close file and serial port
f.close()
s.close()