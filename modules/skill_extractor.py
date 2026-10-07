import re

ALIASES = {
    "ml": "machine learning", "machine-learning": "machine learning",
    "sklearn": "scikit-learn", "scikit learn": "scikit-learn",
    "powerbi": "power bi", "power-bi": "power bi",
    "large language models": "llm", "large language model": "llm",
    "retrieval augmented generation": "rag", "retrieval-augmented generation": "rag",
    "amazon web services": "aws", "pyspark": "spark"
}

def normalize(text: str) -> str:
    text = text.lower()
    for old, new in ALIASES.items():
        text = re.sub(rf"(?<!\w){re.escape(old)}(?!\w)", new, text)
    return re.sub(r"\s+", " ", text)

def extract_skills(text: str, vocabulary):
    t = normalize(text)
    found = []
    for skill in vocabulary:
        s = skill.strip().lower()
        if s and re.search(rf"(?<!\w){re.escape(s)}(?!\w)", t):
            found.append(s)
    return sorted(set(found))
