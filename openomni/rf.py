from rflib import *

def configure_rfcat(device, bitrate=40625):
	"""configure_rfcat is used to setup rfcat to decode omnipod signals"""
	device.setFreq(433.91e6)
	device.setMdmModulation(MOD_2FSK)
	device.setPktPQT(1)
	device.setMdmSyncMode(SYNCM_CARRIER_16_of_16)
	device.makePktFLEN(50)
	device.setEnableMdmManchester(True)
	device.setMdmDRate(bitrate)
	device.setRFRegister(0xdf18, 0x70)
	enable_preamble(device)

def disable_preamble(device):
	device.setMdmNumPreamble(MFMCFG1_NUM_PREAMBLE0)
	device.setMdmSyncWord(0xabab)

def enable_preamble(device):
	device.setMdmNumPreamble(MFMCFG1_NUM_PREAMBLE_8)
	device.setMdmSyncWord(0x54c3)
