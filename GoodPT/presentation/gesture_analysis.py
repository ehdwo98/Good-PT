import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import cv2
import warnings
warnings.filterwarnings("ignore")

def movenet(input_image, module):
    """Runs detection on an input image.

    Args:
        input_image: A [1, height, width, 3] tensor represents the input image
        pixels. Note that the height/width should already be resized and match the
        expected input resolution of the model before passing into this function.

    Returns:
        A [1, 1, 17, 3] float numpy array representing the predicted keypoint
        coordinates and scores.
    """
    model = module.signatures['serving_default']

    # SavedModel format expects tensor type of int32.
    input_image = tf.cast(input_image, dtype=tf.int32)
    # Run model inference.
    outputs = model(input_image)
    # Output is a [1, 1, 17, 3] tensor.
    keypoints_with_scores = outputs['output_0'].numpy()
    return keypoints_with_scores

def gesture_analysis(cap):
    model_name = "movenet_lightning"

    if "movenet_lightning" in model_name:
        module = hub.load("https://tfhub.dev/google/movenet/singlepose/lightning/4")
        input_size = 192
    else:
        raise ValueError("Unsupported model name: %s" % model_name)
    
    count = 0
    flag = -1
    count_action = {1:0, 2:0} # action = {1:'back', 2:'turn'}
    prev = {'action':0, 'count':0}
    count_static = 0
    left_wrist = 0
    right_wrist = 0
    left_wrist_prev = 0
    right_wrist_prev = 0

    while True:
        ret, frame = cap.read() # read frame
        
        if not ret: 
            break
        
        # reshape image
        img = frame.copy()
        image = tf.cast(img, dtype=tf.float32)
            
        input_image = tf.expand_dims(image, axis=0)
        input_image = tf.image.resize_with_pad(input_image, input_size, input_size)

        # Run model inference.
        keypoints_with_scores = movenet(input_image, module)

        keypoints = np.squeeze(np.multiply(keypoints_with_scores, [1000, 1000, 1]))
        keypoints_shown = [i for i in range(17) if keypoints[i][2]>0.4]
        
        # 정면 인식
        if 0 not in keypoints_shown or (1 not in keypoints_shown and 2 not in keypoints_shown):
            flag=1
        elif 3 not in keypoints_shown or 5 not in keypoints_shown:
            flag=2
        elif 4 not in keypoints_shown or 6 not in keypoints_shown:
            flag=2
        else:
            flag=0
        
        if flag != -1:
            if prev['action']==flag:
                prev['count']+=1
            else:
                if prev['action']==1 or prev['action']==2:
                    count_action[prev['action']]+=prev['count']
                prev['action']=flag
                prev['count']=1
        
        # 역동성 체크
        movement_distance_left_wrist = 0
        movement_distance_right_wrist = 0
        
        if count>0:
            # 손의 이동 거리 계산
            if 9 in keypoints_shown:
                left_wrist = np.array([keypoints[9][1], keypoints[9][0]])
                movement_distance_left_wrist = np.linalg.norm(abs(left_wrist - left_wrist_prev))
                left_wrist_prev = left_wrist
            else:
                left_wrist = left_wrist_prev
            if 10 in keypoints_shown:
                right_wrist = np.array([keypoints[10][1], keypoints[10][0]])
                movement_distance_right_wrist = np.linalg.norm(abs(right_wrist - right_wrist_prev))
                right_wrist_prev = right_wrist
            else:
                right_wrist = right_wrist_prev
            # print(movement_distance_left_wrist, movement_distance_right_wrist)
        
        # 역동성 측정
        threshold = 10
        if movement_distance_left_wrist <= threshold and movement_distance_right_wrist <= threshold:
            count_static += 1
        # else:
        #     print("사람이 역동적으로 움직이고 있습니다.")
        
        # cv2.imshow('presentation', frame)
        # cv2.imshow('presentation', frame)
        count += 1
        
        # 영상 종료
        # if cv2.waitKey(10) & 0xFF==ord('q'):
        #     break
        # if cv2.waitKey(10) & 0xFF==ord('q'):
        #     break

    cap.release()
    # cv2.destroyAllWindows()
    
    # 제스처 사용 비율
    gesture_rate = (1 - count_static / count)
    
    # 정면 응시 비율
    gaze_rate = (1 - (count_action[1] + count_action[2]) / count)
    
    
    return (gesture_rate, gaze_rate)
    '''
    print('total frame:', count)
    print('뒤돌아 있음:', count_action[1], '/', count_action[1]/count)
    print('옆을 보고 있음:', count_action[2], '/', count_action[2]/count) # 오른쪽으로 도는 것을 잘 인식하지 못함 (왼, 뒤로 인식)
    print('정적인 비율', count_static, '/', count_static/count) # 손목으로 체크 (제스쳐)
    if count_static/count >= 0.9:
        print('너무 움직임이 없습니다. 발표 시 내용에 맞는 제스쳐를 해보세요.')
    elif count_static/count <= 0.79:
        print('너무 움직임이 많습니다. 발표 시 몸의 움직임을 줄여보세요.')
    '''