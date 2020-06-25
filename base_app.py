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
sns.set(font_scale=4.5)

###------------------------LOAD & DEFINE DATA------------------------###

# Load pipeline models

model_svc = joblib.load('resources/lscv_model.pkl')
model_lr = joblib.load('resources/lr_model.pkl')
model_knn = joblib.load('resources/knn_model.pkl')

# Load your raw data
raw = pd.read_csv("resources/train.csv")


# Most Frequent pro hashtags

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

# Brand ambassodors available, People & Organisations

people = ['Candice Hutchings','Immy Lucas','Leonardo DiCaprio' ,'McKenzie Wark','Neil deGrasse Tyson',
          'Sedona Christina','Shelbizleee','Susan Sarandon','Taylor Swift' ,'William LeGate']

organisations = ['Beyond meat','Earth Life','EcoPlum','LushCosmetics','Numi Organic Tea',
                 'Patagonia' ,'Seventh Generation','SUSTAIN-Africa','The Climate Reality Project',
                'The YEARS Project']

# Visualisations list to use for EDA & Insights page

viz = ['Tweet distribution' ,'Buzzwords',
       'Length of Tweets','Most used Emojis']

# All models used

all_models = ['Linear SVC' , 'Logistic Regression' , 'K Nearest Neighbors']


# Twitter API Keys

CONSUMER_KEY    = 'egoItCf7bZMp4gopTCXC0WH2O'
CONSUMER_SECRET = 'Ph7fyNWzMnLTb0rgx5w0GPb0bzWlfyUtfVhZZGt5jVk4FJeBxK'

ACCESS_TOKEN  = '840149748354965504-6fGpkvdj6n53uVG5231Oq6PhyLzHlfO'
ACCESS_SECRET = 'f17t2HIfmpsgh1IBxgdugigEH8Xuzhps7gjGT2jfLOgxT'

       
###-----------------------------BUILD APP----------------------------------###

def main():
    """Find your niche App with Streamlit """
    
    html_temp = """
	<div style="background-color:lightblue;padding:10px">
	<h2 style="color:white;text-align:center;">FIND YOUR NICHE </h2>
	</div>
    
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    # Creating sidebar with selection box
    
    options = ['Welcome','EDA & Insights',"Tweet analyser", "Hashtag Generator",
              'Ambassadors & Partners','Live Sentiment Analysis' , 'About Us']
    selection = st.sidebar.radio(label="Select Activity",  
                                    options=options)
                                    
    # Build Welcome page
    
    if selection == 'Welcome' :
        st.markdown('')
        st.markdown('The **Find your niche** app , helps environmentally conscious companies gain **valuable market insights** '\
                    'and maximise their business **marketing strategy** by using cutting edge machine learning tools to efficiently '\
                   '**target potential customers** on Twitter.')
        
        img = Image.open('resources/imgs/Landing_page_image.png')
        st.image(img,width=710)
        
        video_file = open('resources/imgs/Landing_video.mp4', 'rb')
        video_bytes = video_file.read()        
        st.video(video_bytes)
        
    # Build About us page
    
    if selection == 'About Us' :
        
        st.header('Meet the team that made it happen')
        
        st.markdown('')
        st.markdown('**Mandla**')
        img = Image.open('resources/imgs/mandla.jpg')
        st.image(img,width=180)
        st.markdown('https://www.linkedin.com/in/mandla-solomon-095063121/')
        st.markdown('https://github.com/0731325603')
        
        st.markdown('')
        st.markdown('**Chris**')
        img = Image.open('resources/imgs/chris.jpg')
        st.image(img,width=180)
        st.markdown('https://www.linkedin.com/in/nhlanhla-christopher-mahlangu-56b771137/')
        st.markdown('https://github.com/NhlanhlaChris')
        
        st.markdown('')
        st.markdown('**Nicole**')
        img = Image.open('resources/imgs/nicole.jpg')
        st.image(img,width=180)
        st.markdown('http://www.linkedin.com/in/nicole-meinie-xolisa')
        st.markdown('https://github.com/NicoleMeinie')
        
        st.markdown('')
        st.markdown('**Sibonelo**')
        img = Image.open('resources/imgs/sibonelo.jpeg')
        st.image(img,width=180)
        st.markdown('https://www.linkedin.com/in/sibonelo-junior-malakiya-62302b144/')
        st.markdown('https://github.com/SiboneloJunior')
        
        st.markdown('')
        st.markdown('**Philani**')
        img = Image.open('resources/imgs/philani.jpg')
        st.image(img,width=180)
        st.markdown('https://www.linkedin.com/in/philani-mkhize-519995149/')
        st.markdown('https://github.com/Jamakasilwane')
        
                
    # Building Ambassodors & Partners page ( Organisation & People )
    
    if selection == 'Ambassadors & Partners' :
        st.subheader('Align your business with PRO climate change organisations and people')
        cat = ['Organisations' , 'People' ]
        sel = st.selectbox('Select Category' , cat)
        
        # Build Organisation Selection
        
        if sel == 'Organisations' :            
            sel_org = st.selectbox('Select Organisation' , organisations )
            
            # Patagonia    
            if sel_org == 'Patagonia' :
                st.subheader('Patagonia')
                img = Image.open('resources/imgs/Org/patagonia.jpeg')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('Activewear retailers, selling everything from snow gear to fleece '\
                            'to sleeping bags that appeal to the all-things-adventure crowd. '\
                            'Patagonia’s corporate philosophy is all about going green. '\
                            'They’ve built repair centers around the world to increase the longevity '\
                            'of their products and lower their carbon footprint.')
                st.subheader('Get in touch')
                st.markdown('https://www.patagonia.com/home/')
                
            # LushCosmetics
            if sel_org == 'LushCosmetics' :
                st.subheader('LushCosmetics')
                img = Image.open('resources/imgs/Org/lush.png')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('An all-natural bath and body brand that makes everything from shampoos '\
                            'and fragrances to massage bars and bath bombs that inspire worship from '\
                            'beauty bloggers around the globe. Lush is dedicated to eco-friendly products '\
                            'and practices, like creating solid shampoo bars to reduce packaging waste '\
                            'and offering free products to customers who bring in empty product packaging to recycle.')
                st.subheader('Get in touch')
                st.markdown('https://www.lushusa.com/')
                
            # EcoPlum
            if sel_org == 'EcoPlum' :
                st.subheader('EcoPlum')
                img = Image.open('resources/imgs/Org/eco_plum.jpg')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('EcoPlum Business Gifts aims to disrupt the promotional products '\
                            'industry and reduce the amount of plastic and other waste produced '\
                            'by this industry. EcoPlum will help you choose the best product for '\
                            'your audience, have it customized with your branded logo or message, '\
                            'and ensure it lives up to rigorous standards for environmental and social sustainability.')
                st.markdown('https://business.ecoplum.com/')
                
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
                
            # Seventh Generation
            if sel_org == 'Seventh Generation' :
                st.subheader('Seventh Generation')
                img = Image.open('resources/imgs/Org/seven.png')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('Seventh Generation is a cleaning products company that revolutionized '\
                            'the cleaning industry with eco-friendly cleaning products free of harmful '\
                            'toxins and chemicals. Seventh Generation is a pretty traditional green company, '\
                            'but the secret to their success is how they’ve been able to expand outside '\
                            'of the typical customer base by highlighting product benefits that appeal '\
                            'to all consumers—not just eco-folks.')
                st.subheader('Get in touch')
                st.markdown('https://www.seventhgeneration.com/home')
                
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
                
            # Beyond meat
            if sel_org == 'Beyond meat' :
                st.subheader('Beyond meat')
                img = Image.open('resources/imgs/Org/beyond_meat.jpg')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('Beyond Meat is shaking up the food industry by creating delicious, '\
                            'plant-based “meat” products (carnivore approved!) that are better for ' \
                            'human health, the environment, climate change and animals. All of Beyond ' \
                            'Meat’s branding focuses on the good they’re doing for the environment ' \
                            'and their consumers. By combining cool graphics and drool-worthy product photos, '\
                            'they’re able to show the benefit on all sides: how their products are saving ' \
                            'the planet while saving their consumers’ bodies.')
                st.subheader('Get in touch')
                st.markdown('https://www.beyondmeat.com/')
            
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
                
            # Numi Organic Tea
            if sel_org == 'Numi Organic Tea' :
                st.subheader('Numi Organic Tea')
                img = Image.open('resources/imgs/Org/numi_tea.jpg')
                st.image(img,width=150)
                st.subheader('Who are they?')
                st.markdown('Numi Tea’s design and branding screams organic and eco-friendly. '\
                            'Just like green practices are a part of their brand DNA, that '\
                            'eco-friendly vibe is a part of their design DNA as well. '\
                            'Everything in Numi Tea’s design and branding screams organic and eco-friendly. '\
                            'Just like green practices are a part of their brand DNA, that eco-friendly '\
                            'vibe is a part of their design DNA as well. Numi uses a lot of earth tones '\
                            'like brown in their design and branding. This isn’t super common, '\
                            'but makes total sense for an organic brand.')
                st.subheader('Get in touch')
                st.markdown('https://numitea.com/')

        # Build people selection
        
        else :
            sel_people = st.selectbox('Select Person' , people )
            
            # Neil deGrasse Tyson
            if sel_people == 'Neil deGrasse Tyson' :                
                st.subheader('Neil deGrasse Tyson')
                img = Image.open('resources/imgs/People/Neil_tyson.jpg')
                st.image(img,width=180)
                st.subheader('Who are they?')
                st.markdown('Neil deGrasse Tyson is an American astrophysicist, cosmologist,' \
                            'planetary scientist, author, and science communicator. Since 1996,'\
                            'he has been the Frederick P. Rose Director of the Hayden Planetarium'\
                            'at the Rose Center for Earth and Space in New York City.')
                st.subheader('Get in touch')
                st.markdown('https://twitter.com/neiltyson')
                
            # Candice Hutchings
            if sel_people == 'Candice Hutchings' :                
                st.subheader('Candice Hutchings')
                img = Image.open('resources/imgs/People/Candice.png')
                st.image(img,width=180)
                st.subheader('Who are they?')
                st.markdown('Candice, the face of “The Edgy Veg”, is on a journey to revolutionize '\
                            'how we think about food, eco-conscious living, and feminism. Author of the cookbook, '\
                            '”138 Carnivore-Approved Vegan Recipes”, Candice delivers vegan recipes '\
                            'with attitude and comedy. Edgy by nature, both her popular YouTube channel, '\
                            'and Instagram pages have disrupted the vegan community with her candid and '\
                            'humorous take on activism not only for animals and food built differently, '\
                            'but also mental health, the environment, and female empowerment. ')
                st.subheader('Get in touch')
                st.markdown('https://www.youtube.com/user/stillcurrentstudios/about')
                
            
            
            # McKenzie Wark
            if sel_people == 'McKenzie Wark' :                
                st.subheader('McKenzie Wark')
                img = Image.open('resources/imgs/People/McKenzie.jpg')
                st.image(img,width=180)
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
                st.image(img,width=180)
                st.subheader('Who are they?')
                st.markdown('Leonardo Wilhelm DiCaprio is an American actor and producer.'\
                            'He has often played unconventional parts, particularly in biopics and period films.'\
                            'As of 2019, his films have earned US$7.2 billion worldwide,'\
                            'and he has placed eight times in annual rankings of the worlds highest-paid actors.')
                st.subheader('Get in touch')
                st.markdown('https://twitter.com/LeoDiCaprio')
                
                
            # Susan Sarandon
            if sel_people == 'Susan Sarandon' :                
                st.subheader('Susan Sarandon')
                img = Image.open('resources/imgs/People/Susan.jpg')
                st.image(img,width=180)
                st.subheader('Who are they?')
                st.markdown('Susan Abigail Sarandon is an American actress and activist.'\
                            'She has received an Academy Award, a British Academy Film Award,'\
                            'and a Screen Actors Guild Award, and has been nominated for nine Golden Globe Awards.'\
                            'Known for her social and political activism, she was appointed'\
                            'a UNICEF Goodwill Ambassador in 1999 and received the Action Against Hunger Humanitarian Award in 2006.')
                st.subheader('Get in touch')
                st.markdown('https://twitter.com/SusanSarandon')
                
            # Sedona Christina
            if sel_people == 'Sedona Christina' :                
                st.subheader('Sedona Christina')
                img = Image.open('resources/imgs/People/Sedona.png')
                st.image(img,width=180)
                st.subheader('Who are they?')
                st.markdown('Sedona is a 25 year old Canadian living in Seattle, advocating sustainable vegan '\
                            'and intentional living. She describes herself as a millennial gal with a knack for wellness, '\
                            'movement, self care, entrepreneurialism, and leaving this world better than we found it.')
                st.subheader('Get in touch')
                st.markdown('https://www.youtube.com/user/720tanner/about')

                
                
            # Shelbizleee
            if sel_people == 'Shelbizleee' :                
                st.subheader('Shelbizleee')
                img = Image.open('resources/imgs/People/Shelbi.png')
                st.image(img,width=180)
                st.subheader('Who are they?')
                st.markdown('Shelbi has a Bachelor\'s degree in Environmental Science and a passion for sustainability. '\
                            'Her  mission for her  youtube channel is to create a community where the average person '\
                            'can come and feel like they can make a difference. Living a sustainable lifestyle can '\
                            'be a daunting task, but her videos can help you break it down step by step and explore '\
                            'the best tips & tricks of eco-minimalism.')
                st.subheader('Get in touch')
                st.markdown('https://www.youtube.com/user/Shelbizleee')
                
            # William LeGate
            if sel_people == 'William LeGate' :                
                st.subheader('William LeGate')
                img = Image.open('resources/imgs/People/William.jpg')
                st.image(img,width=180)
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
                st.image(img,width=180)
                st.subheader('Who are they?')
                st.markdown('Taylor Alison Swift is an American singer-songwriter.'\
                            'She is known for her narrative songwriting, that often centers'\
                            'around her personal life and has received widespread critical praise and media coverage.')
                st.subheader('Get in touch')
                st.markdown('https://twitter.com/taylorswift13')
                
            # Immy Lucas
            if sel_people == 'Immy Lucas' :                
                st.subheader('Immy Lucas')
                img = Image.open('resources/imgs/People/Immy.png')
                st.image(img,width=180)
                st.subheader('Who are they?')
                st.markdown('Immy is  the creator of the YouTube channel \'Sustainably Vegan\' and environmental movement, '\
                            'The Low Impact Movement. She describes herself as "just a regular person who loves '\
                            'the environment and tries their best everyday to lower their waste and live a low '\
                            'impact lifestyle."  She believes in the importance of intersectionality and inclusivity, '\
                            'which is why her channel is meant for everyone, whoever you are.')
                st.subheader('Get in touch')
                st.markdown('https://www.youtube.com/channel/UCkq2gEWE-i647M71bh7zDxA/about')
                

    
    # Building out Hashtag generation page
    
    if selection == 'Hashtag Generator' :
        st.subheader('Generate PRO climate change hashtags your business can use for social media ads')
        num_hash = st.slider('Drag the slider to select the number of Hashtags to generate' , 1, 10 )
        if st.button("Generate"):           
            rand_hash = random.sample(pro_hash,num_hash) 
            for i in range(len(rand_hash)):                
                st.success(rand_hash[i])
                
    # Build Market Research tools page
    
    if selection == "EDA & Insights":
        st.subheader("Relevant exploratory data analysis to aid your market research")
        
        select_viz = st.selectbox('Select Information' , viz)
        
        if select_viz == 'Tweet distribution' :
            disp = Image.open('resources/imgs/Tweet_distribution.png')
            st.image(disp,width=600)
            st.subheader('Insights')
            st.markdown('* Most tweets are PRO climate change - That is good news for environmentally conscious companies.')
            st.markdown('* 23% of the tweets are Facts/News - Meaning there is a lot of media coverage towards the topic.')
            
        if select_viz == 'Buzzwords' :
            disp_1 = Image.open('resources/imgs/word_cloud.png')
            st.image(disp_1,width=650)            
            st.subheader('Insights')
            st.markdown('* The top 3 buzzwords accross all classes are **climate**, **change** and **rt (Retweet)**.'\
                       'The frequency of **rt ( Retweet )** means that a lot of the same information and/or '\
                        'opinions are being shared and viewed by large audiences.')
            st.markdown('* In PRO climate change tweets... words like **real**, **believe**, **think** and **fight** occur frequently. ')
            st.markdown('* In contrast ANTI climate change tweets contain words like **hoax**, **scam**, **tax**, '
                        '**liberal** and **fake**.')
            
        if select_viz == 'Length of Tweets' :
            disp = Image.open('resources/imgs/tweet_length.png')
            st.image(disp,width=600)
            st.subheader('Insights')
            st.markdown('* PRO climate change tweets are generally longer with **consistent length** distribution ,'
                       'most tweets from this class aim to educate and raise awareness ,hence giving more attention and detail '\
                       'to the content.')
            st.markdown('* ANTI climate change tweets are generally shorter with **inconsistent length** distribution, '
                       'generally this is due to fact that most people who dismiss man-made climate change support their stance '\
                       'with other peoples theories , which often have no basis.')
            st.markdown('* Neutral climate change tweets tend to have the **most variability** in tweet length.')
            st.markdown('* News/Factual climate change tweets tend to have the **least variability** in tweet length, '
                       'Which is expected considering that news reporters aim to be consise and direct at all times.' )

        if select_viz == 'Most used Emojis' :
            disp = Image.open('resources/imgs/all_emojis.png')
            st.image(disp,width=600)
            st.subheader('Insights')
            st.markdown('* The Tweets emojis show varying sentiment , From expressing **care** and **concern** '\
                        '( i.e Heart and Globe emojis ) to an expression of **ridicule** and **disbelief** '\
                        '( i.e Laughing and Rolling eyes emojis ).')
            
    # Build Tweet analyser page
    
    if selection == "Tweet analyser":
        st.subheader("Predict a person's stance on climate change based on their tweet")
        
        # Creating a text box for user input
        tweet_text = st.text_area("Enter Tweet")
        
        # Create tweet classifier logic ( with 3 models )
        
        model_list = st.selectbox('Select classification model ' , all_models)

        if model_list == 'Linear SVC' :
            final_model = model_svc
        elif model_list == 'Logistic Regression' :
            final_model = model_lr
        else :
            final_model = model_knn
        
        if st.button("Classify"):
                  
            # Transform user input with vectorizer
            vect_text = [tweet_text]
            prediction = final_model.predict(vect_text)
              
            if prediction[0] == 0:
                prediction = 'Neutral'
                c_img = Image.open('resources/imgs/neutral.png')
                st.warning("This Tweet is : {}".format(prediction))
                st.image(c_img,width=100)

            elif prediction[0] == 1:
                prediction = 'PRO Climate Change'
                c_img = Image.open('resources/imgs/pro.png')
                st.success("This Tweet is : {}".format(prediction))
                st.image(c_img,width=100)

            elif prediction[0] == 2:
                prediction = 'Factual News'
                c_img = Image.open('resources/imgs/news.png')
                st.info("This Tweet is : {}".format(prediction))
                st.image(c_img,width=100)

            else:
                prediction = 'ANTI Climate Change'
                c_img = Image.open('resources/imgs/anti.png')
                st.error("This Tweet is : {}".format(prediction))
                st.image(c_img,width=100)
          
    
    # Build Live Tweet Streaming page
    
    if selection == "Live Sentiment Analysis":
            st.subheader("Gauge how people felt about climate change in the last 24-hours")
            disp = Image.open('resources/imgs/twitter_api.png')
            st.image(disp,width=250)
            if st.button("Generate Daily Sentiment"):
                
                # Define Twitter API authentication
                with st.spinner('Collecting 200 Latest Tweets, Please Wait...'):
                    auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
                    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
                    api = tw.API(auth, wait_on_rate_limit=True)

                    # Twitter search words

                    search_words = "#climatechange" + " -filter:retweets"

                    # Get yesterdays date
                    
                    today = date.today()
                    yesterday = today - timedelta(days = 1)
                    date_since = yesterday
                    
                    # Collect a list of tweets and store them in a df

                    tweets = tw.Cursor(api.search,
                               q=search_words,
                               lang="en",
                               since=date_since).items(200)                    

                    tweet_list = [tweet.text for tweet in tweets]

                    tweet_df = pd.DataFrame(data=tweet_list, 
                        columns=['message'])

                    # Predict the sentiment

                    X = tweet_df['message']
                    y_pred = model_svc.predict(X)
                    tweet_df['sentiment'] = y_pred
                    
                    # Calculate percentages
                    
                    pro_p = (len(tweet_df[tweet_df['sentiment'] == 1])/len(tweet_df))*100
                    anti_p = (len(tweet_df[tweet_df['sentiment'] == -1])/len(tweet_df))*100
                    news_p = (len(tweet_df[tweet_df['sentiment'] == 2])/len(tweet_df))*100
                    neutral_p = (len(tweet_df[tweet_df['sentiment'] == 0])/len(tweet_df))*100
                    
                    # Plot target distribution

                    fig, axes = plt.subplots(figsize=(35, 30))

                    pie_chart = axes.pie(tweet_df['sentiment'].value_counts(),
                                labels=[f'Pro ({round(pro_p ,2)}%)',
                                        f'News ({round(news_p,2)}%)',
                                        f'Neutral ({round(anti_p,2)}%)',
                                        f'Anti ({round(neutral_p,2)}%)'],
                                        )
                    
                    fig.suptitle('Distribution of the Tweets', fontsize=50)
                    plt.tight_layout()
                st.success('Done!')
                st.pyplot()                
                
            
            
# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
    main()
