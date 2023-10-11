from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/", methods=["GET"])
def indexPage():
    return render_template("index.html")

@app.route("/a/<album>", methods=["POST", "GET"])
def questionPage(album):
    albumLine =  FindAlbumLine(album)
    dictOfAnswers = FindQuestionsAtAlbumLine(albumLine)
    return render_template("something.html", data=dictOfAnswers, album=album)

def FindQuestionsAtAlbumLine(line):
    with open("questions.txt", "r") as questionsTXT:
        questionsTXTSplitted = questionsTXT.read().split("\n")

        questions = [[f"{questionsTXTSplitted[line]}".split("text=")[1], line], [f"{questionsTXTSplitted[line+4]}".split("text=")[1], line+4]]
        questionChosen = random.choice(questions)
        lineForQuestion = questionChosen[1]
        print(questions)
        allAnswersToQuestion = [questionsTXTSplitted[lineForQuestion + 1].split("=")[1], questionsTXTSplitted[lineForQuestion + 2].split("=")[1], questionsTXTSplitted[lineForQuestion + 3].split("=")[1]]


    
        response = {"q":questionChosen, "answers": [allAnswersToQuestion]}
        return response





def FindAlbumLine(album):
    with open("questions.txt", "r") as questionsTXT:
        amountsLinesWentThry = 0
        for line in questionsTXT.read().split("\n"):
            amountsLinesWentThry += 1
            if line.startswith("a="):
                albumThereIs = line.split("a=")[1]
                if albumThereIs == album:
                    return amountsLinesWentThry
    


if __name__ == "__main__":
    app.run(host="localhost", port=5000)