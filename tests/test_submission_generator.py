from src.ranking.candidate_ranker import (
    rank_candidates
)

from src.utils.data_loader import (
    load_candidates
)

from src.output.submission_generator import (
    save_submission
)

candidates = load_candidates(
    "data/candidates.jsonl"
)

ranked = rank_candidates(
    candidates[:1000]
)

save_submission(
    ranked,
    "submission.csv"
)