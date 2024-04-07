import pandas as pd


# Load the data from the spreadsheet
file_path = "C:/Users/drewb/Downloads/baseball.xlsx"
data = pd.read_excel(file_path)


# Filter data for seasons before 2009
historical_data = data[data['Year'] < 2009]


# Extract relevant columns
team_data = historical_data[['Team', 'Runs Scored', 'Runs Allowed', 'Wins', 'OBP', 'SLG', 'Team Batting Average', 'Playoffs']]




# Function to predict playoffs based on team values
def predict_playoffs(team_values):
    # Use a simple heuristic based on historical data
    # You can replace this with more sophisticated models like machine learning in real-world applications
    runs_scored = team_values['Runs Scored']
    runs_allowed = team_values['Runs Allowed']
    wins = team_values['Wins']
    on_base_percentage = team_values['OBP']
    slugging_percentage = team_values['SLG']
    batting_average = team_values['Team Batting Average']


    # Simple logic for prediction
    if (runs_scored > runs_allowed) and (wins > 90) and (on_base_percentage > 0.33) and (slugging_percentage > 0.4) and (batting_average > 0.25):
        return 1
    else:
        return 0


# Iterate over teams and predict playoffs
predictions = {}
for index, row in team_data.iterrows():
    team_values = row.drop(['Team', 'Playoffs'])  # Drop team name and playoff status
    prediction = predict_playoffs(team_values)
    predictions[row['Team']] = prediction


# Check predictions against actual playoff status from 2009-2012
actual_playoffs = data[(data['Year'] >= 2009) & (data['Year'] <= 2012)][['Team', 'Playoffs']]


# Compare predictions with actual data
accuracy = 0
for index, row in actual_playoffs.iterrows():
    if row['Team'] in predictions:
        if predictions[row['Team']] == row['Playoffs']:
            accuracy += 1


# Calculate accuracy percentage
accuracy_percentage = (accuracy / len(actual_playoffs)) * 100


# Final predictions
print("Final Predictions:")
for team, prediction in predictions.items():
    print(f"{team}: {'Yes' if prediction == 1 else 'No'}")


print("\nAccuracy on historical data (2009-2012): {:.2f}%".format(accuracy_percentage))
print("Note: This is a simple heuristic model and not a sophisticated prediction algorithm.")
