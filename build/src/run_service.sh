#rm /tmp/snapshots.jl
echo "Running scrapy search ..."
cd /scrapy_project/scrapy_topic_search && scrapy crawl topic_search_spider -o /tmp/snapshots.jl &>> /tmp/scrapy-search.log
echo "Time series results:"
python3 /scrapy_project/search_results_to_hit_count.py -i /tmp/snapshots.jl
