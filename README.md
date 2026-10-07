# EduPath AI

**Intelligent Academic & Career Pathway Recommendation System**

EduPath AI is a capstone-ready prototype that analyzes a student's resume or skills, measures alignment with a target data/AI career, identifies skill gaps, and recommends courses, portfolio projects, and a personalized learning roadmap.

## Features
- PDF, DOCX and TXT resume parsing
- Vocabulary-based NLP skill extraction with aliases
- Career-readiness percentage and transparent matched/missing skills
- Six data/AI career profiles
- Course and portfolio-project recommendations based on skill gaps
- Personalized ordered learning roadmap
- Alternative-career ranking
- Interactive Streamlit dashboard
- Rule-based advisor that works without a paid API
- Unit tests and sample resume

## Architecture
Student Resume/Profile -> Text Extraction -> Skill Extraction -> Career Skill Profile -> Matching & Gap Analysis -> Course/Project Recommendation -> Roadmap -> Dashboard/Advisor

## Run locally
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Test
```bash
pytest
```

## Research / Capstone Question
**Can a transparent skill-gap-based recommendation system convert a student's existing academic and professional profile into useful, personalized career-learning pathways?**

## Suggested Evaluation
1. Create 30-100 synthetic or consented student profiles.
2. Have 2-3 reviewers label relevant target skills/courses for each profile.
3. Measure skill extraction precision, recall and F1.
4. Evaluate recommendation Precision@K / Recall@K.
5. Conduct a small usability survey (usefulness, clarity, trust, actionability; 1-5 Likert scale).
6. Compare the proposed personalized approach against a popularity/random baseline.

## Ethical considerations
- Do not use protected attributes to rank students.
- Do not present readiness scores as hiring probabilities.
- Explain which skills produced each recommendation.
- Validate skill profiles and recommendations with domain experts.
- Use only consented/de-identified student data for research evaluation.

## Capstone extensions
- Replace vocabulary extraction with sentence-transformer embeddings or an NER model.
- Add a grounded RAG advisor using official university course/career documents.
- Add prerequisite-aware course sequencing using a graph.
- Connect live job descriptions and measure market-skill gaps.
- Add authentication and persistent student progress.

## Academic integrity
This repository is a starting implementation. Adapt, test, document and explain your own contribution, and follow your course's rules for AI assistance and external/open-source code.
