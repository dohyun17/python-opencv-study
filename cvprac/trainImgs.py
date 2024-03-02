import os
import cv2
from faceDetector import FaceDetector

class TrainImgs():
    def __init__(self):
        PATH = os.getcwd()
        cur_dir = os.path.join(PATH, 'cvprac')
        self.data_folder_path = os.path.join(cur_dir, "training_data")
        
        #detect face
        self.detector = FaceDetector()
    
    def prepare_training_data(self):
        #--STEP-1--
        # get the directories (one directory for each subject) in data folder
        dirs = os.listdir(self.data_folder_path)
        
        # list to hold all subject faces
        faces = []
        # list to hold labels for all subjects
        labels = []
        
        #let's go through each directory and read images within it
        for dir_name in dirs:
            
            # our subject directories start with letter 's' so
            #ignore any non-relevant directories if any
            if not dir_name.startswith('s'):                
                continue
            
            #--STEP-2--
            #extract label number of subject from dir_name
            #format of dir name = slabel
            #, so removing letter 's' from dir_name will give us label
            label = int(dir_name.replace("s", ""))
            
            #build path of directory contain images for current subject
            #sample subject_dir_path = "training_data/s1"
            subject_dir_path = os.path.join(self.data_folder_path , dir_name)
            
            # get the images names that are inside the given subject directory
            subject_images_names = os.listdir(subject_dir_path)
            
            #--STEP-3--
            #go through each image name, read image,
            #detect face and add face to list of faces
            for image_name in subject_images_names:
                #print("3")
                #ignore system files like .DS_Store
                if image_name.startswith("."):
                    #print("3-1")
                    continue
                
                #build image path
                #sample image path=training_data/s1/user_1.jpg
                image_path = os.path.join(subject_dir_path ,image_name)
                print(image_path)
                if image_path[image_path.index(".") + 1 : ] == 'db':
                    continue
                #read image
                image = cv2.imread(image_path)
                
                #display an image window to show the image
                cv2.imshow("Training on image ..", cv2.resize(image, (400, 500)))
                cv2.waitKey(100)                
                
                face, rect = self.detector.detect_face(image)
                
                #--STEP-4--
                # for the purpose of this tutorial
                # we will ignore faces that are not detected
                if face is not None:
                    # add face to list of faces
                    faces.append(face)
                    labels.append(label)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        return faces, labels