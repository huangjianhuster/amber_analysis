#!~/.conda/envs/comp/bin/gnuplot --persist

# matrixfile = "covar_AE_prod1.dat"
matrixfile = ARG1
outfile = ARG2

set term svg
set output outfile

set palette defined (-1 "blue", 0 "white", 1 "red")
set size ratio -1
stats matrixfile matrix

set xrange [0:sqrt(STATS_records)]
set yrange [0:sqrt(STATS_records)]

set cbrange [-1:1]

plot matrixfile matrix with image
