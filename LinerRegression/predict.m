function p = predict(X,y,theta, lamda)
X = [ones(size(X,1),1) X];
p = ((y - X*theta ) < lamda);
end
