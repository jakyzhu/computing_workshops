

install.packages("sqldf") #may or may not be necessary
library(sqldf)
## Load sample dataset
data(titanic3,package="PASWR")

## Take a look at the data
colnames(titanic3)
head(titanic3)
view(titanic3)

## Query Data with sqldf

sqldf('select age, count(*) from titanic3 where age is not null group by age')

#Store data
df <- sqldf('select age, count(*) from titanic3 where age is not null group by age')

# Take a look at the data
plot(df$age,df$'count(*)',main=Distribution of Ages on the Titanic")