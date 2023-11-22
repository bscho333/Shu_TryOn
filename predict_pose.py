import cv2
import numpy as np
import os
import json
import argparse

coco_points_name = {
            "Nose": 0, "Neck": 1,
            "RShoulder": 2, "RElbow": 3, "RWrist": 4,
            "LShoulder": 5, "LElbow": 6, "LWrist": 7,
            "RHip": 8, "RKnee": 9, "RAnkle": 10,
            "LHip": 11, "LKnee": 12, "LAnkle": 13,
            "REye": 14, "LEye": 15,
            "REar": 16, "LEar": 17,
            "Background": 18}

body_25_points_name = {
            "Nose": 0, "Neck": 1,
            "RShoulder": 2, "RElbow": 3, "RWrist": 4,
            "LShoulder": 5, "LElbow": 6, "LWrist": 7,
            "MidHip": 8, "RHip": 9, "RKnee": 10,
            "RAnkle": 11, "LHip": 12, "LKnee": 13,
            "LAnkle": 14, "REye": 15, "LEye": 16,
            "REar": 17, "LEar": 18, "LBigToe": 19,
            "LSmallToe": 20, "LHeel": 21, "RBigToe": 22,
            "RSmallToe": 23, "RHeel": 24, "Background": 25}

coco_point_pairs = [[1, 0], [1, 2], [1, 5],
                            [2, 3], [3, 4], [5, 6],
                            [6, 7], [1, 8], [8, 9],
                            [9, 10], [1, 11], [11, 12],
                            [12, 13], [0, 14], [0, 15],
                            [14, 16], [15, 17]]

body_25_point_pairs = [[0, 1], [0, 15], [0, 16], [1, 2], [1, 5], [1, 8], [8, 9], [8, 12], [9, 10], [12, 13], [2, 3],
                      [3, 4], [5, 6], [6, 7], [10, 11], [13, 14], [15, 17], [16, 18], [14, 21], [19, 21], [20, 21],
                      [11, 24], [22, 24], [23, 24]]

threshold = 0.1

class general_coco_model(object):
    def __init__(self, modelpath):
        # Specify the model to be used
        #   Body25: 25 points
        #   COCO:   18 points
        #   MPI:    15 points
        self.inWidth = 368
        self.inHeight = 368
        self.threshold = threshold
        self.pose_net = self.general_coco_model(modelpath)

    def general_coco_model(self, modelpath):
        self.points_name = coco_points_name
        self.num_points = 18
        self.point_pairs = coco_point_pairs
        prototxt   = os.path.join(
            modelpath, 
            'pose_deploy_linevec.prototxt')
        caffemodel = os.path.join(
            modelpath, 
            'pose_iter_440000.caffemodel')
        coco_model = cv2.dnn.readNetFromCaffe(prototxt, caffemodel)

        return coco_model

    def predict(self, imgfile):
        img_cv2 = cv2.imread(imgfile)
        img_height, img_width, _ = img_cv2.shape
        inpBlob = cv2.dnn.blobFromImage(img_cv2, 
                                        1.0 / 255, 
                                        (self.inWidth, self.inHeight),
                                        (0, 0, 0), 
                                        swapRB=False, 
                                        crop=False)
        self.pose_net.setInput(inpBlob)
        self.pose_net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        self.pose_net.setPreferableTarget(cv2.dnn.DNN_TARGET_OPENCL)

        output = self.pose_net.forward()

        H = output.shape[2]
        W = output.shape[3]
        
        points = []
        for idx in range(self.num_points):
            probMap = output[0, idx, :, :] # confidence map.

            # Find global maxima of the probMap.
            minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

            # Scale the point to fit on the original image
            x = (img_width * point[0]) / W
            y = (img_height * point[1]) / H

            if prob > self.threshold:
                points.append(x)
                points.append(y)
                points.append(prob)
            else:
                points.append(0)
                points.append(0)
                points.append(0)

        return points

class general_body25_model(object):
    def __init__(self, modelpath):
        # Specify the model to be used
        #   Body25: 25 points
        #   COCO:   18 points
        #   MPI:    15 points
        self.inWidth = 368
        self.inHeight = 368
        self.threshold = threshold
        self.pose_net = self.general_body25_model(modelpath)

    def general_body25_model(self, modelpath):
        self.points_name = body_25_points_name
        self.num_points = 25
        self.point_pairs = body_25_point_pairs
        prototxt   = os.path.join(
            modelpath,
            'pose_deploy.prototxt')
        caffemodel = os.path.join(
            modelpath,
            'pose_iter_584000.caffemodel')
        body25_model = cv2.dnn.readNetFromCaffe(prototxt, caffemodel)

        return body25_model

    def predict(self, imgfile):
        img_cv2 = cv2.imread(imgfile)
        frame = img_cv2.copy()
        img_height, img_width, _ = img_cv2.shape
        inpBlob = cv2.dnn.blobFromImage(img_cv2,
                                        1.0 / 255,
                                        (self.inWidth, self.inHeight),
                                        (0, 0, 0),
                                        swapRB=False,
                                        crop=False)
        self.pose_net.setInput(inpBlob)
        self.pose_net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        self.pose_net.setPreferableTarget(cv2.dnn.DNN_TARGET_OPENCL)

        output = self.pose_net.forward()

        H = output.shape[2]
        W = output.shape[3]

        points = []
        for idx in range(self.num_points):
            probMap = output[0, idx, :, :]  # confidence map.

            # Find global maxima of the probMap.
            minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

            # Scale the point to fit on the original image
            x = (img_width * point[0]) / W
            y = (img_height * point[1]) / H

            if prob > self.threshold:
                points.append(x)
                points.append(y)
                points.append(prob)
            else:
                points.append(0)
                points.append(0)
                points.append(0)
        return points


def generate_pose_keypoints(img_file, pose_file):

    modelpath = 'pose'
    pose_model = general_body25_model(modelpath)

    res_points = pose_model.predict(img_file)

    pose_data = {"version": 1.3,
                 "people":  [
                                {
                                    "person_id": [-1],
                                    "pose_keypoints_2d": res_points
                                }
                            ]
                }

    pose_keypoints_path = pose_file

    json_object = json.dumps(pose_data, indent = 4) 
  
    # Writing to sample.json 
    with open(pose_keypoints_path, "w") as outfile: 
        outfile.write(json_object) 
    print('File saved at {}'.format(pose_keypoints_path))


def generate_img_from_json(pose_file, img_file, save_path, model='body25'):
    points_name = body_25_points_name if model == 'body25' else coco_points_name
    point_pairs = body_25_point_pairs if model == 'body25' else coco_point_pairs
    with open(pose_file) as f:
        data = json.load(f)
    pose_keypoints = data['people'][0]['pose_keypoints_2d']
    img = cv2.imread(img_file)
    img_height, img_width, _ = img.shape
    for pair in point_pairs:
        partA = pair[0]
        partB = pair[1]
        if pose_keypoints[partA*3+2] > threshold and pose_keypoints[partB*3+2] > threshold:
            cv2.line(img, (int(pose_keypoints[partA*3]), int(pose_keypoints[partA*3+1])),
                     (int(pose_keypoints[partB*3]), int(pose_keypoints[partB*3+1])), (0, 255, 0), 3)
    for i in range(0, len(pose_keypoints), 3):
        x = int(pose_keypoints[i])
        y = int(pose_keypoints[i+1])
        prob = pose_keypoints[i+2]
        cv2.circle(img, (x, y), 5, (0, 255, 255), -1)
        cv2.putText(img, str(i//3), (x + 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
    cv2.imwrite(save_path, img)
    print('File saved at {}'.format(save_path))

def parse_args():
    parser = argparse.ArgumentParser(description="Full inference script")

    parser.add_argument(
        "--img_dir",
        type=str,
        # default="stabilityai/stable-diffusion-2-inpainting",
        help="Path to input directory",
    )

    parser.add_argument(
        "--output_dir",
        type=str,
        # default="result",
        help="Path to the output directory",
    )

    parser.add_argument(
        "--pose_dir",
        type=str,
        # default="stabilityai/stable-diffusion-2-inpainting",
        help="Path to input directory",
    )

    args = parser.parse_args()
    env_local_rank = int(os.environ.get("LOCAL_RANK", -1))
    if env_local_rank != -1 and env_local_rank != args.local_rank:
        args.local_rank = env_local_rank

    return args
def main():
    args = parse_args()
    img_file = args.img_dir
    pose_file = args.pose_dir
    generate_img_from_json(pose_file, img_file, args.output_dir, model='body25')

if __name__ == '__main__':
    main()
