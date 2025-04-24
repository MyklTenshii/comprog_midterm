import os.path


users = None
fusers = None
link = r"C:\Users\Jhamai\Desktop\comp_app_midterm\doc.txt"
flink = r"C:\Users\Jhamai\Desktop\comp_app_midterm\filtered_list.txt"
if os.path.exists(link):
    users = open(link)
    fusers = open(flink, "a")
else:
    print("HELL NAH")
raw_data = []



def splitter():
    with users as namelist:
        for names in namelist:
            x = names.split()
            raw_data.append(x)
            

def stringBuild(roow):
    stri = ""
    for data in roow:
        stri += data + " "
    return stri

def filter():
    i = 0
    for row in raw_data:
         if int(row[2]) < 18:
             continue
         elif row[3] == "True":
              continue
         elif (str(row[4]) == "Active") or (str(row[4]) == "Suspended"):
              continue
         else:
             i+=1
             out = stringBuild(row)
             fusers.write(out + "\n")
             print("Filtered data has been written to filtered_users.txt\n" + "-----" + " Filtered Users Report " + "-----")
             print("Total users that meet the criteria: " + str(i))
             print(f"User ID: {int(row[0])}, Name: {row[1]}, Age: {int(row[2])}, Status: {row[4]}\n")


def main():
    splitter()
    filter()

main()