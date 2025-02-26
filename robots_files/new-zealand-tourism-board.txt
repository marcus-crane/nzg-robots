# robots-prod.txt
# Production Robots File
# 20210921 0841

# ----- DEFAULT CRAWLER RULES -----
User-agent: *
# - RESOURCE PATHS SS -
Disallow: /api/
Disallow: /farefinder/
Disallow: /admin/
Disallow: /dev/
Disallow: /health/check/
Disallow: /Security/
Disallow: /CMSSecurity/
Disallow: /RemoveOrphanedPagesTask/
Disallow: /SiteTreeMaintenanceTask/
Disallow: /UserDefinedFormController/
# - Default crawl delay
Crawl-delay:5

# ----- DISABLED CRAWLERS -----
User-agent: *Fetch*
User-agent: http://www.almaden.ibm.com/cs/crawler
User-agent: BorderManager*
User-agent: webcollage*
User-agent: Java*
User-agent: grub-client
User-agent: lwp*
User-agent: *TunnelPro*
User-agent: LinkWalker
User-agent: Offline Explorer
User-agent: larbin
User-agent: 008
User-agent: MJ12bot
User-agent: BLEXBot
User-agent: dotbot
User-agent: Yeti
User-agent: SemrushBot
Disallow: /

# ----- Swiftype specific config
User-agent: Swiftbot
Crawl-delay: 0.25
