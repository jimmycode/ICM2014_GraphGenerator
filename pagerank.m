function [ answer ] = pagerank( A, p )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
for i = 1:1000
    p = A'*p;
end
answer = sortrows(cat(2, p ,(1:length(p))'),1);
return
end
