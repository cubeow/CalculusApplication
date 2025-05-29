import random

# List of all the questions and answers
allQuestionsAndAnswers = [
    ["sin(x)", "cos(x)",],
    ["cos(x)", "-sin(x)"],
    ["-sin(x)", "-cos(x)"],
    ["-cos(x)", "sin(x)"],
    ["csc(x)", "-csc(x)cot(x)"],
    ["-csc(x)", "csc(x)cot(x)"],
    ["-tan(x)", "-sec^2(x)"],
    ["tan(x)", "sec^2(x)"],
    ["-cot(x)", "csc^2(x)"],
    ["cot(x)", "-csc^2(x)"],
    ["sec(x)", "sec(x)tan(x)"],
    ["-sec(x)", "-sec(x)tan(x)"],
    ["arcsin(x)", "1/sqrt(1-x^2)"],
    ["arccos(x)", "-1/sqrt(1-x^2)"],
    ["arctan(x)", "1/(1+x^2)"],
    ["arccot(x)", "-1/(1+x^2)"],
    ["arcsec(x)", "1/(|x|sqrt(x^2-1))"],
    ["arccsc(x)", "-1/(|x|sqrt(x^2-1))"],
    ["cos(2x)", "-2sin(2x)"],
    ["sin(2x)", "2cos(2x)"],
    ["ln(x)", "1/x"],
    ["e^x", "e^x"],
    ["sin^2(x)", "sin(2x)"],
    ["cos^2(x)", "-sin(2x)"],
    ["x^2", "2x"],
    ["x^6 + 23x^4 + 17x^2 + 1", "6x^5 + 92x^3 + 34x"],
    ["(1/4)x^4", "x^3"],
    ["ln(2x-cos2x)", "(2+2sin2x)/(2x-cos2x)"]
]


# Generates derivative/integral question and answers
def generateQuestion(questionType):
  keyVal = random.choice(allQuestionsAndAnswers)
  if questionType == "derivative":
    question = keyVal[0]
    answer = keyVal[1]
  else:
    question = keyVal[1]
    answer = keyVal[0]
  return question, answer


# Error traps for an integer input
while True:
  # Asks for number of questions generated
  numQuestionsToGenerate = input(
      "How many questions would you like generated? ")
  try:
    numQuestionsToGenerate = int(numQuestionsToGenerate)
    break
  except ValueError:
    print("That's not a valid number!")

answerList = []

# Picks an integral or derivative and prints the question
for i in range(numQuestionsToGenerate):
  questionType = random.choice(["derivative", "integral"])
  output = generateQuestion(questionType)
  print("\n" + str(i + 1) + ". What's the " + questionType + " of: " +
        str(output[0]))

  # Stores the answers
  if questionType == "derivative":
    answerList.append(output[1])
  else:
    answerList.append(output[1] + " + C")

# Generates answers upon request
askForAnswers = input("\nInput anything for the answers: ")
for index, element in enumerate(answerList):
  print("\n" + str(index + 1) + ". " + str(element))
