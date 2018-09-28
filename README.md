Runing train model
1. Download data from
2. -Put all .xml file in VOCdevkit/VOC2018/Annotaions/

   -Put all Images (.jpg) file in VOCdevkit/VOC2018/JPEGImages


3. Set up requirement.txt

   pip install -r requirements.txt 
4. Create list files for train, test, validation

   python create_listname.py
5. Run VOC annotation file

   python voc_annotation.py
6. Run training 

   python train.py


