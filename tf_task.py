import luigi
import os
import re
import string
import math
from scipy.spatial import distance
from operator import itemgetter
from config import INPUT_FILE_PATH


"""
Compute TF - This step should compute the term-frequency for each term in each document.
How To Run: python tf_task.py TFTask --path 'result' --workers=2
"""
class TFTask(luigi.Task):
	path = luigi.Parameter(default="result")
	
	def run(self):
		#docs =  self.input()

		input_file =  self.input().path
		if input_file:
			docs_dic = {}
			count = 0
			total_words = 0
			with open(self.input().path, 'r' ) as docs:

				docs_list = docs.read().split("\n%\n")
				#print docs_list

				for doc in docs_list:
					words = doc.replace("\n","").strip().split()
					words_count = len(words) 
					word_dic = {}
					word_dic['total_words'] = words_count 
					for word in words: 											
						word =  word.strip()
						if word in word_dic:
							tmp = word_dic[word]
							word_dic[word] = tmp + 1
						else:
							word_dic[word] = 1
					for key in word_dic.keys():
						total_words_doc = word_dic['total_words']
						if key not in 'total_words':
							c =  word_dic[key]
							word_dic[key] = float(c) / float(total_words_doc) 	
					docs_dic[count] = word_dic
					#print docs_dic
					count =  count +1		
			with open('result/tf'.format(self.path), 'w') as out_file:
				for i in range(0, count):
					word_dic = docs_dic[i]
					for word in word_dic.keys():
						out_file.write("{}:{} ".format(word, word_dic[word]) )
					out_file.write('\n%\n')						
				out_file.close()			
						
	def output(self):
		return luigi.LocalTarget("{}/tf".format(self.path))
	
	def requires(self):
		return CleanTask()



"""
Compute TF-IDF - This step will compute the TF-IDF weight of each term in each document
How To Run: python tf_task.py TFIDFTask --path 'result' --workers=2
"""		
class TFIDFTask(luigi.Task):
	path = luigi.Parameter(default="result")	
	
	def output(self):
		return luigi.LocalTarget("{}/tfidf".format(self.path))
	
	def requires(self):
		return [TFTask(), IDFTask()]
		
	def run(self):
		tf_dic = {}
		idf_dic  = {}
		count = 0
		with open(self.input()[0].path, 'r') as tf_file:
		 	tf_list = tf_file.read().split("\n%\n")
			for doc in tf_list:
				terms = doc.replace("\n","").split()
				temp_tf_dic = {}
				for term in terms:
					k, v = term.split(":")
					if k.strip() and k not in 'total_words':
						temp_tf_dic[k.strip()] = v.strip()
				if not len(temp_tf_dic) == 0:		
					tf_dic[count] = temp_tf_dic
					count =  count + 1		
						
		with open(self.input()[1].path, 'r') as idf_file:
				idf_list = idf_file.read().split()		
				for term in idf_list:
					#print '========== {}'.format(term)
					k, v = term.split(":")
					if k.strip():
						idf_dic[k.strip()] = v.strip()
						
		with open('{}/tfidf'.format(self.path), 'w') as out_file:
			
			for i in range(0, count):
				temp_tf_dic = tf_dic[i]
				for key in temp_tf_dic.keys():
					key_tf = temp_tf_dic[key]
					if key in idf_dic.keys():
						key_idf = idf_dic[key]
						out_file.write('{}:{} '.format( key, float(key_tf)*float(key_idf)))
					else:
						out_file.write('{}:0 '.format( key))
				out_file.write("\n%\n")
								
			out_file.close()



"""
Compute Similarity - This step should determine the similarity between all documents by calculating the Euclidian Distance between each TF-IDF vector.
How To Run: python tf_task.py SimilarityTask --path 'result' --workers=2
"""
class SimilarityTask(luigi.Task):
	path =  luigi.Parameter(default="result")

	def output(self):
		return luigi.LocalTarget("{}/similarity.csv".format(self.path))
		
	def requires(self):
		return TFIDFTask()	
			
	def run(self):
		tfidf_vec_all = []
		count = 0
		sim_list = []
		with open(self.input().path, 'r') as tf_file:
		 	tf_list = tf_file.read().split("\n%\n")
			for doc in tf_list:
				terms = doc.replace("\n","").split()
				tfidf_vec = []
				for term in terms:
					k, v = term.split(":")
					if k.strip():
						tfidf_vec.append(float(v.strip()))
				if not len(tfidf_vec) == 0:		
					tfidf_vec_all.append( tfidf_vec)
					count =  count + 1	

		for i in range(0, count):
			for j in range(i+1, count):
				a = tfidf_vec_all[i]
				b = tfidf_vec_all[j]
				a_len = len(tfidf_vec_all[i])
				b_len = len(tfidf_vec_all[j])
				if a_len > b_len:
					for k in range(b_len, a_len):
						b.append(0)
				else:				
					for k in range(a_len, b_len):
						a.append(0)
				# now calculate the Euclidean dist	
				d =  distance.euclidean(a,b)
				temp_list = [i, j, d]
				sim_list.append(temp_list)
		#sort according to the similarity
		sorted(sim_list, key=itemgetter(2))	
		with open("{}/similarity.csv".format(self.path), 'w') as out_file:
			for sim in sim_list:
				out_file.write('{},{},{}'.format(sim[0], sim[1], sim[2]))
				out_file.write("\n")
			out_file.close()
									
				
"""
Compute IDF - This step should compute the inverse document frequency for each term
How To Run: python tf_task.py IDFTask --path 'result' --workers=2
"""									 	
class IDFTask(luigi.Task):
	path =  luigi.Parameter(default="result")
	
	
	def output(self):
		return luigi.LocalTarget("{}/idf".format(self.path))
	
	
	def requires(self):
		return CleanTask()
		
	
	def run(self):
		input_file =  self.input().path
		if input_file:
			words_list = []
			words_doc_list = []
			count = 0
			total_docs = 0
			with open(self.input().path, 'r' ) as docs:
				docs_list = docs.read().split("\n%\n")
				total_docs = len(docs_list)
				for doc in docs_list:
					words = doc.replace("\n","").strip().split()
					temp_list = []
					for word in words:
						words_list.append(word)
						temp_list.append(word)
					words_doc_list.append(temp_list)	
			with open('{}/idf'.format(self.path), 'w') as out_file:
				for word in words_list:
					count_word = 0
					for doc in words_doc_list:
						if word in doc:
							count_word = count_word + 1
						else:
							pass
					out_file.write('{}:{} '.format(word, (math.log(float(total_docs)/ float(count_word)))))		



"""
Parse/Cleanup - This step should parse the documents.txt file and remove any punctuation
How To Run: python tf_task.py CleanTask --path 'result' --workers=2
"""	
class CleanTask(luigi.Task):
	path = luigi.Parameter(default="result")
	
	def run(self):
		count = 0
		content = ""
		punc = set(string.punctuation)
		with open(INPUT_FILE_PATH, 'r') as docs:
		
			for doc in docs.read().split("%"):
				doc =  doc.strip()
				count = count + 1
				doc = ''.join( c for c in doc if c not in punc)
				if not content :
					content = doc 
				else:	
					content = content+ '\n%\n' + doc 
		with open("{}/parsed_document".format(str(self.path)), 'w') as out_file:
			out_file.write(content)
			out_file.close()

			
	def output(self):
		return luigi.LocalTarget("{}/parsed_document".format(str(self.path)))
		
	def requires(self):
		return []	
		
		
if __name__ == "__main__":
	luigi.run()
					

