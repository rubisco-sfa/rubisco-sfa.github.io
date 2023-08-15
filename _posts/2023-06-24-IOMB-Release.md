---
layout: post
subject: "Release of the International Ocean Model Benchmarking (IOMB) configuration"
author: Nathan Collier
---

The code, datasets, and auxillary files needed to reproduce the analysis described in [Fu2022](https://doi.org/10.1029/2022JC018965) and which generated [figure 5.22](https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-5#figure-5-22) of the AR6 WG1 report (shown below) is now a supported configuration in the ILAMB codebase. You will need to update to at least `v2.7` and then use the following resources.

* The ocean benchmarking data may be obtained via `ilamb-fetch --remote_root https://www.ilamb.org/IOMB-Data` or can be incorporated directly into your analysis scripts using the IOMB [intake](https://github.com/nocollier/intake-ilamb) catalog.
* If you have a question about this analysis or a suggestion for another dataset, please raise an issue [here](https://github.com/rubisco-sfa/IOMB-Data). This repository also houses the scripts we use to automatically download and format our reference data.
* You will need this configuration [file](https://github.com/rubisco-sfa/ILAMB/blob/master/src/ILAMB/data/iomb.cfg) which describes the set of reference data to compare against models.
* We have applied this configuration to a collection of CMIP6 models and host the [results](https://www.ilamb.org/dev/IOMB/) for the community to use.

[<img width=750px src="https://www.ipcc.ch/report/ar6/wg1/downloads/figures/IPCC_AR6_WGI_Figure_5_22.png">](https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-5#figure-5-22)