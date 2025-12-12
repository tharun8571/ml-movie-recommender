
import pickle
import pandas as pd
import gradio as gr

# ---------------------------
# LOAD DATA
# ---------------------------
with open('new_dataset.pkl', 'rb') as f:
    movies = pickle.load(f)

with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

movies = pd.DataFrame(movies)
movie_titles = sorted(movies['title'].tolist())

# ---------------------------
# RECOMMEND FUNCTION
# ---------------------------
def recommend(movie_name):
    movie_name = movie_name.strip().lower()

    try:
        index = movies[movies['title'].str.lower() == movie_name].index[0]
    except:
        return ["Movie not found in dataset!"]

    distances = similarity[index]
    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:11]

    recommended_titles = []
    for i in movie_list:
        recommended_titles.append(movies.iloc[i[0]]['title'])

    return recommended_titles

# ---------------------------
# GLOW STYLE + CLICKABLE GOOGLE SEARCH
# ---------------------------
def style_tags_glow(titles):
    html = """
    <style>
    .tag-box {
        display:inline-block;
        background:#1a1a1a;
        color:white;
        padding:10px 18px;
        margin:6px;
        border-radius:20px;
        font-size:15px;
        border:1px solid #444;
        transition: all 0.25s ease;
        animation: fadeIn 0.7s ease forwards;
        opacity:0;
        text-decoration:none;
    }

    .tag-box:hover {
        transform: scale(1.17);
        background:#222;
        border:1px solid #00ffc8;
        box-shadow:
            0 0 10px rgba(0, 255, 200, 0.7),
            0 0 20px rgba(0, 255, 200, 0.5),
            0 0 30px rgba(0, 255, 200, 0.3);
        cursor:pointer;
    }

    @keyframes fadeIn {
        from { opacity:0; transform:translateY(8px); }
        to   { opacity:1; transform:translateY(0px); }
    }

    /* Glowing button */
    #glow-btn {
        background: linear-gradient(90deg, #00ffc8, #00b3ff);
        color:white !important;
        padding:14px 22px;
        font-size:18px;
        font-weight:bold;
        border:none;
        border-radius:12px;
        cursor:pointer;
        transition:0.25s ease;
        animation: neonPulse 1.5s infinite ease-in-out;
        box-shadow: 0 0 12px rgba(0,255,200,0.5);
    }

    #glow-btn:hover {
        transform: scale(1.07);
        box-shadow:
            0 0 15px rgba(0,255,200,0.8),
            0 0 30px rgba(0,255,200,0.6),
            0 0 45px rgba(0,255,200,0.4);
    }

    @keyframes neonPulse {
        0%   { box-shadow: 0 0 8px rgba(0,255,200,0.4); }
        50%  { box-shadow: 0 0 25px rgba(0,255,200,0.9); }
        100% { box-shadow: 0 0 8px rgba(0,255,200,0.4); }
    }
    </style>

    <div style="padding:10px;">
    """

    delay = 0.0
    for t in titles:
        query = t.replace(" ", "+") + "+movie"
        google_url = f"https://www.google.com/search?q={query}"

        html += f"""
        <a href="{google_url}" target="_blank"
           class="tag-box" style="animation-delay:{delay}s;">
           🔍 {t}
        </a>
        """
        delay += 0.1

    html += "</div>"
    return html


def recommend_ui(movie_name):
    titles = recommend(movie_name)
    return style_tags_glow(titles)

# ---------------------------
# BUILD UI
# ---------------------------
with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("""
    # 🎦 **MOVIE RECOMMENDER**
    ### TOP REVELENT MOVIES 🌐✨
    """)

    with gr.Row():
        movie_input = gr.Dropdown(
            choices=movie_titles,
            label="Select Movie",
            value=movie_titles[0],
            interactive=True
        )
        btn = gr.Button("Recommend", elem_id="glow-btn")

    output = gr.HTML()

    btn.click(fn=recommend_ui, inputs=movie_input, outputs=output)

demo.launch(share=False) # Changed share=True to share=False for local deployment setup
