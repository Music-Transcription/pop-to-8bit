from rpca_mask import svs_RPCA

def svs(wave, fs=44100., v_centered=True):
    """
    Parameters
    ----------
    wave : ndarray
         Audio signal
    fs : float
         Sample rate.
    v_centered : bool
         If the vocal in the audio is centered.
    
    Returns
    -------
    voice : ndarray
            Separated voice.
    accom : ndarray
            Accompaniment part.
    """

    X = wave

    # make sure the shape matches our need
    if wave.shape[0] < wave.shape[1]:
        X = X.T
    # requires mono audio signal for RPCA
    if X.ndim > 1:
        rpca_wave = X[:, 1] + X[:, 0]

    voice, accom = svs_RPCA(rpca_wave, fs)

    if v_centered == True:
        accom = (X[:, 1] - X[:, 0]) / 2 

    return voice, accom

