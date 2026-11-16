## Introduction
Bumle Business uses a VPN connection to access the company's servers. The company has identified suspicious activity and needs a way to inspect server log data to help identify and investigate potentially unwanted activity.

This project is a Python/Pycharm based log-analyzer. Its only purpose is to read the supplied **cyber_security_log_sample.txt** file, which then proceeds to log the entries, present statistics, searches, make tables and graphs through a menu-driven interface within the terminal.

## Features
**-** Event statistics: This feature counts how often each event type occurs.\
**-** Log level statistics: This feature counts the occurrences of each log level, this is levels such as *INFO*, *WARN*, and *ALERT*\
**-** IP statistics: This feature counts the warnings and alerts, ordered by their total number of log entries.\
**-** Graphs: This feature display charts for event types, log levels and warnings and alerts per ip.\
**-** Log table: This feature is within the graphs, however this show a table with every entry, and for each and all level, time, user, message and etc, basically everything within the supplied log_sample file.\
**-** Search: This feature allows the user to search log entries by username, source IP address, status or a time interval.\

## Installation and usage
### Requirements
**-** Matplotlib\
**-** Numpy\
**-** Plotly\
*All these can be downloaded once you start the script the first time.*

### Run the code: *Bumle Business_kode.py*
A menu will start within your terminal, select the feature you want to try out.

**Menu options**
**1** Event Statistics\
**2** Log Level Statistics\
**3** IP statistics\
**4** Graphs\
**5** Search by user, IP address, status, or time interval\
**0** Exit Program\

*Note: Number **0** can at all times be used to either exit or go back within the menu.*

## Project Structure
We have chosen to divide every model of the project into their own small python codes, this allowed us to work on separate tasks, and for easy troubleshooting.

# Files
**Bumle Business_kode.py** Main menu and navigation between features

**cyber_security_log_sample.txt** Sample log data used by the program

**log_reader.py** Loads and processes raw log entries and calculates statistics

**event_stats.py** Displays event statistics

**level_stats.py** Displays log level statistics

**ip_stats.py** Displays warnings and alerts per source IP address

**graphs.py** Creates charts, the scatter plot, and the log table

**search.py** Searches logs by user, IP address, status, and time interval

## Scrum

The project was organized using SCRUM and carried out in one Sprint
named **VPN-logovervågning**.

### User Stories
A User Story describes a feature from the perspective of the person who
needs it. It normally explains who needs the feature, what they need,
and why they need it.

The Sprint backlog included these user needs -
Example on a backlog:

**-** As an IT administrator, I want to load the log file so I can analyze the data.

### Tasks
Tasks are the smaller development activities needed to complete a User
Story. The team added tasks to the backlog and worked on them during the
Sprint.
Examples of tasks from the Sprint included:

**-** Open `cyber_security_log_sample.txt` and read it line by line.


### Acceptance Criteria
Acceptance criteria define the conditions that must be met before a User
Story can be considered complete.

For example, the User Story about loading the log file can have these
acceptance criteria:

**-** The program can open the supplied log file.
**-** The program reads the file line by line.
**-** The log entries are processed into a structure that can be used by the other program modules.

For the statistics User Stories, the program must count the relevant
entries and display the results. For search functionality, the user must
be able to select a search type and receive matching log entries or a
message when no entries match.

Acceptance criteria make it possible to check whether the delivered
functionality meets the intended requirement.


### Task Board
The Task Board was used to organize the backlog and follow the status of
the work. It contained the columns **Backlog item**, **To do**, **In
progress**, **Testing**, and **Done**.


## Conclusion
The project provides a menu-driven tool for loading, processing,
searching, and presenting the supplied VPN log data. It gives the user
an overview of event types and log levels, highlights warnings and
alerts associated with source IP addresses, and makes it possible to
inspect log entries through searches and a table.

The project is divided into separate Python modules, and the SCRUM Task
Board was used to track the work during the Sprint.

Possible future improvements include adding more robust file and input
error handling, improving the scatter-plot analysis to investigate
relationships between two meaningful numerical log attributes, and
adding further filtering and reporting options.
