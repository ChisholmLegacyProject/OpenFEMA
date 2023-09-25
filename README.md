# OpenFEMA
OpenFEMA
This repository contains the Python and R code needed to pull, process and analyze OpenFEMA Data by zip code. 

## Setup and Installation
Clone this repository:https://github.com/ChisholmLegacyProject/OpenFEMA

Create a virtual environment and activate it:

bash Copy code python3 -m venv venv source venv/bin/activate

## FEMA Flood Claims Analysis (R)
This code retrieves National Flood Insurance Program (NFIP) claims data from FEMA and extracts claims for New York State to a CSV file for analysis.

## Data Source
The data is sourced from FEMA's OpenFEMA portal using the rfema R package. Specifically the NFIP claims dataset:

Dataset: fimaNfipClaims

## Usage
The script performs the following:

Loads the rfema package Queries the NFIP claims dataset fields Filters claims to only New York State between 2010-2022 Writes the filtered dataframe to a CSV file Requirements R and RStudio rfema package (install.packages("rfema"))

## Configuration
No additional configuration required.

## Output
The filtered claims data is written to data.csv in the current working directory.

## Resources
-OpenFEMA portal: https://www.fema.gov/openfema

-rfema package: https://cran.r-project.org/web/packages/rfema/index.html

-FEMA NFIP claims dataset: https://www.fema.gov/openfema-dataset-national-flood-insurance-program-claims

## Contributing
Contributions are welcomed! Please read the CONTRIBUTING.md for the process for submitting pull requests to us.

## Contact
If you have any questions, feel free to open an issue or contact us directly.

## Additional Information
This project uses data from the FEMA Open Data Portal, but is not endorsed or funded by any government entity.
