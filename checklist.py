from genericpath import exists
import os

BASEDIR = "F:/Baekjoon-Python/"
print_lst = []

# Find Solved Code That Place Wrong Position
files = [f for f in os.listdir(BASEDIR + "Problem ID") if (not(os.path.isfile(os.path.join(BASEDIR + "Problem ID", f))))]
for file in files:
    start = int((file.split('~'))[0])
    codes = [f for f in os.listdir(BASEDIR + "Problem ID/" + file) if (not(os.path.isfile(os.path.join(BASEDIR + "Problem ID" + file, f))))]
    for code in codes:
        codenum = int((code.split('.'))[0])
        if(codenum < start or start + 99 < codenum):
            print_lst.append("[" + file + "] " + code + " doesn't match. Must move it")

# Find Rank and Problem ID in "RankList.txt"
solved_list = open(BASEDIR + "RankList.txt")
solved_list_lst = solved_list.read().split('----------')
solved_list_total = []
for i in solved_list_lst:
    tmp = i.strip().split('\n')

    rank_dir = BASEDIR + "Rank/" + tmp[0][1:]
    print("Find in : " + rank_dir)
    # Find In Rank Directory
    for j in tmp[1:]:
        if(not(os.path.isfile(rank_dir + "/" + j + ".py"))):
            print_lst.append("[" + tmp[0][1:] + "] " + j + " doesn't exists")

    prob_dir = BASEDIR + "Problem ID/"
    # Find In Rank Directory
    for j in tmp[1:]:
        dirname = str((int(j) // 100) * 100) + "~" + str((int(j) // 100) * 100 + 99)
        if(not(os.path.isfile(prob_dir + dirname + "/" + j + ".py"))):
            print_lst.append("[Problem ID] " + j + " doesn't exists")

# Find Rank and Problem ID in "README.md"
readme_list = open(BASEDIR + "README.md")
readme_list_lst = readme_list.read().split('\n')
readme_list_total = []
prob_lst = []
for i in readme_list_lst:
    if(i.startswith("- ")):
        prob_lst.append(i[5:-4])

for i in prob_lst:
    prob_dir = BASEDIR + "Problem ID/"
    # Find In Rank Directory
    dirname = str((int(i) // 100) * 100) + "~" + str((int(i) // 100) * 100 + 99)
    if(not(os.path.isfile(prob_dir + dirname + "/" + i + ".py"))):
        print_lst.append("[README] " + i + " doesn't exists")

# Find Wrong Problem ID in "RankList.txt" and "README.md"
exists_codes = []
files = [f for f in os.listdir(BASEDIR + "Problem ID") if (not(os.path.isfile(os.path.join(BASEDIR + "Problem ID", f))))]
for file in files:
    codes = [f for f in os.listdir(BASEDIR + "Problem ID/" + file) if (not(os.path.isfile(os.path.join(BASEDIR + "Problem ID" + file, f))))]
    for code in codes:
        exists_codes.append(code.split('.')[0])

readme_file = open(BASEDIR + "README.md").read()
for code in exists_codes:
    if(readme_file.find(code) == -1):
        print_lst.append("[In README] " + code + " doesn't exists")
    
# Print All Errors
print_lst.sort()
for _ in print_lst:
    print(_)