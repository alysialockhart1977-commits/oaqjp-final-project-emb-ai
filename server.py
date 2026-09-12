"""
Flask server for the Emotion Detection web application.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emote_detector():
    """
    Analyze emotion from user text and return formatted response.
   
    Returns:
        str: A formatted response showing emotion scores and dominant emotion.
    """
    # Get the text from the web page input
    text_to_analyze = request.args.get("textToAnalyze")

    # Call the emotion detector function
    response = emotion_detector(text_to_analyze)

    # Extract emotion scores
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    # Handle blank input errors
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Return formatted text response
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, "
        f"'disgust': {disgust}, "
        f"'fear': {fear}, "
        f"'joy': {joy}, "
        f"'sadness': {sadness}, "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Render the main HTML page.
    
    Returns:
        str: The rendered HTML template.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
