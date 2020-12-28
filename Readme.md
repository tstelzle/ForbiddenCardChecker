# Yu-Gi-Oh Forbidden Card Checker

## Idea
This script shall help you with checking if card in your deck is forbidden.

This tool will check for german and english cards.

## Starting the script
You will need to install the python dependencies.
Therefore you will have to run the following command.

```bash
pip install -r requirements.txt
```

To run the script you will have to make a '.txt' file with the cards of your deck. Each card shoudl be in a separate line. 
Watch out for typing errors, as the script will otherwise not be able to check the card.

This file name needs to be your first parameter to the script.
If the file is not in the same directory as the script please obviously put in the whole path.

The second paramater is conditional. As the script will always save the forbidden cards into a '.csv' file it will not download the cards if this file exits.
Witht setting '-u' as a second parameter you will force it to update the forbidden cards.

### Running On Windows

On Windows open the start menu and type "cmd". Then press enter.
In the opened window type
```bash
python
```
to install to programming language on your computer.
You can check if this went succesfully with typing
```bash
 python --version
```
This should show the version which you installed.

Afterwards you have to download this code by from this page.
If you downloaded the zip file and extracted it, you can move via the command line to the appropriated folder with the command "cd". 
```bash
cd <name_of_directory>
```
If you downloaded it to your dekstop you can run:
```bash
cd Desktop\ForbiddenCardChecker-main\ForbiddenCardChecker-main
```
When you reached the directory, in which the requirements.txt is, you can run the next command to install the dependencies of the program.
```bash
pip install -r requirements.txt
```
After this everything is setup and you can run the programm, like in the examples shown below.

## Examples
```bash
python3 cmd_main.py aqua_deck.txt
```
```bash
python3 cmd_main.py main_deck.txt -u
```

## Running The Server

You can run the programm also as a website on your maching via docker.
Therefore you can just use the given docker-compose.yml to start everything.
```bash
docker-compose up -d
```
Afterwards you should be able to reach the website with "<machine_ip>:9102".
The first time it downloads the current forbidden cards, hence it takes a bit longer.
