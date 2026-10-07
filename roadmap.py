PRIORITY = ['statistics','sql','python','pandas','machine learning','scikit-learn','data visualization','tableau','power bi','deep learning','pytorch','tensorflow','nlp','llm','rag','langchain','vector databases','spark','hadoop','etl','airflow','databases','docker','aws','mlops','git']

def build_roadmap(missing):
    missing=set(missing)
    ordered=[x for x in PRIORITY if x in missing] + sorted(missing-set(PRIORITY))
    return [{'Step': i+1, 'Skill': s.title(), 'Goal': f'Learn {s} and demonstrate it in a small practical artifact.'} for i,s in enumerate(ordered)]
