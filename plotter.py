import os

class Plotter():
    global pionts, s
    s = ()
    pionts = []
    def setSize(self ,x, y):
        global s
        s = (y, x)
        
    
    def addPiont(self, pos, marker="⁜"):
        
        """
        addes a piont to be displayed on the grid
        SYNTAX:
        pos is a tuple first is x second y
        marker is the char to be dsiplayed on the grid
        dont set this to nothing
        """
        """
        try:
            os.system("cls")
        except:
            os.sytem("clear")
        """
        print(f"piont set: {pos}")
        pionts.append([pos, marker])
        
    def Draw(self):
        xi, yi = 0, 0
        for x in range(s[0]):
            xi += 1
            if s[1] > 100:
                if xi < 10:
                    print(f"{xi}  |",end="")
                elif xi < 100:
                    print(f"{xi} |", end="")
                    
            if s[1] > 1000:
                print("sorry but this program probably wont work right if the x value is greater then 999\nand any ways is your screeen really that big?!")
            elif s[1] > 10:
                if xi < 10:
                    print(f"{xi} |",end="")
                else:
                    print(f"{xi}|", end="")
            elif s[1] < 10:
                print(f"{xi}|", end="")
                    
                
            
            for y in range(s[1]):
                yi += 1
                piont = False
                for z in pionts:
                    if z[0][0] == xi:
                        if z[0][1] == yi:
                            if piont == False:
                                print(z[1], end="")
                                piont = True
                
                if xi == 1:
                    print("¬", end="")
                elif piont == False:
                    print(" ", end="")
            yi = 0
            print("|")
        
            




# same stuff as in the tutrial in the readme
# except foo is renamed grid here so it looks better

if __name__ == "__main__":
    grid = Plotter()
    grid.setSize(20, 10)
    grid.addPiont((5,10), marker='+')
    grid.Draw()
