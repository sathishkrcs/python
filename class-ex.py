print "Hello World!\n"
import re

class ipl():
    teamName = "No team name set"
    def __init__(self):
        self.teamName = "Team name is not set yet"
    def setTeamName(self, teamname):
        self.teamName = teamname
    def getTeamName(self):
        print(self.teamName)


ip = ipl();
#ip.setTeamName('csk');
print(ip.getTeamName());

name = "tserttzsdfasdt"

nm = re.search('(t.*t){2}', name)

if (nm):
  print("YES! We have a match!")
else:
  print("No match")

r='sat'
try:
    print(1+r)
except NameError as ve:
    print('NameError', ve)
except TypeError as ve:
    print('TypeError', ve)


t = (1,2,3,4,5,6)    

for e in t:
    print(e + 10)
