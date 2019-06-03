
load('data_lab');
X = data_lab(1:750,1);
y = data_lab(1:750,2);
lamba = 10^-10;
testX = data_lab(751:1000, 1);
testY = data_lab(751:1000, 2);
theta = [0;0];
Inner = 150000;
alpha = 1*10^-5;
[cost, theta] = costFuntion(X, y , theta, alpha, Inner);
fprintf("%f", cost);
theta
p = predict(testX, testY, theta, lamba);
count = 0;
for i = 1:size(p)
if(p(i)==1)
count = count+1;
end
end
fprintf("Accuracy of test: %f", count/size(p,1));
