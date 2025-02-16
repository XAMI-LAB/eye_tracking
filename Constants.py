
import matplotlib
import os

class Constants():

	# only change this path!
	# main path where the dataset is stored
	DATASET_PATH = os.path.join("/", "Volumes", "SD_DISK", "XAMI-MIMICv2.0", "")

	# mimic core path
	MIMIC_CORE_TABLES = ["patients", "admissions", "transfers"]
	MIMIC_CORE_PATH = lambda dataset_path, patient_id, table: os.path.join(dataset_path, "patient_" + str(patient_id), "Core",  table +".csv" )

	# mimic ed paths
	MIMIC_ED_TABLES = ["diagnosis", "edstays", "medrecon", "pyxis", "triage"]
	MIMIC_ED_PATH = lambda dataset_path, patient_id, table: os.path.join(dataset_path, "patient_" + str(patient_id), "ED",  table + ".csv" )

	# mimic cxr paths
	MIMIC_DICOM_PATH = lambda dataset_path, patient_id, study_id, dicom_id: os.path.join(dataset_path, "patient_" + str(patient_id), "CXR-DICOM", study_id, dicom_id + ".dcm")
	MIMIC_JPG_PATH   = lambda dataset_path, patient_id, study_id, dicom_id: os.path.join(dataset_path, "patient_" + str(patient_id), "CXR-JPG",   study_id, dicom_id + ".jpg")
	MIMIC_CXR_REPORT = lambda dataset_path, patient_id, study_id: os.path.join(dataset_path, "patient_" + str(patient_id), "CXR-DICOM", study_id + ".txt")

	# mimic cxr neg bio annotations
	MIMIC_NEG_BIO_PATH = lambda dataset_path, patient_id: os.path.join(dataset_path, "patient_" + str(patient_id), "CXR-JPG", "cxr_negbio.csv" )

	# mimic cxr chexpert annotations
	MIMIC_CHEXPERT_PATH = lambda dataset_path, patient_id: os.path.join(dataset_path, "patient_" + str(patient_id), "CXR-JPG", "cxr_chexpert.csv" )

	# mimic cxr metadata
	MIMIC_CHEXPERT_PATH = lambda dataset_path, patient_id: os.path.join(dataset_path, "patient_" + str(patient_id), "CXR-JPG", "cxr_meta.csv" )

	# eye gaze bounding boxes
	EYE_GAZE_BBOX_PATH = lambda dataset_path, patient_id : os.path.join(dataset_path, "patient_" + str(patient_id), "EyeGaze", "bounding_boxes.csv" )
	
	# main path where MIMIC-EYE's state will be saved
	CACHE_PATH = os.path.join(".", "cache", "mimic_eye_state.pkl")
	
	# main unit of MIMIC-EYE where the dataset will be stored in memory
	CACHE = {
						"REFLACX" : 0,							# counts how many patients are in REFLACX dataset
						"EYE_GAZE" : 0,							# counts how many patients are in EYE GAZE dataset
						"OVERLAP" : 0,							# counts how many patients overlap REFLACX and EYE GAZE
						"PATIENTS" : {},						# dictionary containing all information about a single patient
						"XRAY_TO_PATIENT" 	: {},		# dictionary mapping an XRayID to a PatientID
						"XRAY_TO_DIAGNOSIS" : {},		# dictionary mapping an XRayID to a Diagnosis (Eye Gaze only)
						"XRAY_TO_ABNORMALITY" : {},	# dictionary mapping an XRayID to an Abnormality
	}

	# for display purposes ----------------------------------------------
	FONT = { 'family': 'Ubuntu', 'size': 12}

	COLORS = { "butter": [ '#fce94f', '#edd400', '#c4a000'],
			"orange": [ '#fcaf3e', '#f57900', '#ce5c00'],
			"chocolate": [ '#e9b96e', '#c17d11', '#8f5902'],
			"chameleon": [ '#8ae234', '#73d216', '#4e9a06'],
			"skyblue": [ '#729fcf', '#3465a4', '#204a87'],
			"plum": [ '#ad7fa8', '#75507b', '#5c3566'],
			"scarletred":[ '#ef2929', '#cc0000', '#a40000'],
			"aluminium": [ '#eeeeec', '#d3d7cf', '#babdb6', '#888a85', '#555753', '#2e3436'],}