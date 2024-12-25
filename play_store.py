from google_play_scraper import app, reviews, Sort

def fetch_app_reviews(ids):
    # Fetch reviews
    for app_id in ids:
        try:
            app_info = app(
                app_id, 
                lang='en',  # Language of the reviews
                country='us',  # Country code
            )
            print(f"[{app_info['title']}]")
            result, continuation_token = reviews(
                app_id,
                lang='en',  # Language of the reviews
                country='us',  # Country code
                sort=Sort.MOST_RELEVANT,  # Sort by newest reviews
                count=25,  # Number of reviews to fetch
                filter_score_with=None  # Filter by score (1-5)
            )
            # Print the reviews
            for review in result:
                print(f"{review['content']}")
        except Exception as e:
            print(f"Error fetching reviews for {app_id}: {e}")

if __name__ == "__main__":
    app_ids = {"your_app_id"}  
    fetch_app_reviews(app_ids)