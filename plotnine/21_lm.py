from plotnine.data import economics
from plotnine import ggplot, aes, facet_grid, labs, geom_point, geom_smooth, xlab, ylab

print(ggplot(economics)
        + aes(x="date", y="uempmed")
        + geom_point()
        + geom_smooth(color="red", method="lm")
        + xlab("date (year)")
        + ylab("unemploynment"))
