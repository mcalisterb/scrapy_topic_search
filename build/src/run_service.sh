#rm /tmp/snapshots.jl
echo "Running scrapy search ..."
cd /scrapy_project/scrapy_topic_search && scrapy crawl topic_search_spider -o /tmp/snapshots.jl &>> /mnt/search_outputs/scrapy-search.log
echo "Converting results to time series ..."

if [ -f /mnt/search_outputs/hit_count_time_series.txt ] ; then
    rm /mnt/search_outputs/hit_count_time_series.txt
fi
python3 /scrapy_project/search_results_to_hit_count.py -i /tmp/snapshots.jl  &>> /mnt/search_outputs/hit_count_time_series.txt

echo "Time series results:"
cat /mnt/search_outputs/hit_count_time_series.txt
