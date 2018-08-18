# luigi-tfidf-similarity


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

