import serial
import time
import threading


global Xbee #xbee
Xbee = serial.Serial('/dev/ttyUSB0', 115200)

time_int = 0

def printit():          #print out the angle every 5 seconds
        threading.Timer(5.0, printit).start()
        print ("{0:.3f}".format(angle))

#Body
cycle_time = 10 #length of osc duration
time_base = time.time()
initial_heading  = float(input("Initial angle?" ))
timer_baseval = time.time()


while True:
        try:
		if (initial_heading >= 360):
		    initial_heading= initial_heading - 360

		if (initial_heading <= 0):
                    initial_heading = 360 + initial_heading 


                time_int = ((initial_heading/360) * cycle_time ) + ((time.time() - time_base))
                #While the heading of the roomba is <360 degrees, rotate the roomba by 2.5 degrees per second
                
                

                if (time_int >= 10):  #if the heading angle is over or equal to 360, or less than 0 then a pulse will be sent out
                    broadcast = '1'
                    Xbee.write(broadcast.encode())
                    time_base = time.time()

               # if (time_int <= 0)
                 #    broadcast = '1'
                 #   Xbee.write(broadcast.encode())
                 #   angle = angle + 360

                
                    
                if (time.time() - timer_baseval >= 1):
                    timer_baseval = timer_baseval + 1
                    print ("{0:.3f}, {0:.1f}".format(time_int, initial_heading))
                

                if Xbee.inWaiting() > 0:
                    message = Xbee.read(Xbee.inWaiting()).decode()
                    #if (cycle_time - time_int > 5 ):
		    initial_heading = initial_heading + ((cycle_time - time_int)*0.25) * (360/cycle_time)

                   # elif (angle >= 180):
                     #   initial_heading = initial_heading + ((360 - angle)*0.25)
                    


               # if (initial_heading >= 360):
                #    initial_heading = initial_heading - 360
                #    time_base = time_base - cycle_time

                    
               # if (initial_heading <= 0):
                #    initial_heading = 360 + initial_heading
                #    time_base = time_base + cycle_time


        except KeyboardInterrupt:
            break

