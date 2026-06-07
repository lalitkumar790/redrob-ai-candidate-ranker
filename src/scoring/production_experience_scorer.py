PRODUCTION_KEYWORDS = [
    "production",
    "retrieval",
    "ranking",
    "search",
    "recommendation",
    "embeddings",
    "llm",
    "machine learning",
    "ml",
    "a/b",
    "evaluation",
    "semantic search",
    "vector",
    "pipeline",
    "deployment"
]


def calculate_production_experience_score(candidate):

    score = 0

    history = candidate.get(
        "career_history",
        []
    )

    for role in history:

        description = role.get(
            "description",
            ""
        ).lower()

        for keyword in PRODUCTION_KEYWORDS:

            if keyword in description:
                score += 5

    return min(score, 100)