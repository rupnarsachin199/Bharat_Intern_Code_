import nltk
from nltk.corpus import stopwords

# Download the stopwords corpus if not already downloaded
nltk.download('stopwords')

def parse_resume(resume_text, job_keywords):
    # Tokenize the resume text into individual words
    resume_tokens = nltk.word_tokenize(resume_text.lower())
    
    # Remove stopwords from the resume tokens
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in resume_tokens if token.isalpha() and token not in stop_words]
    
    # Count the number of occurrences of each keyword in the resume
    keyword_counts = {keyword: filtered_tokens.count(keyword) for keyword in job_keywords}
    
    # Find the candidate with the highest keyword count
    best_candidate = max(keyword_counts, key=keyword_counts.get)
    
    return best_candidate

# Example usage
resume = '''
John Doe
Software Engineer

Skills:
- Python
- Java
- Machine Learning
- Web Development

Experience:
- Software Engineer at XYZ Inc.

Education:
- Bachelor's Degree in Computer Science

'''

job_keywords = ['python', 'machine learning', 'web development']

best_candidate = parse_resume(resume, job_keywords)
print("Best candidate:", best_candidate)