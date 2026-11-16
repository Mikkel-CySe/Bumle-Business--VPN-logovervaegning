## Introduction
Bumle Business uses a VPN connection to access the company's servers. The company has identified suspicious activity and needs a way to inspect server log data to help identify and investigate potentially unwanted activity.

This project is a Python/Pycharm based log-analyzer. Its only purpose is to read the supplied **cyber_security_log_sample.txt** file, which then proceeds to log the entries, present statistics, searches, make tables and graphs through a menu-driven interface within the terminal.

## Features
** - ** Event statistics: This feature counts how often each event type occurs.
** - ** Log level statistics: This feature counts the occurrences of each log level, this is levels such as *INFO*, *WARN*, and *ALERT*
** - ** IP statistics: This feature counts the warnings and alerts, ordered by their total number of log entries.
** - ** Graphs: This feature display charts for event types, log levels and warnings and alerts per ip.
** - ** Log table: This feature is within the graphs, however this show a table with every entry, and for each and all level, time, user, message and etc, basically everything within the supplied log_sample file.
** - ** Search: This feature allows the user to search log entries by username, source IP address, status or a time interval.

## Installation and usage
# Requirements
** - ** Matplotlib
** - ** Numpy
** - ** Plotly
*All these can be downloaded once you start the script the first time.*

# Run the code: *Bumle Business_kode.py*
A menu will start within your terminal, select the feature you want to try out.

**Menu options**
** 1 ** Event Statistics
** 2 ** Log Level Statistics
** 3 ** IP statistics
** 4 ** Graphs
** 5 ** Search by user, IP address, status, or time interval
** 0 ** Exit Program

*Note:* Number **0** can at all times be used to either exit or go back within the menu.

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
