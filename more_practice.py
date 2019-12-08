# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a ballot vote counter.
total_ballots = 0
#2.Create a list for the counties.
# Empty County list
counties = []
#3. Create a dictionary where the county is the key and the votes cast for each county in the election are the values.
# Empty dictionary where the county is the key and the votes cast
ballots_cast_in_each_county = {}
#4. Create an empty string that will hold the county name that had the largest turnout.
county_with_the_largest_voter_turnout = ""
county_with_the_most_votes = 0
the_percentage_of_all_votes_cast = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_ballots += 1
        # Print the county name from each row.
        county_name = row[1]

        if county_name not in counties:
            # Add the county name to the counties list.
            counties.append(county_name)
            #begin tracking the ballots cast in each county.
            ballots_cast_in_each_county[county_name] = 0
        # add the ballots cast to the county's count
        ballots_cast_in_each_county[county_name] += 1

election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_ballots:,}\n"
    f"-------------------------\n"
    f"\nCounty Votes:\n")
print(election_results, end="")


# Determine the percentage of ballot for each county by looping through the counts.
# 1. Iterate through the counties.
for county in ballots_cast_in_each_county:
    # 2. Retrieve vote count of a counties.
    ballots = ballots_cast_in_each_county[county]
    # 3. Calculate the percentage of ballot.
    ballot_percentage = float(ballots) / float(total_ballots) * 100
    county_election_results = (f"{county}: {ballot_percentage:.1f}% ({ballots:,})")
    
    print(f"{county_election_results}\n")
    
    if (float(ballots) > county_with_the_most_votes) and (ballot_percentage > the_percentage_of_all_votes_cast):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         county_with_the_most_votes = ballots
         the_percentage_of_all_votes_cast = ballot_percentage
         # And, set the winning_candidate equal to the candidate's name.
         county_with_the_largest_voter_turnout = county


print("---------------------------------\n")    
print(f"County with largest turnout: {county_with_the_largest_voter_turnout}\n")
print("---------------------------------")    


# Create an empty string that will hold the county name that had the largest turnout.
# This is like getting vote winner. 

# Declare a variable that represents the number of votes that a county received. 
# Hint: Inside a for loop, add an if statement to check if the county name has already been recorded. 
# If not, add it to the list of county names.

# Inside the with open() function where you are outputting the file, do the following:

# Create three if statements to print out the voter turnout results similar to the results shown above.

# Add the results to the output file.
# Print the results to the command line.