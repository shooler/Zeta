def Sort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue
    
def dSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]<currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue
     
 #----------------------------------------------------------                         

def main():
    f = open('info.txt', 'r')
    filedata = f.read()
    f.close
    print  "\n\n\n\n\n\n\n\n##########-Help-##########\n\n",\
           "Type any of these commands\n",\
           "bag - show your inventory",\
           "help - print this dialog\n",\
           "go 'direction' - move to new location\n",\
           "go back - return to last location\n",\
           "pickup 'item' - pick up item at current location\n",\
           "sort 'ascending / descending - list items at current location\n",\
           "drop item - drop an item from your inventory\n",\
           "\n##########-Help-##########\n\n\n\n\n\n\n\n"
         
    inventory = []
    currentloc = 'Clearing'
    prevloc = 'Clearing'
    
    with open('info.txt', 'r') as f:
            locations = []
            description = []
            rel_dir = []
            items = []
            lines = [e.strip() for e in f.readlines()]
                    
            line = 0;
            while line != len(lines):
                if lines[line].startswith('//'):
                    line += 1
                    continue
                if '_' in lines[line]:
                    x = lines[line]
                    x = x.replace('_','')
                    locations.append(x)
                    description.append(lines[line+1])
                if '*' in lines[line]:
                    line = line + 1
                    directions_pre = {}
                    while not '*' in lines[line]:
                        key, value = lines[line].split(' : ')
                        directions_pre[key] = value
                        line = line + 1
                    rel_dir.append(directions_pre)              
                if '#' in lines[line]:
                    line = line + 1
                    pre_it = []
                    while not '#' in lines[line]:
                        pre_it.append(lines[line])
                        line = line + 1
                    items.append(pre_it)
                line += 1
                
            locanddesc = dict(zip(locations, description))
            directions = dict(zip(locations, rel_dir))
            item_loc = dict(zip(locations, items))

    while True:
        
 #----------------------------------------------------------         
 
        print("\n---" + currentloc + "---\n")
        print(locanddesc[currentloc] + "\n")
        store = raw_input("Enter a Command: ").strip()
        store = store.split()
        if len(store) == 0:
            print ("\nNo input given\n")
            continue        
            
 #----------------------------------------------------------   
 
        command = store[0].lower()
        if command == 'sort':
            if store[1].lower() == 'ascending':
                listb = item_loc[currentloc]
                #listb = sorted(lista)
                #if you want to use insertion sort
                Sort(listb)
                print "\n"
                for line in listb:
                    print (line)       
                print "\n"
                continue
                    
            if store[1].lower() == 'descending':
                listb = item_loc[currentloc]
                #listb = sorted(lista, reverse = True)
                #if you want to use insertion sort
                dSort(listb)
                print "\n"
                for line in listb:
                    print (line)                  
                print "\n"
                continue
                
        if command == 'bag':
            for item in inventory:
                print item
            continue
            
        if command == 'help':
            print  "\n\n\n\n##########-Help-##########\n\n",\
                   "Type any of these commands\n",\
                   "help - print this dialog\n",\
                   "bag - show your inventory",\
                   "go 'direction' - move to new location\n",\
                   "go back - return to last location\n",\
                   "pickup 'item' - pick up item at current location\n",\
                   "sort 'ascending / descending - list items at current location\n",\
                   "drop item - drop an item from your inventory\n",\
                   "\n##########-Help-##########\n\n\n\n\n\n\n\n"
            continue
                   
        if command == 'go':
            if len(store) == 1:
                print ("\nGo where?")
                continue
            if store[1].lower() == 'back':
                currentloc = prevloc
            if len(store) > 2:
                print("\nToo many inputs")
                continue
            if store[1].lower() in directions[currentloc]:
                prevloc = currentloc
                currentloc = directions[currentloc][store[1].lower()]
        elif command == 'pickup':
            if len(store)==1:
                print("\nPick up what?")
                continue
            if len(store) > 2:
                print("\nToo many inputs")
                continue
            if store[1].lower() in inventory:
                print("\nYou don't see a " + store[1] + " anywhere.")
            if store[1].lower() in item_loc[currentloc]:
                inventory.append(store[1])
                item_loc[currentloc].remove(store[1].lower())
                print("\nYou picked up " + store[1])   
        elif command == 'drop':
            if len(store)==1:
                print("\nDrop up what?")
                continue
            if len(store) > 2:
                print("\nToo many inputs")
                continue
            if store[1].lower() in inventory:
                print("\nYou drop " + store[1])
                inventory.remove(store[1])
                item_loc[currentloc].append(store[1])
        elif command == 'quit':
            return
        elif command == 'save':
            save_name = raw_input("Enter a name to save as: ")
            print("\nSaving your progress...\n")
            # f = open('info.txt', 'w')
            # f.write(filedata)
            # f.close()
            
        elif command == 'look':
            print(locanddesc[currentloc])
            print "\nItems:\n"
            lista = item_loc[currentloc]
            for items in lista:
                print (items)
        else:
            print("\nInvalid\n")
main()