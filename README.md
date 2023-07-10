
# TrafficViolation - Dashboard

This project, developed during the Data Viking event, aims to provide valuable insights into traffic violations by extracting and analyzing data from the Brazilian government website.

[Data Viking Event](https://lnkd.in/dbJm4Utf)

## Project Enhancements

Some enhancements have been made to the original codebase:

-   **Expanded Data**: In addition to retrieving and analyzing existing data, the project now includes data from the year 2023 as well.
-   **Spark Integration**: Spark has been incorporated into the data processing pipeline, enabling more efficient data analysis and manipulation.
-   **Additional Analyses**: Some new analysis modules have been added to the project, providing a broader range of insights and visualizations.

## Repository Structure

-   The `.ipynb` file contains the Jupyter Notebook, which includes both exploratory analyses and the ETL (Extract, Transform, Load) process. The ETL process generates data files in the gold layer format, which are utilized in the dashboard analysis.
-   The `app` directory contains the dashboard application (which will consume those files).

## How to Run the Project

To run the project, follow these steps:

1.  Set up a virtual environment for the project.
2.  Install the necessary requirements using pip. You can find the required packages listed in the requirements.txt file.
`
$ pip install -r /path/to/requirements.txt
`

4.  Execute the application by running the appropriate command.
`$ python app.py` 

Make sure to adjust the command as needed based on your operating system and setup.
