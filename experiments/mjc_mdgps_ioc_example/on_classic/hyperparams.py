""" Hyperparameters for MJC peg insertion policy optimization. """
import imp
import os.path
from gps.gui.config import generate_experiment_info

BASE_DIR = '/'.join(str.split(__file__, '/')[:-2])
default = imp.load_source('default_hyperparams', BASE_DIR+'/hyperparams.py')

EXP_DIR = '/'.join(str.split(__file__, '/')[:-1]) + '/'

# Update the defaults
common = default.common.copy()
common.update({
    'experiment_dir': EXP_DIR,
    'data_files_dir': EXP_DIR + 'data_files/',
    'target_filename': EXP_DIR + 'target.npz',
    'log_filename': EXP_DIR + 'log.txt',
})

if not os.path.exists(common['data_files_dir']):
    os.makedirs(common['data_files_dir'])

# Algorithm
algorithm = default.algorithm.copy()
algorithm.update({
    'sample_on_policy': True,
    'step_rule': 'classic',
})

algorithm['cost'].update({
	'experiment_dir': common['experiment_dir']
})

algorithm['policy_opt'].update({
    'weights_file_prefix': common['data_files_dir'] + 'policy',
})

config = default.config.copy()
config.update({
    'common': common,
    'algorithm': algorithm,
})

common['info'] = generate_experiment_info(config)
