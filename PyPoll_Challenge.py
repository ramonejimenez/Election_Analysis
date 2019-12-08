# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Initialize a ballot vote counter.
total_ballots = 0
counties = []
ballots_cast_in_each_county = {}
county_with_the_largest_voter_turnout = ""
county_with_the_most_votes = 0
the_percentage_of_all_votes_cast = 0


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

# with open(file_to_save, "w") as txt_file:
#     election_results = (
#         f"\nElection Results\n"
#         f"-------------------------\n"
#         f"Total Votes: {total_ballots:,}\n"
#         f"-------------------------\n"
#         f"\nCounty Votes:\n")
#     print(election_results, end="")

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


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_ballots:,}\n"
        f"-------------------------\n"
        f"County Votes:\n"
        #county results here
        f"---------------------------------\n"
        f"County with largest turnout: {county_with_the_largest_voter_turnout}\n"
        f"------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
