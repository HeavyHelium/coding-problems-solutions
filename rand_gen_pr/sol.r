sim.r <- function(n) {
  numbers <- c(1, 2, 3, 4)
  probs <- c(0.1, 0.5, 0.2, 0.2)
  sample(numbers, size = n, 
         replace = FALSE, prob = probs)
}

table(replicate(10000, sim.r(1)))