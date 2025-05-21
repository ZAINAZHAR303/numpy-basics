rgb_img = imread("zain.jpg");
gray_img = rgb2gray(rgb_img);
figure, imshow(gray_img),title('orginal Grayscale Image');

% Step 2: Add Sa;t and peeper Noise

In = imnoise(gray_img,'salt & pepper');
imshow(In), title('Noisy Gray');



% Step 3: Create Mean Filter
h = fspecial('average',[3,3]);
I_mean = imfilter(In, h);
figure, imshow(I_mean), title('mean filter')


% Apply Median filter

meadian_fil = medfilt2(In,[3,3]);
figure, imshow(meadian_fil), title("median filter")

