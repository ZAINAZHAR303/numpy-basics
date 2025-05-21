A=9;
B=10;
x= [1 2 3; 4 5 6 ;7 8 9];
% imread - read image
% imshow - 
% rgb2gray - 
rgb = imread("zain.jpg");
gray  = rgb2gray(rgb);
figure;
subplot(1,1,2)
imshow(rgb);
subplot(1,3,1);
imshow(gray);
% imshow(rgb)

% imageviewset(rgb)
% gray_img = rgb2gray(rgb);
% 
% 
% hist=imhist(gray_img);
% imshow(hist);
% disp(x);
% z = imread('zain.jpg');
% imshow(z);
% 
% info = imfinfo("zain.jpg");
% disp(info);

% z = imread('zain.jpg');
% h = fspecial('average', [5 5]); % Create a 5x5 averaging filter
% z_filtered = imfilter(z, h); % Apply the filter
% imshow(z_filtered); % Display the filtered image

