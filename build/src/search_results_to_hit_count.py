import argparse
from datetime import datetime
import json
import sys

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(
        description='Outputs scrapy topic search results as a time series of hit counts')
    PARSER.add_argument(
        '-i', '--input',
        help="The input file name")
    ARGS = PARSER.parse_args()

    usage_help_str = "USAGE: python search_results_to_hit_count.py -i <input_filename.jl>"

    if (not ARGS.input):
       print("Input mode not provided!")
       print(usage_help_str)
       sys.exit(0)

    try:
        input_file = open(ARGS.input)
        input_file_lines = input_file.readlines()
    except Exception as e:
        print("Error while trying to open and read input file, check for correct formatting!")
        sys.exit(0)

    search_results = []
    try:
        for line in input_file_lines:
            json_line = json.loads(line)
            search_results.append(json_line)

        time_series_results = {}
        for result in search_results:
            curr_time_stamp = result['timestamp']
            
            if curr_time_stamp in time_series_results:
                new_count = time_series_results[curr_time_stamp][0] + 1
                new_items = time_series_results[curr_time_stamp][1] + result['items']
                time_series_results[curr_time_stamp] = [new_count, new_items]
            else:
                time_series_results[curr_time_stamp] = [1,result['items']]

        sorted_times = sorted(time_series_results.keys())
        sorted_time_series_list = []
        #sorted(sorted_times)
        for time in sorted_times:
            d = {"Time stamp":str(datetime.fromtimestamp(time)), "Hit counts":time_series_results[time][0], "Search results":time_series_results[time][1]}
            sorted_time_series_list.append(d)
            #print(d)
            
            #out_str = "test"
            #out_str = "{\"Time stamp\":\"" + str(datetime.fromtimestamp(time)) + "\", \"Hit counts\":" + str(time_series_results[time][0]) + ", \"Search results\": " + str(time_series_results[time][1]) + "}"
            #print(out_str)
        print(json.dumps(sorted_time_series_list))

    except Exception as e:
        print("Error while trying to read input file lines and convert to time series, check for correct formatting!")
        print(e)
        sys.exit(0)

   


