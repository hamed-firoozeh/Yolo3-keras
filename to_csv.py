import os
import glob
import pandas as pd


annotation_list = []
image_labels = os.path.join(os.getcwd()+'/labels')
image_file = os.path.join(os.getcwd()+'/images')
# print('Path : \n', image_labels)

cntr = 0

for csv_file in glob.glob(image_labels + '/*.txt'):
    filename = csv_file#os.path.basename(csv_file)

    cntr += 1
    print(str(cntr) + '  ' + filename)

    csv_wr = open('train_labels.csv', 'a')

    df = pd.read_csv(filename, delimiter=' ',
                     names=['class', 'Xmin','Ymin', 'Xmax', 'Ymax'])
        
    filename2 = filename.replace('.txt','.jpg')

    
    n = df.shape[0]
    if n > 0:
        tmp_str = '{:s} {:d},{:d},{:d},{:d}'.format(filename2, int(df['Xmin'][0]), int(df['Ymin'][0]), int(df['Xmax'][0]), int(df['Ymax'][0]))
    #elif n > 1:
     #   for indx in range(1,n):
     #       tmp_str +=  ',{:d},{:d},{:d},{:d}'.format(int(df['Xmin'][indx]), int(df['Ymin'][indx]), int(df['Xmax'][indx]), int(df['Ymax'][indx]))
    tmp_str +=  ',0\r\n'  # class
    
    csv_wr.write(tmp_str)

csv_wr.close()

print('\nComplete !')
