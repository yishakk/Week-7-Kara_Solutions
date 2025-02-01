
/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

{{ config(materialized='table') }}

WITH pharmacy AS (
    SELECT
        id,
        Date,
        Message_ID,
       Channel_Title,
        Channel_Username,
        Message,
        Message_Date,
        Media_Path
    FROM
        pharmacy
    WHERE
        Message IS NOT NULL
)
SELECT * FROM pharmacy
