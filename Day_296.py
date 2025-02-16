


# pip install wordcloud

from wordcloud import WordCloud

text_ = '''Python is my favorite programming language. 
My favorite Python libraries are Pandas, Numpy, and Matplotlib; 
Pandas is my favorite'''

wordcloud = WordCloud(width=800, height=500,
                      background_color='white')

wordcloud.generate(text_)

wordcloud.to_file("wordcloud.png")























