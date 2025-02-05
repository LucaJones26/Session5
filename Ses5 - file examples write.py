# lets create a virtual diary
with open("diary.txt", "a") as fp:
    while True:
     text = input("How do you feel today? (type q to quit); ") # when pressing q then done journaling
     if text == "q":
         break
     fp.write(f"{text}/n") # this is the same # fp.write(text + "/n") # this is the same
     # meant to be able to see diary as a file


