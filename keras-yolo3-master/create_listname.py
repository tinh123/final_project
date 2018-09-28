import os
def main():
    f_train = open('VOCdevkit/VOC2018/ImageSets/Main/train.txt','w')
    f_test = open('VOCdevkit/VOC2018/ImageSets/Main/test.txt','w')
    f_val = open('VOCdevkit/VOC2018/ImageSets/Main/val.txt','w')
    l = os.listdir('VOCdevkit/VOC2018/Annotations/')
    for i in range(len(l)):
        li = l[i].split('.')[0]
        if i <= 200:
            f_val.writelines(li+'\n')
        elif i>200 and i<600:
            f_test.writelines(li+'\n')
        else:
            f_train.writelines(li+'\n')
    f_train.close()
    f_test.close()
    f_val.close()
        
    # sets = ['train','test', 'val']
    # for set_ in sets:
    #     with open('VOCdevkit/VOC2018/ImageSets/Main/'+set_+'.txt','w') as f:
    #         l=os.listdir('VOCdevkit/VOC2018/data/'+set_)
    #         for i in l:
    #             li=i.split('.')[0] 
    #             f.writelines(li+'\n')
if __name__=="__main__":
    main()