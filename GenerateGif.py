import os,sys
import imageio
#infer the haplotypes of SNPs
def read_go(file_name):
    imgs = os.listdir(file_name)
    print(type(imgs[0]))
    print(imgs[0:2])
    imgs = (file_name+"/"+i for i in imgs if i.endswith('.png'))
    return imgs

def GenerateGif(imgs):
    Gif_Raw = []
    img_sorted = []
    for img in imgs:
        #print(img)
        img_sorted.append(img)
    img_sorted.sort()
    #print(img_sorted)
    for img in img_sorted:
        print(img)
        Gif_Raw.append(imageio.imread(img))
    Gif = imageio.mimsave('/Users/apple/Desktop/IGEM/post/tracking/WormTrack/trackfigure/Imgprocessing.gif',Gif_Raw,duration = 0.05)

if __name__ == "__main__":
    imgs = read_go("/Volumes/igem/WormTrack/WormTrack_summer/ImgeProcessing")
    GenerateGif(imgs)
















