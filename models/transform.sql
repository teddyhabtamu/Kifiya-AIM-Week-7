WITH cleaned_data AS (
    SELECT
        id,
        channel,
        message
    FROM
        {{ ref('messages') }}
)
SELECT
    id,
    channel,
    message
FROM
    cleaned_data