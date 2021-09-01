# Initial Findings

After getting feedback from booth team, pulled the data stored from TypeForm into Google Sheets doc. When prepping the data to be in a format I could import into pandas, found that the way it was saved was a CSV file. This CSV had titles with commas, which meant that any Google sheet formulas did not create clean data.

# Process to Resolve

Here is the process taken to resolve, thus allowing creation of the program.

1. I used the Google sheets formula `=TRANSPOSE(SPLIT('Sheet Name'!B2, ",", TRUE, TRUE))` to take the single cell of all the sessions ranked in order and split them into rows using commas as delimiters
2. Searched against the session titles in TypeForm to create single cells with the titles (instead of split cells if there were commas in the title) - only update top 10
3. Create [a new sheet](https://docs.google.com/spreadsheets/d/1L2a44kmtYrP8ATYbLbU1PH_9i70uj2OEbQTPuhlwSWY/edit?usp=sharing) for:
   - Create a cleaned up sheet for each day & booth personnel's top 10 sessions
   - Create a **Raw Agenda** sheet that takes each day's sessions, removes duplicates, and adds the start/end times
   - **Booth Schedule** for when ready to mark people down for volunteering

*Return to README [here](README.MD).*
