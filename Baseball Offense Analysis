#install.packages("corrplot")
#install.packages("treemap")
library(corrgram)
library(RColorBrewer)
library(ggplot2)
library(tidyr)
library(corrplot)
# set directory
setwd("~/R/Data")
# read in csv file from notepad
teamData <- read.csv("Batting.txt"
                     , header = TRUE
                     , stringsAsFactors = FALSE
                     , sep = ","
)
# check to make sure data score is >=100
if (ncol(teamData)*4*(nrow(teamData)/100) >=100) {
  print("You have good data!")} else {print("You need to find better data!")
}
# it says my dataset is large enough!
ncol(teamData)
nrow(teamData)
str(teamData)

teamData <- na.omit(teamData)

#subset team data to only work with players over 500 PA
teamData <- teamData[teamData$PA >= 500,]

#add a new stat called Total bases per plate appearance or TBPA
teamData$TBPA <- teamData$TB/teamData$PA

#set up color scheme
my.colors <- brewer.pal(nrow(teamData), "Blues")

##############################Summary Plots###############################################
par(mfrow = c(2,2))

boxplot(teamData$SO
        , col = my.colors[4]
        , main = "Distribution of Strikeouts"
        )

boxplot(teamData$BA
        , col = my.colors[5]
        , main = "Distribution of Batting Average"
)

boxplot(teamData$SLG
        , col = my.colors[6]
        , main = "Distribution of Slugging Percentage"
)

boxplot(teamData$TBPA
        , col = my.colors[7]
        , main = "Distribution of Total Bases Per Plate Appearance (TBPA)"
)

#############################distribution of strikeouts by age#############################
# create matrix showing mean strikeouts by age
a <- tapply(teamData$SO, list(teamData$Age), mean)
# barplot showing info above
barplot(a
     , col = my.colors
     , pch = 16
     , main = "Mean Strikeouts by Age for National League Hitters"
     , ylab = "Strikeouts"
     , xlab = "Age"
     )


# showing the distribution of age of major league players
#hist(teamData$Age
 #    , main = "Distribution of Age of Major League Players in 2019"
  #   , xlab = "Age"
   #  , col = my.colors
#)
ageMean <- mean(teamData$Age)

# showing the distribution of batting averages using a boxplot
#boxplot(teamData$BA
 #       , main = "Distribution of Batting Averages in the Major Leagues for 2019"
  #      , ylim = c(0, .6)
   #     , yaxt = "n"
    #    , ylab = "Batting Averages"
        
#)
#title(sub="Data Provided by Baseball-Reference.com"
 #     , adj=1
  #    , line=3
   #   , font=2
#)

##############################Density of Strikeouts############################################
d <- density(teamData$SO)
plot(d
     , main = "Density of Strikeouts in National League in 2019"
     , col = "blue"
)
polygon(d,
        col = my.colors[3]
        )

#############################Effect of Strikeouts on Batting Average##########################
colorscheme <- my.colors
colorscheme[teamData$Age > ageMean] <- "blue"
colorscheme[teamData$Age < ageMean] <- "red"

ggplot(teamData) + 
  aes(x = SO, y = BA) +
  geom_point(pch = 16, size = 3, col = colorscheme) + 
  geom_smooth(method = lm) +
  ggtitle("Effect of Strikeouts on Batting Average") +
  scale_x_continuous(breaks = c(60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200)) +
  scale_y_continuous(breaks = c(.240, .270, .300, .330)) 

ggplot(teamData) + 
  aes(x = SO, y = SLG) +
  geom_point(pch = 16, size = 3, col = colorscheme) + 
  geom_smooth(method = lm) +
  ggtitle("Effect of Strikeouts on Slugging (Power)") +
  scale_x_continuous(breaks = c(60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200))

#smoothScatter(teamData$SO
 #    , teamData$BA 
   #  , col = colorscheme
  #   , pch = 16
   #  , cex = 2
  #   , ylim = .6
#)

############################Correlation Matrix with Strikeouts###############################
teamData2 <- subset(teamData, select = c(BA, OBP, OPS, SO, TBPA))
cor <- corrgram::corrgram(teamData2)
corrplot(cor
         , method = "square"
         , col = my.colors
         )



##############################Effect of Strikeouts on Power####################################


# Subset data to players over 500 PAs
o500 <- teamData[teamData$PA>500,]
o500 <- na.omit(o500)

# Distribution of Strikeouts
ggplot(o500) +
  aes(y = SO, color = "green", mapping = SO) +
  geom_boxplot() +
  coord_flip()

ggplot(o500) +
  aes(x = SO, y = BA, color = SO > 100) +
  geom_point() 
# difference between over and under 100 SOs with smoothing line
ggplot(o500) +
  aes(x = SO, y = BA, color = SO > 100) +
  geom_point() +
  geom_smooth() +
  geom_vline(xintercept = 100, lty=2, lwd = 1.5)

hist(o500$Age)
mean(o500$Age)

ggplot(o500) +
  aes(x = Age, y = OPS, color = Age > 28) +
  geom_point() +
  geom_smooth() +
  geom_vline(xintercept = 28, lty=2, lwd = 1.5)




top10 <- o500[order(o500$OPS, decreasing = T),]

top10$Name

treemap(top10[1:10,]
        , index = c("Name")
        , vSize = "SLG"
      #  , vColor = "OBP"
        , fontsize.labels = 18
        , palette = "Greens"
        , type = "dens"
)

#top10matrix <- as.matrix(top10[1:10,])
#barplot(top10matrix.OPS
      #  , names.arg = top10matrix$Name
#)



#########################Saved but not using yet##############################
df <- teamData
str(df)
# Creating a new column and stat called TB/PA
df$TBPA <- df$TB / df$PA

# Get names of indexes for which column PlateAppearances has value < 500
df2 <- df[df$PA > 500,]


#boxplot showing summary of TBPA
boxplot(df2$TBPA
        , col = "red"
        )

# sorting the values by TB/PA
orderTBPA <- df2[order(df2$TBPA, decreasing = T),]


# initial plot of TB/PA to see the data
hist(df2$TBPA)

# Scatterplot of TB/PA
plot(df2$TBPA)

# Effect of strikeouts on TB/PA
plot(df2$SO, df2$TBPA)
# get the mean for vline in scatterplot
mean(df2$SO)

ggplot(df2) +
  aes(x = SO, y = TBPA, color = SO > 120) +
  geom_point() +
  geom_smooth() +
  geom_vline(xintercept = 120, lty=2, lwd = 1.5
)

# creating datafrome over all players with under 120 strikeouts
sodfless120 <- df2[df2$SO < 120, ]
a <- mean(sodfless120$TBPA)

# creating dataframe over all players with over 120 strikeouts

sodfmore120 = df2[df2$SO > 120,]
b <- mean(sodfmore120$TBPA)

# Creating bar graph to shows effects of strikeouts on over and under 120 strikeout groups
my.colors <-  brewer.pal(3, "Blues")
c <- c(a, b)
barplot(c
        , names.arg = c("Less Than 120 Strikeouts", "More than 120 Strikeouts") 
        , col = my.colors
        )

df2 <- na.omit(df2)
lm(TBPA~., data = df2)
