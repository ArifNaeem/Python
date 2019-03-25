def maze_manual ():
 maze=[ ['2','0','1','0','0','0','1'],['1','0','1','0','1','0','1'],['1','0','1','0','1','0','1'],['1','0','1','0','1','0','1'],['1','0','0','0','1','0','0']]

 print("MAZE:")
 for elements in maze:
   for sub_element in elements:
       print(sub_element,end=" ")
   print()

 reached=0
 row=0
 column=0
 while reached==0:
    print("Note:\n0=path\n1=wall")
    movement=input("INPUT DIRECTIONS LEFT/RIGHT/UO/DOWN:")
    if movement=="right"or movement=="left" or movement=="up" or movement=="down":
     if movement=="right":
         if maze[row][column+1]=="0":
           maze[row][column]="0"
           maze[row][column+1]="2"
           column+=1
         else:
              print("wall,you can not go there!!!") 
         print("MAZE:")
         for elements in maze:
              for sub_element in elements:
                  print(sub_element,end=" ")
              print()     
     if movement=="left":
         if maze[row][column-1]=="0":
           maze[row][column]="0"
           maze[row][column-1]="2"
           column-=1
         else:
              print("wall,you can not go there!!!") 
         print("MAZE:")
         for elements in maze:
              for sub_element in elements:
                  print(sub_element,end=" ")
              print()
     if movement=="up":
         if maze[row-1][column]=="0":
           maze[row][column]="0"
           maze[row-1][column]="2"
           row-=1
         else:
              print("wall,you can not go there!!!") 
         print("MAZE:")
         for elements in maze:
              for sub_element in elements:
                  print(sub_element,end=" ")
              print()                        
     if movement=="down":
         if maze[row+1][column]=="0":
           maze[row][column]="0"
           maze[row+1][column]="2"
           row+=1
         else:
              print("wall,you can not go there!!!") 
         print("MAZE:")
         for elements in maze:
              for sub_element in elements:
                  print(sub_element,end=" ")
              print() 
     if row==4 and column==6:  
         print('!!----------------YOU WON-------------------------!!') 
         break               
    else:
    
      print("\n\nINPUT IS INVALID PLEASE INPUT VALID DIRECTION\n\n")          

##        note:  maze game funtion is use to call game...
