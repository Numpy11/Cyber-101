def main() -> None:
    combined_list = make_lists()
    search_lists(combined_list)
    ##name = name_lookup_prompt(combined_list)
    ##party = party_lookup_prompt(combined_list)
    ##state = state_lookup_prompt(combined_list)
    ##vote = vote_lookup_prompt(combined_list)
    ##print("Vote: " + vote)


def make_lists():
    # opening senate1 file into program as "f"
    with open("senate1.csv", "r") as f:
        # reading it into a list
        senlist = f.read().rstrip().splitlines()

    # Separate header from data
    senate_data = senlist[1:]

    ### printing it to see if it works (great success!)
    ##print(senlist[:5])

    # opening congress' into program as "e"
    with open("congress.csv", "r") as e:
        conglist = e.read().rstrip().splitlines()
    ##print(conglist[:5])  # same as senlist

    ##size_s = len(senlist)  # getting length of list and putting it in a box
    ##print(size_s)  # printing the box's content

    ##size_c = len(conglist)  # Ditto
    ##print(size_c)  # Ditto**2

    # Add congress data
    combined_list = [
        tuple(part.strip() for part in row.split(",") if part.strip())
        for row in conglist
        if row.strip()
    ]
    # Add senate data in same format ad congress data
    for line in senate_data:
        without_quotes = line[1:-1]
        name_and_party_data, vote = without_quotes.split(", ", 1)
        name, party_state_with_parens = name_and_party_data.split(" ", 1)
        party_state = party_state_with_parens[1:-1]
        party, state = party_state.split("-", 1)
        if party == "D":
            party = "Democratic"
        elif party == "R":
            party = "Republican"
        elif party == "I":
            party = "Independent"
        else:
            raise ValueError("Unhandled party type " + repr(party))
        combined_list.append((name, party, state, vote))

    return combined_list


def name_lookup_prompt(data):
    name = input("Please enter a representative's name: ").strip().lower()
    results = [row for row in data if name == row[0].lower()]
    if results:
        print("Results for name: " + name)
        for result in results:
            print(result)
    else:
        print("No results found for name: " + name)

    return results


def party_lookup_prompt(data):
    party = input("Please enter an established party's name: ").strip().lower()
    results = [row for row in data if row[1].lower() == party]
    if results:
        print("Results for party: ")
        for result in results:
            print(result)
    else:
        print("No results found for party: " + party)

    return results


def state_lookup_prompt(data):
    state = input("Please enter the name of the state in question: ").strip().lower()
    results = [row for row in data if state == row[2].lower()]
    if results:
        print("Results for state: ")
        for result in results:
            print(result)
    else:
        print("No results found for state: " + state)

    return state


def vote_lookup_prompt(data):
    vote = input('Please enter either "Yay" or "Nay": ').strip().lower()
    results = [row for row in data if vote == row[3].lower()]
    if results:
        print("Results for vote: ")
        for result in results:
            print(result)
    else:
        print("No results found for vote: " + vote)

    return vote


def search_lists(combined_list):
    ui = ""
    print(
        "*** This is a program intended to allow the user to assess relevant statistics\n"
        "Of The 2002 vote to declare war on Iraq\n"
        "Users may search based on the following criteria: name, party, state, vote ***\n"
        "Or enter "
        '"q" to quit'
    )
    done = False
    while not done:
        ui = input("Please enter which criteria you would like to search based upon: ")

        if ui == "name":
            name_lookup_prompt(combined_list)
        elif ui == "party":
            party_lookup_prompt(combined_list)
        elif ui == "state":
            state_lookup_prompt(combined_list)
        elif ui == "vote":
            vote_lookup_prompt(combined_list)
        elif ui.lower() == "q":
            done = True


if __name__ == "__main__":
    main()
