# FINRA-shortsale-data
Automated scripts for collecting and aggregating all of FINRA's short sale data. The finished dataset is around 1.7GB in size and contains every ticker's daily short sale volume from August 1 2009 to May 19 2023 inclusive, with the ability to aggregate more recent data if needed. Each ticker's daily short sale volume contains all short sales listed under the NYSE TRF, the NASDAQ/Chicago TRF, NASDAQ/Carteret TRF, Over-the-counter Reporting Facilities, and the FINRA Alternative Display Facility.

The FINRA data downloader takes around 1 hour to run. The FINRA data aggregator takes around 1.5 minutes. This dataset has potential applications in academic research and quantitative trading.
