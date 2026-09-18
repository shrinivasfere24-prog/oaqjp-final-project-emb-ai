import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

        result = emotion_detector("I am so angry with you")
        self.assertEqual(result['dominant_emotion'], 'anger')

        result = emotion_detector("I am so disgusted with you")
        self.assertEqual(result['dominant_emotion'], 'disgust')

        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

        result = emotion_detector("I am so afraid")
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
