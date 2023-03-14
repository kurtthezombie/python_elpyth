class Player():
    def __init__(self, userid:str, username:str, accstatus:str):
        self.userid = userid
        self.username = username
        self.accstatus = accstatus

    def __eq__(self, username)->bool:
        return self.username == username
    
    def __str__(self)->str:
        return f"{self.userid} {self.username} {self.accstatus}"

def displaymenu():
    print("=====================")
    print("ComShop Top-Up System")
    print("=====================")



def main():
     displaymenu()

if __name__ == "__main__":
    main()