google_bert_path= '/data/gavin/research/OpenPAR/MSP60K_Benchmark_Dataset/LLM-PAR/weights/google-bertbert-base-uncased'
minigpt4_path= '/data/gavin/research/OpenPAR/MSP60K_Benchmark_Dataset/LLM-PAR/weights/vicuna-7b/prerained_minigpt4_7b.pth'
vicuna_7b_path= '/data/gavin/research/OpenPAR/MSP60K_Benchmark_Dataset/LLM-PAR/weights/vicuna-7b'
blip2_path = '/data/gavin/research/OpenPAR/MSP60K_Benchmark_Dataset/LLM-PAR/weights/blip2_pretrained_flant5xxl.pth'
eva_vit_g_path = '/data/gavin/research/OpenPAR/MSP60K_Benchmark_Dataset/LLM-PAR/weights/eva_vit_g.pth'

def get_pkl_rootpath(dataset):
    if dataset=="RAPv1":
        root_path='/data/liangtao/DataSets/PAR_Dataset/RAPv1/RAP_dataset'
        pkl_path='/data/liangtao/DataSets/PAR_Dataset/RAPv1/rap1_template.pkl'
    elif dataset=="RAPv2":  
        root_path='/data/liangtao/DataSets/PAR_Dataset/RAPv2/RAP_dataset'
        pkl_path='/data/liangtao/DataSets/PAR_Dataset/RAPv2/rap2_template.pkl'
    elif dataset=="PETA": 
        root_path='/data/liangtao/DataSets/PAR_Dataset/PETA/images'
        pkl_path='/data/liangtao/DataSets/PAR_Dataset/PETA/peta_template.pkl'
    elif dataset=="PA100k": 
        root_path='/data/liangtao/DataSets/PAR_Dataset/PA100k/release_data/release_data'
        pkl_path='/data/liangtao/DataSets/PAR_Dataset/PA100k/pa100k_template.pkl'
    elif dataset=="RAPzs": 
        root_path='/data/liangtao/DataSets/PAR_Dataset/RAPv2/RAP_dataset'
        pkl_path='/data/liangtao/DataSets/PAR_Dataset/RAPv2/rapzs_template.pkl'
    elif dataset=="PETAzs":
        root_path='/data/liangtao/DataSets/PAR_Dataset/PETA/images'
        pkl_path='/data/liangtao/DataSets/PAR_Dataset/PETA/petazs_template.pkl'
    elif dataset=="MSP":
        root_path='/data/liangtao/DataSets/PAR_Dataset/MSP/images'
        pkl_path='/data/liangtao/DataSets/PAR_Dataset/MSP/msp_random_template.pkl'
    elif dataset=="MSPCD":
        root_path='/data/liangtao/DataSets/PAR_Dataset/MSP/images'
        pkl_path='/data/liangtao/DataSets/PAR_Dataset/MSP/msp_cd_template.pkl'
    return pkl_path, root_path
