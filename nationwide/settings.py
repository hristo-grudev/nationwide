BOT_NAME = 'nationwide'

SPIDER_MODULES = ['nationwide.spiders']
NEWSPIDER_MODULE = 'nationwide.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'nationwide.pipelines.NationwidePipeline': 100,

}