# plot histogram
binwidth = 0.05

bin(x,width)=width*floor(x/width)

p "./dist_0.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_1.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_2.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_3.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_4.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_5.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_6.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_7.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_8.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_9.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_10.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_11.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_12.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_13.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_14.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_15.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_16.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_17.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_18.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_19.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_20.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_21.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_22.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_23.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_24.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_25.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_26.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_27.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_28.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_29.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_30.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_31.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_32.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_33.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_34.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_35.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_36.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_37.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_38.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_39.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes,\
"./dist_40.0/prod_dist.dat" using (bin($8,binwidth)):(1.0) smooth freq with boxes
