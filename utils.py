from glob import glob


train_img_list = glob('C:/Users/User/PycharmProjects/yolov5_hardhat/Hardhat_Workers/train/images/*.jpg')
test_img_list = glob('C:/Users/User/PycharmProjects/yolov5_hardhat/Hardhat_Workers/test/images/*.jpg')
print(len(train_img_list), len(test_img_list))

from sklearn.model_selection import train_test_split

test_img_list, valid_img_list = train_test_split(test_img_list, test_size=0.5, random_state=777)
print(len(test_img_list), len(valid_img_list))



with open('C:/Users/User/PycharmProjects/yolov5_hardhat/Hardhat_Workers/train.txt', 'w') as f:
    f.write('\n'.join(train_img_list) + '\n')
with open('C:/Users/User/PycharmProjects/yolov5_hardhat/Hardhat_Workers/test.txt', 'w') as f:
    f.write('\n'.join(test_img_list) + '\n')
with open('C:/Users/User/PycharmProjects/yolov5_hardhat/Hardhat_Workers/valid.txt', 'w') as f:
    f.write('\n'.join(valid_img_list) + '\n')

train parameters

--img 416
--batch 32
--epochs 160
--data C:\Users\User\PycharmProjects\yolov5_hardhat\Hardhat_Workers\data.yaml
--cfg C:\Users\User\PycharmProjects\yolov5_hardhat\yolov5-master\models\yolov5s.yaml
--weights ''
--name hardhat_results

valid parameters

--img 416
--iou 0.65
--half
--data C:\Users\User\PycharmProjects\yolov5_hardhat\Hardhat_Workers\data.yaml
--weights C:\Users\User\PycharmProjects\yolov5_hardhat\yolov5-master\runs\train\hardhat_results\weights\best.pt

inference parameters

--img 416
--conf 0.4
--source C:\Users\User\PycharmProjects\yolov5_hardhat\Hardhat_Workers\test\images
--weights C:\Users\User\PycharmProjects\yolov5_hardhat\yolov5-master\runs\train\hardhat_results\weights\best.pt