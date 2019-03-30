import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
# from kivy.garden
from kivy.uix.textinput import TextInput
import time
from Code.Scripts.predict import predict
from kivy.properties import StringProperty,ColorProperty,NumericProperty,BooleanProperty
from Code.Scripts.Analysis import count_tweets,count_unique_tweets
kivy.require("1.10.0")


loginids = {"yash":"yash","vivek":"vivek","animesh":"animesh"}

class HomeLogoImage(Image):
    pass


class FeedbackScreen(Screen):
    button_visible = NumericProperty()
    label_visible = NumericProperty()
    button_disabled = BooleanProperty()
    entered_text_nav = StringProperty()
    entered_text_cost = StringProperty()
    entered_text_response = StringProperty()
    entered_text_others = StringProperty()

    def __init__(self, **kwargs):
        super(FeedbackScreen, self).__init__(**kwargs)
        self.entered_text_nav = "Kindly rate us and let us know your valuable feedback"
        self.entered_text_cost = "Kindly rate us and let us know your valuable feedback"
        self.entered_text_response = "Kindly rate us and let us know your valuable feedback"
        self.entered_text_others = "Kindly rate us and let us know your valuable feedback"
        self.label_visible = 0
        self.button_visible = 1
        self.button_disabled = False

    def submit(self,nav,cost,response,others):
        print("Pressed")
        text = ""
        text += "nav : "+nav
        text += "\ncost : "+cost
        text += "\nresponse : "+response
        text += "\nothers : "+others
        file_name = str(int(time.time()))+".txt"
        with open("C:\\Users\\Vivek Rao\\PycharmProjects\\Campaign-Assistant-master\\Code\\Resources\\Feedback\\"+file_name, 'w') as txt_file:
            txt_file.writelines(text)
        self.label_visible = 1
        self.button_visible = 0
        self.button_disabled = True

    def clear_text_others(self):
        self.entered_text_others = ""

    def clear_text_response(self):
        self.entered_text_response = ""

    def clear_text_cost(self):
        self.entered_text_cost = ""

    def clear_text_nav(self):
        self.entered_text_nav = ""


class TextInputFeedbackScreen(TextInput):
    pass


class AnalysisScreen(Screen):
    tweets_collected = StringProperty()
    unique_tweets = StringProperty()
    positives = StringProperty()
    negatives = StringProperty()

    def __init__(self, **kwargs):
        super(AnalysisScreen,self).__init__(**kwargs)
        self.unique_tweets = '0'
        self.tweets_collected = '0'
        self.positives = '0'
        self.negatives = '0'

    def refresh_values(self):
        print("Refreshed")
        self.tweets_collected = str(count_tweets())
        self.unique_tweets = str(count_unique_tweets())
        self.negatives = 'no data'
        self.positives = 'no data'
        print(self.tweets_collected)
        print(self.unique_tweets)


class LoginScreen(Screen):
    pass


class LoginScreenTextInput(TextInput):
    pass


class LoginLogoImage(Image):
    pass


class LoginScreenLabel(Label):
    pass


class LoginScreenButton(Button):

    def __init__(self,**kwargs):
        super(LoginScreenButton,self).__init__(**kwargs)

    def pressed(self,user_id,password):
        print("pressed")


class AboutUsScreenDescriptionLabel(Label):
    pass


class AboutUsScreenLabel(Label):
    pass


class AboutUsScreen(Screen):
    pass


class PopularityGraphScreen(Screen):
    pass


class TopicLabel(Label):
    pass


class WordCloudScreen(Screen):
    path_to_cloud = StringProperty()

    def __init__(self,**kwargs):
        super(WordCloudScreen,self).__init__(**kwargs)
        self.path_to_cloud = "C:\\Users\\Vivek Rao\\PycharmProjects\\Campaign-Assistant-master\\Code\\Resources\\dummy_cloud.png"

    def on_select(self,text):
        print(text," selected")
        if "rahul" in text.lower():
            self.path_to_cloud = "C:\\Users\\Vivek Rao\\PycharmProjects\\Campaign-Assistant-master\\Code\\Resources\\rahul_cloud.png"
        elif "modi" in text.lower():
            self.path_to_cloud = "C:\\Users\\Vivek Rao\\PycharmProjects\\Campaign-Assistant-master\\Code\\Resources\\modi_cloud.png"


class LabelFeedbackScreen(Label):
    pass


class HomeScreen(Screen):
    pass


class LogoImage(Image):
    pass


class SentimentTestScreen(Screen):
    predicted_sentiment = StringProperty()
    predicted_sentiment_color = ColorProperty()

    def __init__(self, **kwargs):
        super(SentimentTestScreen, self).__init__(**kwargs)
        self.predicted_sentiment_color = [1,1,1,1]

    def predict_sentiment(self,input_text):
        predicted_value = predict(input_text)
        print("For the text input ",input_text,"; result is ",predicted_value)
        if predicted_value == -1:
            self.predicted_sentiment = "negative"
            self.predicted_sentiment_color = [1,0,0.4,1]
        elif predicted_value == 1:
            self.predicted_sentiment = "positive"
            self.predicted_sentiment_color = [0,1,0.6,1]

        else:
            self.predicted_sentiment = "can not classify"


class AnalysisScreenLabel(Label):
    pass


class ScreenManagement(ScreenManager):
    pass


class HomeScreenButton(Button):
    pass


class BackButton(Button):
    pass


kivy_file = Builder.load_file('CampaignAssistantGui.kv')


class MyApp(App):

    def build(self):
        return kivy_file


if __name__ == "__main__":
    MyApp().run()
