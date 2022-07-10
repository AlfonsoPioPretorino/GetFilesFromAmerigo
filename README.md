# GetFilesFromAmerigo

A quick and easy console application to download all your files that are stored on [Amerigo app](https://www.amerigo-app.com/).
It consists in a console-based app that it is using the "Web server" feature that is provided by Amerigo.

Through a few steps, you will be able to download or visualize all your data stored on Amerigo.


##  Available Commands

| Commands  | Description |
| ------------- |:-------------:|
| /help     | Will show inside the console the current avaiable commands with a little description.     |
| /nav {location}    | Allows to navigate inside folders in your Amerigo storage.    |
| /download {filename}     | If a filename will be not specified, the app will download all files inside that specific folder. If a filename is specified, the app will download just the specified file.     |
| /back      | Goes back with navigation (E.g: You are in ..:8080/folder/folder1. If u execute the "/back" command, you will navigate back to "..:8080/folder".    |
| /quit      | Close the app at any time during his execution.     |
### Tips and Tricks
* `/nav`: If you will not specify the folder name, it will navigate back to the "home" folder;
* `/download {filename}`: "filename" parameter could just contain some text that _**UNIQUELY**_ identify the desired file (E.g: i want to download just the IMG_123.jpg file. If i 100% sure that there isn't another file with the same "id", i can type `/download 123`, the app will download exactly the file i wanted to.

## What I will working on
1. I will implement the english "version";
1. I will implement the `/ignore` command that briefly, will allow you to ignore some files, so they will be not download.

