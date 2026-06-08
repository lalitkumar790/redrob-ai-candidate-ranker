# import streamlit as st
# import pandas as pd

# from src.utils.data_loader import (
#     load_candidates
# )

# from src.jd.jd_parser import (
#     parse_job_description
# )

# from src.ranking.candidate_ranker import (
#     rank_candidates
# )


# st.set_page_config(
#     page_title="RankForge AI",
#     layout="wide"
# )

# st.title(
#     "RankForge AI Candidate Ranker"
# )

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.metric(
#         "Candidates",
#         "100,000"
#     )

# with col2:
#     st.metric(
#         "Scoring Signals",
#         "8"
#     )

# with col3:
#     st.metric(
#         "Output",
#         "Top 100"
#     )


# st.write(
#     """
#     AI-powered candidate ranking system for
#     Search, Retrieval, Recommendation and
#     Machine Learning roles.
#     """
# )




# jd_text = st.text_area(
#     "Paste Job Description",
#     height=250
# )




# if st.button(
#     "Rank Candidates"
# ):

#     if not jd_text.strip():

#         st.error(
#             "Please enter a job description."
#         )

#     else:

#         with st.spinner(
#             "Loading candidates and ranking..."
#         ):

#             candidates = load_candidates(
#                 "data/candidates.jsonl"
#             )

#             jd_data = parse_job_description(
#                 jd_text
#             )

#             ranked = rank_candidates(
#                 candidates,
#                 jd_data
#             )

#         st.success(
#             f"Successfully ranked {len(ranked)} candidates."
#         )

#         top20 = pd.DataFrame(
#             ranked[:20]
#         )

#         st.subheader(
#             "Top 20 Candidates"
#         )

#         st.dataframe(
#             top20[
#                 [
#                     "candidate_id",
#                     "title",
#                     "final_score",
#                     "job_match_score",
#                     "production_experience_score",
#                     "evidence_score"
#                 ]
#             ],
#             use_container_width=True
#         )

#         csv_data = (
#             pd.DataFrame(
#                 ranked[:100]
#             )
#             .to_csv(
#                 index=False
#             )
#         )

#         st.download_button(
#             label="Download Top 100 CSV",
#             data=csv_data,
#             file_name="top100_candidates.csv",
#             mime="text/csv"
#         )



import streamlit as st
import pandas as pd

from src.utils.data_loader import (
    load_candidates
)

from src.jd.jd_parser import (
    parse_job_description
)

from src.ranking.candidate_ranker import (
    rank_candidates
)

from src.reasoning.explanation_generator import (
    generate_explanation
)


st.set_page_config(
    page_title="RankForge AI",
    page_icon="🤖",
    layout="wide"
)


st.title(
    "🤖 RankForge AI Candidate Ranker"
)

st.markdown(
    """
    AI-powered candidate ranking system for
    Search, Retrieval, Recommendation and
    Machine Learning roles.
    """
)


col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Candidates",
        "100,000"
    )

with col2:
    st.metric(
        "Scoring Signals",
        "8"
    )

with col3:
    st.metric(
        "Output",
        "Top 100"
    )


st.divider()


default_jd = """
We are hiring an AI Engineer with experience in:

- Retrieval
- Ranking
- RAG
- LangChain
- Embeddings
- LLMs
- Recommendation Systems
- A/B Testing
"""


jd_text = st.text_area(
    "Paste Job Description",
    value=default_jd,
    height=250
)


if st.button(
    "🚀 Rank Candidates",
    use_container_width=True
):

    if not jd_text.strip():

        st.error(
            "Please enter a job description."
        )

    else:

        with st.spinner(
            "Loading candidates and ranking..."
        ):

            candidates = load_candidates(
                "data/candidates.jsonl"
            )

            jd_data = parse_job_description(
                jd_text
            )

            ranked = rank_candidates(
                candidates,
                jd_data
            )

        st.success(
            f"Successfully ranked {len(ranked)} candidates."
        )

        st.divider()

        st.subheader(
            "📌 Detected JD Skills"
        )

        st.write(
            jd_data["required_skills"]
        )

        st.divider()

        best_candidate = ranked[0]

        st.subheader(
            "🏆 Best Match"
        )

        col1, col2 = st.columns(
            [2, 1]
        )

        with col1:

            st.success(
                f"""
                Candidate ID: {best_candidate['candidate_id']}

                Role: {best_candidate['title']}

                Final Score: {best_candidate['final_score']}
                """
            )

        with col2:

            st.metric(
                "JD Match",
                best_candidate[
                    "job_match_score"
                ]
            )

        st.subheader(
            "🧠 Ranking Reasoning"
        )

        st.info(
            generate_explanation(
                best_candidate
            )
        )

        st.divider()

        st.subheader(
            "📊 Top 20 Ranked Candidates"
        )

        top20_df = pd.DataFrame(
            ranked[:20]
        )

        st.dataframe(
            top20_df[
                [
                    "candidate_id",
                    "title",
                    "final_score",
                    "job_match_score",
                    "production_experience_score",
                    "evidence_score"
                ]
            ],
            use_container_width=True
        )

        st.divider()

        st.subheader(
            "⬇ Download Results"
        )

        top100_df = pd.DataFrame(
            ranked[:100]
        )

        csv_data = top100_df.to_csv(
            index=False
        )

        st.download_button(
            label="Download Top 100 CSV",
            data=csv_data,
            file_name="top100_candidates.csv",
            mime="text/csv"
        )