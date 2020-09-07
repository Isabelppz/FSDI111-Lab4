"""
    Program: Warehouse management system
    Functionality:
       - Repeated menu
       - Register items to the catalog
            id(auto generated)
            title
            category
            price
            stock
        -Display Catalog
        -Display items with no stock (out of stock)
        -Saving / retrieving data to/ from file
        -Update the stock of an item
            -Show the list items
            -Ask the user to choose an id
            -Ask the user for the new stock value
            -Find the item with selected id
            -Update the stock
            -Save changes
        -Print the total value of the stock (sum(price*stock))
        -Remove an Item from the Catalog
        -Register a Sale
            -Show the list of items
            -ask the user to choose an Id
            -Ask the user to provide the Qtty
            -Update the stock
        -Have a log of events
            -file name for the logs
            -a list for the log entries(list of string)
            -add_log_event function that receives an string
            -save_log
            -read_log
            -update existing functions to register log entries
        -Display the log of events
        -Display list of categories (unique categories) CR
"""
from menu import menu, clear, header
from item import Item
import datetime
import pickle

    #global vars
    catalog=[]
    last_id=0
    data_file= 'warehouse.data'
    log.file='log.data'

def save_catalog():
    global data_file
    writer = open(data_file, "wb") #create file(overwrite), open it to write binary
    pickle.dump(catalog, writer)
    writer.close()
    print("**Data Saved!!")
    # print(date_file)

def read_catalog():
    try:
        global data_file
        global last_id
        reader = open(data_file,"rb")
        temp_list= pickle.load(reader)

    for item in temp_list:
        catalog.append(item)

    last = catalog[-1]
    last_id= last.id

    how_many = len(catalog)
    print("**Loaded" + str(how_many)+ "items")
    except:
        print("**No file found, db is empty")

def save_log():
    global log_file
    writer = open(log_file, "wb")
    pickle.dump(log, writer)
    writer.close()
    print ("***Log Saved!!")

def read_log():
    try:
        global log_file
        reader = open (log_files, "rb")
        temp_list = pickle.load(reader)

        for entry in temp_list:
            log.append(entry)
            how _many=len(log)
            print("**Loaded"+ str(how_many)+ "log entries")
    except:
        print("**Error loading log entries")

#functions
def register_item():
    global last_id
    header(" Register new Item")

    title= input("New item title:    ")
    category = input ("New item category:   ")
    price= float(input ("New item price:   "))
    stock= int(input("New Item stock:    "))

    new_item = Item() #Create instances of a class (objects)
    last_id +=1
    new_item.id=last_id
    new_item.title=title
    new_item.category=category
    new_item.price=price
    new_item.stock=stock

    catalog.append(new_item)
    add_log_event("Newitem", "Added item: " + str(last_id))
    print("Item created!")

def display_catalog():
    """ clear()
    print("-" *30)
    print("Current Catalog")
    print("-" *30) """
  """   print("there are: "+ str(size) + "items") """
    size= len(catalog)
    header("Current Catalog ("+ str(size) + "items)")

    #print("-" * 70)
     print("|" +'ID'.rjust(2)
        + "|" + 'Title'.ljust(24)
        + "|" + 'Category'.ljust(15)
        + "|" + 'Price'.rjust(10)
        + "|" + 'Stock'.rjust(5)+ "|")
    print("-" * 70)

    for item in catalog:
        print("|" + str(item.id).rjust(2)
        + "|" + item.title.ljust(24)
        + "|" + item.category.ljust(15)
        + "|" + str(item.price).rjust(10)
        + "|" + str(item.stock.rjust(5)+ "|")

     print("-"*70)

def display_not_stock():
    size= len(catalog)
    header("Out of stock (" + str(size) + " items)")

    #print("-" *70)
        print("|" +'ID'.rjust(2)
        + "|" + 'Title'.ljust(24)
        + "|" + 'Category'.rjust(15)
        + "|" + 'price'.rjust(10)
        + "|" + 'Stock'.rjust(5)+ "|")
    print("-" * 70)

    for item in catalog:
        if(item.stock==0):
        print("|" + str(item.id).rjust(2)
        + "|" + item.title.ljust(24)
        + "|" + item.category.ljust(15)
        + "|" + str(item.price.rjust(10)
        + "|" + str(item.stock).rjust(5)+ "|")

    print("-" * 70)

def update_stock(opc):
    display_catalog()
    id = int(input("Please select an Id from the list: "))
   """  msg=''
    if(opc==1):
        msg= "New Stock value: "
    else:
        msg="Number of items to sale: " """
    #stock = int(input("New stock value: "))
    #find the item with id = id
    found = False
    for item in catalog:
        if(item.id==id):
            found = True
            
            if(opc==1):
                stock=int(input("New Stock value"))
                item.stock=stock
                print('Stock updated!')
                add_log_event("SetStock", "Updated stock for item:  " + str(item.id))
            else:
                sold= int(input("Number of items to sale: "))
                item.stock -= sold #(item.stock -= sold) , decrease the stock value by the number of sold items
                print('Stock registered!')
                add_log_event("Sale", "Sold" + str(sold)+ "items of item: "+ str(item.id))

    if(not found):
        print("Error : Selected Id does not exists, try again")

def calculate_stock_value():
    total= 0.0
    for item in catalog:
        total += (item.price * item.stock)

    print("Total Stock Value $"+ str(total))

def remove_item():
    display_catalog()
    id=int(input("Select the id of the item to remove: "))
    found= False
    for item in catalog:
        if(item.id==id):
            catalog.remove(item)
            found= True
            add_log_event("Remove", "Remove item: " + str(item.id))
            break

    if(found):
        print("Item from catalog")
    else:
        print("Error, selected Id it's incorrect try again!")

def add_log_event(event_type, event_description)
    entry = "12:00" + " | " + event_type.ljust(10)  + " | " + event_description
    log.append(entry)
    save_log()

def get_current_time():
    now= datetime.datetime.now()
    return now.strftime("%b/%d/%Y/ %T")

def add_log_event(event_type, event_description):
    entry = get_current_time()+ "|" + event_type.ljust(10)+ "|" + event_description
    log.append(entry)
    save_log()

def print_log():
    header("log of events")
    for entry in log:
        print(entry)

#instructions
#start menu

#first load data
    read_catalog()
    input("Press enter to continue")

    opc = ''
    while(opc !='x'):
        clear()
        menu()
        print("/n")
        opc= input("please select an option: ..")

    if(opc=='1'):
        register_item()
        save_catalog()
    elif(opc=='2'):
        display_catalog()
    elif(opc=='3'):
        display_no_stock()
    elif(opc=='4'):
        update_stock(1) #update stock
        save_catalog()
    elif(opc=='5'):
        calculate_stock_value()
    elif(opc=='6'):
        remove_item()
        save_catalog()
    elif(opc=='7'):
        update_stock(2) #register a sale
        save_catalog()
    elif(opc=='8'):
        print_log()

    input ("Press enter to continue...")