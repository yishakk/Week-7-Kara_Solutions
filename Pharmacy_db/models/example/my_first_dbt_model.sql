
/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/
WITH my_first_dbt_model AS (
    SELECT
        id,
        message_id,
        channel_title,
        channel_username,
        message,
        message_Date,
        media_path
    FROM
        public.cleaned_data
    WHERE
        message IS NOT NULL
)
SELECT * FROM my_first_dbt_model
