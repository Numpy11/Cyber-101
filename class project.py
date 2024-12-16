def main():
    clean_lists = make_lists()
    print(clean_lists)
    search = search_lists(clean_lists)
    name = name_lookup_prompt(clean_lists)
    party = party_lookup_prompt(clean_lists)
    state = state_lookup_prompt(clean_lists)
    vote = vote_lookup_prompt(clean_lists)
    print("Vote: " + vote)


def make_lists():
    with open("senate1.csv", "r") as f:  # opening senate1 file into program as "f"
        senlist = f.readlines()  # reading it into a list
    print(senlist[:5])  # printing it to see if it works (great success!)
    with open("congress.csv", "r") as e:  # opening congress' into program as "e"
        conglist = e.readlines()
    print(conglist[:5])  # same as senlist
    size_s = len(senlist)  # getting length of list and putting it in a box
    print(size_s)  # printing the box's content
    size_c = len(conglist)  # Ditto
    print(size_c)  # Ditto**2
    combined_list = [  # Im going to start reformatting senlist into the same format as conglist (conglist is better)
        [
            part.strip()
            for part in row.replace("(", ",")
            .replace(")", ",")
            .replace("-", ",")
            .split(",")
            if part.strip()
        ]
        for row in senlist + conglist
        if row.strip()
        and row.strip()
        != "DATA\n"  # This is my way of removing the old senlist's header from the new list
    ]
    headers = ["Name", "Party", "State", "Vote"]

    combined_list.insert(
        0, headers
    )  # this inserts the new headers into the list in case we want to save it to a file

    print(combined_list)
    return combined_list, conglist


def name_lookup_prompt(data):
    name = input("Please enter a representative's name: ").strip()
    results = [row for row in data if name in row[0]]
    if results:
        print("Results for name: " + name)
        for result in results:
            print(result)
    else:
        print("No results found for name: " + name)

    return results


def party_lookup_prompt(data):
    party = input("please enter an established party's name: ").strip()
    results = [row for row in data if party in row[1]]
    if results:
        print("Results for party: ")
    return results


def state_lookup_prompt(data):
    state = input("Please enter the name of the state in question: ").strip()
    results = [row for row in data if state in row[2]]
    if results:
        print("Results for party: ")
    return state


def vote_lookup_prompt(data):
    vote = input('Please enter either "Yay" or "Nay": ').strip()
    results = [row for row in data if vote in row[3]]
    if results:
        print("Results for vote: ")
    return vote


def search_lists(data):
    ui = ""
    print(
        "*** This is a program intended to allow the user to assess relevant statistics\n"
        "Of The 2002 vote to declare war on Iraq\n"
        "Users may search based on the following criteria: name, party, state, vote ***\n"
        "Or enter "
        '"q" to quit'
    )
    while ui != "q":
        done = False
        ui = input("Please enter which criteria you would like to search based upon: ")

        if ui == "name":
            name_lookup_prompt(data)
        elif ui == "party":
            party_lookup_prompt(data)
        elif ui == "state":
            state_lookup_prompt(data)
        elif ui == "vote":
            vote_lookup_prompt(data)
        elif ui.lower() == "q":
            done = True

    return ui


if __name__ == "__main__":
    main()
