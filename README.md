# Datapao_Takehometest
This repository contains analytics and insights derived from provided data regarding employee office attendance.

## Project Overview

The goal is to generate some analytics from the provided data:

1. **Office Attendance Analysis**
   - Calculate each employee's time and days spent in the office during February.
   - Write the analysis to a CSV file with fields: user_id, time, days, average_per_day, rank.

2. **Longest Work Session Analysis**
   - Identify the employee with the longest work session in February.
   - Write the analysis to a CSV file with fields: user_id, session_length.

3. **Insights**
   - Visualize employee attendance analysis in Analytics_chart.png file.
   - Synthesis providing context to visualized data and recommendations.
     
### Requirements

- **Language:** Python
- **Libraries:** Only Python Standard Library
- **Output Files:** Include in the repository
  - /output/first.csv (user_id, time, days, average_per_day, rank)
  - /output/second.csv (user_id, session_length)

### Instructions

#### Setup

1. **Clone this Repository**

    ```bash
    git clone <git url>
    ```
2. Navigate to the project directory:

    ```bash
    cd Datapao_Takehometest
    ```
## Execution

 Run the main script:

    ```bash
    python3 Office_sess_analytics.py
    ```

## Output

Upon successful execution, the program generates two output CSV files:

- `/output/first.csv`: Contains user-wise analytics (user_id, time, days, average_per_day, rank).
- `/output/second.csv`: Lists the user with the longest work session and the session length.

 ## Testing
- To test if the application passes all requirements and handles edge cases such as an empty dataset, run:
  ```
  python3 test.py
  ```
