#!/usr/bin/python
##!/data/apps/python/2.7.2/bin/python



import sys
import subprocess
import datetime
from collections import defaultdict
import os
from subprocess import STDOUT
from multiprocessing.pool import ThreadPool
from itertools import izip_longest
from subprocess import Popen


NUMBER_OF_CORES = 4;

QPs = ["22","27","32","37"]
#QPs = ["22"]

HOME = os.environ["HOME"]
PIN_BASE = HOME + '/intra-pin-memapprox'
videos = [["Cactus_1920x1080_50", "1080p", "50","1920x1080"]]
#videos = [ ["Cactus_1920x1080_50", "1080p", "50","1920x1080"], ["BasketballDrive_1920x1080_50", "1080p", "50","1920x1080"], ["Cactus_3840x2160_60fps", "4k", "60","3840x2160"], ["Coastguard_3840x2160_60fps", "4k", "60", "3840x2160"]]
#videos = [["Cactus_1920x1080_50", "1080p", "50","1920x1080"], ["BasketballDrive_1920x1080_50", "1080p", "50","1920x1080"],["Cactus_3840x2160_60fps", "4k", "60","3840x2160"], ["Coastguard_3840x2160_60fps", "4k", "60", "3840x2160"]]

#taskset -c {8}
#nucleos = [ "8", "10", "12","14","16","18","20","22", "9","11","13","15","17","19", "21"]
nucleos = range(0,NUMBER_OF_CORES)
# 25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]



mkdir = '''mkdir {0}_qp{3}_{1}_{2}'''

cd = '''{0}_qp{3}_{1}_{2}'''

cmd = '''taskset -c {10} {0}/pin \
-t {0:}/source/tools/ManualExamples/obj-intel64/memapprox.so   \
-- {0:}/x265_2.5/build/linux/x265 \
--input-res {1} \
--fps {2} \
--preset 5 \
--bframes 0 \
--b-adapt 0 \
--keyint -1 \
-f 80 \
--qp {9} \
--input ./{5}.yuv \
--no-wpp --no-pmode  --no-pme --lookahead-slices 0 --pool "-" \
-o {0:}/x265_2.5/outputs/{5}/videos/{5}_qp{9}_{6}_{7:}.265 \
--wber-intra {6:} \
--rber-intra {7:} \
--psnr  \
--csv-log-level 2 \
--csv {0:}/x265_2.5/outputs/{5}/csv/{5}_qp{9}_{6}_{7:}.csv \
--tune psnr \
--tune ssim'''

BERS = [ "0" ]
#BERS = [ "1E-7", "1E-6", "1E-5", "1E-4", "1E-3"]
#WERS = [ "1E-7", "1E-6", "1E-5", "1E-4", "1E-3", "1E-32", "0" ]
WERS = ["1E-7", "1E-6", "1E-5", "1E-4", "1E-3", "0" ]
#WERS = ["0"]
#BERS = ["1E-31", "1E-32", "1E-34", "1E-36", "1E-38"]


#tp = ThreadPool(20)





#def work(command):
#	print "\ncommand 2 = " + str(command) + "\n"
#	subprocess.Popen(command, stderr=STDOUT, stdout="saida.txt", shell=True)
	
 



def run_pin_experiments():
	os.chdir("outputs/") #mudar diretorio para memapprox.log
	CMDd = []
	CD =[]
	countProcess =0
	for video in videos:
		subprocess.call("mkdir " + str(video[0]), shell=True)
		os.chdir(str(video[0]))
		subprocess.call("mkdir logs", shell=True)
		subprocess.call("mkdir csv", shell=True)
		subprocess.call("mkdir videos" , shell=True)
		for qp in QPs:
			for ber in BERS:
			    for wer in WERS:
			   
                                        #cria os arquivos para a saida da tela
				    simout = '{0}/x265_2.5/outputs/{1}/logs/{1}_qp{4}_{2}_{3}.log'.format(PIN_BASE, video[0], wer, ber, qp)
				    simout_f = open(simout, "w")
					#cria os comandos de chamada
				    aux = [cmd.format(PIN_BASE, video[3], video[2], HOME, video[1], video[0], wer, ber, countProcess, qp, str(nucleos[countProcess])), cd.format(video[0], wer, ber, qp), simout_f]
				    CMDd.append(aux)

					#cria os diretorios dos memoapprox.log
    				    MK = mkdir.format(video[0], wer, ber, qp)
				    subprocess.call(MK, shell=True)
    				    countProcess +=1
					#limita o numero de processos pra nao dar overload no servidor.
				    if len(CMDd) >= NUMBER_OF_CORES:
					call_cmd(CMDd)
					CMDd = []
					countProcess = 0
		os.chdir("../")

	call_cmd(CMDd)
	CMDd = []
	countProcess = 0
				
	

def call_cmd( CMDd ):

	for command in CMDd:
		print "\n\n comand = " + str(command)

	#instacia as threads  |call     |folder                        |outs
	groups = [(Popen(commands[0], cwd= "./",  stdout=commands[2], stderr=commands[2], shell=True) 
			for commands in CMDd)] * NUMBER_OF_CORES
	

	for processes in izip_longest(*groups): 
  		for p in filter(None, processes):
       			p.wait()


if __name__ == "__main__":
 
  run_pin_experiments()

 #os.system('echo Simulacoes Intra Terminadas. | mail -s Simulacao_Gaci_G3 idmachado@inf.ufpel.edu.br')
