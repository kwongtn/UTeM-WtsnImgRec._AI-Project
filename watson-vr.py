import sys, os, string, json
from ibm_watson import VisualRecognitionV3

def line():
    print("=====================================================================================================================")

def space(fname):
    i = 0
    while i < fname:
        print() 
        i += 1

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

url = "https://gateway.watsonplatform.net/visual-recognition/api"

# Authentication
blockPrint()
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    iam_apikey='{insert-your-api-key-here}'
)

enablePrint()
print("Before we start, please make sure that you are connected to the internet.")
b = 1
while b > 0:
    path = input("Path to image? (Local file) : ")
    blockPrint()
    # Classify image
    with open(path, 'rb') as images_file:
        classes = visual_recognition.classify(
            images_file,
            threshold='0.0',
        classifier_ids='default').get_result()
    enablePrint()


    space(10)
    line()
    space(1)
    print("->> IBM Watson recognizes a " + classes["images"][0]["classifiers"][0]["classes"][0]["class"] + " from the image with a " + str(round(classes["images"][0]["classifiers"][0]["classes"][0]["score"] * 100, 5)) + "%" + " confidence.")
    space(2)
    line()
    print("| ",'{:^28}'.format("Recognized Object"), "|", '{:>20}'.format("Confidence  |"), '{:<60}'.format("  Object Hierarchy"),"|")
    line()
    y = 0
    for x in classes["images"][0]["classifiers"][0]["classes"] :
        print("|", end="")
        print('{:>30}'.format(classes["images"][0]["classifiers"][0]["classes"][y]["class"]),"|", '{:>20}'.format(str(round(classes["images"][0]["classifiers"][0]["classes"][y]["score"] * 100, 5)) + " %" + " |"), '  ', end='')
        if "type_hierarchy" in classes["images"][0]["classifiers"][0]["classes"][y] :
            print('{:<59}'.format(classes["images"][0]["classifiers"][0]["classes"][y]["type_hierarchy"]), end="")
            print("|")
        else:
            print('{:>60}'.format(" |"))
        y += 1
    line()
    space(2)
    print("For more details, please visit https://cloud.ibm.com/apidocs/visual-recognition .")
    print("Program created by KwongTN.")

    space(2)

    os.system("pause")