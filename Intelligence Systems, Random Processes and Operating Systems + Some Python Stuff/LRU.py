print(" \n############# ################ #################### ################\n")
print(" Name: Achintya Kamath \n Roll Number: R030 \n MBA Tech Artificial Intelligence \n Batch: B2 \n Date: 20/09/2022 \n Experiment 9 - Page Replacement")
 
def LeastUsed(page, max_paige):
    Paige_List = list()
    Used_Paige = list()

    Faults = 0

    for i in page:
        if i not in Paige_List:
            Faults +=1
            Used_Paige.append(i)

            if len(Paige_List) < max_paige:
                Paige_List.append(i)

            else:
                Paige_List.append(i)
                index = Paige_List.index(Used_Paige[0])           
                Paige_List.pop(index)               
                Used_Paige.pop(index)

        else:
            if i in Used_Paige:
                Used_Paige.pop(Used_Paige.index(i))
                Used_Paige.append(i)
            else:
                Used_Paige.append(i)               
    return Faults
  

if __name__=="__main__":
    print(f"\n\tThis program showcases the Least Recently Used Page Replacement Algorithm.", end="\n\n\t")

    Paiges = list(map(int, input('Please enter the sequence of Pages: ').strip().split()))

    print(" ", end="\n\t")

    Max_Paiges=int(input('Please enter maximum number of pages in a frame: '))

    print("\n\tThe number of Page Faults occured while implementing Least Recently Used Page Replacement are:", LeastUsed(Paiges, Max_Paiges), end="\n\n")
