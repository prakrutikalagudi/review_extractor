# review_extractor
Web Scraping Review Extractor
This project is a Flask-based web application designed to scrape reviews from a provided URL, extracting relevant information such as review title, body, rating, and reviewer. It displays the reviews in JSON format as a response.
Solution Approach
1.	Flask Framework: The web application uses Flask for the backend, handling HTTP requests and rendering the frontend.
2.	Web Scraping: The scrape_reviews function uses requests to fetch the webpage and BeautifulSoup to parse the HTML content, extracting relevant review details from the specified URL.
3.	API Endpoint: The /scrape endpoint accepts a POST request with a URL parameter, scrapes the reviews, and returns them as JSON. If any error occurs during scraping, a descriptive error message is returned.
4.	Frontend: The application renders a simple form via the / route where users can input a URL. After submitting the form, the server scrapes the reviews and sends them back as a JSON response.
System Architecture
•	Frontend: Simple HTML form for submitting URLs.
•	Backend: Flask handles requests, scrapes data using BeautifulSoup, and responds with JSON.
•	Web Scraping: requests and BeautifulSoup libraries are used to fetch and parse the web page, extracting review data.
•	Error Handling: Errors are captured and returned to the frontend for better user experience.
Diagram

 
Running the Project
1.	Clone the repository:
git clone <repository_url> 
cd <repository_directory> 
2.	Install dependencies: Ensure you have Python 3.x installed. Install the required dependencies using pip:
pip install -r requirements.txt 
3.	Run the Flask app:
Start the server:
python app.py 
By default, the application will be accessible at http://192.168.1.9:8080/. You can change the port number by modifying the port variable in app.py.
4.	Access the Web App:
Open a web browser and navigate to http://192.168.1.9:8080/. You will see the input form where you can submit a URL.
5.	Submit a URL:
After entering the URL, click the submit button. The server will scrape the reviews from the webpage and display the results as a JSON response.
API Usage
POST /scrape
Request
•	Method: POST
•	URL: /scrape
•	Parameters:
•	url: The URL of the webpage to scrape reviews from.
Response
•	On success:
•	Status: 200 OK
•	Body: A JSON object containing a list of reviews, each with the following fields:
•	title: The title of the review (or "No Title" if not available).
•	review_body: The body of the review (or "No Body" if not available).
•	rating: The rating given by the reviewer (or "No Rating" if not available).
•	reviewer: The name of the reviewer (or "Anonymous" if not available).
•	On failure:
•	Status: 400 Bad Request or 500 Internal Server Error
•	Body: A JSON object with an error message.
Example Request:
{
  "url": "https://www.flipkart.com/apple-iphone-16-black-128-gb/product-reviews/itmb07d67f995271?pid=MOBH4DQFG8NKFRDY&lid=LSTMOBH4DQFG8NKFRDYKOOGZ6&marketplace=FLIPKART"
}
Example Response:
{
        "title": "Terrific purchase",
        "review-body": "This phone is very good and value for money Camera \u2b50\u2b50 \u2b50 Battery  \u2b50\u2b50\u2b50\u2b50 Display \u2b50\u2b50\u2b50 Performance \u2b50\u2b50\u2b50\u2b50READ MORE",
        "rating": "5",
        "reviewer": "AJEET MANDAL"
    },
    {
        "title": "Just wow!",
        "review-body": "Nice Phone Under This Range Fully Satisfy \ud83d\ude03\ud83d\ude03\ud83d\ude03\ud83d\ude03\ud83d\ude03 Battry Backup Is AwesomeREAD MORE",
        "rating": "5",
        "reviewer": "Flipkart Customer"
    },
    {
        "title": "Worth every penny",
        "review-body": "Good looking \ud83e\udd29 battery backup 95% good \ud83d\udc4dCamera \ud83d\udcf8 quality batter \ud83e\udd0fNice Processor for BGMI Price range all-over best.\u2705READ MORE",
        "rating": "5",
        "reviewer": "Deepak Sah"
    }


