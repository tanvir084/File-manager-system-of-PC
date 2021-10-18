import os
import shutil
import turtle
import time
import glob
import fnmatch
import datetime

def server_time():
    currentDT=datetime.datetime.now()

    print("Server time is now:")
    print (currentDT.strftime("%Y-%m-%d %H:%M:%S"))
    print (currentDT.strftime("%Y/%m/%d"))
    print (currentDT.strftime("%H:%M:%S"))
    print (currentDT.strftime("%I:%M:%S %p"))
    print (currentDT.strftime("%a, %b %d, %Y"))

    return currentDT

def filter_list(full_list, excludes):
    s = set(excludes)
    return (x for x in full_list if x not in s)

def greating_option():
    turtle.Turtle._screen = None
    turtle.TurtleScreen._RUNNING = True
    wn=turtle.Screen()
    wn.bgcolor('black')
    turtle.color('blue')
    style = ('Courier', 20, 'italic')
    #turtle.write('Hello!', font=style, align='center')
    turtle.setposition(-10, 100)
    turtle.write('Welcome to new file management system', font=style, align='center')
    turtle.hideturtle()

    #turtle.setposition(100,-100)
    star=turtle.Turtle()
    star.hideturtle()
    star.color('blue')
    star.speed(15)
    star.setposition(15,-100)
    #star.align('center')

    #if star.distance(-25, 50) < 5:  # turtle is upon the target
    #    star.goto(100, 100)
    
    for i in range(100):
        #star.hideturtle()
        star.forward(150)
        star.right(124)

    #turtle.ontimer(greating_option, 1000000)
    time.sleep(1)
    #turtle.Screen().bye()
    turtle.bye()

def ending_option():
    turtle.Turtle._screen = None
    turtle.TurtleScreen._RUNNING = True
    
    wn=turtle.Screen()
    wn.bgcolor('black')
    t2=turtle.Turtle()
    t2.color('blue')
    style = ('Courier', 18, 'italic')
    #turtle.write('Hello!', font=style, align='center')
    t2.setposition(-10, 200)
    t2.write('Thanks for using this file management system', font=style, align='center')
    t2.hideturtle()

    colors=['red', 'purple', 'blue', 'green', 'orange', 'yellow']

    t=turtle.Pen()
    #turtle.bgcolor('black')
    t.speed(20)
    #t.hideturtle()

    for x in range(150):
        t.pencolor(colors[x%6])
        t.width(x/100)
        t.forward(x)
        t.left(59)

    time.sleep(2)
    #turtle.done()
    turtle.bye()

def background_option():
    #turtle.Turtle._screen = None
    #turtle.TurtleScreen._RUNNING = True

    """t=turtle.Turtle()
    screen=turtle.Screen()
    #screen.setup(400, 400)

    #p=os.path.join(os.getcwd(), "22.gif")
    screen.bgpic("22.gif")

    time.sleep(4)
    turtle.bye()"""

    turtle.hideturtle()

    turtle.bgcolor("black")
    #t=turtle.Turtle()
    s=turtle.Screen()
    #s.setup(300, 300)
    #s.hideturtle()

    turtle.setposition(-10, 150)
    #turtle.hideturtle()
    style = ('Courier', 20, 'italic')
    turtle.color('blue')
    turtle.write('File management system', font=style, align='center')
    turtle.hideturtle()

    s.bgpic("1.png")
    time.sleep(2)
    s.update()
    s.bgpic("3.png")
    time.sleep(2)
    s.update()
    s.bgpic("2.png")
    time.sleep(2)
    s.update()
    s.bgpic("4.png")
    time.sleep(2)
    s.update()
    s.bgpic("5.png")
    time.sleep(2)
    s.update()
    s.bgpic("6.png")
    time.sleep(2)
    s.update()
    time.sleep(2)
    turtle.bye()


#t=turtle.Turtle()
#s=turtle.Screen()
#s.setup(300, 300)

#s.bgpic("22.gif")

def print_path_option():
    global path
    print("Now, you are in")
    print(path)

    print_option()

def print_option():
    print("\n")
    i=0
    print("File list:")
    while i<len(file_list):
        print(file_list[i])
        i=i+1

    print("\n\n")
    i=0
    print("Folder list:")
    while i<len(folder_list):
        print(folder_list[i])
        i=i+1

    print("\n\n")

def print_file_option():
    print("\n")
    i=0
    print("File list:")
    while i<len(file_list):
        print(file_list[i])
        i=i+1

def print_folder_option():
    print("\n")
    i=0
    print("Folder list:")
    while i<len(folder_list):
        print(folder_list[i])
        i=i+1

def change_file_folder_option():
    global path
    global file_list
    global all_list
    global folder_list

    file_list=[]
    folder_list=[]
    all_list=[]

    all_list=os.listdir(path)

    with os.scandir(path) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file():
                 #print(entry.name)
                file_list.append(entry.name)

    folder_list=list(filter_list(all_list, file_list))


def forward_option():
    global path
    global file_list
    global all_list
    global folder_list
    path=path+"\\"
    
    if len(folder_list)==0:
        print("You cannot go backward because there is no directory further")
        print("So, please choose other option")

    else:
        #print_path_option()        
        print("Now you are in:")
        print(path)
        print_folder_option()
        
        print("Please, choose your directory or folder from folder list")
        selection=input()

        selection_path=path+selection

        if os.path.isdir(selection_path):
            path=path+selection

            change_file_folder_option()

            print("\n")
            
            print_file_option()

            print("\n\n")

            print_folder_option()
            
            print("\n\n")

        else:
            print("You choose wrong path. Please, try again")


def backward_option():
    global path
    global drives
    global file_list
    global all_list
    global folder_list
    p_list=list(path)

    if(len(p_list)==0 or len(p_list)==3):
        #print("You can not go back any more, choose other option")
        #print("\n")
        
        print("Drives:")
        i=0
        while i<len(drives):
            print(drives[i])
            i+=1

        print("Please, select your drive:")
        selection=input()

        path=selection+":\\"

        all_list=[]
        file_list=[]
        folder_list=[]

        all_list=os.listdir(path)

        with os.scandir(path) as it:
            for entry in it:
                if not entry.name.startswith('.') and entry.is_file():
                    #print(entry.name)
                    file_list.append(entry.name)

        folder_list=list(filter_list(all_list, file_list))

        print("In ", selection, " drives:")

        print_option()
              
    else:
        print_path_option()
        
        p_list.reverse()

        i=0

        while p_list[i]!='\\':
            del(p_list[i])

        #print(p_list)

        if len(p_list)>3:
            del(p_list[0])

        p_list.reverse()

        path="".join(p_list)

        #print(path)

        file_list=[]
        all_list=[]
        folder_list=[]

        all_list=os.listdir(path)

        with os.scandir(path) as it:
            for entry in it:
                if not entry.name.startswith('.') and entry.is_file():
                    #print(entry.name)
                    file_list.append(entry.name)

        folder_list=list(filter_list(all_list, file_list))

        #print("In ", selection, " drives:")

        print("\n")
        
        i=0

        print("File list:")
        while i<len(file_list):
            print(file_list[i])
            i=i+1

        print("\n\n")
        i=0
        print("Folder list:")
        while i<len(folder_list):
            print(folder_list[i])
            i=i+1

        print("\n\n")

def new_option():
    global path
    global file_list
    global all_list
    global folder_list

    print("Option")
    print("File")
    print("Folder")
    print("Please, choose your option:")
    op_choose=input()

    if op_choose=="File":
        print("Please, write your file name with extention(as file_name+.extention)")
        file_name=input()
        my_file=open(path+'/'+file_name, 'w')
        my_file.close

        print("Your work is done!!!")

    elif op_choose=="Folder":
        print("Please, write your folder name")

        n_folder=input()
        create_path=path+'/'+n_folder

        try:  
            os.makedirs(create_path)
        except OSError:  
            print ("Creation of the directory %s failed" % create_path)
        else:  
            print ("Successfully created the directory %s" % create_path)
    else:
        print("You make a mistake, try again")

    change_file_folder_option()

def rename_option():
    global path
    global file_list
    global all_list
    global folder_list

    print_option()

    print("Option")
    print("Single")
    print("Advance")
    print("Please, choose your option:")
    choice=input()
    if choice=="Single":
        print("Please, enter your old file name with extention or folder name")
        old_name=input()
        print("Now, enter your new file or folder name")
        new_name=input()

        old_path=path+'/'+old_name
        new_path=path+'/'+new_name
            

        try:  
            os.rename(old_path, new_path)
        except OSError:  
            print("Renamming of the directory %s failed" % new_path)
        else:  
            print("Successfully renamed the directory %s" % new_path)
    elif choice=="Advance":
        print("In this option, you can rename all folder or same type file in a pattern way")
        print("Choose your system")
        print("Folder")
        print("File")
        sys_choose=input()
        if sys_choose=="Folder":
            print("Please, choose your rename option:")
            print("Rename as system 1, 2, 3..., please write int")
            print("Rename as system a0..z0, a1,b1, please write alb_int")
            print("Rename as system your choice+1, your choice+2, please write my_int")

            rename_option=input()
            
            if rename_option=="int":
                i=0
                while i<len(folder_list):
                    try:  
                        os.rename(path+'/'+folder_list[i], path+'/'+str(i+1))
                    except OSError:  
                        print("Renamming of the directory %s failed" % folder_list[i])
                    i+=1
                print("Your work is done!!!")
                    
            elif rename_option=="alb_int":
                i=0
                new_folder_list=[]
                while i<len(folder_list):
                    j=0
                    while j<26:
                        join=chr(97+j)+str(i)
                        #print(join)
                        new_folder_list.append(os.path.join(path, join))
                        j+=1
                        if j==len(folder_list):
                            break
                    if j==len(folder_list):
                        break
                    i+=1

                i=0
                while i<len(new_folder_list):
                    try:  
                        os.rename(path+'/'+folder_list[i], new_folder_list[i])
                    except OSError:  
                        print("Renamming of the directory %s failed" % folder_list[i])
                    i+=1
                print("Your work is done!!!")
            elif rename_option=="my_int":
                print("Please, write your folder choice name")
                my_rename=input()

                i=0
                while i<len(folder_list):
                    try:  
                        os.rename(path+'/'+folder_list[i], path+'/'+my_rename+str(i+1))
                    except OSError:  
                        print("Renamming of the directory %s failed" % folder_list[i])
                    i+=1
                print("Your work is done!!!")
            else:
                print("You mistake something")
                    
        elif sys_choose=="File":        
            print("Please, choose your rename option:")
            print("Rename as system 1, 2, 3..., please write int")
            print("Rename as system a0..z0, a1,b1, please write alb_int")
            print("Rename as system your choice+1, your choice+2, please write my_int")

            rename_option=input()

            f=0

            print("Now, choose your file extension:")
            file_ext=input()
            old_file_list=[]
            new_file_list=[]
            for file in file_list:
                if fnmatch.fnmatch(file, '*'+file_ext):
                    old_file_list.append(os.path.join(path,file))
            
            if rename_option=="int":
                f=1
                i=0
                while i<len(old_file_list):
                    #new_file_list.append(os.path.join(path, (str(i+1)+file_ext)))
                    new_file_list.append(path+'/'+str(i+1)+file_ext)
                    i+=1
            
            elif rename_option=="alb_int":
                f=1
                i=0
                while i<len(old_file_list):
                    j=0
                    while j<26:
                        join=chr(97+j)+str(i)+file_ext
                        #print(join)
                        new_file_list.append(os.path.join(path, join))
                        j+=1
                        if j==len(old_file_list):
                            break

                    if j==len(old_file_list):
                        break
                    i+=1

            elif rename_option=="my_int":
                f=1
                print("Please, write your folder choice name")
                my_rename=input()

                i=0
                while i<len(old_file_list):
                    new_file_list.append(os.path.join(path, my_rename+str(i+1)+file_ext))
                    i+=1
            if f==1:
                i=0
                while i<len(old_file_list):
                    try:  
                        os.rename(old_file_list[i], new_file_list[i])
                    except OSError:  
                        print("Renamming of the directory %s failed" % old_file_list[i])
                    #else:  
                     #   print("Successfully renamed the directory %s" % new_file_list[i])
                    i+=1
                print("Your work is done!!!")
            else:
                print("You make a mistake")
                
    file_list=[]
    folder_list=[]
    all_list=[]

    all_list=os.listdir(path)

    with os.scandir(path) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file():
                #print(entry.name)
                file_list.append(entry.name)

    folder_list=list(filter_list(all_list, file_list))        
            

def delete_option():
    global path
    global file_list
    global all_list
    global folder_list

    print("Delete Option")
    print("Single")
    print("Multiple")

    print("Please, choose your delete option:")

    del_option=input()

    if del_option=="Single":
        print_file_option()
        print_folder_option()

        print("Please, write your file or folder name")
        m_file=input()
        # define the name of the directory to be created
        create_path = path+'/'+m_file

        if os.path.isfile(create_path):
            try:
                os.remove(create_path)
            except OSError:
                print ("Deletion of the file %s failed" % create_path)
            else:
                print ("Successfully deleted the file %s" % create_path)
        elif os.path.isdir(create_path):
            try:  
                os.rmdir(create_path)
            except OSError:  
                print ("Deletion of the directory %s failed" % create_path)
            else:  
                print ("Successfully deleted the directory %s" % create_path)
                
        change_file_folder_option()
        
    elif del_option=="Multiple":
        print_file_option()
        print_folder_option()

        print("Please, write your file or folder name")
        m_file=input()

        create_path = path+'/'+m_file
        
        if os.path.isfile(create_path):
            try:
                os.remove(create_path)
            except OSError:
                print ("Deletion of the file %s failed" % create_path)
            else:
                print ("Successfully deleted the file %s" % create_path)
        elif os.path.isdir(create_path):
            try:  
                os.rmdir(create_path)
            except OSError:  
                print ("Deletion of the directory %s failed" % create_path)
            else:  
                print ("Successfully deleted the directory %s" % create_path)

        change_file_folder_option()
        
        while 1:
            print("If your deleting is done, write finish, else go")
            loop_control=input()

            if loop_control=="finish":
                break
            elif loop_control=="go":
                print_file_option()
                print_folder_option()

                print("Please, write your file or folder name")
                m_file=input()

                create_path = path+'/'+m_file

                if os.path.isfile(create_path):
                    try:
                        os.remove(create_path)
                    except OSError:
                        print ("Deletion of the file %s failed" % create_path)
                    else:
                        print ("Successfully deleted the file %s" % create_path)
                elif os.path.isdir(create_path):
                    try:  
                        os.rmdir(create_path)
                    except OSError:  
                        print ("Deletion of the directory %s failed" % create_path)
                    else:  
                        print ("Successfully deleted the directory %s" % create_path)

                change_file_folder_option()
                
            else:
                print("Please, write finish or go")
        
def copy_option():
    global path
    global file_list
    global all_list
    global folder_list
    print("Option")
    print("Copy file")
    print("Copy folder")
    print("Please, choose your copy option")
    
    op_choose=input()
    if op_choose=="Copy file":
        print("Option")
        print("One file")
        print("Select more")
        print("Please, select your option:")
        choice=input()
        if choice=="One file":
            print_file_option()
            
            print("Please, choose your file")
            choose_file=input()
            copy_path=path+'/'+choose_file
            print("If you want copy here write Done")
            print("Else, choose your destination using Forward or Backward")
            
            destination=input()
            while destination!="Done":
                if destination=="Forward":
                    print_option()
                    forward_option()
                elif destination=="Backward":
                    backward_option()
                else:
                    print("You made a spelling mistake, which was %s" %destination)

                print("If you want to copy here, write finish, else go")
                loop_control=input()
                if loop_control=="finish":
                    break
                elif loop_control=="go":
                    print("Choose your destination using Forward or Backward")
                    destination=input()
                else:
                    print("Print, please write finish or go")

            try:
                shutil.copy(copy_path, path)
            except IOError:
                print("Copy of the file %s failed" %choose_file)
            print("Your work is done!!!")
            
        elif choice=="Select more":
            copy_file_list=[]
            choose_file_list=[]
                
            print("Two or more file")
            print("Select all")
            op_choose=input()

            if op_choose=="Two or more file":

                print_file_option()
                
                while 1:
                    print("Please, choose your desire file")
                    choose_file=input()
                    choose_file_list.append(choose_file)
                    copy_file_list.append(path+'/'+choose_file)
                    print("If your work is done, write finish, else go")
                    loop_control=input()
                    if loop_control=="finish":
                        break
            elif op_choose=="Select all":
                i=0

                while i<len(file_list):
                    choose_file_list.append(file_list[i])
                    copy_file_list.append(path+'/'+file_list[i])
                    i=i+1
                print("Sucessfully choose all")
                
            print("If you want copy here write Done")
            print("Else, choose your destination using Forward or Backward")
            
            destination=input()
            while destination!="Done":
                if destination=="Forward":
                    print_option()
                    forward_option()
                elif destination=="Backward":
                    backward_option()
                else:
                    print("You made a spelling mistake, which was %s" %destination)

                print("If you want to copy here, write finish, else go")
                loop_control=input()
                if loop_control=="finish":
                    break
                elif loop_control=="go":
                    print("Choose your destination using Forward or Backward")
                    destination=input()
                else:
                    print("Print, please write finish or go")

            i=0
            while i<len(copy_file_list):
                try:
                    shutil.copy(copy_file_list[i], path)
                except IOError:
                    print("Copy of the file %s failed" %choose_file_list[i])
                i=i+1
                #print(i)
            print("Your work is done!!!")
        else:
            print("You choose a wrong option, which was  %s" %choice)
                
            
    elif op_choose=="Copy folder":
        print("Option")
        print("One folder")
        print("Select more")
        print("Please, select your option:")
        choice=input()
        if choice=="One folder":
            print_folder_option()
            
            print("Please, choose your folder")
            choose_folder=input()
            copy_path=path+'/'+choose_folder
            print("If you want copy here write Done")
            print("Else, choose your destination using Forward or Backward")
            
            destination=input()
            while destination!="Done":
                if destination=="Forward":
                    print_option()
                    forward_option()
                elif destination=="Backward":
                    backward_option()
                else:
                    print("You made a spelling mistake, which was %s" %destination)

                print("If you want to copy here, write finish, else go")
                loop_control=input()
                if loop_control=="finish":
                    break
                elif loop_control=="go":
                    print("Choose your destination using Forward or Backward")
                    destination=input()
                else:
                    print("Print, please write finish or go")

            try:
                shutil.copytree(copy_path, path+'/'+choose_folder)
            except IOError:
                print("Copy of the folder %s failed" %choose_folder)
            print("Your work is done!!!")
        elif choice=="Select more":
            copy_folder_list=[]
            choose_folder_list=[]
            
            print("Two or more folder")
            print("Select all")
            op_choose=input()

            if op_choose=="Two or more folder":
                print_folder_option()

                while 1:
                    print("Please, choose your desire folder")
                    choose_folder=input()
                    choose_folder_list.append(choose_folder)
                    copy_folder_list.append(path+'/'+choose_folder)
                    print("If your work is done, write finish, else go")
                    loop_control=input()
                    if loop_control=="finish":
                        break
            elif op_choose=="Select all":
                i=0
                print("Path")
                
                while i<len(folder_list):
                    #print("In loop ", folder_list[i])
                    choose_folder_list.append(folder_list[i])
                    copy_folder_list.append(path+'/'+folder_list[i])
                    i=i+1
                print("Sucessfully choose all")

            print("If you want copy here write Done")
            print("Else, choose your destination using Forward or Backward")
            
            destination=input()
            while destination!="Done":
                if destination=="Forward":
                    print_option()
                    forward_option()
                elif destination=="Backward":
                    backward_option()
                else:
                    print("You made a spelling mistake, which was %s" %destination)

                print("If you want to copy here, write finish, else go")
                loop_control=input()
                if loop_control=="finish":
                    break
                elif loop_control=="go":
                    print("Choose your destination using Forward or Backward")
                    destination=input()
                else:
                    print("Print, please write finish or go")

            i=0
            
            while i<len(copy_folder_list):
                try:
                    shutil.copytree(copy_folder_list[i], path+'/'+choose_folder_list[i])
                except IOError:
                    print("Copy of the folder %s failed" %choose_folder_list[i])
                i=i+1
            print("Your work is done!!!")
        else:
            print("You choose a wrong option, which was  %s" %choice)
            
    else:
        print("You choose a wrong option, which was  %s" %op_choose)

    change_file_folder_option()


def cut_option():
    global path
    global file_list
    global all_list
    global folder_list

    print("Option")
    print("Cut file")
    print("Cut folder")
    print("Please, choose your cut option")
    
    op_choose=input()

    if op_choose=="Cut file":
        print("Option")
        print("One file")
        print("Select more")
        print("Please, select your option:")
        choice=input()
        if choice=="One file":
            print_file_option()
            
            print("Please, choose your cut file")
            choose_file=input()
            cut_path=path+'/'+choose_file

            print("If you want copy here write done")
            print("Else, choose your destination using Forward or Backward")
            
            destination=input()
            while destination!="Done":
                if destination=="Forward":
                    print_option()
                    forward_option()
                elif destination=="Backward":
                    backward_option()
                else:
                    print("You made a spelling mistake, which was %s" %destination)

                print("If you want to copy here, write finish, else go")
                loop_control=input()
                if loop_control=="finish":
                    break
                elif loop_control=="go":
                    print("Choose your destination using Forward or Backward")
                    destination=input()
                else:
                    print("Print, please write finish or go")

            try:
                shutil.move(cut_path, path)
            except IOError:
                print("Copy of the file %s failed" %choose_file)
            print("Your work is done!!!")
            
        elif choice=="Select more":
            cut_file_list=[]
            choose_file_list=[]
            print("Two or more file")
            print("Select all")
            op_choose=input()

            if op_choose=="Two or more file":
                print_file_option()

                while 1:
                    print("Please, choose your desire cut file")
                    choose_file=input()
                    choose_file_list.append(choose_file)
                    cut_file_list.append(path+'/'+choose_file)
                    print("If your work is done, write finish, else go")
                    loop_control=input()
                    if loop_control=="finish":
                        break
            elif op_choose=="Select all":
                i=0

                while i<len(file_list):
                    print(file_list[i])
                    choose_file_list.append(file_list[i])
                    cut_file_list.append(path+'/'+file_list[i])
                    i=i+1
                print("Sucessfully choose all")

        
            print("If you want copy here write done")
            print("Else, choose your destination using Forward or Backward")
            
            destination=input()
            while destination!="Done":
                if destination=="Forward":
                    print_option()
                    forward_option()
                elif destination=="Backward":
                    backward_option()
                else:
                    print("You made a spelling mistake, which was %s" %destination)

                print("If you want to copy here, write finish, else go")
                loop_control=input()
                if loop_control=="finish":
                    break
                elif loop_control=="go":
                    print("Choose your destination using Forward or Backward")
                    destination=input()
                else:
                    print("Print, please write finish or go")
            
            i=0
            while i<len(cut_file_list):
                try:
                    shutil.move(cut_file_list[i], path)
                except IOError:
                    print("Cut of the file %s failed" %choose_file_list[i])
                i=i+1
            print("Your work is done!!!")
        else:
            print("You choose a wrong option, which was  %s" %choice)
    
    elif op_choose=="Cut folder":
        print("Option")
        print("One folder")
        print("Select more")
        print("Please, select your option:")
        choice=input()
        if choice=="One folder":
            print_folder_option()
            
            print("Please, choose your cut folder")
            choose_folder=input()
            cut_path=path+'/'+choose_folder
            print("If you want copy here write done")
            print("Else, choose your destination using Forward or Backward")
            
            destination=input()
            while destination!="Done":
                if destination=="Forward":
                    print_option()
                    forward_option()
                elif destination=="Backward":
                    backward_option()
                else:
                    print("You made a spelling mistake, which was %s" %destination)

                print("If you want to copy here, write finish, else go")
                loop_control=input()
                if loop_control=="finish":
                    break
                elif loop_control=="go":
                    print("Choose your destination using Forward or Backward")
                    destination=input()
                else:
                    print("Print, please write finish or go")

            try:
                shutil.move(cut_path, path)
            except IOError:
                print("Copy of the folder %s failed" %choose_folder)
            print("Your work is done!!!")
        elif choice=="Select more":
            cut_folder_list=[]
            choose_folder_list=[]
            
            print("Two or more folder")
            print("Select all")
            op_choose=input()

            if op_choose=="Two or more folder":
                print_folder_option()
                
                while 1:
                    print("Please, choose your desire folder")
                    choose_folder=input()
                    choose_folder_list.append(choose_folder)
                    cut_folder_list.append(path+'/'+choose_folder)
                    print("If your work is done, write finish, else go")
                    loop_control=input()
                    if loop_control=="finish":
                        break
            elif op_choose=="Select all":
                i=0

                while i<len(folder_list):
                    choose_folder_list.append(folder_list[i])
                    cut_folder_list.append(path+'/'+folder_list[i])
                    i=i+1
                print("Sucessfully choose all")

            print("If you want copy here write done")
            print("Else, choose your destination using Forward or Backward")
            
            destination=input()
            while destination!="Done":
                if destination=="Forward":
                    print_option()
                    forward_option()
                elif destination=="Backward":
                    backward_option()
                else:
                    print("You made a spelling mistake, which was %s" %destination)

                print("If you want to copy here, write finish, else go")
                loop_control=input()
                if loop_control=="finish":
                    break
                elif loop_control=="go":
                    print("Choose your destination using Forward or Backward")
                    destination=input()
                else:
                    print("Print, please write finish or go")

            i=0
            
            while i<len(cut_folder_list):
                try:
                    shutil.move(cut_folder_list[i], path)
                except IOError:
                    print("Cut of the folder %s failed" %choose_folder_list[i])
                i=i+1
            print("Your work is done!!!")
        else:
            print("You choose a wrong option, which was  %s" %choice)

    else:
        print("You choose a wrong option, which was  %s" %op_choose)

    change_file_folder_option()

def view_style_option():
    global path
    global file_list
    global all_list
    global folder_list

    print("View style option")
    #print("Option")
    print("Time")
    print("Size")
    print("Albatical")
    print("Extension")
    print("Random")

    print("Please, choose your view style option")
    choice=input()

    if choice=="Time":
        file_pairs=[]
        folder_pairs=[]

        print("Order option")
        print("Ascending")
        print("Descending")
        print("Please, choose your order:")
        order_choose=input()
        
        if order_choose=="Ascending" or order_choose=="Descending":
            for file in file_list:
                location=os.path.join(path, file)
                ttime=os.path.getmtime(location)
                #l_time=time.ctime(ttime)
                file_pairs.append((file, ttime))

            for file in folder_list:
                location=os.path.join(path, file)
                ttime=os.path.getmtime(location)
                #l_time=time.ctime(ttime)
                folder_pairs.append((file, ttime))
                
            if order_choose=="Ascending":
                file_pairs.sort(key=lambda s:s[1])
                folder_pairs.sort(key=lambda s:s[1])
            elif order_choose=="Descending":
                file_pairs.sort(key=lambda s:s[1], reverse=True)
                folder_pairs.sort(key=lambda s:s[1], reverse=True)
        
            style_file_pairs=[]
            style_folder_pairs=[]
            i=0
            while i<len(file_pairs):
                #pairs[i][0]=time.ctime(pairs[i][0])
                #print(pairs[i][0])
                a=time.ctime(file_pairs[i][1])
                style_file_pairs.append((file_pairs[i][0], a))
                i+=1

            i=0
            while i<len(folder_pairs):
                a=time.ctime(folder_pairs[i][1])
                style_folder_pairs.append((folder_pairs[i][0], a))
                i+=1

            print("\n")
            print("File list:")
            for pair in style_file_pairs:
                print(pair)

            print("\n")
            print("Folder list:")

            for pair in style_folder_pairs:
                print(pair)
        else:
            print("You do a spelling mistake, which was %s" %order_choose)

    elif choice=="Size":
        file_pairs=[]
        folder_pairs=[]

        print("Order option")
        print("Ascending")
        print("Descending")
        print("Please, choose your order:")
        order_choose=input()
        
        if order_choose=="Ascending" or order_choose=="Descending":
            for file in file_list:
                location=os.path.join(path, file)
                ttime=os.path.getsize(location)
                #l_time=time.ctime(ttime)
                file_pairs.append((file, ttime))

            for it in folder_list:
                location=os.path.join(path, it)
                ttime=os.path.getsize(location)
                #l_time=time.ctime(ttime)
                folder_pairs.append((it, ttime))
                
            if order_choose=="Ascending":
                file_pairs.sort(key=lambda s:s[1])
                folder_pairs.sort(key=lambda s:s[1])
            elif order_choose=="Descending":
                file_pairs.sort(key=lambda s:s[1], reverse=True)
                folder_pairs.sort(key=lambda s:s[1], reverse=True)
        

            print("\n")
            print("File list:")
            for pair in file_pairs:
                print(pair)

            print("\n")
            print("Folder list:")

            for pair in folder_pairs:
                print(pair)
        else:
            print("You do a spelling mistake, which was %s" %order_choose)

    elif choice=="Extension":
        style_file_list=file_list
        style_file_list.sort(key = lambda f: os.path.splitext(f)[1])

        print("\n")
        print("File list:")
        for item in style_file_list:
                print(item)

        print("\n")
        print("Folder list:")

        for pair in folder_list:
                print(pair)

    elif choice=="Albatical":
        print("Order option")
        print("Ascending")
        print("Descending")
        print("Please, choose your order:")
        order_choose=input()

        if order_choose=="Ascending" or order_choose=="Descending":
            if order_choose=="Ascending":
                print("\nFile list")
                for i in file_list:
                    print(i)
                    
                print("\nFolder list:")
                for i in folder_list:
                    print(i)
            else:
                style_file_list=file_list
                style_file_list.sort(reverse=True)

                print("\nFile list")
                for i in style_file_list:
                    print(i)

                style_folder_list=folder_list
                style_folder_list.sort(reverse=True)
                print("\nFolder list:")
                for i in style_folder_list:
                    print(i)
        else:
            print("You do a spelling mistake, which was %s" %order_choose)
    elif choice=="Random":
        print("Please, choose your file extension such as .txt, .py etc or Folder:")
        op_choose=input()
        if op_choose=="Folder":
            if len(folder_list)==0:
                print("There is no folder in this directory")
            else:
                print("Folder list:")
                for i in folder_list:
                    print(i)
                print("\n")
        else:
            style_file_list=[]
            for file in file_list:
                if fnmatch.fnmatch(file, '*'+op_choose):
                    style_file_list.append(file)

            if len(style_file_list)==0:
                print("There is no kind of file in this directory")
            else:
                print("File list")
                for item in style_file_list:
                    print(item)
                print("\n")
    else:
        print("Choose a wrong option, which was %s" %choice)
    
    """
    practice:::
    list=os.listdir(path)

    pairs=[]

    #for file in  list:
        location=os.path.join(path, file)
        size=os.path.getsize(location)
        pairs.append((size, file))
    
    pairs.sort(key=lambda s:s[0])

    for pair in pairs:
        print(pair)

    files=glob.glob('/*txt')
    files=glob.glob(path+'/*.txt')
    #files.sort(key=os.path.getmtime)
    #print("\n".join(files))"""
    """for file in files:
        print(file)

    item='.txt'
    for item in file_list:
        print(item)
    print("Something happend")

    for file in files:
        print(file)
    
    for file in file_list:
        if fnmatch.fnmatch(file, '*.txt'):
            print(file)

    file_list.sort(key = lambda f: os.path.splitext(f)[1])

    for item in file_list:
        print(item)"""
    #print("Something happend")

def search_option():
    global path
    print_path_option()

    print("You can search here")
    print("Please, write your search file, folder, extension name:")
    
    search_op=input()
    
    matches = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, '*'+search_op):
            matches.append(os.path.join(root, filename))

    outputList = []
    for root, dirs, files in os.walk(path):
        for d in dirs:
            if d.upper() == search_op.upper():
                outputList.append(os.path.join(root, d))
        #for d in files:
         #   if d.upper() == search_op.upper():
          #      outputList.append(os.path.join(root, d))

    if len(matches)==0 and len(outputList)==0:
        print("Nothing found in this directory")
    else:
        if len(matches)>0:
            print("Search results:")
            for item in matches:
                print(item)
        else:
            print("Search results:")
            for item in outputList:
                print(item)

def text_file_edit_option():
    global path
    
    print("This is a extra feature of this system")
    print("In this feature, you can make new txt file")
    print("You can also read, write and change data of your desire text file")

    print_file_option()

    print("Option")
    print("Making new txt file in this directory, write 1")
    print("Just read the file, write 2")
    print("Delete everything and write something, write 3")
    print("Delete nothing and write after these data, write 4")

    print("Please, write here your choice number for your desire working:")
    num_choose=input()

    if num_choose=="1":
        print("Please, write your txt file name")
        file_name=input()

        with open(path+'/'+file_name+'.txt', 'w') as my_file:
            content=my_file.write("")
        print("Your work is done!!!")

    elif num_choose=="2":
        print("Please, write your desire txt file name from above file list:")
        txt_file=input()
        
        try:
            with open(path+'/'+txt_file, 'r') as my_file:
                content=my_file.read()
                print(content)
        except FileNotFoundError:
            print("There is no such kind of txt file")
            
    elif num_choose=="3":
        print("Please, write your desire txt file name from above file list:")
        txt_file=input()
    
        try:
            with open(path+'/'+txt_file, 'r') as my_file:
                content=my_file.read()
                print(content)
        except FileNotFoundError:
            print("There is no such kind of txt file")
        
        print("Suceesfully delete every data. Now, write something what you want to write")
        write=input()

        with open(path+'/'+txt_file, 'w') as write_file:
            write_file.write(write)

    elif num_choose=="4":
        print("Please, write your desire txt file name from above file list:")
        txt_file=input()
        
        try:
            with open(path+'/'+txt_file, 'r') as my_file:
                content=my_file.read()
                print(content)
        except FileNotFoundError:
            print("There is no such kind of txt file")
            
        print("Now, write something what you want write after above data")
        write=input()
        
        with open(txt_file, 'a') as ss_file:
            ss_file.write(write)

    else:
        print("You mistake something, correctly write your number")

    change_file_folder_option()
        
path=""

file_list=[]
all_list=[]
folder_list=[]
drives=[]

background_option()
greating_option()

while 1:
    #turtle.ontimer(greating_option(), 1000000)
    print("Welcome to new file management system")
    start_time=server_time()
    print("Home")
    print("Exit")

    print("Please, choose Home for entry or Exit for out of this system")
    c_option=input()

    if c_option=="Home":
        drives = [ chr(x) + ":" for x in range(65,90) if os.path.exists(chr(x) + ":") ]

        print("Drives:")
        i=0

        while i<len(drives):
            print(drives[i])
            i+=1

        print("\n\n")

        path=""
        file_list=[]
        all_list=[]
        folder_list=[]

        print("Please, choose your drive:")
        selection=str(input())
            
        path=selection+":\\"

        #print(path)

        #print(os.listdir)

        #print(os.listdir(path))

        all_list=os.listdir(path)

        with os.scandir(path) as it:
            for entry in it:
                if not entry.name.startswith('.') and entry.is_file():
                    #print(entry.name)
                    file_list.append(entry.name)

        folder_list=list(filter_list(all_list, file_list))

        print("In ", selection, " drives:")

        i=0

        print("File list:")
        while i<len(file_list):
            print(file_list[i])
            i=i+1

        print("\n\n")

        i=0
            
        print("Folder list:")
        while i<len(folder_list):
            print(folder_list[i])
            i=i+1

        print("\n\n")

        while 1:
            print("Option")
            print("Location")
            print("Forward")
            print("Backward")
            print("Copy")
            print("Cut")
            print("View style")
            print("Search")
            print("New file or folder")
            print("Rename file or folder")
            print("Delete file or folder")
            print("Text file editor")
            print("Home")

            print("Please, choose your option")

            option=input()

            if option=="Location":
                print_path_option()
            elif option=="Forward":
                forward_option()
            elif option=="Backward":
                backward_option()
            elif option=="Copy":
                copy_option()
            elif option=="Cut":
                cut_option()
            elif option=="View style":
                view_style_option()
            elif option=="Search":
                search_option()
            elif option=="New file or folder":
                new_option()
            elif option=="Rename file or folder":
                rename_option()
            elif option=="Delete file or folder":
                delete_option()
            elif option=="Text file editor":
                text_file_edit_option()
            elif option=="Home":
                break
            else:
                print("Please, choose a valid option")

    elif c_option=="Exit":
        print("Thank you for usisg this file management system")
        end_time=server_time()
        print("The spend time of using this system is:")
        print(end_time-start_time)
        c_path=os.getcwd()
        print("The system is running from ")
        print(c_path)
        print("this place")
        #background_option()
        ending_option()
        break
    else:
        print("Please, correctly write your option")
