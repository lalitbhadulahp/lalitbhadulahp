import os 
  
# Function to rename multiple files 
def main(): 
    dir = "/home/lalitbhadula/Music/newone/"
    for count, filename in enumerate(os.listdir(dir)): 
        dst = str(count+1) + ".png"
        src = dir + filename 
        dst = dir + dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__':
    # Calling main() function 
    main() 