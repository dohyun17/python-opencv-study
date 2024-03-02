from trainImgs import TrainImgs

trainImg = TrainImgs()

##################################################
###    머신러닝이 사진들을 읽고 학습하는 구간     ###
faces, labels = trainImg.prepare_training_data()