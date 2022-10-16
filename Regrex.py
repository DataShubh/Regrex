def regex(s):
  l= []
  for k in d.keys(): # # dict_keys(['orders', 'errors'])
    for i in range(len(d[k])):
      for n in d[k][i].values(): # dict_values([1]) dict_values([2])...
        try :
         l.append(int(n)) # to append 'n' as a int data type from dict_values
        except ValueError : # if 'n' is not a int type 
         i+=1 # move to next dict_values([ ])
        else:
          break # to get out of loop
  return(l) # retrun the final integer dictionary values     
    
