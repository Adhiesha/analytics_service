CREATE TABLE IF NOT EXISTS analytics.web_analytics (
    eventType String,
    payload String,
    timestamp DateTime
) ENGINE = MergeTree()
ORDER BY timestamp;
