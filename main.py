import os
from dipy.workflows.segment import recognize_bundles_flow
import json
import nibabel as nib
import numpy as np

if __name__ == '__main__':
    print('Begin Recobundles')    
    with open('config.json') as config_json:
        config = json.load(config_json)

    print(config['data_file'])   
    img = nib.load(config['data_file'])
    wtrk = config['moving_tck']
    etrk = config['static_tck']
    wtrk = str(wtrk)
    etrk = str(etrk)
    print('Loaded files')
    path = os.getcwd()
    w_file = nib.streamlines.load(wtrk)
    nib.streamlines.save(w_file.tractogram, path+'/mv.trk')


    print('Performing affine shifts')
    
    e_file = nib.streamlines.load(etrk)
    
    e_file.tractogram.apply_affine(np.linalg.inv(img.affine))    
    from dipy.tracking.streamline import transform_streamlines
    #streamlines = list(e_file.streamlines)
    streamlines = transform_streamlines(e_file.streamlines, np.linalg.inv(img.affine))
    #streamlines = list(streamlines) 
    tractogram = nib.streamlines.Tractogram(streamlines, affine_to_rasmm=img.affine)
    #tractogram.apply_affine(np.linalg.inv(img.affine))
    
    nib.streamlines.save(tractogram, path+'/st.trk')
    print('Converted tck to trk')
    print('Performed affine shifts')
    
    bundles_flow = path+'/bundles_flow/'
    if not os.path.exists(bundles_flow):
        os.makedirs(bundles_flow)

    recognize_bundles_flow(streamline_files= path+'/mv.trk', model_bundle_files=path+'/st.trk',slr = False, out_dir=bundles_flow,verbose=True)
    print('Ran Recobundles')
    mv_of_st = bundles_flow+'mv_of_st.trk'
    mvst = nib.streamlines.load(mv_of_st)
    nib.streamlines.save(mvst.tractogram, bundles_flow+'mv_of_st.tck')
    
    st_of_mv = bundles_flow+'st_of_mv.trk'
    stmv = nib.streamlines.load(st_of_mv)
    nib.streamlines.save(stmv.tractogram, bundles_flow+'st_of_mv.tck')

    print('Converted trk to tck')
    print('Finished')
