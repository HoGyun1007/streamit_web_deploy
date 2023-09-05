import streamlit as st
from PIL import Image
import torch
from torchvision import transforms, models  # torchvision 추가
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor

# 미리 학습된 가중치 로드 (CPU로 매핑)
weights = torch.load('/Users/imhogyun/my_project/streamit_web_deploy/model_29.pt', map_location=torch.device('cpu'))

# 모델 초기화 (예: 'fasterrcnn_resnet50_fpn')
model = models.detection.fasterrcnn_resnet50_fpn(pretrained=False) 

# 분류기에서 사용할 출력 특성 수 가져오기
in_features = model.roi_heads.box_predictor.cls_score.in_features

# 미리 학습된 헤드 대신 새로운 것 설정 (여기서 num_classes는 클래스 수에 따라 변경)
num_classes = 10  # including background 
model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

model.load_state_dict(weights)
model.eval()

st.title('Custom Faster R-CNN Image Classifier')

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")  # convert("RGB") 추가
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    if st.button('Predict'):
        # 이미지 전처리 및 예측 진행

        preprocess = transforms.Compose([
            transforms.ToTensor(),
        ])

        input_tensor = preprocess(image)  # 이미지 -> 텐서 변환 
        input_batch = input_tensor.unsqueeze(0)  # 배치 차원 추가

        with torch.no_grad():
            prediction = model(input_batch)

            pred_boxes = [[i[0], i[1], i[2], i[3]] for i in list(prediction[0]['boxes'].detach().numpy())]
            pred_labels_indices =[i for i in list(prediction[0]['labels'].detach().numpy())] 

            class_names=['background', '벤츠_C-Class', '아우디_A4', '아우디_A6', '아우디_Q7', '벤츠_A-Class','벤츠_CLA-Class','아우디_A7','아우디_Q5', '벤츠_CLS-Class'] # 클래스 이름을 여러분의 데이터셋에 맞게 변경해주세요.
            pred_labels = [class_names[i] for i in pred_labels_indices]

            st.write(f'예측된 차종: {pred_labels}')
