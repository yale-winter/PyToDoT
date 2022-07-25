![pytodot2](https://user-images.githubusercontent.com/5803874/180697407-44c2fe00-685f-42a9-a345-3c2ac2207896.JPG)

^ custom AI created promotional artwork for pytodot

- - - - - - - - - - - - - - - - - - - - - - - - -
**pytodot: Python To-Do Tracker**
- - - - - - - - - - - - - - - - - - - - - - - - -
Create a google sheet online or use with .csv offline with the following schema:

| To-Dos | Date Assigned | Date Complete | Priority |
| --- | --- | --- | --- |
| To-do | 3.1.22 | 3.5.22 | 0 |
| To-do 2 | 3.5.22 | 3.5.22 | 1 |


**To load your live google sheet online (set so anyone with the link can view):**<br/>
Change import_online to True, and replace ___online_url___ with that part of your url<br/><br/>
**To load your offline .csv:**<br/>
Download your To-Dos as .csv (only downloading selected collumns and rows)<br/>
And name the document 'ToDos.csv' and place in the same folder<br/><br/>
**How to Use:**
- Import the package to see your to-do list and details.
- Use command pytodot.commands.find_to_do_progress() to list out to-dos
- Use command pytodot.commands.to_do(x) to see full details of to-do x
