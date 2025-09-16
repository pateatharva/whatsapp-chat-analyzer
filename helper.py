# from urlextract import URLExtract
# from wordcloud import WordCloud
# import pandas as pd
# from collections import Counter
# import emoji

# extract = URLExtract()

# def fetch_stats(selected_user, df):
#     if selected_user != 'Overall':
#         df = df[df['user'] == selected_user]

#     num_messages = df.shape[0]
#     words = []

#     for message in df['message']:
#         words.extend(message.split())

#     num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

#     links = []
#     for message in df['message']:
#         links.extend(extract.find_urls(message))

#     return num_messages, len(words), num_media_messages, len(links)


# def most_busy_users(df):
#     x = df['user'].value_counts().head()
#     df = round((df['user'].value_counts() / df.shape[0]) * 100, 2) \
#         .reset_index().rename(columns={'index': 'name', 'user': 'percent'})
#     return x, df


# def create_wordcloud(selected_user, df):
#     f = open('stop_hinglish.txt', 'r')
#     stop_words = f.read()

#     if selected_user != 'Overall':
#         df = df[df['user'] == selected_user]

#     temp = df[df['user'] != 'group_notification']
#     temp = temp[temp['message'] != '<Media omitted>\n']

#     def remove_stop_words(message):
#         y = []
#         for word in message.lower().split():
#             if word not in stop_words:
#                 y.append(word)
#         return " ".join(y)

#     wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
#     temp['message'] = temp['message'].apply(remove_stop_words)
#     df_wc = wc.generate(temp['message'].str.cat(sep=" "))
#     return df_wc


# def most_common_words(selected_user, df):
#     f = open('stop_hinglish.txt', 'r')
#     stop_words = f.read()

#     if selected_user != 'Overall':
#         df = df[df['user'] == selected_user]

#     temp = df[df['user'] != 'group_notification']
#     temp = temp[temp['message'] != '<Media omitted>\n']

#     words = []
#     for message in temp['message']:
#         for word in message.lower().split():
#             if word not in stop_words:
#                 words.append(word)

#     most_common_df = pd.DataFrame(Counter(words).most_common(20))
#     return most_common_df


# def emoji_helper(selected_user, df):
#     if selected_user != 'Overall':
#         df = df[df['user'] == selected_user]

#     emojis = []
#     for message in df['message']:
#         emojis.extend([c for c in message if c in emoji.EMOJI_DATA])

#     emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
#     return emoji_df


# def monthly_timeline(selected_user, df):
#     if selected_user != 'Overall':
#         df = df[df['user'] == selected_user]

#     timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

#     time = []
#     for i in range(timeline.shape[0]):
#         time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

#     timeline['time'] = time
#     return timeline


# def daily_timeline(selected_user, df):
#     if selected_user != 'Overall':
#         df = df[df['user'] == selected_user]

#     daily_timeline = df.groupby('only_date').count()['message'].reset_index()
#     return daily_timeline


# def week_activity_map(selected_user, df):
#     if selected_user != 'Overall':
#         df = df[df['user'] == selected_user]
#     return df['day_name'].value_counts()


# def month_activity_map(selected_user, df):
#     if selected_user != 'Overall':
#         df = df[df['user'] == selected_user]
#     return df['month'].value_counts()


# def activity_heatmap(selected_user, df):
#     if selected_user != 'Overall':
#         df = df[df['user'] == selected_user]

#     user_heatmap = df.pivot_table(index='day_name', columns='period',
#                                   values='message', aggfunc='count').fillna(0)
#     return user_heatmap
from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji
from textblob import TextBlob

extract = URLExtract()

def fetch_stats(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    num_messages = df.shape[0]
    words = []
    for message in df['message']:
        words.extend(message.split())

    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages, len(words), num_media_messages, len(links)

def most_busy_users(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2) \
        .reset_index().rename(columns={'index': 'name', 'user': 'percent'})
    return x, df

def create_wordcloud(selected_user, df):
    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    temp['message'] = temp['message'].apply(remove_stop_words)
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user, df):
    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    words = []
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df

def emoji_helper(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])

    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
    return emoji_df

def monthly_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time
    return timeline

def daily_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()
    return daily_timeline

def week_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    return df['day_name'].value_counts()

def month_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    return df['month'].value_counts()

def activity_heatmap(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    user_heatmap = df.pivot_table(index='day_name', columns='period',
                                  values='message', aggfunc='count').fillna(0)
    return user_heatmap

def sentiment_analysis(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # Filter out group notifications and media messages
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    # Perform sentiment analysis
    def get_sentiment(message):
        analysis = TextBlob(message)
        # Polarity ranges from -1 (negative) to 1 (positive)
        if analysis.sentiment.polarity > 0:
            return 'Positive'
        elif analysis.sentiment.polarity < 0:
            return 'Negative'
        else:
            return 'Neutral'

    # Apply sentiment analysis to each message
    temp['sentiment'] = temp['message'].apply(get_sentiment)

    # Count the number of messages for each sentiment
    sentiment_counts = temp['sentiment'].value_counts()

    return sentiment_counts

def summarize_chat(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # Filter out group notifications and media messages
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    # Basic summary statistics
    total_messages = temp.shape[0]
    total_words = sum(len(message.split()) for message in temp['message'])
    most_active_date = temp['only_date'].value_counts().idxmax()
    most_active_day = temp['day_name'].value_counts().idxmax()

    # Sentiment summary
    sentiment_counts = temp['message'].apply(lambda x: TextBlob(x).sentiment.polarity)
    avg_sentiment = sentiment_counts.mean()
    sentiment_label = "mostly positive" if avg_sentiment > 0 else "mostly negative" if avg_sentiment < 0 else "neutral"

    # Construct summary
    summary = (
        f"Summary for {selected_user}:\n"
        f"- Total Messages: {total_messages}\n"
        f"- Total Words: {total_words}\n"
        f"- Most Active Date: {most_active_date}\n"
        f"- Most Active Day: {most_active_day}\n"
        f"- Sentiment: The conversation is {sentiment_label} (average polarity: {avg_sentiment:.2f})"
    )
    return summary

def extract_keywords(selected_user, df):
    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    words = []
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    # Get top 10 keywords
    keywords = pd.DataFrame(Counter(words).most_common(10), columns=['Word', 'Count'])
    return keywords