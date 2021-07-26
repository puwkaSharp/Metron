import sys
import os
import argparse
from tkinter import Tk    
from tkinter.filedialog import askopenfilename

def main():

    # input path
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default='FROM_EXPLORER', help="Input file to format")
    args = parser.parse_args()
    inputPath = args.input
    
    if inputPath == 'FROM_EXPLORER':
        Tk().withdraw()
        inputPath = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        print(inputPath.replace("/", "\\"))
        if not inputPath:
            print("Файл не выбран! Завершение работы")
            sys.exit()
    
    print("Выбран файл:", inputPath.replace(os.getcwd(), ""))
        
    # folders check
    rawFolderExists = os.path.exists('raw')
    formattedFolderExists  = os.path.exists('formatted')

    if rawFolderExists and formattedFolderExists:
        print("Папки raw и formatted обнаружены")
    elif not formattedFolderExists:
        print("Папка formatted не обнаружена, создание папки")
        os.mkdir("formatted")
    elif not rawFolderExists:
            print("Папка raw не обнаружена. Завершение работы")
            sys.exit()
    else:
        print("Ошибка. Завершение работы")
        sys.exit()

    # reading raw rule text
    f = open(inputPath, "r")
    ruleText = f.read()
    f.close

    # calculating formatted rule text
    newRuleText = ruleText.replace("\n ", "\n").replace(" \n", "\n").replace("\n", " ").replace("  ", " ")

    # output path
    outputPath = inputPath.replace("raw", "formatted")
    #print("Путь был:", inputPath)
    #print("А стал:", outputPath)
    #print("Домашняя папка:", os.getcwd())

    # creating folders
    outputPathExists = os.path.exists(outputPath)
    if not outputPathExists:
        base = os.getcwd()
        papki = os.path.split(outputPath)[0].replace(os.getcwd(), "")
                    
        spisok = papki.split("\\")
        spisok.remove("")

        i = 0
        while i < len(spisok):
            if not os.path.exists(base + "\\" + spisok[i]):
                os.mkdir(base + "\\" + spisok[i])
                print("Создана папка:", os.path.relpath(base) + "\\" + spisok[i])
            base = base + "\\" +  spisok[i]
            i += 1
        
    # writing formatted rule text
    f = open(outputPath, 'w')
    f.write(newRuleText)
    f.close

    print("Файл \"", outputPath.replace(os.getcwd(), ""), "\" создан")

if __name__ == "__main__":
    main() 
