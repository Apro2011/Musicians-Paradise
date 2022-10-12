# Musicians Paradise #

**About the project**

Musicians can upload their own content and "like" others'. This project is made using Python, Django HTML, CSS, JavaScript and jQuery-AJAX. Frontend is purely made of HTML and CSS. On the Backend, Python and Django is used. There is a function in the project for "like/unlike". For that function to work without reloading the page, jQuery-AJAX and JavaScript is used.

A user has to signup by clicking the signup button on the bottom of the front page, which will take you to the signup page and after signing up the user will be taken back to the front page, where the user has to again login by clicking the login button on the bottom of the front page, which will take the user to the login page where he will login and then again will be taken to the front page. Now the options on the bottom has changed. The user can either create his/her own blog or he can logout. Also, the user can click on the cards in the front page and see other user's content and "Like/Unlike" it. Only logged in users can "like" or "unlike".

In the bottom of the front page logged in users can see "create your own blog" link. It will take users to the page from where the user will be able to post his/her own music and write about it.


**Advantages**

1. Media files are stored in and accesed from *Amazon S3* bucket.
2. Project is deployed on PythonAnywhere.
3. jQery-AJAX is using JSON response sent from the backend to change the "like" button and "likes"   in the frontend.
4. Front End has a good design.
5. Class Based Views are used for every functionality except for "like" buttons.
6. Test Driven Development has beed done properly.


**Disadvantages**

1. Users cannot delete their blogs.
2. Users can and have to upload only 3 music pieces. He/She can post more blogs for more music.
3. After the user presses, "Create Blog" button after selecting the songs and photo, it takes about 4-5 minutes to get posted as a card on the front page. This is because, media files are being stored in and accesed from *Amazon S3 bucket* which is an AWS cloud functionality.


**Conclusion**

This project has helped me learn a lot about web development as a whole. I would like every musician to use this webapp test it. It was very hard and exciting. Also, this project is my own idea. I hope in future I can learn more and more and improve my skills for better. So yeah! this is ***Musicians Paradise***.

Website Link: https://aprodev2011.pythonanywhere.com/


**Updates**

Amazon AWS has suspended my account so now the media files are stored in *Google Cloud Storage Bucket*. So yes it's not Amazon S3 anymore it's Google Cloud Storage.
