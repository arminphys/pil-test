import os
import torch

def init_distributed_mode(args):
    if 'SLURM_PROCID' in os.environ:
        slurm_procid = os.environ['SLURM_PROCID']
        ntasks = int(os.environ['SLURM_NTASKS'])
        node_list = os.environ['SLURM_NODELIST']
        num_gpus = torch.cuda.device_count()

        print('Found', num_gpus, 'gpus')
        print('Found SLURM_PROCID', slurm_procid)
        print('Found SLURM_NTASKS', ntasks)
        print('Found SLURM_NODELIST', node_list)
        
        return
    
    if 'RANK' in os.environ and 'WORLD_SIZE' in os.eviron:
        print('Have been started with RANK and WORLD_SIZE')
        return

    print('No SLURM_PROCID, and no proper RANK and WORLD_SIZE')