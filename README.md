______________
INSTALLATION:
______________

Docker build:

$<INSTALL_DIR> $ docker-compose build

_______
TO RUN:
_______

1) Configure the SEARCH_TOPIC, TIME_RANGE and SEARCH_URLS by editing this file
$<INSTALL_DIR> $ ./settings/topic_search_settings.py

2) Run the service using:
$<INSTALL_DIR> $ docker-compose up

3) Check the search results in this file:
$<INSTALL_DIR> $ ./search_outputs/hit_count_time_series.txt







