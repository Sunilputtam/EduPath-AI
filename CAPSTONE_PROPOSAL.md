# Capstone Project Proposal — EduPath AI

## Title
EduPath AI: An Intelligent Academic and Career Pathway Recommendation System

## Problem Statement
Students often know the career they want but do not know how their current skills compare with the skills expected for that career. Course catalogs, online learning platforms, project ideas, and career information are distributed across many sources. This can make planning inconsistent and overwhelming.

## Proposed Solution
EduPath AI is an explainable recommendation application that converts a student's resume or self-reported skills into a personalized career-learning pathway. The system extracts relevant technical skills, compares them with a selected target career profile, identifies gaps, and recommends courses, portfolio projects, and an ordered learning roadmap.

## Objectives
1. Extract career-relevant skills from student resumes.
2. Quantify alignment with transparent role-specific skill profiles.
3. Identify missing skills for a selected target career.
4. Recommend courses and projects that cover the identified gaps.
5. Generate an actionable learning sequence.
6. Evaluate extraction quality, recommendation relevance, and usability.

## Data
The MVP includes curated career, course, and project skill mappings. The research version can expand these using public course catalogs and public job descriptions. Evaluation should use synthetic, public, de-identified, or consented profiles.

## Methods
- Resume text extraction from PDF/DOCX/TXT
- NLP normalization and skill extraction
- Set-based explainable career matching
- Content-based course/project recommendation
- Rule-based roadmap sequencing
- Interactive Streamlit visualization
- Future extension: embeddings and retrieval-augmented generation (RAG)

## Evaluation
Skill extraction will be evaluated with precision, recall, and F1 against manually labeled profiles. Recommendations can be evaluated with Precision@K/Recall@K against expert relevance judgments. A small user study can measure usefulness, clarity, trust, and actionability using Likert-scale responses. A non-personalized baseline can be used for comparison.

## Expected Outcome
A working web application that helps students understand their career skill gaps and produces explainable recommendations for what to learn and build next.

## Innovation
The project integrates resume understanding, career-gap analysis, course recommendations, project recommendations, and roadmap generation in one explainable workflow rather than providing a single prediction or generic course list.

## Ethical Considerations
The system will not use protected characteristics for recommendations and will not interpret its skill-match score as hiring probability. Recommendations will expose the skill evidence behind them. Any student data used for evaluation should be consented or de-identified.
