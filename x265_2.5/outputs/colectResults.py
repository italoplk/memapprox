#!/usr/bin/python
##!/data/apps/python/2.7.2/bin/python



import sys
import subprocess
import datetime
from collections import defaultdict
import os
from os import listdir
from subprocess import STDOUT
from multiprocessing.pool import ThreadPool
from itertools import izip_longest
from subprocess import Popen




QPs = ["22","27","32","37"]
HOME = os.environ["HOME"]
PIN_BASE = HOME + '/home/Documentos/pin-memapprox/'

#videos = ["Cactus_3840x2160_60fps","Coastguard_3840x2160_60fps", "Cactus_1920x1080_50", "BasketballDrive_1920x1080_50"]
#videos = ["Cactus_3840x2160_60fps"]
videos = ["Cactus_1920x1080_50"]
#taskset -c {8}



#mkdir = '''{0}_qp{3}_{1}_{2}'''

#cd = '''{0}_qp{3}_{1}_{2}/'''

cmd = ''' {0}pin \
-t {0:}/source/tools/ManualExamples/obj-intel64/memapprox.so   \
  -- {0:}/examples/x265_2.5/build/linux/x265 \
--input-res {1} \
--fps {2} \
--preset 5 \
-f 80 \
--qp {9} \
--input /data/videos/{4:}/{5}.yuv \
--frame-threads 1 --no-wpp --no-pmode  --no-pme --lookahead-slices 0 \
-o {0:}/examples/x265_2.5/outputs/{5}/videos/{5}_qp{9}_{6}_{7:}.265 \
--wber-me {6:} \
--rber-me {7:} \
--psnr  \
--csv-log-level 2 \
--csv {0:}/examples/x265_2.5/outputs/{5}/csv/{5}_qp{9}_{6}_{7:}.csv \
--tune psnr \
--tune ssim'''


BERS = ["0","1E-3", "1E-4","1E-5","1E-6"]
WBERS =["0"]
#tp = ThreadPool(20)







for video in videos:
	
	arquivoEscrita = open("./Pin_readings_Intra/"+str(video) + ".csv", "w")
	if len(WBERS) == 1:	
		for qp in QPs:

			arquivoEscrita.write("QP "+ str(qp) + "\n")
			#arquivoEscrita.write("\n\n,Original,Original,WBER 1E-3, WBER 1E-3, WBER 1E-4, WBER 1E-4, WBER 1E-5, WBER 1E-5, WBER 1E-6, WBER 1E-6, WBER 1E-7, WBER 1E-7\n" )
			for wber in WBERS:
	

				for rber in BERS:
					arquivoLeitura = open("./"+str(video)+ "/csv/"+str(video)+ "_qp"+str(qp)+ "_"+str(wber) + "_" + str(rber) + ".csv", "r")
					for line in arquivoLeitura:
						split = line.split(",")
						if split[0] == "Command":
							linha = arquivoLeitura.next()
							split = linha.split(",")
							bitrate = split[4]								
							psnr = split[5]
							arquivoEscrita.write("RBER " + str(wber) + "," + str(bitrate) + "," + str(psnr) + "\n")
			arquivoEscrita.write("\n\n")
	
	elif len(BERS) == 1:
		#arquivoEscrita.write("\n\n,Original,Original,WBER 1E-3, WBER 1E-3, WBER 1E-4, WBER 1E-4, WBER 1E-5, WBER 1E-5, WBER 1E-6, WBER 1E-6, WBER 1E-7, WBER 1E-7\n" )
		for qp in QPs:

			arquivoEscrita.write("QP "+ str(qp) + "\n")
			#arquivoEscrita.write("\n\n,Original,Original,WBER 1E-3, WBER 1E-3, WBER 1E-4, WBER 1E-4, WBER 1E-5, WBER 1E-5, WBER 1E-6, WBER 1E-6, WBER 1E-7, WBER 1E-7\n" )
			for wber in WBERS:
	

				for rber in BERS:
					arquivoLeitura = open("./"+str(video)+ "/csv/"+str(video)+ "_qp"+str(qp)+ "_"+str(wber) + "_" + str(rber) + ".csv", "r")
					for line in arquivoLeitura:
						split = line.split(",")
						if split[0] == "Command":
							linha = arquivoLeitura.next()
							split = linha.split(",")
							bitrate = split[4]								
							psnr = split[5]
							arquivoEscrita.write("WBER " + str(wber) + "," + str(bitrate) + "," + str(psnr) + "\n")
			arquivoEscrita.write("\n\n")
	

















