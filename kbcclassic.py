listofquestion = {
    "What is the capital city of Nepal?": "Kathmandu",
    "Who started to unified a Nepal's states?": "Prithivi Narayan Shah",
    "How many provinces in Nepal": "Seven",
    "Who is the first prime-minister of Nepal?":"Bhimsen Thapa",
    "In Which year, The most devastating Earthquake had happened in Nepal?": 2072,
    "Who is the light of Asia?": "Gautam Buddha"
}
sum=0
for x in listofquestion:
        print(x)
        answer= input("Enter the answer of the question:")
        if str(listofquestion[x]).lower() == answer.strip().lower():
           print("That's the correct answer, You win Rs 10,000")
           sum+=10000
        else:
           print("That's the incorrect answer, You lose Rs 5,000")
           sum=sum-5000

print("You win Rs",sum)