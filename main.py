import os
from dipy.workflows.align import whole_brain_slr_flow
from dipy.workflows.segment import recognize_bundles_flow
import json
import nibabel as nib


if __name__ == '__main__':

    with open('config.json') as config_json:
        config = json.load(config_json)

    wtrk = config['moving_tck']
    etrk = config['static_tck']
    wtrk = str(wtrk)
    etrk = str(etrk)

    path = os.getcwd()
    w_file = nib.streamlines.load(wtrk)
    nib.streamlines.save(w_file.tractogram, path+'/mv.trk')

    e_file = nib.streamlines.load(etrk)
    nib.streamlines.save(e_file.tractogram, path+'/st.trk')

    bundles_flow = path+'/bundles_flow/'
    if not os.path.exists(bundles_flow):
        os.makedirs(bundles_flow)

<<<<<<< HEAD
    recognize_bundles_flow(streamline_files=path+'/st.trk', model_bundle_files=path+'/mv.trk',out_dir=bundles_flow,verbose=True)
=======
    recognize_bundles_flow(streamline_files= path+'/st.trk', model_bundle_files=path+'/mv.trk',out_dir=bundles_flow,verbose=True)
>>>>>>> fc428fc93c8c24c3763a1e2277f9f701ebf9cf86
    #horizon_flow(input_files=bundles_flow)s
