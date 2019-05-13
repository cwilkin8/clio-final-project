# clio-final-project
Data was scraped from <http://ghf.destinationnext.com/immigration/Search.aspx> 

"immigration1 (2).csv" contains immigration records with date of arrival, destination, origin country, #people traveling together, and vessel name

"immigrant_families2.csv" contains demographic information of immigrant records including name, age, sex, and occupation

These two tables can be joined using "family_record_num" 

"map.csv" contains the destination county for records from 1844-1850 in a mappable format. I standardized the spelling and formatting of destination counties in OpenRefine and then imported the data back into R as this csv.

The shape files I used for the map were too big to upload to GitHub, but I downloaded the 1860 county files from NHGIS. I used 1860 boundaries because some of my data was from the year 1850 and included counties that were not yet formed in the 1850 census shape files

"app.R" is the code to make the shiny visualization that is not included in the project rmd file

"occupation_category.csv" contains the listed occupations I assigned to 13 categories to make the bar graph 
