# GenCodePack 

## Architecture du projet

- GenCodePack
    - GenCode
        - GenCode in Python with all options (CMD)
            - Lite Version with Tkinter
        - GenCodeWeb (Flask)
            - GenCodeWeb with encryption
            - GenCodeWeb without encryption
    - GardeCode
        - GardeCode in Python (CMD)
          - GardeCodeWeb (Flask)


<br><br>

---

To ensure everything works correctly, you need to:

    $ pip install cryptography
    $ pip install pyperclip
    $ pip install flask


If you have a standard Python 3 installation, you only need to install **cryptography**, **pyperclip** and **flask**. Of course, you also need to install [Python](python.org/downloads/).

This set of programs allows you to generate, save, and manage your passwords, as well as their identifiers and sources. It can be used with a Python IDE. GenCode is the most complete version, the Lite version provides a Tkinter GUI, and the Web version is a locally hosted version thanks to Flask. GardeCode allows you to manage your passwords and to find a password based on an identifier or a website. The version is not yet complete and not yet introduced with Flask.

---

## Tutorials for each service :

<u>Pour GenCode (les versions python)</u>

  - Install Python and the pip function
  - Install the necessary modules using ```pip install requirements.txt```
  - Double click on the program, if there are no issues, everything should be displayed in the command prompt. For the Lite version, it will be a graphical interface.

<u>Pour GenCode (les version web) </u>

  - Install Python and the pip function
  - Install the necessary modules using ```pip install requirements.txt```
  - Double click on the program, and the website will open automatically. If it doesn't open, click on the IP (127.0.0.1:5000/) written in the CMD.

<u>Pour GardeCode (version python)</u>

  - Install Python and the pip function
  - Install the necessary modules using ```pip install requirements.txt```
  - Double click on the program, and a CMD window will open for the program. 

<u>Pour GardeCode (version web)</u>
  - Install Python and the pip function
  - Install the necessary modules using ```pip install requirements.txt```
  - Double click on the program, and the website will open automatically. If it doesn't open, click on the IP (127.0.0.1:5000/) written in the CMD.
---

## Bugs :
- The Python versions may have some issues, but after several tests, there shouldn't be any problems. However, the web version is more stable. No issues have been reported.


---
## Things to know:


  - To avoid any issues and not lose your passwords, do not delete the key.key file or the password file.
  - For everything to work correctly, the key and the files must match. Normally, the organization of the GitHub files should not cause any problems.
  <br>
  - If you are not familiar with the field of computer science, I recommend using GenCodeWeb without encryption if it is not necessary. The program guarantees your data, but the decryption key is stored on the computer, so there is a possibility of someone accessing all the data.


---
## Credits :

Made 100% by Adrien Pichon, some functions have been corrected by ChatGPT 3 from OpenIA. The beginning of the project dates back to 10/22.

---
## Future features :

The next step is to be able to put everything on a web page, manage codes...
* [ ] Migrate 100% online with servers... (someday if I have the skills)


