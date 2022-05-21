WITH main AS (SELECT post_year,
       post_month,
       tag,
       month_count -- optional, not needed in main table

FROM (

  SELECT datepart(year,Posts.CreationDate) as post_year,
         datepart(month,Posts.CreationDate) as post_month,
         tags.TagName as tag,
         COUNT(*) as month_count

  FROM PostTags as pt
    INNER JOIN Posts
    ON pt.PostId = Posts.Id
    INNER JOIN Tags as tags
    ON pt.TagId = tags.Id

  WHERE tags.TagName in ('express', 'django', 'ruby-on-rails',
                         'laravel', 'spring', 'angular', 'reactjs',
                         'vue.js')
  AND Posts.PostTypeId = 1
  GROUP BY datepart(year,Posts.CreationDate),
           datepart(month,Posts.CreationDate),
           tags.TagName

     ) AS subquery


GROUP BY post_year,
         post_month,
         tag,
         month_count),

sub AS (SELECT datepart(year,Posts.CreationDate) as post_year,
               datepart(month,Posts.CreationDate) as post_month,
               count(*) as total
        FROM Posts WHERE PostTypeId = 1
        GROUP BY datepart(year,Posts.CreationDate),
                 datepart(month,Posts.CreationDate))


SELECT main.post_year as 'year',
       main.post_month as 'month',
       tag as 'tag',
       month_count as 'month count per tag',
       total as 'overall count',
       month_count * 100.0 / total as 'percent',
       SUM(month_count) OVER(PARTITION BY tag
                             ORDER BY main.post_year,
                                      main.post_month
                             ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as 'running count'
FROM main INNER JOIN sub ON main.post_year = sub.post_year
                         WHERE main.post_month = sub.post_month
ORDER BY main.post_year,
         main.post_month,
         tag;
