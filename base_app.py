"""

    Simple Streamlit webserver application for serving developed classification
    models.

    Author: TEAM_3_DBN

    Description: This file is used to launch a minimal streamlit web
    application. You are expected to extend the functionality of this script
    as part of your predict project.

"""
# Streamlit dependencies
import streamlit as st
import joblib,os


# Data dependencies
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import random

# Load pipeline model

model = joblib.load('resources/lscv_model.pkl')

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

people = ['Neil deGrasse Tyson' , 'Bill McKibben',
          'McKenzie Wark' , 'Leonardo DiCaprio' ,'Susan Sarandon', 
         'Brenda Ekwurzel' , 'Oliver Milman' , 'Ellie Goulding',
         'Hugh Evans' ,'William LeGate','Taylor Swift' , 'Amy Harmon','John Legend',
         'Bill Nye']

organisations = ['Beyond Coal','Environmental Protection Agency','Rainforest Connection',
                'SUSTAIN-Africa','ClimateLaunchpad','The Climate Reality Project',
                'The YEARS Project','Docsforclimate','Earth Life',
                'Greenpeace']

# List of visualisations to use for insights and information page

viz = ['How Tweets are spread' ,'Most Used Words',
       'Length of Tweets','Named Entities' ,'Most used Emojis' ]
       

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
    options = ["Belief Predictor AI", "Hashtag Generator",
              'Ambassodors & Partners','Market Research Tools']
    selection = st.sidebar.selectbox("Select Activity", options)
    
    # Building out Brand Ambassodors page ( Organisation & People )
    if selection == 'Ambassodors & Partners' :
        st.subheader('Align your business with people and organisations who believe in climate change')
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
                st.markdown('The Beyond Coal movement is a campaign by environmental '\
                            'group the Sierra Club to promote renewable energy instead of coal. ' \
                            'Their primary objective is to close coal power plants in the United States.')
                st.markdown('https://beyond-coal.eu/')
                
            # Epa
            if sel_org == 'Environmental Protection Agency' :
                st.subheader('Environmental Protection Agency')
                img = Image.open('resources/imgs/Org/epa.png')
                st.image(img,width=150)
                st.markdown('The Environmental Protection Agency is an independent agency,' \
                            'specifically an independent executive agency, of the United States' \
                            'federal government for environmental protection.')
                st.markdown('https://www.epa.gov/')
                
            # Rainforest
            if sel_org == 'Rainforest Connection' :
                st.subheader('Rainforest Connection')
                img = Image.open('resources/imgs/Org/rainforest.jpg')
                st.image(img,width=150)
                st.markdown('Rainforest Connection (RFCx) creates acoustic monitoring' \
                            'systems for those who wish to end illegal deforestation in real-time.')
                st.markdown('https://rfcx.org/home')
                
            # Sustain    
            if sel_org == 'SUSTAIN-Africa' :
                st.subheader('SUSTAIN-Africa')
                img = Image.open('resources/imgs/Org/sustain_africa.png')
                st.image(img,width=150)
                st.markdown('SUSTAIN-Africa is an IUCN-led initiative supporting Inclusive'\
                            'Green Growth (IGG) in Africa, with a particular focus on implementing'\
                            'a shared vision of economic growth, ecosystem resilience and social'\
                            'prosperity in Africa.')
                st.markdown('http://www.waterandnature.org/initiatives/sustain')
                
            # ClimateLaunchPad
            if sel_org == 'ClimateLaunchpad' :
                st.subheader('ClimateLaunchpad')
                img = Image.open('resources/imgs/Org/climate_lp.jpg')
                st.image(img,width=150)
                st.markdown('ClimateLaunchpad is the world’s largest green business ideas competition.'\
                            'Our mission is to unlock the world’s cleantech potential that addresses' \
                            'climate change. The competition creates a stage for those ideas.')
                st.markdown('https://climatelaunchpad.org/')
                
            # ClimateReality
            if sel_org == 'The Climate Reality Project' :
                st.subheader('The Climate Reality Project')
                img = Image.open('resources/imgs/Org/climate_reality.jpg')
                st.image(img,width=150)
                st.markdown('The Climate Reality Project is a non-profit organization'\
                            'involved in education and advocacy related to climate change.')
                st.markdown('https://www.climaterealityproject.org/')
                
            # The Years Project
            if sel_org == 'The YEARS Project' :
                st.subheader('The YEARS Project')
                img = Image.open('resources/imgs/Org/the_years_project.jpg')
                st.image(img,width=150)
                st.markdown('The YEARS Project is an education and communications effort' \
                            'designed to elevate climate change as the biggest issue of our time.')
                st.markdown('https://theyearsproject.com/')
                
            # Docforclimate
            if sel_org == 'Docsforclimate' :
                st.subheader('Docsforclimate')
                img = Image.open('resources/imgs/Org/doc_for_climate.png')
                st.image(img,width=150)
                st.markdown('The purpose of the letter is to increase public and political awareness' \
                            'about the urgency of climate change and to demonstrate the link' \
                            'between climate change and health. In addition, the letter' \
                            'specifies measures that are needed to reduce greenhouse gas emissions.')
                st.markdown('https://www.docsforclimate.be/')
            
            # Earth Life    
            if sel_org == 'Earth Life' :
                st.subheader('Earth Life')
                img = Image.open('resources/imgs/Org/earth_life.jpg')
                st.image(img,width=150)
                st.markdown('Earthlife Africa’s Johannesburg branch was founded in 1988' \
                            'to mobilise civil society around environmental issues in relation to people.')
                st.markdown('https://earthlife.org.za/')
                
            # Greenpeace
            if sel_org == 'Greenpeace' :
                st.subheader('Greenpeace')
                img = Image.open('resources/imgs/Org/greenpeace.png')
                st.image(img,width=150)
                st.markdown('Greenpeace is a non-governmental environmental organization'\
                            'with offices in over 55 countries and an international coordinating'\
                            'body in Amsterdam, the Netherlands'\
                            'Greenpeace exists because this fragile earth deserves a voice.'\
                            'It needs solutions. It needs change. It needs action.')
                st.markdown('https://www.greenpeace.org/international/')

        # Build people selection
        
        else :
            sel_people = st.selectbox('Select Person' , people )
            
            # Neil deGrasse Tyson
            if sel_people == 'Neil deGrasse Tyson' :                
                st.subheader('Neil deGrasse Tyson')
                img = Image.open('resources/imgs/People/Neil_tyson.jpg')
                st.image(img,width=150)
                st.markdown('Neil deGrasse Tyson is an American astrophysicist, cosmologist,' \
                            'planetary scientist, author, and science communicator. Since 1996,'\
                            'he has been the Frederick P. Rose Director of the Hayden Planetarium'\
                            'at the Rose Center for Earth and Space in New York City.')
                st.markdown('https://twitter.com/neiltyson')
                
            # Bill McKibben
            if sel_people == 'Bill McKibben' :                
                st.subheader('Bill McKibben')
                img = Image.open('resources/imgs/People/Bill_Mc.jpg')
                st.image(img,width=150)
                st.markdown('William Ernest "Bill" McKibben is an American environmentalist,'\
                            'author, and journalist who has written extensively on the impact'\
                            'of global warming. He is the Schumann Distinguished Scholar at Middlebury College'\
                            'and leader of the climate campaign group 350.org.')
                st.markdown('https://twitter.com/billmckibben')
                
            
            
            # McKenzie Wark
            if sel_people == 'McKenzie Wark' :                
                st.subheader('McKenzie Wark')
                img = Image.open('resources/imgs/People/McKenzie.jpg')
                st.image(img,width=150)
                st.markdown('McKenzie Wark (born 1961) is an Australian-born writer and scholar.'\
                            'Wark is known for her writings on media theory, critical theory,'\
                            'new media, and the Situationist International. Her best known works'\
                            'are A Hacker Manifesto and Gamer Theory. She is Professor of Media and Cultural Studies'\
                            'at The New School in New York City. Wark is a trans woman; her pronouns are she/her.')
                st.markdown('https://twitter.com/mckenziewark')
                
            # Leonardo DiCaprio
            if sel_people == 'Leonardo DiCaprio' :                
                st.subheader('Leonardo DiCaprio')
                img = Image.open('resources/imgs/People/Leo.jpg')
                st.image(img,width=150)
                st.markdown('Leonardo Wilhelm DiCaprio is an American actor and producer.'\
                            'He has often played unconventional parts, particularly in biopics and period films.'\
                            'As of 2019, his films have earned US$7.2 billion worldwide,'\
                            'and he has placed eight times in annual rankings of the worlds highest-paid actors.')
                st.markdown('https://twitter.com/LeoDiCaprio')
                
                
            # Neil deGrasse Tyson
            if sel_people == 'Susan Sarandon' :                
                st.subheader('Susan Sarandon')
                img = Image.open('resources/imgs/People/Susan.jpg')
                st.image(img,width=150)
                st.markdown('Susan Abigail Sarandon is an American actress and activist.'\
                            'She has received an Academy Award, a British Academy Film Award,'\
                            'and a Screen Actors Guild Award, and has been nominated for nine Golden Globe Awards.'\
                            'Known for her social and political activism, she was appointed'\
                            'a UNICEF Goodwill Ambassador in 1999 and received the Action Against Hunger Humanitarian Award in 2006.')
                st.markdown('https://twitter.com/SusanSarandon')
                
            # Brenda Ekwurzel
            if sel_people == 'Brenda Ekwurzel' :                
                st.subheader('Brenda Ekwurzel')
                img = Image.open('resources/imgs/People/Brenda.jpg')
                st.image(img,width=150)
                st.markdown('Brenda Ekwurzel is a senior climate scientist and the director of climate'\
                            'science for the Climate & Energy Program at the Union of Concerned Scientists (UCS).'\
                            'In her role, she ensures that program analyses reflect robust and relevant climate science,'\
                            'and researches the influence of major carbon producers on rising global average temperatures and sea level.')
                st.markdown('https://twitter.com/BrendaEkwurzel')
                
            # Oliver Milman
            if sel_people == 'Oliver Milman' :                
                st.subheader('Oliver Milman')
                img = Image.open('resources/imgs/People/Oliver.jpg')
                st.image(img,width=150)
                st.markdown('Oliver Milman is an environment reporter for Guardian US.')
                st.markdown('https://twitter.com/olliemilman')
                
            # Ellie Goulding
            if sel_people == 'Ellie Goulding' :                
                st.subheader('Ellie Goulding')
                img = Image.open('resources/imgs/People/Ellie.jpg')
                st.image(img,width=150)
                st.markdown('Elena Jane Goulding is an English singer and songwriter.'\
                            'Her career began when she met record producers Starsmith and Frankmusik,'\
                            'and she was later spotted by Jamie Lillywhite, who later became her manager and A&R.'\
                            'After signing to Polydor Records in July 2009, Goulding released her debut extended play,'\
                            'An Introduction to Ellie Goulding later that year.')
                st.markdown('https://twitter.com/elliegoulding')
                
            # Hugh Evans
            if sel_people == 'Hugh Evans' :                
                st.subheader('Hugh Evans')
                img = Image.open('resources/imgs/People/Hugh.jpg')
                st.image(img,width=150)
                st.markdown('Hugh Evans is an Australian humanitarian. Evans is the co-founder of'\
                            'both The Oaktree Foundation and Global Citizen, a Global Poverty Project.'\
                            'He has received domestic and international accolades for his work'\
                            'in promoting youth advocacy and volunteerism in order to reduce extreme poverty in developing countries.')
                st.markdown('https://twitter.com/Hughcevans')
                
            # William LeGate
            if sel_people == 'William LeGate' :                
                st.subheader('William LeGate')
                img = Image.open('resources/imgs/People/William.jpg')
                st.image(img,width=150)
                st.markdown('William LeGate is an American entrepreneur, Thiel Fellow,'\
                            'computer programmer and activist. A self-taught programmer from the age of 12,'\
                            'LeGate was brought to the publics attention three years later when The New York Times'\
                            'recommended one of the iOS applications he had programmed during middle school.')
                st.markdown('https://twitter.com/williamlegate')
                
            
            # Taylor Swift
            if sel_people == 'Taylor Swift' :                
                st.subheader('Taylor Swift')
                img = Image.open('resources/imgs/People/Taylor.jpg')
                st.image(img,width=150)
                st.markdown('Taylor Alison Swift is an American singer-songwriter.'\
                            'She is known for her narrative songwriting, that often centers'\
                            'around her personal life and has received widespread critical praise and media coverage.')
                st.markdown('https://twitter.com/taylorswift13')
                
            # Amy Harmon
            if sel_people == 'Amy Harmon' :                
                st.subheader('Amy Harmon')
                img = Image.open('resources/imgs/People/Amy.jpg')
                st.image(img,width=150)
                st.markdown('Amy Harmon (born September 17, 1968) is an American journalist.'\
                            'She won a Pulitzer Prize as a correspondent for The New York Times'\
                            'covering the impact of science and technology on everyday life.'\
                            'Harmon uses narrative storytelling to illuminate the human dilemmas'\
                            'posed by advances in science. In 2013, she was named a Guggenheim Fellow.')
                st.markdown('https://twitter.com/amy_harmon')
                
            
            # John Legend
            if sel_people == 'John Legend' :                
                st.subheader('John Legend')
                img = Image.open('resources/imgs/People/John.jpg')
                st.image(img,width=150)
                st.markdown('John Roger Stephens, known professionally as John Legend,'\
                            'is an American singer, songwriter, producer, actor, and philanthropist.'\
                            'Prior to the release of Legends debut album, Get Lifted,'\
                            'he had collaborated with already established artists and signed to Kanye West GOOD Music.')
                st.markdown('https://twitter.com/johnlegend')
                
            # Bill Nye
            if sel_people == 'Bill Nye' :                
                st.subheader('Bill Nye')
                img = Image.open('resources/imgs/People/Bill_Nye.jpg')
                st.image(img,width=150)
                st.markdown('William Sanford Nye, popularly known as Bill Nye the Science Guy,'\
                            'is an American science communicator, television presenter, and mechanical engineer.'\
                            'He is best known as the host of the PBS and syndicated childrens science'\
                            'show Bill Nye the Science Guy, the Netflix show Bill Nye Saves the World,'\
                            'and for his many subsequent appearances in popular media as a science educator.')
                st.markdown('https://twitter.com/BillNye')

    
    # Building out Hashtag generation page
    if selection == 'Hashtag Generator' :
        st.subheader('Generate Hashtags your business can use for social media ads')
        num_hash = st.slider('Select number of Hashtags to generate' , 1, 10 )
        if st.button("Generate"):           
            rand_hash = random.sample(pro_hash,num_hash) 
            for i in range(len(rand_hash)):                
                st.success(rand_hash[i])
            

    # Building out the "Market Research tools" page
    if selection == "Market Research Tools":
        st.subheader("Relevant statistical analysis to aid your market research")
        # You can read a markdown file from supporting resources folder
        select_viz = st.selectbox('Select Information' , viz)
        
        if select_viz == 'How Tweets are spread' :
            disp = Image.open('resources/imgs/Tweet_distribution.png')
            st.image(disp,width=600)
            st.subheader('Insights')
            st.markdown('* Most Tweets are PRO Climate Change - That is good news for your Product\Service')
            st.markdown('* 23% of the tweets are Facts/News - Meaning lots of media coverage towards the topic')
            
        if select_viz == 'Most Used Words' :
            disp = Image.open('resources/imgs/frequent_words.png')
            st.image(disp,width=850)
            st.subheader('Insights')
            st.markdown('* Use Frequent PRO Climate-Change words towards your branding and advertising')
            st.markdown('* AVOID Frequent ANTI Climate-Change words towards your branding and advertising')
            st.markdown('* AVOID all TRUMP related words')
            
        if select_viz == 'Length of Tweets' :
            disp = Image.open('resources/imgs/tweet_length.png')
            st.image(disp,width=600)
            st.subheader('Insights')
            st.markdown('* PRO Climate Change Tweets are generally longer with consistent length distribution')
            st.markdown('* ANTI Climate Change Tweets are generally shorter with inconsistent length distribution')
            
            
        if select_viz == 'Named Entities' :
            disp = Image.open('resources/imgs/entities.png')
            st.image(disp,width=720)
            st.markdown('In information extraction, a named entity is a real-world object,'\
                        'such as persons, locations, organizations, products, etc.,'\
                        'that can be denoted with a proper name. It can be abstract or have a physical existence.')
            st.subheader('Insights')
            st.markdown('* Organisations , People & Geo-Political entities appear frequently in tweets')
            st.markdown('* Time and Location information appear less in tweets')
            st.markdown(' More info on the subject - https://monkeylearn.com/blog/named-entity-recognition/ ' )
        
        if select_viz == 'Most used Emojis' :
            disp = Image.open('resources/imgs/top_emoji.png')
            st.image(disp,width=600)
            st.subheader('Insights')
            st.markdown('* Lastly , Spice up your Tweets with these emojis')
            
        
            
            


    # Building out the predication page
    if selection == "Belief Predictor AI":
        st.subheader("Predict if a person believes in climate change based on their tweet")
        # Creating a text box for user input
        tweet_text = st.text_area("Enter Tweet")
        # Create tweet classifier logic
        if st.button("Classify"):
                  
            # Transforming user input with vectorizer
            vect_text = [tweet_text]
            prediction = model.predict(vect_text)
              
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
            

# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
    main()
