# Project 3    : AI Recommendation Logic
# Intern Name  : Divyanjali Mandadi
# Batch        : 2026
# Organization : DecodeLabs
# System       : Tech Stack Recommender

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

job_roles = {
    "Data Scientist":
        "python sql machine learning data analysis statistics pandas numpy",

    "ML Engineer":
        "python machine learning tensorflow pytorch deep learning algorithms",

    "Data Analyst":
        "sql python excel data analysis power bi tableau reporting",

    "Backend Developer":
        "python java sql apis rest django flask databases",

    "Frontend Developer":
        "javascript html css react nodejs ui design",

    "DevOps Engineer":
        "aws docker kubernetes git ci cd linux cloud automation",

    "Cloud Architect":
        "aws azure cloud computing infrastructure automation devops",

    "Cybersecurity Analyst":
        "networking security ethical hacking linux firewalls encryption",

    "Full Stack Developer":
        "javascript python html css react nodejs databases apis",

    "AI Research Scientist":
        "python deep learning neural networks research mathematics statistics",

    "Database Administrator":
        "sql mysql postgresql mongodb database optimization performance",

    "Mobile App Developer":
        "flutter dart java kotlin android ios mobile development",

    "Business Analyst":
        "excel sql reporting data analysis communication requirements stakeholders",

    "System Administrator":
        "linux windows networking servers automation shell scripting",

    "Blockchain Developer":
        "solidity ethereum smart contracts cryptography python javascript"
}

print("=" * 55)
print("   Tech Stack Recommender")
print("   AI-Powered Career Path Matching Engine")
print("   Powered by TF-IDF + Cosine Similarity")
print("   DecodeLabs | Batch 2026")
print("=" * 55)

print("\nAvailable Skills You Can Enter:")
print("   python, sql, machine learning, javascript,")
print("   docker, aws, cloud, java, deep learning,")
print("   react, git, linux, tensorflow, excel,")
print("   networking, security, data analysis, etc.")

print("\n" + "-" * 55)
print("STEP 1: INGESTION - Enter your skills")
print("-" * 55)

skill1 = input("\nEnter your Skill 1: ").strip().lower()
skill2 = input("Enter your Skill 2: ").strip().lower()
skill3 = input("Enter your Skill 3: ").strip().lower()

print("\n(Optional) Enter more skills or press Enter to skip:")
skill4 = input("Skill 4 (optional): ").strip().lower()
skill5 = input("Skill 5 (optional): ").strip().lower()

user_skills = f"{skill1} {skill2} {skill3}"
if skill4:
    user_skills += f" {skill4}"
if skill5:
    user_skills += f" {skill5}"

print(f"\nYour Profile   : {user_skills}")
print("Ingestion Complete")

print("\n" + "-" * 55)
print("STEP 2: SCORING - Calculating Similarities")
print("-" * 55)

job_names        = list(job_roles.keys())
job_descriptions = list(job_roles.values())
all_documents    = [user_skills] + job_descriptions

vectorizer   = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(all_documents)

user_vector       = tfidf_matrix[0]
job_vectors       = tfidf_matrix[1:]
similarity_scores = cosine_similarity(user_vector, job_vectors)[0]

print("TF-IDF Vectorization Complete")
print("Cosine Similarity Scores Calculated")

print("\n" + "-" * 55)
print("STEP 3: SORTING - Ranking by Best Match")
print("-" * 55)

scored_jobs = list(zip(job_names, similarity_scores))
sorted_jobs = sorted(scored_jobs, key=lambda x: x[1], reverse=True)

print("All Jobs Ranked by Similarity Score")

print("\n" + "-" * 55)
print("STEP 4: FILTERING - Top 3 Results Only")
print("-" * 55)

top_n      = 3
top_results = sorted_jobs[:top_n]

print("\n" + "=" * 55)
print("      YOUR TOP CAREER RECOMMENDATIONS")
print("=" * 55)
print(f"\n   Based on your skills: {user_skills}\n")

ranks = ["Rank 1", "Rank 2", "Rank 3"]

for i, (job, score) in enumerate(top_results):
    percentage  = score * 100
    bar_filled  = int(percentage / 5)
    bar         = "#" * bar_filled + "-" * (20 - bar_filled)

    print(f"   {ranks[i]}: {job}")
    print(f"   Match Score  : {percentage:.1f}%")
    print(f"   [{bar}]")
    print(f"   Skills Needed: {job_roles[job][:55]}...")
    print()

print("-" * 55)
print("ALL JOB MATCH SCORES:")
print("-" * 55)
for job, score in sorted_jobs:
    percentage = score * 100
    marker     = "***" if percentage > 50 else "   "
    print(f"   {marker} {job:35s}: {percentage:.1f}%")
