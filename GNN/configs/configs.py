# regression datasets

ESOL = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/benchmark/ESOL',
    'raw_name': 'ESOL.csv',
    'atom_types' : 100,
    'bond_type_num' : 4,
    'target_idxs': [1],
    'base_lr': 3e-4,
    'factor': 0.95,
    'patience': 10,
    'batch': 32,
    'num_passing': 3,
    'num_passing_before': 3,
    'num_passing_pool':1,
    'num_passing_after':1,
    'num_passing_mol':1
}

FreeSolv = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/benchmark/FreeSolv',
    'raw_name': 'FreeSolv.csv',
    'atom_types' : 100,
    'bond_type_num' : 4,
    'target_idxs': [1],
    'base_lr': 1e-3,
    'factor': 0.90,
    'patience': 5,
    'batch': 64,
    'num_passing': 3,
    'num_passing_before': 3,
    'num_passing_pool':1,
    'num_passing_after':1,
    'num_passing_mol':2
}

Lipo = {
        'root': '/home/kongyue/private-kongyue/paper-RGNN/data/benchmark/Lipo',
        'raw_name': 'Lipophilicity.csv',
        'atom_types' : 100,
        'bond_type_num' : 4,
        'target_idxs' : [1],
        'base_lr': 1e-3,
        'factor': 0.95,
        'patience': 10,
        'batch': 32,
        'num_passing': 3,
        'num_passing_before': 3,
        'num_passing_pool':1,
        'num_passing_after':1,
        'num_passing_mol': 1
}




# classification datasets

MUV = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/benchmark/MUV',
    'raw_name': 'muv.csv',
    'atom_types' : 100,
    'bond_type_num' : 4,
    'target_idxs': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],
    'num_classes': 17,
    'pos_weight': 60,
    'base_lr': 1e-3,
    'factor': 0.95,
    'patience': 5,
    'batch': 512,
    'num_passing': 3,
    'num_passing_before': 3,
    'num_passing_pool':1,
    'num_passing_after':1,
    'num_passing_mol':2
}

HIV = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/benchmark/HIV',
    'raw_name': 'HIV.csv',
    'atom_types' : 100,
    'bond_type_num' : 4,
    'target_idxs' : [1],
    'num_classes': 1,
    'pos_weight': 10,
    'base_lr': 1e-3,
    'factor': 0.95,
    'patience': 10,
    'batch': 128,
    'num_passing': 3,
    'num_passing_before': 3,
    'num_passing_pool':1,
    'num_passing_after':1,
    'num_passing_mol':1
}

BACE = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/benchmark/bace',
    'raw_name': 'bace.csv',
    'atom_types' : ['C','H','O','N','Cl','S','F','Br','P','I','Sn',
                    'As','Ti','Cu','Hg','Sb','Ca','Pb','Bi', 
                    'Se','Ni','Au','Te'],
    'bond_type_num' : 4,
    'target_idxs': [1],
    'num_classes': 1,
    'pos_weight': 1.2,
    'base_lr': 1e-3,
    'factor': 0.95,
    'patience': 10,
    'batch': 8,
    'num_passing': 3,
    'num_passing_before': 3,
    'num_passing_pool':1,
    'num_passing_after':1,
    'num_passing_mol':1
}

BBBP = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/benchmark/BBBP',
    'raw_name': 'BBBP.csv',
    'atom_types' : ['C','H','O','N','Cl','S','F','Br','P','I','Sn',
                    'As','Ti','Cu','Hg','Sb','Ca','Pb','Bi', 
                    'Se','Ni','Au','Te','B'],
    'bond_type_num' : 4,
    'target_idxs': [1],
    'num_classes': 1,
    'pos_weight': 0.8,
    'base_lr': 1e-3,
    'factor': 0.95,
    'patience': 10,
    'batch': 32,
    'num_passing': 3,
    'num_passing_before': 3,
    'num_passing_pool':1,
    'num_passing_after':1,
    'num_passing_mol':1
}

Tox21 = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/benchmark/Tox21',
    'raw_name': 'tox21.csv',
    'atom_types' : 100,
    'bond_type_num' : 4,
    'target_idxs': [1,2,3,4,5,6,7,8,9,10,11,12],
    'num_classes': 12,
    'pos_weight': 5,
    'base_lr': 1e-3,
    'factor': 0.95,
    'patience': 5,
    'batch': 64,
    'num_passing': 3,
    'num_passing_before': 3,
    'num_passing_pool':1,
    'num_passing_after':1,
    'num_passing_mol':1
}

ToxCast = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/benchmark/ToxCast',
    'raw_name': 'toxcast.csv',
    'atom_types' : 100,
    'bond_type_num' : 4,
    'target_idxs': list(range(1,618)),
    'num_classes': 617,
    'pos_weight': 10,
    'base_lr': 1e-3,
    'factor': 0.95,
    'patience': 5,
    'batch': 32,
    'num_passing': 3,
    'num_passing_before': 3,
    'num_passing_pool':1,
    'num_passing_after':1,
    'num_passing_mol':1
}

SIDER = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/benchmark/SIDER',
    'raw_name': 'sider.csv',
    'atom_types' : 100,
    'bond_type_num' : 4,
    'target_idxs':  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],
    'num_classes': 27,
    'pos_weight': 0.7,
    'base_lr': 1e-3,
    'factor': 0.95,
    'patience': 5,
    'batch': 32,
    'num_passing': 3,
    'num_passing_before': 3,
    'num_passing_pool':2,
    'num_passing_after':1,
    'num_passing_mol':1
}



ClinTox = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/benchmark/ClinTox',
    'raw_name': 'clintox.csv',
    'atom_types' : 100,
    'bond_type_num' : 4,
    'target_idxs': [1,2],
    'num_classes': 2,
    'pos_weight': 0.8,
    'base_lr': 1e-3,
    'factor': 0.95,
    'patience': 10,
    'batch': 32,
    'num_passing': 3,
    'num_passing_before': 3,
    'num_passing_pool':2,
    'num_passing_after':1,
    'num_passing_mol':1
}




############## Kinase数据集 ##########
## classification dataset
AKT1 = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/kinase/AKT1',
    'raw_name': 'AKT1.csv',
    'atom_types' : 100,
    'bond_type_num' : 4,
    'target_idxs': [1],
    'num_classes': 1,
    'pos_weight': 1,
    'base_lr': 1e-3,
    'factor': 0.95,
    'patience': 10,
    'batch': 32,
    'num_passing': 3,
    'num_passing_before': 3,
    'num_passing_pool':2,
    'num_passing_after':1,
    'num_passing_mol':1
}

AURKA = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/kinase/AURKA',
    'raw_name': 'AURKA.csv',
    'atom_types' : 100,
    'bond_type_num' : 4,
    'target_idxs': [1],
    'num_classes': 1,
    'pos_weight': 1,
    'base_lr': 1e-3,
    'factor': 0.95,
    'patience': 10,
    'batch': 32,
    'num_passing': 3,
    'num_passing_before': 2,
    'num_passing_pool':2,
    'num_passing_after':1,
    'num_passing_mol':3
}

BRAF = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/kinase/BRAF',
    'raw_name': 'BRAF.csv',
    'atom_types' : 100,
    'bond_type_num' : 4,
    'target_idxs': [1],
    'num_classes': 1,
    'pos_weight': 0.8,
    'base_lr': 1e-3,
    'factor': 0.95,
    'patience': 10,
    'batch': 32,
    'num_passing': 3,
    'num_passing_before': 3,
    'num_passing_pool':2,
    'num_passing_after':1,
    'num_passing_mol':1
}

BTK = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/kinase/BTK',
    'raw_name': 'BTK.csv',
    'atom_types' : 100,
    'bond_type_num' : 4,
    'target_idxs': [1],
    'num_classes': 1,
    'pos_weight': 1,
    'base_lr': 1e-3,
    'factor': 0.95,
    'patience': 10,
    'batch': 32,
    'num_passing': 3,
    'num_passing_before': 2,
    'num_passing_pool':2,
    'num_passing_after':1,
    'num_passing_mol':3
}

CDK2 = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/kinase/CDK2',
    'raw_name': 'CDK2.csv',
    'atom_types' : 100,
    'bond_type_num' : 4,
    'target_idxs': [1],
    'num_classes': 1,
    'pos_weight': 1,
    'base_lr': 1e-3,
    'factor': 0.95,
    'patience': 10,
    'batch': 32,
    'num_passing': 3,
    'num_passing_before': 2,
    'num_passing_pool':2,
    'num_passing_after':1,
    'num_passing_mol':1
}

CK1 = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/kinase/CK1',
    'raw_name': 'CK1.csv',
    'atom_types' : 100,
    'bond_type_num' : 4,
    'target_idxs': [1],
    'num_classes': 1,
    'pos_weight': 1,
    'base_lr': 1e-3,
    'factor': 0.95,
    'patience': 10,
    'batch': 32,
    'num_passing': 3,
    'num_passing_before': 3,
    'num_passing_pool':1,
    'num_passing_after':1,
    'num_passing_mol':2
}

EGFR = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/kinase/EGFR',
    'raw_name': 'EGFR.csv',
    'atom_types' : 100,
    'bond_type_num' : 4,
    'target_idxs': [1],
    'num_classes': 1,
    'pos_weight': 1,
    'base_lr': 1e-3,
    'factor': 0.95,
    'patience': 10,
    'batch': 32,
    'num_passing': 3,
    'num_passing_before': 3,
    'num_passing_pool':2,
    'num_passing_after':1,
    'num_passing_mol':1
}

MAP4K2 = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/kinase/MAP4K2',
    'raw_name': 'MAP4K2.csv',
    'atom_types' : 100,
    'bond_type_num' : 4,
    'target_idxs': [1],
    'num_classes': 1,
    'pos_weight': 1.5,
    'base_lr': 1e-3,
    'factor': 0.95,
    'patience': 10,
    'batch': 32,
    'num_passing': 3,
    'num_passing_before': 3,
    'num_passing_pool':1,
    'num_passing_after':1,
    'num_passing_mol':2
}

mTOR = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/kinase/mTOR',
    'raw_name': 'mTOR.csv',
    'atom_types' : 100,
    'bond_type_num' : 4,
    'target_idxs': [1],
    'num_classes': 1,
    'pos_weight': 0.3,
    'base_lr': 1e-3,
    'factor': 0.95,
    'patience': 10,
    'batch': 32,
    'num_passing': 3,
    'num_passing_before': 3,
    'num_passing_pool':2,
    'num_passing_after':1,
    'num_passing_mol':1
}

PIM1 = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/kinase/PIM1',
    'raw_name': 'PIM1.csv',
    'atom_types' : 100,
    'bond_type_num' : 4,
    'target_idxs': [1],
    'num_classes': 1,
    'pos_weight': 0.8,
    'base_lr': 1e-3,
    'factor': 0.95,
    'patience': 10,
    'batch': 32,
    'num_passing': 3,
    'num_passing_before': 2,
    'num_passing_pool':1,
    'num_passing_after':1,
    'num_passing_mol':3
}


############## 其他数据集 ##########
## classification dataset
Muta_train = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/muta',
    'raw_name': '1_mutagenic_train_7647.csv',
    'atom_types' : ['C','H','O','N','Cl','S','F','Br','P','I','Sn',
                    'As','Ti','Cu','Hg','Sb','Ca','Pb','Bi', 
                    'Se','Ni','Au','Te'],
    'num_classes': 1,
    'bond_type_num' : 4,
    'pos_weight': 1,
    'target_idxs' : 1,
    'base_lr': 1e-3,
    'factor': 0.95,
    'patience': 10,
    'batch': 32,
    'num_passing': 3,
    'num_passing_before': 3,
    'num_passing_pool':1,
    'num_passing_after':1,
    'num_passing_mol':1
}

Muta_test = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/muta',
    'raw_name': '1_mutagenic_test_203.csv',
    'atom_types' : ['C','H','O','N','Cl','S','F','Br','P','I','Sn',
                    'As','Ti','Cu','Hg','Sb','Ca','Pb','Bi', 
                    'Se','Ni','Au','Te'],
    'num_classes': 1,
    'bond_type_num' : 4 ,
    'pos_weight': 1,
    'target_idxs' : 1,
    'base_lr': 1e-3,
    'factor': 0.95,
    'patience': 10,
    'batch': 32,
    'num_passing': 3,
    'num_passing_before': 3,
    'num_passing_pool':1,
    'num_passing_after':1,
    'num_passing_mol':1
}

Carcino = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/carcino',
    'raw_name': '1_carcinogenicity_smi_1216.csv',
    'atom_types' : ['C','H','O','N','Cl','S','F','Br','P','I','Sn',
                    'As','Ti','Cu','Hg','Sb','Ca','Pb','Bi', 
                    'Se','Ni','Au','Te'],
    'bond_type_num' : 4,
    'target_idxs' : 1,
    'num_classes': 1,
    'pos_weight': 0.8,
    'base_lr': 1e-3,
    'factor': 0.95,
    'patience': 10,
    'batch': 50,
    'num_passing': 3,
    'num_passing_before': 3,
    'num_passing_pool':1,
    'num_passing_after':1,
    'num_passing_mol':1
}

AMES = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/AMES',
    'raw_name': 'ames_6621.csv',
    'atom_types' : ['C','H','O','N','Cl','S','F','Br','P','I','Sn',
                    'As','Ti','Cu','Hg','Sb','Ca','Pb','Bi', 
                    'Se','Ni','Au','Te'],
    'bond_type_num' : 4,
    'target_idxs' : 1,
    'num_classes': 1,
    'pos_weight': 1,
    'target_idxs' : 1,
    'base_lr': 1e-3,
    'factor': 0.95,
    'patience': 10,
    'batch': 64,
    'num_passing': 3,
    'num_passing_before': 3,
    'num_passing_pool':1,
    'num_passing_after':1,
    'num_passing_mol':1
}

BioDeg = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/BioDeg',
    'raw_name': 'biodeg_1836.csv',
    'atom_types' : ['C','H','O','N','Cl','S','F','Br','P','I','Sn',
                    'As','Ti','Cu','Hg','Sb','Ca','Pb','Bi', 
                    'Se','Ni','Au','Te'],
    'bond_type_num' : 4,
    'target_idxs' : 1,
    'num_classes': 1,
    'pos_weight': 1,
    'target_idxs' : 1,
    'base_lr': 1e-3,
    'factor': 0.95,
    'patience': 10,
    'batch': 32,
    'num_passing': 3,
    'num_passing_before': 2,
    'num_passing_pool':1,
    'num_passing_after':1,
    'num_passing_mol':1
}



AURKA_explain = { 'root': '/home/kongyue/private-kongyue/paper-RGNN/data/vis/AURKA',
    'raw_name': 'AURKA.csv',
    'atom_types' : 100,
    'bond_type_num' : 4,
    'target_idxs': [1],
    'num_classes': 1,
    'pos_weight': 1,
    'base_lr': 1e-3,
    'factor': 0.95,
    'patience': 10,
    'batch': 1,
    'num_passing': 3,
    'num_passing_before': 2,
    'num_passing_pool':1,
    'num_passing_after':1,
    'num_passing_mol':1
}

