"""

    Simple Streamlit webserver application for serving developed classification
    models.

    Author: TEAM_3_DBN

    Description: This file is used to launch a minimal streamlit web
    application. You are expected to extend the functionality of this script
    as part of your predict project.

"""
###------------------------IMPORT LIBRARIES------------------------###

# Streamlit dependencies
import streamlit as st
import joblib,os


# Data dependencies
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import random
from datetime import date, timedelta
import tweepy as tw

# Plotting dependencies
import seaborn as sns
import matplotlib.style as style 
sns.set(font_scale=3.5)

###------------------------DEFINE DATA------------------------###

# Load pipeline model

model_svc = joblib.load('resources/lscv_model.pkl')
model_lr = joblib.load('resources/lr_model.pkl')
model_knn = joblib.load('resources/knn_model.pkl')

# Load your raw data
raw = pd.read_csv("resources/train.csv")


# List of all Most Frequent pro hashtags

pro_hash = ['#climate','#BeforeTheFlood','#climatechange','#ImVotingBecause','#COP22',
 '#ParisAgreement','#ActOnClimate','#globalwarming','#environment',
 '#BeforetheFlood','#NoDAPL','#science','#ClimateCounts','#ClimateAction','#qanda',
 '#EarthDay','#EarthToMarrakech','#EPA','#ClimateChangeIsReal',
 '#EarthHour','#Women4Climate','#ClimateMarch','#Africa','#climatemarch',
 '#Cities4Climate','#actonclimate','#itstimetochange','#SDGs','#CleanPowerPlan',
 '#SaveTheEPA','#swingdist','#energy','#education','#StrongerTogether','#globalgoals',
 '#agriculture','#IoT','#Sustainability','#StepsToReverseClimateChange','#globalcitizen',
 '#IntForestDay','#adaptation','#marchforscience','#vegan','#WhyIMarch','#WorldVeganDay',
 '#health','#ClimateFacts','#StandUp','#ClimateofHope','#EarthHourUK','#ThursdayThoughts',
 '#cleanenergy','#showthelove','#MyClimateAction','#Climatechange','#WomensMarch',
 '#NatGeo','#beforetheflood','#actuallivingscientist','#G20','#QandA','#green','#eco',
 '#GreenNewDeal','#UniteBlue','#MarchForScience','#SDG13','#WEF','#Analytics','#deforestation',
 '#ClimateVoter','#Iamwithher','#SaveOurOcean','#AMJoy','#foodsecurity','#mitigation']

# List of Brand ambassodors available, who are pro climate change

people = ['Amy Harmon','Bill Nye','Bill McKibben','Brenda Ekwurzel','Ellie Goulding',
          'Hugh Evans','John Legend','Leonardo DiCaprio' ,'McKenzie Wark','Neil deGrasse Tyson',
          'Oliver Milman' ,'Susan Sarandon','Taylor Swift' ,'William LeGate']

organisations = ['Beyond Coal','ClimateLaunchpad','Docsforclimate','Earth Life',
                 'Environmental Protection Agency','Greenpeace',
                 'Rainforest Connection','SUSTAIN-Africa','The Climate Reality Project',
                'The YEARS Project']

# List of visualisations to use for insights and information page

viz = ['How Tweets are spread' ,'Most Used Words',
       'Length of Tweets','Most used Emojis' ]

# List of all models

all_models = ['Linear SVC' , 'Logistic regression' , 'K nearest neighbors']


# Twitter API Keys

CONSUMER_KEY    = 'egoItCf7bZMp4gopTCXC0WH2O'
CONSUMER_SECRET = 'Ph7fyNWzMnLTb0rgx5w0GPb0bzWlfyUtfVhZZGt5jVk4FJeBxK'

ACCESS_TOKEN  = '840149748354965504-6fGpkvdj6n53uVG5231Oq6PhyLzHlfO'
ACCESS_SECRET = 'f17t2HIfmpsgh1IBxgdugigEH8Xuzhps7gjGT2jfLOgxT'

       
# The main function where we will build the actual app

def main():
    """Tweet Classifier App with Streamlit """

    # Creates a main title and subheader on your page -
    # these are static across all pages
    # st.title("Climate Change Belief Predictor")
    # st.subheader("Predict if a person believes in climate change based on thier tweet")
    
    html_temp = """
	<div style="background-color:lightblue;padding:10px">
	<h2 style="color:white;text-align:center;">Climate Change Business Targeting App </h2>
	</div>
    
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    #st.subheader("Predict if a person believes in climate change based on thier tweet")
    
    # Creating sidebar with selection box -
    # you can create multiple pages this way
    
    options = ['Welcome',"Tweet analyser", "Hashtag Generator",
              'Ambassadors & Partners','Live Sentiment Analysis']
    # selection = st.sidebar.selectbox("Select Activity", options)
    selection = st.sidebar.radio(label="Select Activity",  
                                    options=options)
                                    
    # Building out landing page
    
    if selection == 'Welcome' :
        video_file = open('resources/imgs/Landing_video.mp4', 'rb')
        video_bytes = video_file.read()        
        st.video(video_bytes)
        
    
    # Building out Brand Ambassodors page ( Organisation & People )
    if selection == 'Ambassadors & Partners' :
        st.subheader('Align your business with PRO climate change organisations and people')
        cat = ['Organisations' , 'People' ]
        sel = st.selectbox('Select Category' , cat)
        
        # Build Organisation Selection
        
        if sel == 'Organisations' :            
            sel_org = st.selectbox('Select Organisation' , organisations )
            
            # Beyond coal    
            if sel_org == 'Beyond Coal' :
                st.subheader('Beyond Coal')
                img = Image.open('resources/imgs/Org/beyond_coal.jpg')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('The Beyond Coal movement is a campaign by environmental '\
                            'group the Sierra Club to promote renewable energy instead of coal. ' \
                            'Their primary objective is to close coal power plants in the United States.')
                st.subheader('Get in touch')
                st.markdown('https://beyond-coal.eu/')
                
            # Epa
            if sel_org == 'Environmental Protection Agency' :
                st.subheader('Environmental Protection Agency')
                img = Image.open('resources/imgs/Org/epa.png')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('The Environmental Protection Agency is an independent agency,' \
                            'specifically an independent executive agency, of the United States' \
                            'federal government for environmental protection.')
                st.subheader('Get in touch')
                st.markdown('https://www.epa.gov/')
                
            # Rainforest
            if sel_org == 'Rainforest Connection' :
                st.subheader('Rainforest Connection')
                img = Image.open('resources/imgs/Org/rainforest.jpg')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('Rainforest Connection (RFCx) creates acoustic monitoring' \
                            'systems for those who wish to end illegal deforestation in real-time.')
                st.subheader('Get in touch')
                st.markdown('https://rfcx.org/home')
                
            # Sustain    
            if sel_org == 'SUSTAIN-Africa' :
                st.subheader('SUSTAIN-Africa')
                img = Image.open('resources/imgs/Org/sustain_africa.png')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('SUSTAIN-Africa is an IUCN-led initiative supporting Inclusive'\
                            'Green Growth (IGG) in Africa, with a particular focus on implementing'\
                            'a shared vision of economic growth, ecosystem resilience and social'\
                            'prosperity in Africa.')
                st.subheader('Get in touch')
                st.markdown('http://www.waterandnature.org/initiatives/sustain')
                
            # ClimateLaunchPad
            if sel_org == 'ClimateLaunchpad' :
                st.subheader('ClimateLaunchpad')
                img = Image.open('resources/imgs/Org/climate_lp.jpg')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('ClimateLaunchpad is the world’s largest green business ideas competition.'\
                            'Our mission is to unlock the world’s cleantech potential that addresses' \
                            'climate change. The competition creates a stage for those ideas.')
                st.subheader('Get in touch')
                st.markdown('https://climatelaunchpad.org/')
                
            # ClimateReality
            if sel_org == 'The Climate Reality Project' :
                st.subheader('The Climate Reality Project')
                img = Image.open('resources/imgs/Org/climate_reality.jpg')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('The Climate Reality Project is a non-profit organization'\
                            'involved in education and advocacy related to climate change.')
                st.subheader('Get in touch')
                st.markdown('https://www.climaterealityproject.org/')
                
            # The Years Project
            if sel_org == 'The YEARS Project' :
                st.subheader('The YEARS Project')
                img = Image.open('resources/imgs/Org/the_years_project.jpg')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('The YEARS Project is an education and communications effort' \
                            'designed to elevate climate change as the biggest issue of our time.')
                st.subheader('Get in touch')
                st.markdown('https://theyearsproject.com/')
                
            # Docforclimate
            if sel_org == 'Docsforclimate' :
                st.subheader('Docsforclimate')
                img = Image.open('resources/imgs/Org/doc_for_climate.png')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('The purpose of the letter is to increase public and political awareness' \
                            'about the urgency of climate change and to demonstrate the link' \
                            'between climate change and health. In addition, the letter' \
                            'specifies measures that are needed to reduce greenhouse gas emissions.')
                st.subheader('Get in touch')
                st.markdown('https://www.docsforclimate.be/')
            
            # Earth Life    
            if sel_org == 'Earth Life' :
                st.subheader('Earth Life')
                img = Image.open('resources/imgs/Org/earth_life.jpg')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('Earthlife Africa’s Johannesburg branch was founded in 1988' \
                            'to mobilise civil society around environmental issues in relation to people.')
                st.subheader('Get in touch')
                st.markdown('https://earthlife.org.za/')
                
            # Greenpeace
            if sel_org == 'Greenpeace' :
                st.subheader('Greenpeace')
                img = Image.open('resources/imgs/Org/greenpeace.png')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('Greenpeace is a non-governmental environmental organization'\
                            'with offices in over 55 countries and an international coordinating'\
                            'body in Amsterdam, the Netherlands'\
                            'Greenpeace exists because this fragile earth deserves a voice.'\
                            'It needs solutions. It needs change. It needs action.')
                st.subheader('Get in touch')
                st.markdown('https://www.greenpeace.org/international/')

        # Build people selection
        
        else :
            sel_people = st.selectbox('Select Person' , people )
            
            # Neil deGrasse Tyson
            if sel_people == 'Neil deGrasse Tyson' :                
                st.subheader('Neil deGrasse Tyson')
                img = Image.open('resources/imgs/People/Neil_tyson.jpg')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('Neil deGrasse Tyson is an American astrophysicist, cosmologist,' \
                            'planetary scientist, author, and science communicator. Since 1996,'\
                            'he has been the Frederick P. Rose Director of the Hayden Planetarium'\
                            'at the Rose Center for Earth and Space in New York City.')
                st.subheader('Get in touch')
                st.markdown('https://twitter.com/neiltyson')
                
            # Bill McKibben
            if sel_people == 'Bill McKibben' :                
                st.subheader('Bill McKibben')
                img = Image.open('resources/imgs/People/Bill_Mc.jpg')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('William Ernest "Bill" McKibben is an American environmentalist,'\
                            'author, and journalist who has written extensively on the impact'\
                            'of global warming. He is the Schumann Distinguished Scholar at Middlebury College'\
                            'and leader of the climate campaign group 350.org.')
                st.subheader('Get in touch')
                st.markdown('https://twitter.com/billmckibben')
                
            
            
            # McKenzie Wark
            if sel_people == 'McKenzie Wark' :                
                st.subheader('McKenzie Wark')
                img = Image.open('resources/imgs/People/McKenzie.jpg')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('McKenzie Wark (born 1961) is an Australian-born writer and scholar.'\
                            'Wark is known for her writings on media theory, critical theory,'\
                            'new media, and the Situationist International. Her best known works'\
                            'are A Hacker Manifesto and Gamer Theory. She is Professor of Media and Cultural Studies'\
                            'at The New School in New York City. Wark is a trans woman; her pronouns are she/her.')
                st.subheader('Get in touch')
                st.markdown('https://twitter.com/mckenziewark')
                
            # Leonardo DiCaprio
            if sel_people == 'Leonardo DiCaprio' :                
                st.subheader('Leonardo DiCaprio')
                img = Image.open('resources/imgs/People/Leo.jpg')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('Leonardo Wilhelm DiCaprio is an American actor and producer.'\
                            'He has often played unconventional parts, particularly in biopics and period films.'\
                            'As of 2019, his films have earned US$7.2 billion worldwide,'\
                            'and he has placed eight times in annual rankings of the worlds highest-paid actors.')
                st.subheader('Get in touch')
                st.markdown('https://twitter.com/LeoDiCaprio')
                
                
            # Neil deGrasse Tyson
            if sel_people == 'Susan Sarandon' :                
                st.subheader('Susan Sarandon')
                img = Image.open('resources/imgs/People/Susan.jpg')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('Susan Abigail Sarandon is an American actress and activist.'\
                            'She has received an Academy Award, a British Academy Film Award,'\
                            'and a Screen Actors Guild Award, and has been nominated for nine Golden Globe Awards.'\
                            'Known for her social and political activism, she was appointed'\
                            'a UNICEF Goodwill Ambassador in 1999 and received the Action Against Hunger Humanitarian Award in 2006.')
                st.subheader('Get in touch')
                st.markdown('https://twitter.com/SusanSarandon')
                
            # Brenda Ekwurzel
            if sel_people == 'Brenda Ekwurzel' :                
                st.subheader('Brenda Ekwurzel')
                img = Image.open('resources/imgs/People/Brenda.jpg')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('Brenda Ekwurzel is a senior climate scientist and the director of climate'\
                            'science for the Climate & Energy Program at the Union of Concerned Scientists (UCS).'\
                            'In her role, she ensures that program analyses reflect robust and relevant climate science,'\
                            'and researches the influence of major carbon producers on rising global average temperatures and sea level.')
                st.subheader('Get in touch')
                st.markdown('https://twitter.com/BrendaEkwurzel')
                
            # Oliver Milman
            if sel_people == 'Oliver Milman' :                
                st.subheader('Oliver Milman')
                img = Image.open('resources/imgs/People/Oliver.jpg')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('Oliver Milman is an environment reporter for Guardian US.')
                st.subheader('Get in touch')
                st.markdown('https://twitter.com/olliemilman')
                
            # Ellie Goulding
            if sel_people == 'Ellie Goulding' :                
                st.subheader('Ellie Goulding')
                img = Image.open('resources/imgs/People/Ellie.jpg')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('Elena Jane Goulding is an English singer and songwriter.'\
                            'Her career began when she met record producers Starsmith and Frankmusik,'\
                            'and she was later spotted by Jamie Lillywhite, who later became her manager and A&R.'\
                            'After signing to Polydor Records in July 2009, Goulding released her debut extended play,'\
                            'An Introduction to Ellie Goulding later that year.')
                st.subheader('Get in touch')
                st.markdown('https://twitter.com/elliegoulding')
                
            # Hugh Evans
            if sel_people == 'Hugh Evans' :                
                st.subheader('Hugh Evans')
                img = Image.open('resources/imgs/People/Hugh.jpg')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('Hugh Evans is an Australian humanitarian. Evans is the co-founder of'\
                            'both The Oaktree Foundation and Global Citizen, a Global Poverty Project.'\
                            'He has received domestic and international accolades for his work'\
                            'in promoting youth advocacy and volunteerism in order to reduce extreme poverty in developing countries.')
                st.subheader('Get in touch')
                st.markdown('https://twitter.com/Hughcevans')
                
            # William LeGate
            if sel_people == 'William LeGate' :                
                st.subheader('William LeGate')
                img = Image.open('resources/imgs/People/William.jpg')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('William LeGate is an American entrepreneur, Thiel Fellow,'\
                            'computer programmer and activist. A self-taught programmer from the age of 12,'\
                            'LeGate was brought to the publics attention three years later when The New York Times'\
                            'recommended one of the iOS applications he had programmed during middle school.')
                st.subheader('Get in touch')
                st.markdown('https://twitter.com/williamlegate')
                
            
            # Taylor Swift
            if sel_people == 'Taylor Swift' :                
                st.subheader('Taylor Swift')
                img = Image.open('resources/imgs/People/Taylor.jpg')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('Taylor Alison Swift is an American singer-songwriter.'\
                            'She is known for her narrative songwriting, that often centers'\
                            'around her personal life and has received widespread critical praise and media coverage.')
                st.subheader('Get in touch')
                st.markdown('https://twitter.com/taylorswift13')
                
            # Amy Harmon
            if sel_people == 'Amy Harmon' :                
                st.subheader('Amy Harmon')
                img = Image.open('resources/imgs/People/Amy.jpg')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('Amy Harmon (born September 17, 1968) is an American journalist.'\
                            'She won a Pulitzer Prize as a correspondent for The New York Times'\
                            'covering the impact of science and technology on everyday life.'\
                            'Harmon uses narrative storytelling to illuminate the human dilemmas'\
                            'posed by advances in science. In 2013, she was named a Guggenheim Fellow.')
                st.subheader('Get in touch')
                st.markdown('https://twitter.com/amy_harmon')
                
            
            # John Legend
            if sel_people == 'John Legend' :                
                st.subheader('John Legend')
                img = Image.open('resources/imgs/People/John.jpg')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('John Roger Stephens, known professionally as John Legend,'\
                            'is an American singer, songwriter, producer, actor, and philanthropist.'\
                            'Prior to the release of Legends debut album, Get Lifted,'\
                            'he had collaborated with already established artists and signed to Kanye West GOOD Music.')
                st.subheader('Get in touch')
                st.markdown('https://twitter.com/johnlegend')
                
            # Bill Nye
            if sel_people == 'Bill Nye' :                
                st.subheader('Bill Nye')
                img = Image.open('resources/imgs/People/Bill_Nye.jpg')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('William Sanford Nye, popularly known as Bill Nye the Science Guy,'\
                            'is an American science communicator, television presenter, and mechanical engineer.'\
                            'He is best known as the host of the PBS and syndicated childrens science'\
                            'show Bill Nye the Science Guy, the Netflix show Bill Nye Saves the World,'\
                            'and for his many subsequent appearances in popular media as a science educator.')
                st.subheader('Get in touch')
                st.markdown('https://twitter.com/BillNye')

    
    # Building out Hashtag generation page
    if selection == 'Hashtag Generator' :
        st.subheader('Generate Hashtags your business can use for social media ads')
        num_hash = st.slider('Select number of Hashtags to generate' , 1, 10 )
        if st.button("Generate"):           
            rand_hash = random.sample(pro_hash,num_hash) 
            for i in range(len(rand_hash)):                
                st.success(rand_hash[i])
            
    # Building out the predication page
    if selection == "Tweet analyser":
        st.subheader("Predict a person's stance on climate change based on their tweet")
        # Creating a text box for user input
        tweet_text = st.text_area("Enter Tweet")
        # Create tweet classifier logic ( with 3 models )
        
        model_list = st.selectbox('Select classification model ' , all_models)

        if model_list == 'Linear SVC' :
            final_model = model_svc
        elif model_list == 'Logistic regression' :
            final_model = model_lr
        else :
            final_model = model_knn
        
        if st.button("Classify"):
                  
            # Transforming user input with vectorizer
            vect_text = [tweet_text]
            prediction = final_model.predict(vect_text)
              
            if prediction[0] == 0:
                prediction = 'Neutral'
                c_img = Image.open('resources/imgs/neutral.png')

            elif prediction[0] == 1:
                prediction = 'PRO Climate Change'
                c_img = Image.open('resources/imgs/pro.png')

            elif prediction[0] == 2:
                prediction = 'Factual News'
                c_img = Image.open('resources/imgs/news.png')

            else:
                prediction = 'ANTI Climate Change'
                c_img = Image.open('resources/imgs/anti.png')
  
            st.success("This Tweet is : {}".format(prediction))
            st.image(c_img,width=100)
        
    
    # Build Live Tweet Streaming page
    
    if selection == "Live Sentiment Analysis":
            st.subheader("Gauge how people felt about climate change in the last 24-hours")
            disp = Image.open('resources/imgs/twitter_api.png')
            st.image(disp,width=100)
            if st.button("Generate Daily Sentiment"):
                
                # Define Twitter API authentication
                with st.spinner('Collecting Tweets, Please Wait...'):
                    auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
                    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
                    api = tw.API(auth, wait_on_rate_limit=True)

                    # Twitter search words

                    search_words = "#climatechange" + " -filter:retweets"

                    # Get yesterdays date
                    today = date.today()
                    yesterday = today - timedelta(days = 1)
                    date_since = yesterday

                    tweets = tw.Cursor(api.search,
                               q=search_words,
                               lang="en",
                               since=date_since).items(200)

                    # Collect a list of tweets

                    tweet_list = [tweet.text for tweet in tweets]

                    tweet_df = pd.DataFrame(data=tweet_list, 
                        columns=['message'])

                    # Predict the sentiment

                    X = tweet_df['message']
                    y_pred = model_svc.predict(X)
                    tweet_df['sentiment'] = y_pred
                    
                    # Displaying target distribution

                    fig, axes = plt.subplots(figsize=(25, 20))

                    pie_chart = axes.pie(tweet_df['sentiment'].value_counts(),
                                labels=['Pro', 'News', 'Neutral', 'Anti'])
                    
                    fig.suptitle('Distribution of the Tweets', fontsize=35)
                st.success('Done!')
                st.pyplot()                
                
            
            
# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
    main()
