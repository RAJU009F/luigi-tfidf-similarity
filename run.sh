rm -r result
mkdir result
luigid --background --logdir logs
python tf_task.py SimilarityTask --path 'result' --workers=2


