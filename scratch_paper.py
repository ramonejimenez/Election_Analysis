# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    if (ballots > winning_count) and (ballot_percentage > winning_percentage):
         winning_count = votes
         winning_percentage = ballot_percentage
         county_with_the_most_votes = county