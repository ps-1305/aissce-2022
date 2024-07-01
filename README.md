# ▶️prashant-srivastav-1305/aissce-2022
Hospital management system (GUI version) <br>
A computer science project for: 
All India Senior Secondary Certificate Examination - 2022
<br>

```
Modules used:
1. mysql-connector-python [SQL related operations]
2. datetime [Displaying date & time on bill] 
3. tkinter [Creating a GUI]
```

```
Code files:
login_screen.py : The initial login interface
app.py : Main app
backend.py : SQL activites happen here 
```

```
Image resources used:
icon.ico : icon
main_logo.png : logo to be displayed in login screen
```

```
Updates: 
07.01.2022 == (0.1.0)
- login screen added - main interface added - addPatient() command added 

09.01.2022 == (0.2.0)
- login screen updated - main interface functions added - getInfo() - 
updatePatient() - updatePatient_search() - admit() - showAll() - 
font updated for the whole program - GUI improved

17.01.2022 == (0.2.1)
- added comments to [app.py] and [backend.py]

22.01.2022 == (0.3.0)
- selective searching added - a new window for selective search now 
implemented - comments updated - diagnosis variable changed to ward 

23.01.2022 == (0.4.0)
- added discharge patient through two new commands - discharge() and 
billing() - comments updated - GUI improved - billing system implemented
- the bill is now saved in a .txt file in the ../bills directory - also 
some quality of life changes 

03.02.2022 == (0.4.1)
- removed unused code and unneccessary comments - added comments to 
[login_screen.py] - tweaked the bill's structure and added days to it
- also tweaked the login interface by adding a new statement

14.02.2022 == (1.0.0)
- first release - improved graphics and ui - fixed bug of discharge
command having error when u close it among others - cleaned the 
code and also made it more readable - new tabular interface and scrollbar
- icons changed for the whole application - error codes added - new bill design
```

![Photos](https://github.com/prashant-srivastav-1305/aissce-2022/blob/main/screenshots/screenshots-1.png)
![Photos](https://github.com/prashant-srivastav-1305/aissce-2022/blob/main/screenshots/screenshots-2.png)
![Photos](https://github.com/prashant-srivastav-1305/aissce-2022/blob/main/screenshots/screenshots-3.png)

```
Future:
- No. of available wards
- Save the bill in pdf form at your desired location
- Improve the bill design further
- Add an about page
- Add administrator functionality to the 'admin' account
```

```
MIT License
Copyright (c) 2022 Prashant Srivastav
*COMPLETE LICENSE AT add-license-1 BRANCH*
```
