"""
Unit tests for EmotionDetection.emotion_detector function.
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """
    Test case for the emotion detector functions
    """
    def test_joy(self):
        """Test detection of joy emotion"""
        response = emotion_detector("I am glad this happened")
        self.assertEqual(response["dominant_emotion"], "joy")

    def test_anger(self):
        """Test detection of anger emotion"""
        response = emotion_detector("I am really mad about this")
        self.assertEqual(response["dominant_emotion"], "anger")

    def test_disgust(self):
        """Test detection of disgust emotion"""
        response = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(response["dominant_emotion"], "disgust")

    def test_sadness(self):
        """Test detection of sadness emotion"""
        response = emotion_detector("I am so sad about this")
        self.assertEqual(response["dominant_emotion"], "sadness")

    def test_fear(self):
        """Test detection of fear emotion"""
        response = emotion_detector("I am really afraid that this happened")
        self.assertEqual(response["dominant_emotion"], "fear")

if __name__ == "__main__":
    unittest.main()
