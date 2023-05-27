# FINRA-shortsale-data
These are two short, automated scripts for collecting and aggregating all of FINRA's short sale data. The finished dataset is around 1.7GB in size and contains every ticker's daily short sale volume from August 1 2009 to May 19 2023 inclusive, with the ability to incorporate more recent data if needed. Each ticker's daily short sale volume contains all short sales listed under the NYSE TRF, the NASDAQ/Chicago TRF, NASDAQ/Carteret TRF, Over-the-counter Reporting Facilities, and the FINRA Alternative Display Facility. This script provides access to large amounts of historical and recent data which would be impossible to get via FINRA's API, which places strict limits on its usage.

The Automated FINRA data downloader takes a while to run, so a machine with good specs is preferred. Run the data downloader first and then run the data aggregator.

This project was made in collaboration with Dr. Jenny Zha Giedt of the George Washington School of Business.
