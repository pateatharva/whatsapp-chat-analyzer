

# import streamlit as st
# import preprocessor
# import helper
# import matplotlib.pyplot as plt
# import seaborn as sns
# import plotly.express as px

# st.set_page_config(page_title="📊 WhatsApp Chat Analyzer", layout="wide")
# st.markdown("<h1 style='text-align:center; color:#FF6F61;'>📊 WhatsApp Chat Analyzer</h1>", unsafe_allow_html=True)
# st.markdown("<p style='text-align:center; color:gray;'>Analyze WhatsApp group chats with statistics, word clouds, emoji insights & AI features</p>", unsafe_allow_html=True)
# st.markdown("---")

# # Sidebar
# with st.sidebar:
#     st.image("https://cdn-icons-png.flaticon.com/512/134/134914.png", width=80)
#     st.title("⚙️ Controls")
#     uploaded_file = st.file_uploader("📂 Upload WhatsApp Chat (.txt)", type=["txt"])

# if uploaded_file is not None:
#     bytes_data = uploaded_file.getvalue()
#     data = bytes_data.decode("utf-8")
#     df = preprocessor.preprocess(data)

#     user_list = df['user'].unique().tolist()
#     if "group_notification" in user_list:
#         user_list.remove("group_notification")
#     user_list.sort()
#     user_list.insert(0, "Overall")

#     with st.sidebar:
#         selected_user = st.selectbox("👤 Select User", user_list)
#         analyze = st.button("🚀 Show Analysis")

#     if analyze:
#         tabs = st.tabs(["📊 Stats", "📅 Timeline", "🔥 Activity", "👥 Users",
#                         "☁️ Words", "😀 Emojis", "😊 Sentiment", "📝 Summary", "🔑 Keywords"])

#         # ---------- TAB 1: STATS ----------
#         with tabs[0]:
#             st.subheader("✨ Key Statistics")
#             num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
#             col1, col2, col3, col4 = st.columns(4)
#             col1.metric("📨 Messages", num_messages)
#             col2.metric("📝 Words", words)
#             col3.metric("📸 Media", num_media_messages)
#             col4.metric("🔗 Links", num_links)

#         # ---------- TAB 2: TIMELINES ----------
#         with tabs[1]:
#             st.subheader("📅 Monthly Timeline")
#             timeline = helper.monthly_timeline(selected_user, df)
#             fig = px.line(timeline, x="time", y="message", title="Messages per Month", markers=True)
#             st.plotly_chart(fig, use_container_width=True)

#             st.subheader("📆 Daily Timeline")
#             daily_timeline = helper.daily_timeline(selected_user, df)
#             fig = px.line(daily_timeline, x="only_date", y="message", title="Messages per Day", markers=True)
#             st.plotly_chart(fig, use_container_width=True)

#         # ---------- TAB 3: ACTIVITY ----------
#         with tabs[2]:
#             st.subheader("⏳ Activity Insights")
#             col1, col2 = st.columns(2)
#             with col1:
#                 st.write("📅 Most Busy Day")
#                 busy_day = helper.week_activity_map(selected_user, df)
#                 fig = px.bar(x=busy_day.index, y=busy_day.values, labels={'x': 'Day', 'y': 'Messages'},
#                              color=busy_day.values, color_continuous_scale="Viridis")
#                 st.plotly_chart(fig, use_container_width=True)
#             with col2:
#                 st.write("📆 Most Busy Month")
#                 busy_month = helper.month_activity_map(selected_user, df)
#                 fig = px.bar(x=busy_month.index, y=busy_month.values, labels={'x': 'Month', 'y': 'Messages'},
#                              color=busy_month.values, color_continuous_scale="Plasma")
#                 st.plotly_chart(fig, use_container_width=True)

#             st.subheader("🔥 Weekly Activity Heatmap")
#             user_heatmap = helper.activity_heatmap(selected_user, df)
#             fig, ax = plt.subplots()
#             ax = sns.heatmap(user_heatmap, cmap="YlGnBu")
#             st.pyplot(fig)

#         # ---------- TAB 4: USERS ----------
#         with tabs[3]:
#             if selected_user == "Overall":
#                 st.subheader("👥 Most Busy Users")
#                 x, new_df = helper.most_busy_users(df)
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     fig = px.bar(x=x.index, y=x.values, labels={'x': 'User', 'y': 'Messages'},
#                                  color=x.values, color_continuous_scale="Sunset")
#                     st.plotly_chart(fig, use_container_width=True)
#                 with col2:
#                     st.dataframe(new_df)
#             else:
#                 st.info("ℹ️ This section is only available for group-level (Overall) analysis.")

#         # ---------- TAB 5: WORDS ----------
#         with tabs[4]:
#             st.subheader("☁️ Word Cloud")
#             df_wc = helper.create_wordcloud(selected_user, df)
#             fig, ax = plt.subplots()
#             ax.imshow(df_wc, interpolation="bilinear")
#             plt.axis("off")
#             st.pyplot(fig)

#             st.subheader("💬 Most Common Words")
#             most_common_df = helper.most_common_words(selected_user, df)
#             fig = px.bar(most_common_df, x=1, y=0, orientation="h", labels={"0": "Word", "1": "Count"},
#                          color=1, color_continuous_scale="Cividis")
#             st.plotly_chart(fig, use_container_width=True)

#         # ---------- TAB 6: EMOJIS ----------
#         with tabs[5]:
#             st.subheader("😀 Emoji Analysis")
#             emoji_df = helper.emoji_helper(selected_user, df)
#             col1, col2 = st.columns(2)
#             with col1:
#                 st.dataframe(emoji_df.head(10))
#             with col2:
#                 fig = px.pie(emoji_df.head(5), values=1, names=0, title="Top Emojis")
#                 st.plotly_chart(fig, use_container_width=True)

#         # ---------- TAB 7: SENTIMENT ----------
#         with tabs[6]:
#             st.subheader("😊 Sentiment Analysis")
#             sentiment_counts = helper.sentiment_analysis(selected_user, df)
#             fig = px.pie(sentiment_counts, values=sentiment_counts.values, names=sentiment_counts.index,
#                          title="Message Sentiments")
#             st.plotly_chart(fig, use_container_width=True)

#         # ---------- TAB 8: SUMMARY ----------
#         with tabs[7]:
#             st.subheader("📝 Chat Summary")
#             summary = helper.summarize_chat(selected_user, df)
#             st.info(summary)

#         # ---------- TAB 9: KEYWORDS ----------
#         with tabs[8]:
#             st.subheader("🔑 Top Keywords")
#             keywords_df = helper.extract_keywords(selected_user, df)
#             fig = px.bar(keywords_df, x="Count", y="Word", orientation="h", color="Count",
#                          color_continuous_scale="Viridis")
#             st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import preprocessor
import helper
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import json
import requests
from streamlit_lottie import st_lottie

# Set page configuration with a custom icon
st.set_page_config(page_title="📊 WhatsApp Chat Analyzer", page_icon="💬", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
/* Main container styling */
.main {
    background: linear-gradient(135deg, #E0F7FA 0%, #B2EBF2 100%);
    padding: 20px;
    border-radius: 10px;
}

/* Sidebar styling */
.sidebar .sidebar-content {
    background-color: #25D366;
    border-radius: 10px;
    padding: 15px;
    color: white;
}

/* Custom button styling */
.stButton>button {
    background-color: #128C7E;
    color: white;
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: bold;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background-color: #0A6E5F;
    transform: scale(1.05);
}

/* Tab styling */
.stTabs [data-baseweb="tab"] {
    font-size: 16px;
    font-weight: 500;
    padding: 10px 20px;
    border-radius: 8px;
    background-color: #F1F9F5;
    margin-right: 5px;
}
.stTabs [data-baseweb="tab"]:hover {
    background-color: #25D366;
    color: white;
}

/* Metric cards */
.stMetric {
    background-color: white;
    border-radius: 10px;
    padding: 15px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

/* Header and text styling */
h1, h2, h3 {
    font-family: 'Roboto', sans-serif;
    color: #128C7E;
}
p {
    font-family: 'Open Sans', sans-serif;
    color: #333;
}

/* Center content */
.centered {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Load Google Fonts
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# Function to load Lottie animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animation
lottie_url = "https://assets5.lottiefiles.com/packages/lf20_3rwasyjy.json"  # Chat-related animation
lottie_json = load_lottieurl(lottie_url)

# Header with animation
with st.container():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("<h1 class='centered'>💬 WhatsApp Chat Analyzer</h1>", unsafe_allow_html=True)
        st.markdown("<p class='centered'>Uncover insights from your WhatsApp group chats with stunning visualizations and AI-powered analysis!</p>", unsafe_allow_html=True)
    with col2:
        st_lottie(lottie_json, height=150, key="chat_animation")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/134/134914.png", width=100)
    st.markdown("<h2 style='color:white;'>⚙️ Controls</h2>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("📂 Upload WhatsApp Chat (.txt)", type=["txt"], help="Upload a WhatsApp chat export in .txt format")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    user_list = df['user'].unique().tolist()
    if "group_notification" in user_list:
        user_list.remove("group_notification")
    user_list.sort()
    user_list.insert(0, "Overall")

    with st.sidebar:
        selected_user = st.selectbox("👤 Select User", user_list, help="Choose a user or 'Overall' for group analysis")
        analyze = st.button("🚀 Analyze Chat", help="Click to generate insights")

    if analyze:
        # Progress bar for analysis
        with st.spinner("Analyzing your chat..."):
            tabs = st.tabs(["📊 Stats", "📅 Timeline", "🔥 Activity", "👥 Users",
                            "☁️ Words", "😀 Emojis", "😊 Sentiment", "📝 Summary", "🔑 Keywords"])

        # ---------- TAB 1: STATS ----------
        with tabs[0]:
            st.subheader("✨ Key Statistics")
            num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("📨 Messages", num_messages)
            with col2:
                st.metric("📝 Words", words)
            with col3:
                st.metric("📸 Media", num_media_messages)
            with col4:
                st.metric("🔗 Links", num_links)

        # ---------- TAB 2: TIMELINES ----------
        with tabs[1]:
            st.subheader("📅 Monthly Timeline")
            timeline = helper.monthly_timeline(selected_user, df)
            fig = px.line(timeline, x="time", y="message", title="Messages per Month", markers=True,
                          color_discrete_sequence=["#128C7E"])
            fig.update_layout(title_font_size=20, title_font_family="Roboto", plot_bgcolor="white")
            st.plotly_chart(fig, use_container_width=True)

            st.subheader("📆 Daily Timeline")
            daily_timeline = helper.daily_timeline(selected_user, df)
            fig = px.line(daily_timeline, x="only_date", y="message", title="Messages per Day", markers=True,
                          color_discrete_sequence=["#25D366"])
            fig.update_layout(title_font_size=20, title_font_family="Roboto", plot_bgcolor="white")
            st.plotly_chart(fig, use_container_width=True)

        # ---------- TAB 3: ACTIVITY ----------
        with tabs[2]:
            st.subheader("⏳ Activity Insights")
            col1, col2 = st.columns(2)
            with col1:
                st.write("📅 Most Busy Day")
                busy_day = helper.week_activity_map(selected_user, df)
                fig = px.bar(x=busy_day.index, y=busy_day.values, labels={'x': 'Day', 'y': 'Messages'},
                             color=busy_day.values, color_continuous_scale="Viridis")
                fig.update_layout(title_font_size=16, title_font_family="Roboto", plot_bgcolor="white")
                st.plotly_chart(fig, use_container_width=True)
            with col2:
                st.write("📆 Most Busy Month")
                busy_month = helper.month_activity_map(selected_user, df)
                fig = px.bar(x=busy_month.index, y=busy_month.values, labels={'x': 'Month', 'y': 'Messages'},
                             color=busy_month.values, color_continuous_scale="Plasma")
                fig.update_layout(title_font_size=16, title_font_family="Roboto", plot_bgcolor="white")
                st.plotly_chart(fig, use_container_width=True)

            st.subheader("🔥 Weekly Activity Heatmap")
            user_heatmap = helper.activity_heatmap(selected_user, df)
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(user_heatmap, cmap="YlGnBu", annot=True, fmt=".0f", cbar_kws={'label': 'Messages'})
            plt.title("Weekly Activity Heatmap", fontsize=16, fontfamily="Roboto")
            st.pyplot(fig)

        # ---------- TAB 4: USERS ----------
        with tabs[3]:
            if selected_user == "Overall":
                st.subheader("👥 Most Busy Users")
                x, new_df = helper.most_busy_users(df)
                col1, col2 = st.columns(2)
                with col1:
                    fig = px.bar(x=x.index, y=x.values, labels={'x': 'User', 'y': 'Messages'},
                                 color=x.values, color_continuous_scale="Sunset")
                    fig.update_layout(title_font_size=16, title_font_family="Roboto", plot_bgcolor="white")
                    st.plotly_chart(fig, use_container_width=True)
                with col2:
                    st.dataframe(new_df.style.set_properties(**{'background-color': '#F1F9F5', 'border-radius': '5px'}))
            else:
                st.info("ℹ️ This section is only available for group-level (Overall) analysis.")

        # ---------- TAB 5: WORDS ----------
        with tabs[4]:
            st.subheader("☁️ Word Cloud")
            df_wc = helper.create_wordcloud(selected_user, df)
            fig, ax = plt.subplots(figsize=(8, 8))
            ax.imshow(df_wc, interpolation="bilinear")
            plt.axis("off")
            st.pyplot(fig)

            st.subheader("💬 Most Common Words")
            most_common_df = helper.most_common_words(selected_user, df)
            fig = px.bar(most_common_df, x=1, y=0, orientation="h", labels={"0": "Word", "1": "Count"},
                         color=1, color_continuous_scale="Cividis")
            fig.update_layout(title_font_size=16, title_font_family="Roboto", plot_bgcolor="white")
            st.plotly_chart(fig, use_container_width=True)

        # ---------- TAB 6: EMOJIS ----------
        with tabs[5]:
            st.subheader("😀 Emoji Analysis")
            emoji_df = helper.emoji_helper(selected_user, df)
            col1, col2 = st.columns(2)
            with col1:
                st.dataframe(emoji_df.head(10).style.set_properties(**{'background-color': '#F1F9F5', 'border-radius': '5px'}))
            with col2:
                fig = px.pie(emoji_df.head(5), values=1, names=0, title="Top Emojis", color_discrete_sequence=px.colors.qualitative.Bold)
                fig.update_layout(title_font_size=16, title_font_family="Roboto")
                st.plotly_chart(fig, use_container_width=True)

        # ---------- TAB 7: SENTIMENT ----------
        with tabs[6]:
            st.subheader("😊 Sentiment Analysis")
            sentiment_counts = helper.sentiment_analysis(selected_user, df)
            fig = px.pie(sentiment_counts, values=sentiment_counts.values, names=sentiment_counts.index,
                         title="Message Sentiments", color_discrete_sequence=px.colors.qualitative.Pastel)
            fig.update_layout(title_font_size=16, title_font_family="Roboto")
            st.plotly_chart(fig, use_container_width=True)

        # ---------- TAB 8: SUMMARY ----------
        with tabs[7]:
            st.subheader("📝 Chat Summary")
            summary = helper.summarize_chat(selected_user, df)
            st.info(summary)

        # ---------- TAB 9: KEYWORDS ----------
        with tabs[8]:
            st.subheader("🔑 Top Keywords")
            keywords_df = helper.extract_keywords(selected_user, df)
            fig = px.bar(keywords_df, x="Count", y="Word", orientation="h", color="Count",
                         color_continuous_scale="Viridis")
            fig.update_layout(title_font_size=16, title_font_family="Roboto", plot_bgcolor="white")
            st.plotly_chart(fig, use_container_width=True)
