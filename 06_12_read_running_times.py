

def main():
    #Open the video_time txt file
    video_file = open("video_time.txt","r")
    #Initialize an acumulator to 0.0
    total = 0.0
    #Initialize a variable to kep count of the video 
    count = 0
    print("Here are the running time ")
    #Get the values from the file and total item 
    for line in video_file:
        #Covert a line to a float 
        run_time = float(line)
        #Add 1 to the count variable
        count +=1
        #Display the time 
        print("Video #", count, ":" ,  run_time)
        #Add the time to total 
        total +=run_time
    #Close the file 
    video_file.close()
    #Displaying the total of the running time 
    print("the total running time is", total,"seconds")

main()