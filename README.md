# Salary Analysis of Software Engineers in Bangladesh

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
2. **Data Cleaning**: Processing and cleaning raw data on Google Colab.
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

### Data Processing & Cleaning

Data processing and cleaning are handled using **Pandas** and **NumPy** in Google Colab, with the following tasks:
- Handling missing or malformed data.
- Transforming salary strings into numerical values (lower, upper, and median).
- Standardizing the format for salary ranges.
- Calculating monthly salary values for yearly recorded entries.

### Data Visualization

Once processed, the data is visualized in **Tableau**. The dashboard offers a collection of visualizations that provide:
- Comparison of median salary benchmarks.
- Industry leaders in median salary, salary range, and company ratings.
- Understand correlations between company ratings and salaries.
- Compare salaries across multiple companies in Bangladesh.

## Project Insights

- **Industry Benchmarks**: The analysis reveals that the **average median salary** for software engineers across companies in Bangladesh stands at **BDT 48K**. Among the **top 10 highest-paying companies**, this figure rises significantly to **BDT 86K**. However, the **top 10 highest-rated companies** offer a lower average median salary of **BDT 63K**, representing a **27% reduction**.

- **Median Salary Distribution**: A majority (**63%**) of median salaries fall within the **BDT 30K to BDT 60K** range, demonstrating a strong concentration of companies offering compensation in this bracket. The overall salary distribution is **right-skewed**, with a few top software engineers earning significantly higher than their peers.

- **Correlation Between Company Ratings & Median Salaries**: While there is a **positive correlation** between company ratings and median salaries, the data indicates that several high-paying companies have received ratings below **4.0**. This suggests that although compensation is competitive, other factors affecting employee satisfaction, such as work-life balance or corporate culture, may be less favorable at these organizations.

- **Top Employers**: **CodeCrafters**, **Welcome Software**, **Cefalo**, and **Binate Solutions** stand out as **top employers**, as they appear in both the **Top 10 Companies by Median Salary** and the **Top 10 Companies by Ratings** lists. These organizations are not only offering competitive compensation but also maintaining strong overall employee satisfaction.
  
The full visual analysis can be accessed in the Tableau dashboard linked above.

## Limitations

- Glassdoor entries frequently lack detailed information on years of experience, resulting in incomplete data sets that may hinder accurate analysis.
- Job titles can vary significantly across companies, which limits the comprehensive representation of roles within the Glassdoor listings.
- Potential bias may arise from the varying likelihood of employees at different companies to report their salaries on Glassdoor, affecting the reliability of the data.

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
