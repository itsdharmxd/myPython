import os,shutil
dict_extention={
      "audio_extention":('.mp3','.m4a','.wav','.flac'),
      "video_extention":('.mp4','.mkv','.MKV','.flv','.mpeg'),
      'doc_extention':('.pdf','.doc','.txt','.docx'),
      'image_extention':('.jpg','.png')
}
print('ENTER THE PATH OF THE FOLDER\nWHERE YOU WANT YOUR MESS UP FILES TO BE ARRANGED \nIN THEIR RESPECTIVE FILE TYPE......................\n{Audio , Video , Image , Documents }\n|\n|\n|')

folder_path=input('ENTER folder path here=')
def file_finder(folder_path,file_extention):
    files=[]
    for fil in os.listdir(folder_path):
        for exten in file_extention:
            if fil.endswith(exten):
                files.append(fil)
    return files            
#print(file_finder(folder_path,))
for extention_type,extention_tuple in dict_extention.items():
    folder_name=extention_type.split('_')[0]+'files'
    folder_pat=os.path.join(folder_path,folder_name)
    os.mkdir(folder_pat) 
    for item in file_finder(folder_path,extention_tuple):
        item_path=os.path.join(folder_path,item)
        item_new_path=os.path.join(folder_pat,item)
        shutil.move(item_path,item_new_path)
    print('calling finder function')
    #print(file_finder(folder_path,extention_tuple))


