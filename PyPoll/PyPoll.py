import csv
import os

# Define file paths
input_file = os.path.join("PyPoll", "Resources", "election_data.csv")
output_file = os.path.join("PyPoll", "Resources", "election_analysis.txt")

# Initialize variables
total_votes = 0
candidate_options = []
candidate_votes = {}
winner = ""
winning_votes = 0

# Read and process CSV data
with open(input_file, "r") as election_data:
    reader = csv.reader(election_data)
    header = next(reader)  # Skip header row

    for row in reader:
        # Count total votes
        total_votes += 1

        # Track candidate votes
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

        # Determine winner (optimized logic)
        current_votes = candidate_votes[candidate_name]
        if current_votes > winning_votes:
            winning_votes = current_votes
            winner = candidate_name

# Open output file in write mode
with open(output_file, "w") as txt_file:
    # Election results header
    election_results = (
        "\n\nElection Results\n"
        "-------------------------------\n"
        f"Total Votes: {total_votes}\n"
        "--------------------------------\n"
    )
    txt_file.write(election_results)

    # Individual candidate results
    for candidate, votes in candidate_votes.items():
        vote_percentage = (votes / total_votes) * 100
        candidate_summary = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        txt_file.write(candidate_summary)

    # Winner analysis
    winner_analysis = (
        "\n--------------------------\n"
        f"Winner: {winner}\n"
        "---------------------------\n"
    )
    txt_file.write(winner_analysis)

print("Election analysis saved to:", output_file)


