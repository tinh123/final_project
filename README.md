Runing train model
1. Download data from
2. Put all .xml file in VOCdevkit/VOC2018/Annotaions/
   Put all Images (.jpg) file in VOCdevkit/VOC2018/JPEGImages
3. Copy 200 file .xml to VOCdevkit/VOC2018/data/val
   Copy 400 file .xml to VOCdevkit/VOC2018/data/test
   Copy all remaining files to VOCdevkit/VOC2018/data/train
4. Set up requirement.txt
   pip install -r requirements.txt 
5. Create list files for train, test, validation
   python create_listname.py
6. Run VOC annotation file
   python voc_annotation.py
7. Run training 
   python train.py

Create list file name will be update later to save space
