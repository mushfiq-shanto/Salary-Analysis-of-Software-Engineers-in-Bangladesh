# Salary Analysis of Software Engineers in Bangladesh Tech Companies

This repository hosts the full pipeline for scraping, processing, analyzing, and visualizing salary data of software engineers working in Bangladesh. The goal is to provide actionable insights for both employers and professionals by leveraging data from Glassdoor.

## Project Overview

This project focuses on analyzing salary data of software engineers in Bangladesh, obtained through Glassdoor. It aims to:
- **Help Tech Companies**: Optimize recruitment strategies, refine compensation plans, and improve employer branding based on competitive analysis.
- **Guide Software Engineers**: Provide early-career professionals with insights into competitive salary benchmarks, enabling informed career decisions.

The final output is an interactive Tableau dashboard that visualizes salary insights. You can explore the dashboard here:
[**Tableau Public: BD Software Engineer Salary Dashboard**](https://public.tableau.com/views/TableauDashboard_17272858139270/BDSoftwareEngineerSalaryDashboard?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## Key Features
- **Comprehensive Salary Data**: Extracted from Glassdoor for software engineers across multiple companies in Bangladesh.
- **Industry Insights**: Interactive visualizations for salary trends, company ratings, and compensation ranges.
- **Data Processing Pipeline**: Automated data cleaning and transformation for further analysis.
- **Correlation Analysis**: Insightful correlations between company ratings and salary levels.

## Project Workflow

The project follows a well-structured data pipeline:
1. **Web Scraping**: Collecting salary data from Glassdoor using a Python script.
2. **Data Cleaning**: Processing and cleaning raw data using Google Colab.
3. **Visualization**: Presenting the cleaned data using Tableau to create an interactive dashboard.

## Data Source

- **Glassdoor**: Software Engineer Salaries in Bangladesh.
  [Glassdoor Bangladesh - Software Engineer Salaries](https://www.glassdoor.com/Salaries/software-engineer-salary-SRCH_IM1237_KO0,17.htm)
  
### Data Fields Scraped
- **Company Name**
- **Company Rating**
- **Salary Range**: Lower, Upper, Median
- **Number of Salary Entries**

## Data Pipeline

### Web Scraping

The web scraper is built using Python's **Selenium** library to extract salary information from Glassdoor. It collects data for various companies, including the range of salaries offered and the overall rating of each company.

The scraper can be customized to include other roles or geographies if needed.

### Data Cleaning & Processing

Data cleaning is handled using **Pandas** and **NumPy** in Google Colab, with the following tasks:
- Handling missing or malformed data.
- Parsing salary strings into numerical values (lower, upper, and median).
- Standardizing the format for salary ranges.
- Calculating additional metrics like average salary and salary distribution.

### Data Visualization

Once processed, the data is visualized in **Tableau**. The dashboard offers an interactive experience where users can:
- View median salaries by company.
- Explore the range of salary offerings within each company.
- Analyze correlations between company ratings and salaries.
- Compare salaries across multiple companies in Bangladesh's tech sector.

## Project Insights

Some of the key insights derived from the project include:
- **Median Salary Distribution**: Identifies which companies lead the market in terms of compensation.
- **Salary Ranges**: Highlights companies offering wide salary ranges, indicating growth potential for employees.
- **Employer Branding Impact**: Correlates company ratings with compensation, providing insights into how salary impacts employee satisfaction.
  
The full visual analysis can be accessed in the Tableau dashboard linked above.

### Build from Source

1. **Clone the Repository**

   Clone this repository to your local machine using Git:

   ```bash
   git clone https://github.com/mushfiq-shanto/glassdoor-bangladesh-software-engineer-salaries-webscraping.git
   ```

2. **Initialize and Activate Virtual Environment (Windows)**

   Navigate to the project directory and set up a virtual environment:

   ```bash
   cd glassdoor-bangladesh-software-engineer-salaries-webscraping
   virtualenv --no-site-packages env1
   source env1/bin/activate
   ```

3. **Install Dependencies**

   Install the required packages using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

After setting up, you can run the web scraper script as per the project requirements. Make sure to activate your virtual environment each time you work with the project.

### Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
