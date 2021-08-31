# Main Requirements
Code to take TypeForm Google sheet feedback, rank requests, and create calendar of volunteer schedule

I am basically the events director for my day job. And right now I am working on creating a booth volunteering schedule that will:

- Ensure we have at least 4 people at the booth at all times (based on prior years expectation of attendees)
- Everyone will have the best opportunity to attend sessions that interest them most (whether for professional or personal reasons)

Instead of trying to relearn Excel, why not create a quick program that will do the heavy lifting for me? Plus, it’s code I can reuse in the future and/or for teaching others cool programming hacks for everyday life.


## Base Needs

### Input

Google Sheets doc with several columns. The 3 main columns we’ll need to focus on are the:

- Day of event (1 - 3)
- Name
- Ranked list of preferred sessions (where the first 5 are expected to be ranked accurately) and are comma delimited

Expecting a file in CSV or XLSX with the session information for easy import. Need to review, but anticipating the following information from said file:

- Speaker names (comma delim)
- Session titles
- Date
- Time (Start / End)
- Duration - should be able to pull from start/end math

### Output

#### Need To Know
1. How can I create a schedule to be able to look at any date and time to see if it’s taken up by some session?
2. Who had the most interest in having attendees?
3. What date/day & time are the preferred sessions?
4. Who could be available at that time for booth duty?
5. Is there ever a time that we don’t have enough people for a shift?
6. Who is available when?
7. Who is not available? (i.e. they are volunteering)

## Nice To Have (More Complexity)

TBD

# Resources Needed

- [Scheduling package](https://www.freecodecamp.org/news/introducing-timeboard-a-python-business-calendar-package-a2335898c697/) - may not be what is needed
- Github (See [Hello World](https://guides.github.com/activities/hello-world/) guide)
- Python
- Pandas
- XLSXWriter + ??? (xld)
- Google Sheet + TypeForm

# Timelines

TBD

==========================================

# Classes Needed

1. User
- Name
- RankedSessions - Linked list of Session objects based on the user’s feedback from TypeForm

2. Report - Perhaps just a class of functions for reporting/planning?

3. Session
- Date
- Time (Start/End)
- Session Title
- Speaker(s) - comma delimiter
- Description (optional)
- User List:  Who ranked at what ranking - need to cluster names together if same rank or be able to tell that easily somehow

4. Calendar stuff

# Functions Needed

## Read in input files

1. read in what
- The session data (Google sheet)
- The TypeForm file (CSV/XLSX)
 
2. Do what with the data
- Create a new Session object for each session
- Created a ranked list of sessions (per day) to see who had the most interest by people

## Additional calculations or planning

- Create a schedule with the top X sessions per day (default is 5)
- Print the data (?)
- Mark on some schedule when people will be “out” and see if we can just create a schedule from that
