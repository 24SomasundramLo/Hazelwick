a_votes = 0
b_votes = 0
c_votes = 0
while True:
    vote = input("Who would you like to vote for, A B or C: ")
    if vote == "END":
            break
    if vote == "A" or vote == "a":
        a_votes = a_votes + 1
    elif vote == "B" or vote == "b":
        b_votes = b_votes + 1
    elif vote == "C" or vote == "c":
        c_votes = c_votes + 1
    else:
         print("Invalid vote")
total = a_votes + b_votes + c_votes
print("There were " + str(total) + " votes in total")
print("Candidate A got " + str(a_votes) + " votes")
print("Candidate B got " + str(b_votes) + " votes")
print("Candidate C got " + str(c_votes) + " votes")