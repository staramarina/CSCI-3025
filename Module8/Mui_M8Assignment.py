# Tiffany M. Mui
# Module 8 Assignment - Main Program
# CSCI-3025: Python Programming
# Purpose: NASA NeoWs Exploration
# Dependencies:
#   Standard: sys, os, pathlib, copy, datetime
#   External: dotenv, requests, pandas, matplotlib, seaborn
#   Custom: Mui_NeoWsHandle.py, Mui_Logging.py,
#           Mui_Ancillary.py, Mui_Analysis.py


import Mui_NeoWsHandle as neows
import Mui_Analysis as analysis
import Mui_Ancillary as aux
import Mui_Logging as log

if __name__ == "__main__":
    # Setup
    err_log = "Mui_M8_Log.txt"
    timeout = 10
    print("\nLet's explore Near-Earth Objects!\n")
    api_key = neows.load_env()
    start = "2026-11-08"
    end = "2026-11-14"

    # NeoWs Feed Endpoint Data Load
    print(f"Pulling feed data from {start} to {end}.....", end="")
    feed_url = neows.build_feed_url(api_key, start, end, err_log)
    feed_json_data = neows.neows_call(feed_url, timeout, err_log)
    feed_all_data = neows.build_dataframe(feed_json_data)
    print(" Done!")

    # NeoWs Feed Endpoint General Data Trim & Clean
    print("Trimming feed data.....", end="")
    feed_trim_data = neows.trim_common_data(feed_all_data)
    print(" Done!")
    print("Cleaning feed data.....", end="")
    feed_data_clean = neows.clean_common_data(feed_trim_data)
    print(" Done!")

    # Didymos Data Load
    didymos_spk_id = "2065803"
    print("Pulling lookup data on Didymos.....", end="")
    lookup_url = neows.build_lookup_url(api_key, didymos_spk_id)
    lookup_json_data = neows.neows_call(lookup_url, timeout, err_log)
    lookup_all_data = neows.build_dataframe(lookup_json_data)
    print(" Done!")

    # Didymos General Data Trim & Clean
    print("Trimming Didymos data.....", end="")
    lookup_trim_data_c = neows.trim_common_data(lookup_all_data)
    lookup_trim_data_s = neows.trim_lookup_data(lookup_trim_data_c)
    print(" Done!")
    print("Cleaning Didymos data.....", end="")
    lookup_data_c_clean = neows.clean_common_data(lookup_trim_data_s)
    lookup_data_clean = neows.clean_lookup_data(lookup_data_c_clean)
    print(" Done!")

    # Tailored Cleaning, Analysis, and Chart Generation
    print(
        "Cleaning, analyzing, and plotting PHO vs. non-PHO per day with "
        "average statistics.....",
        end="",
    )
    neo_chart = analysis.neo_pho_chart(feed_data_clean)
    print(" Done!")
    print(
        "Cleaning, analyzing, and plotting miss distance per day with "
        "average statistics.....",
        end="",
    )
    lun_chart = analysis.lun_miss_chart(feed_data_clean)
    print(" Done!")
    print(
        "Cleaning, analyzing, and plotting PHO minimum and maximum "
        "diameter per day with Didymos comparison points.....",
        end="",
    )
    pho_chart = analysis.pho_size_chart(feed_data_clean, lookup_data_clean)
    print(" Done!")
    print(
        "Cleaning, analyzing, and plotting Didymos orbiting patterns for "
        "Earth and Mars with comparison against DART impact.....",
        end="",
    )
    didymos_chart = analysis.didymos_orbit_chart(lookup_data_clean)
    print(" Done!")

    # Save Charts
    print("Saving PHO vs. non-PHO chart.....", end="")
    check_neo = aux.chart_save(neo_chart, "charts/neo_chart.png")
    if not check_neo[0]:
        log.err_handle(check_neo[1], err_log)
        print(f" FAILED. Check {err_log} for details.")
    else:
        print(" Done!")
    print("Saving miss distance chart.....", end="")
    check_lun = aux.chart_save(lun_chart, "charts/lun_chart.png")
    if not check_lun[0]:
        log.err_handle(check_lun[1], err_log)
        print(f" FAILED. Check {err_log} for details.")
    else:
        print(" Done!")
    print("Saving PHO diameter comparison chart.....", end="")
    check_pho = aux.chart_save(pho_chart, "charts/pho_chart.png")
    if not check_pho[0]:
        log.err_handle(check_pho[1], err_log)
        print(f" FAILED. Check {err_log} for details.")
    else:
        print(" Done!")
    print("Saving Didymos orbit patterns chart.....", end="")
    check_didymos = aux.chart_save(didymos_chart, "charts/didymos_chart.png")
    if not check_didymos[0]:
        log.err_handle(check_didymos[1], err_log)
        print(f" FAILED. Check {err_log} for details.")
    else:
        print(" Done!")
    print("\nAll tasks complete!")
    print("Charts are located in the charts folder.\n")
