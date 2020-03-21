
import pandas as pd
import numpy as np

# format of passwd file:
# username:password:uid:groupid:userid_info:Home_directory:command/shell

def dataOfPasswd(passwdpath = "/etc/passwd"):
    allUsersData = [[]]
    with open(passwdpath) as file:
        for line in file:
            if line.startswith('#'):
                continue
            else:
                x = line.split(":")
                allUsersData.append([x[0], x[2], x[4]])
    
    df = pd.DataFrame(allUsersData, columns=['username', 'uid', 'fullname'])
    return df


# format of group file:
# groupname:password:groupid:group_list

def dataOfGroups(grouppath = "/etc/group"):
    allGroupsData = [[]]
    with open(grouppath) as file:
        for line in file:
            if line.startswith('#'):
                continue
            else:
                x = line.split(":")
                allGroupsData.append([x[0], x[3]])
                
    df = pd.DataFrame(allGroupsData, columns=['username', 'groups'])
    return df


dfpaswd = dataOfPasswd()
dfpaswd['username'].nunique()
dfpaswd=dfpaswd[1:]

dfgroups = dataOfGroups()
dfgroups['username'].nunique()
dfgroups=dfgroups[1:]

finaldf=dfpaswd.merge(dfgroups, on = 'username', how='inner')


finaldf['groups'] = finaldf['groups'].apply(lambda x:str(x).strip().split(","))


finaldf.index=finaldf['username']

finaldf=finaldf.drop(columns=['username'])


jsonOutput = finaldf.to_json(orient='index')
print(jsonOutput)



