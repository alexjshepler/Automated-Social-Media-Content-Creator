[![GitHub issues](https://img.shields.io/github/issues/alexjshepler/Epoch-industry?label=%22bugs%22%20more%20like%20Features&style=for-the-badge)](https://github.com/alexjshepler/Epoch-industry/issues) [![GitHub forks](https://img.shields.io/github/forks/alexjshepler/epoch-industry?style=for-the-badge)](https://github.com/alexjshepler/epoch-industry/network) [![GitHub stars](https://img.shields.io/github/stars/alexjshepler/epoch-industry?style=for-the-badge)](https://github.com/alexjshepler/epoch-industry/stargazers) [![GitHub license](https://img.shields.io/github/license/alexjshepler/epoch-industry?style=for-the-badge)](https://github.com/alexjshepler/Epoch-Industry/blob/master/LICENSE) 

> PLEASE NOTE: This is not this is not a representation of my professional work. This is a personal project that I work on in my own free time. My professional work does not include profanity and contains more legible and professional commit messages and comments

# Media "Manager"

This project is a proof of concept. It is designed to be able to generate content and automatically post it. This is meant for educational purposes only because I am like 99% sure that this violates every single terms of service agreements for every form of social media. The capabilities outlined here only describes the first version. I do intend on making more versions that are more advanced.

## Installation

Clone the [repo](https://github.com/alexjshepler/Epoch-Industry)

```
git clone https://github.com/alexjshepler/Epoch-Industry
```

cd into the repo

```
cd Epoch-Industry
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all of the files in the [requirements.txt](requirements.txt) file

```
pip install -r requirements.txt
```

## Usage

### Running the program

Before you can run the program you must add video, audio, and quotes that it can use.

Once all of the files are added you can run

```
py main.py
```

### Adding files for the program

Before you can run the program there are several files that you need to import. You are going to need a video, audio, and text file

The **video** files are going to need to be either in `.mp4` `.mvk` or `.m4v` format. This will be the video that the program clips from. You can place the videos in the [original video](Assets/Videos/Original) directory. Note, when the program is done with the video, it appends the `.old` filetype to the end and does not delete it. If you would like to save space you will need to delete it. This might be changed later.

The **audio** files are going to need to be in `.mp3` format. This will be the audio that gets overlaid on the videos that get rendered. You can place them in the [audio](Assets/Audio) directory. Note, these get reused unlike the videos or quotes so these won't get the `.old` file type appended to the end and should not be deleted unless required.

The **text** file for the quotes has already been created. The only thing that has to be done is to add the quotes to the [quote](Assets/Quotes/quotes.txt) file. You do not need to worry about duplicates because the program checks for them. However if there is any difference (ie punctuation change, capitalization, etc) it will assume they are different and use both quotes.

## Contributing

Pull requests are welcome and encouraged. When making one however, please make sure to outline what you've done and USE COMMENTS. Please, please, please comment your code. I cannot read your mind and when I go over your code I want to be able to understand what the code does and how it works without having to step through every single line to see what it does. And if you don't know what something does in your code, try to figure it out or comment it. There are bits like that in mine, I won't be too harsh.


![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/alexjshepler/epoch-industry?label=thiccness&style=for-the-badge) ![GitHub repo file count](https://img.shields.io/github/directory-file-count/alexjshepler/epoch-industry?style=for-the-badge) ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/alexjshepler/epoch-industry?style=for-the-badge)