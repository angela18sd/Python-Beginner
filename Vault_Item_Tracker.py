import sys
class Item:
    def __init__(self,name,category,value):
        if not name:
            raise ValueError("Name cannot be blank")
        if not category:
            raise ValueError("Category cannot be blank")
        if value<0:
            raise ValueError("Value cannot be negative") 
        self.name=name
        self.category=category
        self.value=value
    def __str__(self):
        return f"{self.name}({self.category}) - {self.value} gold"
    def appraise(self,multiplier):
        try:
            appraisal=self.value*multiplier
            if multiplier<0:
                raise ValueError("Invalid multiplier")
        except ValueError:
                sys.exit
        return appraisal
    def is_expensive(self):
            return(self.value>=1000)
def main():                   
        print("---WELCOME TO THE VAULT ITEM TRACKER")      
        name=input("Enter item name:").strip()
        category=input("Enter item category (Weapon/Potion/Armor):").strip()
        value=int(input("Enter item gold value:"))
        try:
            item=Item(name,category,value)     #triggers __init__
            print("Item created successfully")
            print(item)
            print(f"Value of item appraised 1.2 times:{item.appraise(1.2)}")
         
            if item.is_expensive():
                print("High valued treasure!")
            else:
                print("Standard item...")
        except ValueError as e:
             print(f"Program failed:{e}")
if __name__=="__main__":
     main()

