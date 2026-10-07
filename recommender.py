def split_skills(value):
    return {x.strip().lower() for x in str(value).split(';') if x.strip()}

def career_match(user_skills, career_row):
    required = split_skills(career_row['skills'])
    user = set(user_skills)
    matched = required & user
    missing = required - user
    score = round(100 * len(matched) / len(required)) if required else 0
    return score, sorted(matched), sorted(missing)

def rank_careers(user_skills, careers_df):
    rows = []
    for _, r in careers_df.iterrows():
        score, matched, missing = career_match(user_skills, r)
        rows.append({'Career': r['career'], 'Match %': score,
                     'Matched Skills': ', '.join(matched), 'Missing Skills': ', '.join(missing)})
    return sorted(rows, key=lambda x: x['Match %'], reverse=True)

def recommend_courses(missing_skills, courses_df, limit=5):
    missing = set(missing_skills)
    out=[]
    for _, r in courses_df.iterrows():
        covered = split_skills(r['skills']) & missing
        if covered:
            out.append((len(covered), ', '.join(sorted(covered)), r))
    out.sort(key=lambda x: x[0], reverse=True)
    return out[:limit]

def recommend_projects(missing_skills, projects_df, limit=4):
    missing=set(missing_skills); out=[]
    for _, r in projects_df.iterrows():
        covered=split_skills(r['skills']) & missing
        if covered: out.append((len(covered), ', '.join(sorted(covered)), r))
    out.sort(key=lambda x:x[0], reverse=True)
    return out[:limit]
