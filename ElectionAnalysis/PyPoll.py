#  Data needed to retrieve
import csv
from functools import total_ordering
import os



# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote Counter
total_votes = 0

winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Candidate Options
candidate_options = []

# Declare the empy dictionary
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load,) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    for row in file_reader:
        # Add to toal vote count.
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:    
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name, vote count, and percentage of votes.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Detrimine winning vote count and candidate
        # Determine if trhe votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
# Print out the winning candidate, vote count, and percentage to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
# Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
