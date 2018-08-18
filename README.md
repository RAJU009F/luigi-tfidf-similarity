# luigi-tfidf-similarity

Rubikloud
Software Engineer Technical Problem
The focus of this test is to evaluate:

Ability to quickly learn a new framework (Luigi)
Ability to manipulate and process data
Competency in software development
Problem
Build a pipeline using the ‘Luigi’ python framework that will compute the similarity of documents using euclidean distance of TF-IDF vectors.

Resources
You can learn more about term frequency-inverse document frequency (TF-IDF) at http://www.tfidf.com/
You can download and learn more about Luigi at https://luigi.readthedocs.io/en/stable/#
Python
Python can be downloaded at https://www.python.org/downloads/ . You may use any version of Python (2 or 3) but please specify which version you are using.

You must implement the code to compute TF-IDF, but you may use any standard or common libraries for any other part of the pipeline. If you do use any external library, please be sure to include which packages you are using in a requirements.txt file

Dataset
The file documents.txt contains all of the documents for which you must compute TF-IDF. Documents are separated by the ‘%’ character

Solution
The Luigi pipeline should contain the following tasks

Parse/Cleanup - This step should parse the documents.txt file and remove any punctuation
Compute TF - This step should compute the term-frequency for each term in each document.
Compute IDF - This step should compute the inverse document frequency for each term
Compute TF-IDF - This step will compute the TF-IDF weight of each term in each document
Compute Similarity - This step should determine the similarity between all documents by calculating the Euclidian Distance between each TF-IDF vector.
Expected output
The final output of the pipeline should be a csv with columns corresponding to:
Document 1 ID
Document 2 ID
Similarity
Document id is in the index of the document according to the order defined by the input file.
Output is ordered from most similar to least.
Similarity computed for each pair of documents in the input where document_id_1 < document_id_2
Example:

1,2,0.1
0,2,0.2
0,1,0.3
Submission
Your submission should contain a run.sh file that contains all steps needed to execute your solution (e.g. set up virtual env, install required libraries, execute solution).
Please include a readme.txt file that contains a brief explanation of your approach to solving this problem, any assumptions you made, instructions for executing the solution, and any other relevant notes.
Place all files in your solution in a single zip file, and be sure to only submit runnable code.
