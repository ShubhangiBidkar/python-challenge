import os
import csv

# Path to collect data from the Resources folder
budget_csv =os.path.join("Resources", "election_data.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidates votes
candidate_options = []
candidate_votes = {}

# Track winning candidate, vote count, and percentage.
winning_cnadidate = ""
winning_count = 0
winning_percentage = 0

# Open and read the csv file
with open(budget_csv) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
 
 # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

 # Read each row of data after the header
    for row in csvreader:
      # Add to the total vote count.
        total_votes +=1

      #Print the candidate name
        candidate_name= row[2]
       
        # If the candidate does not match any exisiting candidate add it to the candidate list.
        if candidate_name not in candidate_options:
              # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            
            # and begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0

    # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print out each candidate's name, vote count, and percentage of votes to the terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print out the winning candidate, vote count, and percentage to terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)   