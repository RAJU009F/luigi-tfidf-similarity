==================================
Environment
------------
Python -version : Python 2.7.6 (default, Oct 26 2016, 20:30:19) 
OS : 
hduser@mukesh-VirtualBox:~/RAJ/luigi/TF-IDF$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 14.04.5 LTS
Release:	14.04
Codename:	trusty


=======================================
Files /Folders
---------------
1. run.sh contains the commands to execute the script
2. tf_task.py : contains the business logic
3. config.py contains the input file path 
4. result: should be created

===================================
Approach followed:
------------------
As per the guidelines given here - http://rubikloud.github.io/Gurdurr/tfidf_pipeline/

1. CleanTask -  take the input document and cleans it saves in result/parsed_document

2. TFTask - is depends on theCleanTask and reads  result/parsed_document and calcuate the TF as per the definition here http://www.tfidf.com/. outputs to result/tf

3. IDFTask - is also depends on theCleanTask and reads  result/parsed_document and calcuate the IDF as per the definition here http://www.tfidf.com/. outputs to result/idf

4. TFIDFTask - is depends on the TFTask, IDFTask  and calcuates the tf-idf as per the definition here -  http://www.tfidf.com/. outputs to tfidf

5. SimilarityTask - is depends on the TFIDFTask and calculate the EUCLIDEAN distance and between each ocument and sort the output in best similarity to worst similarity

==================================================
HOW TO Run
--------------
NOTE:  Assumed that python2.7, luigi and other libraries/packages(import os,import re,import string,import math,from scipy.spatial import distance ) installed 

1.copy the Raju_sol.zip in a folder then extract.
2.Read README.txt 
3. chmod 777 run.sh
4. ./run.sh
5. track the status of tasks in browser UI
===========================================
What happened when I run run.sh in my machine
-------------------------------------------
hduser@mukesh-VirtualBox:~/RAJ/luigi/TF-IDF$ ./run.sh 
/usr/local/lib/python2.7/dist-packages/luigi/parameter.py:261: UserWarning: Parameter "task_process_context" with value "None" is not of type string.
  warnings.warn('Parameter "{}" with value "{}" is not of type string.'.format(param_name, param_value))
DEBUG: Checking if SimilarityTask(path=result) is complete
DEBUG: Checking if TFIDFTask(path=result) is complete
INFO: Informed scheduler that task   SimilarityTask_result_c589211e05   has status   PENDING
DEBUG: Checking if TFTask(path=result) is complete
DEBUG: Checking if IDFTask(path=result) is complete
INFO: Informed scheduler that task   TFIDFTask_result_c589211e05   has status   PENDING
DEBUG: Checking if CleanTask(path=result) is complete
INFO: Informed scheduler that task   IDFTask_result_c589211e05   has status   PENDING
INFO: Informed scheduler that task   CleanTask_result_c589211e05   has status   PENDING
INFO: Informed scheduler that task   TFTask_result_c589211e05   has status   PENDING
INFO: Done scheduling tasks
INFO: Running Worker with 2 processes
DEBUG: Asking scheduler for work...
DEBUG: Pending tasks: 5
DEBUG: Asking scheduler for work...
INFO: [pid 8739] Worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733) running   CleanTask(path=result)
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: CleanTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
INFO: [pid 8739] Worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733) done      CleanTask(path=result)
INFO: Informed scheduler that task   CleanTask_result_c589211e05   has status   DONE
DEBUG: Asking scheduler for work...
DEBUG: Pending tasks: 4
DEBUG: Asking scheduler for work...
INFO: [pid 8741] Worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733) running   TFTask(path=result)
DEBUG: Pending tasks: 3
DEBUG: 2 running tasks, waiting for next task to finish
INFO: [pid 8742] Worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733) running   IDFTask(path=result)
INFO: [pid 8741] Worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733) done      TFTask(path=result)
INFO: Informed scheduler that task   TFTask_result_c589211e05   has status   DONE
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: IDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
INFO: [pid 8742] Worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733) done      IDFTask(path=result)
INFO: Informed scheduler that task   IDFTask_result_c589211e05   has status   DONE
DEBUG: Asking scheduler for work...
DEBUG: Pending tasks: 2
DEBUG: Asking scheduler for work...
INFO: [pid 8745] Worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733) running   TFIDFTask(path=result)
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: TFIDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: TFIDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: TFIDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: TFIDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: TFIDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: TFIDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: TFIDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: TFIDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: TFIDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: TFIDFTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
INFO: [pid 8745] Worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733) done      TFIDFTask(path=result)
INFO: Informed scheduler that task   TFIDFTask_result_c589211e05   has status   DONE
DEBUG: Asking scheduler for work...
DEBUG: Pending tasks: 1
DEBUG: Asking scheduler for work...
INFO: [pid 8758] Worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733) running   SimilarityTask(path=result)
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: SimilarityTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: SimilarityTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: SimilarityTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: SimilarityTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: SimilarityTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: SimilarityTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: SimilarityTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: SimilarityTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: SimilarityTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: SimilarityTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: SimilarityTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: SimilarityTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: SimilarityTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: SimilarityTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: SimilarityTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: SimilarityTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
DEBUG: SimilarityTask_result_c589211e05 is currently run by worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733)
INFO: [pid 8758] Worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733) done      SimilarityTask(path=result)
INFO: Informed scheduler that task   SimilarityTask_result_c589211e05   has status   DONE
DEBUG: Asking scheduler for work...
DEBUG: Done
DEBUG: There are no more tasks to run at this time
INFO: Worker Worker(salt=814688821, workers=2, host=mukesh-VirtualBox, username=hduser, pid=8733) was stopped. Shutting down Keep-Alive thread
INFO: 
===== Luigi Execution Summary =====

Scheduled 5 tasks of which:
* 5 ran successfully:
    - 1 CleanTask(path=result)
    - 1 IDFTask(path=result)
    - 1 SimilarityTask(path=result)
    - 1 TFIDFTask(path=result)
    - 1 TFTask(path=result)

This progress looks :) because there were no failed tasks or missing dependencies

===== Luigi Execution Summary =====

hduser@mukesh-VirtualBox:~/RAJ/luigi/TF-IDF$ ls -ltr result
total 7828
-rw-r--r-- 1 hduser hadoop  222412 Aug 18 06:49 parsed_document
-rw-r--r-- 1 hduser hadoop  633180 Aug 18 06:49 tf
-rw-r--r-- 1 hduser hadoop  748577 Aug 18 06:49 idf
-rw-r--r-- 1 hduser hadoop  621589 Aug 18 06:49 tfidf
-rw-r--r-- 1 hduser hadoop 5780205 Aug 18 06:50 similarity.csv
hduser@mukesh-VirtualBox:~/RAJ/luigi/TF-IDF$ 




======================================================================
RESULTS FOLDER contents after run.sh

hduser@mukesh-VirtualBox:~/RAJ/luigi/TF-IDF$ ls -ltr result
total 7828
-rw-r--r-- 1 hduser hadoop  222412 Aug 18 06:49 parsed_document
-rw-r--r-- 1 hduser hadoop  633180 Aug 18 06:49 tf
-rw-r--r-- 1 hduser hadoop  748577 Aug 18 06:49 idf
-rw-r--r-- 1 hduser hadoop  621589 Aug 18 06:49 tfidf
-rw-r--r-- 1 hduser hadoop 5780205 Aug 18 06:50 similarity.csv
hduser@mukesh-VirtualBox:~/RAJ/luigi/TF-IDF$ 
