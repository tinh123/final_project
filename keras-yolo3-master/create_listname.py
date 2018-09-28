import os
def main():
    sets = ['train','test', 'val']
    for set_ in sets:
        with open('VOCdevkit/VOC2018/ImageSets/Main/'+set_+'.txt','w') as f:
            l=os.listdir('VOCdevkit/VOC2018/data/'+set_)
            for i in l:
                li=i.split('.')[0] 
                f.writelines(li+'\n')
if __name__=="__main__":
    main()