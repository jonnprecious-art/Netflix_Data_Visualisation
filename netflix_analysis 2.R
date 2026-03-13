# Load required library
if (!require(ggplot2)) install.packages("ggplot2", repos="http://cran.us.r-project.org")
library(ggplot2)

# 1. Load Cleaned Data
df <- read.csv('Netflix_shows_movies_cleaned.csv')

# 2. Visualization: Ratings Distribution
# Implementing the distribution of ratings in R
rating_plot <- ggplot(df, aes(x = rating)) +
  geom_bar(fill = "steelblue") +
  theme_minimal() +
  labs(title = "Distribution of Netflix Ratings (R implementation)",
       x = "Rating",
       y = "Count") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Save the plot
ggsave("r_ratings_distribution.png", rating_plot)
print("Saved R plot: r_ratings_distribution.png")
