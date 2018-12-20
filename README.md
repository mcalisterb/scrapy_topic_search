______________
INSTALLATION:
______________

Docker build:

$<INSTALL_DIR> $ docker build -t scrapy_topic_search build/

_______
TO RUN:
_______

Start the service:

$<INSTALL_DIR> $ docker run -d -it -p 8080:8080 scrapy_topic_search


scrapy crawl topic_search_spider -o snapshots.jl






