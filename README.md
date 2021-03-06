# DS3002-Final-Project

*Please see Documentation file for additional information

My Analysis:

For my analysis, I chose to see if there was a correlation between the three variables via a correlation matrix. However, I started by plotting factor against time. I found that there was a positive relationship between 'factor' and 'time,' because 'factor' increased as 'time increased.' I also plotted ‘pi’ against ‘time’ and noticed that after the first couple of minutes after the top of the hour, the graph nearly flatlined. Since the 'pi' values were all nearly identical, I wanted to examine the relationship between 'factor' and 'time.' However, this is only based on the number of minutes elapsed that hour, as the API resets at the top of the hour. I also noticed that once the hour changed, ‘factor' would go back to 1 and 'pi' would have a value of '4.0.' In addition, 'pi' slowly approached the true value of 'pi' as the hour progressed starting with a maximum of four and a minimum close to 3. Finally, I noticed that 'factor' followed a cubic growth sequence where the factor is the current minute cubed. With regards to the correlation matrix, factor had a fairly strong positive correlation with time, and pi had a weaker positive correlation with time, which makes sense in the context of the data. 
