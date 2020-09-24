from datetime import date, datetime
from ummalqura.hijri_date import HijriDate
import time


def FridaysAndFastingTimes():
    """The code used to check if today is the night of Monday or Thursday
        "to tweet about the Fasting on Mondays and Thursdays"
        Also check if it is the night of 13, 14 and 15th of the arabic month to
        tweet a reminder to fast these days"""
    while True:
        tweet_time = datetime.now().strftime("%H:%M:%S")

        """The next two conditions check for Sundays and Wednesdays in every week 
        to tweet at 6 pm to remind followers to fast the next day"""
        if all([datetime.now().strftime("%A").lower() in ['sunday', 'wednesday'], tweet_time == "18:00:00"]):  # Tweet on Sunday and Wednesday night at 6 pm
            time.sleep(1)  # this line to prevent python from sending the tweet many times in one second
            return 'لا تنسوا صيام يوم غد فقد ثبت عن رسول الله صلى الله عليه وسلم أنه كان يصوم الإثنين والخميس فقد قال صلى الله عليه وسلم: إنهما يومان تعرض فيهما الأعمال على الله، فأحب أن يعرض عملي وأنا صائم رواه مسلم في الصحيح '

        """Check if today is Friday or not """
        if datetime.now().strftime("%A").lower() == 'friday' and tweet_time == "12:00:00":  # Tweet on Friday morning at 10 am
            time.sleep(1)  # this line to prevent python from sending the tweet many times in one second
            return 'لانسوا قراءه سوره الكهف والاكثار من الصلاه على النبى صلى الله عليه وسلم يوم الجمعه'

        """Check if today the night of 13, 14, 15 to remind followers to fast the next day """
        ArabicDay = int(HijriDate.get_hijri_date(date.today()).split('-')[2])
        ArabicMonth = int(HijriDate.get_hijri_date(date.today()).split('-')[1])
        if all([ArabicDay in [12, 13, 14], ArabicMonth != 9, tweet_time == "22:00:00"]):
            time.sleep(1)
            return 'غدا هو يوم من الابام البيض. يستحب صيام ثلاثة أيام من كل شهر ، والأفضل أن تكون أيام البيض وهي الثالث عشر والرابع عشر والخامس عشر . وعن أبي ذر قال : قال لي رسول الله صلى الله عليه وسلم : " إذا صمت شيئاً من الشهر فصم ثلاث عشرة وأربع عشرة وخمس عشرة " .'
