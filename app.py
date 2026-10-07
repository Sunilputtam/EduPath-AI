import pandas as pd
import streamlit as st
import plotly.express as px
from modules.resume_parser import extract_text
from modules.skill_extractor import extract_skills
from modules.recommender import split_skills, career_match, rank_careers, recommend_courses, recommend_projects
from modules.roadmap import build_roadmap

st.set_page_config(page_title='SkillMetrixa', page_icon='', layout='wide')
st.title('SkillMetrixa')
st.caption('A Data-Driven Skill Gap Analysis and Career Recommendation System')

@st.cache_data
def load_data():
    return (pd.read_csv('data/careers.csv'), pd.read_csv('data/courses.csv'), pd.read_csv('data/projects.csv'))
careers, courses, projects = load_data()
vocab=set()
for df in (careers,courses,projects):
    for v in df['skills']: vocab |= split_skills(v)

with st.sidebar:
    st.header('Student Profile')
    target=st.selectbox('Target career', careers['career'].tolist())
    uploaded=st.file_uploader('Upload resume', type=['pdf','docx','txt'])
    manual=st.text_area('Or paste skills / resume text', placeholder='Python, SQL, Tableau, machine learning...')

text=manual
if uploaded:
    try: text += '\n' + extract_text(uploaded)
    except Exception as e: st.error(str(e))

skills=extract_skills(text, vocab) if text.strip() else []
target_row=careers[careers['career']==target].iloc[0]
score, matched, missing=career_match(skills,target_row)

c1,c2,c3,c4=st.columns(4)
c1.metric('Career Readiness', f'{score}%')
c2.metric('Skills Detected', len(skills))
c3.metric('Matched', len(matched))
c4.metric('Skill Gaps', len(missing))

if not text.strip():
    st.info('Upload a resume or paste your skills in the sidebar to generate your personalized analysis.')

st.subheader('Career Readiness')
fig=px.bar(pd.DataFrame({'Category':['Matched','Missing'],'Skills':[len(matched),len(missing)]}), x='Category', y='Skills', text='Skills')
st.plotly_chart(fig, use_container_width=True)

left,right=st.columns(2)
with left:
    st.markdown('#### Detected / Matched Skills')
    st.write(', '.join(matched) if matched else 'No target skills detected yet.')
with right:
    st.markdown('#### Missing Skills')
    st.write(', '.join(missing) if missing else 'No gaps for this skill profile.')

st.subheader('Recommended Courses')
course_recs=recommend_courses(missing,courses)
if course_recs:
    for _,covered,r in course_recs:
        with st.expander(f"{r['course']} — {r['level']} · {r['duration_weeks']} weeks"):
            st.write(r['description']); st.caption('Addresses: '+covered)
else: st.write('No course recommendations needed for the current target profile.')

st.subheader('Recommended Portfolio Projects')
project_recs=recommend_projects(missing,projects)
for _,covered,r in project_recs:
    st.markdown(f"**{r['project']}** — {r['difficulty']}  \n{r['description']}  \n*Develops: {covered}*")

st.subheader('Personalized Learning Roadmap')
roadmap=build_roadmap(missing)
if roadmap: st.dataframe(pd.DataFrame(roadmap), use_container_width=True, hide_index=True)
else: st.success('Your listed skills cover the baseline requirements for this target role. Build deeper portfolio evidence next.')

st.subheader('Alternative Career Matches')
ranked=pd.DataFrame(rank_careers(skills,careers))
st.dataframe(ranked, use_container_width=True, hide_index=True)

st.subheader('Rule-Based Academic & Career Advisor')
question=st.text_input('Ask: What should I learn next? Which project should I build?')
if question:
    q=question.lower()
    if 'project' in q:
        answer = project_recs[0][2]['project'] if project_recs else 'an advanced project demonstrating your target-role skills'
        st.write(f'I recommend **{answer}** first because it addresses skills currently missing from your {target} profile.')
    elif 'course' in q or 'learn' in q or 'next' in q:
        if course_recs: st.write(f"Start with **{course_recs[0][2]['course']}**. It directly addresses: {course_recs[0][1]}.")
        else: st.write('Focus on advanced practice, deployment, and portfolio evidence rather than another introductory course.')
    else:
        st.write(f'Your current {target} readiness is **{score}%**. Prioritize these gaps: '+(', '.join(missing[:5]) if missing else 'portfolio depth and interview preparation')+'.')

st.divider()
st.caption('Capstone prototype: recommendations are decision support, not guarantees of academic or employment outcomes.')
