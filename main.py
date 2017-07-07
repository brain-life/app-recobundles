import os
from dipy.workflows.align import whole_brain_slr_flow
from dipy.workflows.segment import recognize_bundles_flow
#from dipy.workflows.viz import horizon_flow
import json


if __name__ == '__main__':

    with open('config.json') as config_json:
        config = json.load(config_json)

    wtrk = config['moving_trk']
    etrk = config['static_trk']
    path = os.getcwd()
    bundles_flow = path+'/bundles_flow/'
    if not os.path.exists(bundles_flow):
        os.makedirs(bundles_flow)
    slr_flow = path+'/slr_flow/'
    if not os.path.exists(slr_flow):
        os.makedirs(slr_flow)
    whole_brain_slr_flow(moving_streamlines_files=wtrk, static_streamlines_file=etrk, out_dir=slr_flow, verbose=True)
    recognize_bundles_flow(streamline_files=etrk, model_bundle_files=wtrk,out_dir=bundles_flow,verbose=True)
    #horizon_flow(input_files=bundles_flow)s
