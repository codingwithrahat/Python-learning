f = open("01_demo.txt", "w") #overwrie
f.write("New Twxt") 
f.close()


f = open("01_demo.txt", 'a')   #append , add at the end
f.write("\nAdd at the end")
f.close()



#if file not exists
#there is no file name 02_demo.txt
f = open("02_demo.txt", "w")  #it will create the file
f.close()
#it also work for mode 'a'
