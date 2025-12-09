from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Free API key for OMDB (you can get your own at http://www.omdbapi.com/apikey.aspx)
API_KEY = "trilogy"  # Demo key with limited requests
# http://www.omdbapi.com/?i=tt3896198&apikey=fecc63b8
@app.route("/", methods=["GET", "POST"])
def home():
    movie = None
    error = None
    
    if request.method == "POST":
        movie_name = request.form.get("movie_name")
        
        try:
            # Call OMDB API
            url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={movie_name}"
            response = requests.get(url)
            data = response.json()
            
            if data.get("Response") == "True":
                movie = data
            else:
                error = f"Movie not found: {data.get('Error', 'Unknown error')}"
        except Exception as e:
            error = f"Error fetching movie data: {str(e)}"
    
    return render_template("index.html", movie=movie, error=error)

if __name__ == "__main__":
    app.run(debug=True)
