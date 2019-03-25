
def count_pattern(check,values):

          
          count=0
          i=0                    
          if len(check)!=0:
             for x in range (0,len(values)):
 
                     if values[x]==check[0]:#if first element is matched then we check other
                         flag=x
                         while i<len(check):
                               if check[i]==values[flag]:
                                     i += 1
                                     flag+=1
                               else:               
                                     break  
                         if i==len(check):
                               count += 1
                               i=0  
          return count
