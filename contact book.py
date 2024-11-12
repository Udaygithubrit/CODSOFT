##--------PHONE DIRECTORY(Contact book)----------------##
# function for adding new contact
def add(name,phone_number,email,address):
   contact=[name,phone_number,email,address]
   contact_book.append(contact)
   print("--------Contact added successfully---------")
# function for viewing full contact book
def view():
   print(contact_book)
   print("--------Contact book viewed succeessfully------")
# function for searching any contact in contact book
def search():
   condition =False
   nme=input("Enter name whose information is to be searched:")#nme means name 
   for val in contact_book:# val is just a vaiable name to access whole contact within a contact book
      if (nme in val):
         print(val)
         condition=True
         break
   if(condition==False):
    print("------Contact is not in contact book--------")
   else:
    print("------Contact searched successfully---------")
# function for updatinng any contact in contact book
def update():
   condition =False
   nme=input("Enter name whose details are to be update:")
   for val in contact_book:
      if (nme in val):
       _name=input("Enter new name:")
       _phonenumber=int(input("Enter new phone number:"))
       _email=input("Enter new email:")
       _address=input("Enter new address:")
       val[0]=_name
       val[1]=_phonenumber
       val[2]=_email
       val[3]=_address
       condition=True
       break
   if(condition==False):
    print("------Contact is not in contact book--------")
   else:
    print("------Contact updated successfully---------") 
# function for deleting any contact in contact book
def delete():
   condition =False
   nme=input("Enter contact name whose details are to be removed:")
   for val in contact_book:
      if(nme in val):
         contact_book.remove(val)
         condition=True
         break
   if(condition==False):
    print("------Contact is not in contact book--------")
   else:
    print("------Contact deleted successfully---------")
# function for asking user what operation he/she wants to perform
def information():
  global contact_book # to access contact book globally so that contact book reamins same for all functions
  while True:
      print("Press 1->For adding new contact:")
      print("Press 2->For viewing all contacts:")
      print("Press 3->For searching any contact:")
      print("Press 4->For updating any contact:")
      print("Press 5->For deleting any contact:")
      print("Press 6->For closing contact book:")
      ch=int(input("Enter your choice:"))# Asking user what he/she wants to perform
      if(ch==1):
         nme=input("Enter name:")#nme mean sname
         pn=input("Enter phone number:")#pn means phone number
         email=input("Enter email:")
         addr=input("Enter address:")#addr means address
         add(nme,pn,email,addr) # calling add function
      elif(ch==2):
         view()# calling view function
      elif(ch==3):
         search()# calling searching function
      elif(ch==4):
         update()# calling updating function
      elif(ch==5):
         delete()# calling delete function
      elif(ch==6):
         print("---------Thank you---------")
         break
      else:
        print("Invalid input!Please try again...")
contact_book=[]# empty list which will further contain all contacts
information()


