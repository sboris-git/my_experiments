# install.packages("devtools", dependencies = TRUE)
# library(devtools)
# install_github("vqv/ggbiplot", force = TRUE)
library(ggbiplot)

getwd()
setwd("/home/stable/Dropbox/Classes/Сучасні методи аналізу/Artificial_Nose")
data <- read.table("potentiometry-3.csv", header=TRUE, sep=";", dec=",")

data.species <- data[, 15]
#log.params <- log(wine[, 1:5])
params <- data[, 1:11]

# apply PCA - scale. = TRUE is highly 
# advisable, but default is FALSE. 
params.pca <- prcomp(params,
                 center = TRUE,
                 scale = TRUE) 
# print method
print(params.pca)
# plot method
plot(params.pca, type = "l")
# summary method
summary(params.pca)
# We can use the predict function if we observe new data and want to predict their PCs values. Just for illustration pretend the last two rows of the iris data has just arrived and we want to see what is their PCs values:
# Predict PCs
predict(params.pca, newdata=tail(params, 2))
g <- ggbiplot(params.pca, obs.scale = 1, var.scale = 1, 
              varname.size = 3, labels.size=3,
              groups = data.species, ellipse = FALSE, 
              circle = TRUE)
#g <- g + scale_color_discrete(name = '')
g <- g + scale_color_manual(name="e-tongue", values=c("green","blue","yellow","magenta","purple","orange","pink","dark blue", "black", "darkgreen","red","brown","black"))
#We can use scale_color_discrete or equivalently scale_color_hue to change legend name or labels, limits, and the hue values used. 
# parameters you can set are h = range of hues in [0, 360], c = chroma (intensity of color), l = luminance (lightness) in [0, 100]; 
# ands some others you can play with.
# g <- g + scale_color_hue(l = 80, c = 250)
g <- g + theme(legend.direction = 'vertical', 
               legend.position = 'right')
print(g)
#ggsave(filename = "plot.pdf", plot = dd, width = 6, height = 7)

