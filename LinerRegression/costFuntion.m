function  [J, theta] = costFuntion(X , y, theta, alpha, Inner )
m = size(X,1);
X = [ones(m,1) X];
for i=1:Inner
  J = (1/(2*m))*sum((X*theta - y).^2);
  temp0 = theta(1) - (alpha*(1/m)).*((X*theta - y)'*X(:,1));
  temp1 = theta(2) - (alpha*(1/m)).*((X*theta - y)'*X(:,2));
  theta(1) = temp0; 
  theta(2) = temp1;
end

end