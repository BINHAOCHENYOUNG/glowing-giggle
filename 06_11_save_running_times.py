#This program will save a running time to a file 


#Case: Chad ask you to write 2 program that help his work. He has classs videos and want to save it running time to a file

#1. A progrme that allow him to enter the running time(in seconds) of each short videos in a project. The running times are saved to a file 

#2. A program that reads the contents of the file, displays the running times, and then displays the total running time of all the videos. 
def main():

#Get the number of videos in a project 
    num_videos = int(input("Enter the number of the videos:"))
#open an output file 
    video_file = open('video_file.txt','w')
    #For each video in the prroject 
    for count in range(1,num_videos+1):
        #get the video's running time 
        run_time = input("Video#"+str(count)+ ":")
        #Wtite the running time to the file 
        video_file.write(str(run_time) +"\n")
    #close the file 
    video_file.close()
    print("The video file has completed")
#call the main 
main()