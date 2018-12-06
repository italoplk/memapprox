#!/bin/bash
sudo /usr/bin/gdb $*


sudo /home/italo/Documentos/pin-memapprox/pin -t /home/italo/Documentos/pin-memapprox/source/tools/ManualExamples/obj-intel64/memapprox.so -- /home/italo/Documentos/pin-memapprox/x265_2.5/build/linux/x265 --input-res 384x192 --wber-trans 1E-4 --rber-trans 0  --no-asm --no-wpp --no-pmode  --no-pme --lookahead-slices 0 --bframes  0 --b-adapt  0 --keyint -1 --tune psnr --psnr --frames 4 --fps 50 --qp 32  --log-level 4 --csv-log-level 2  --psnr --csv x265_BlowingBubbles_2560x1600_FPS-30_Fr-200_QP-32_TesteWER2_picYUV.csv --input /home/italo/Documentos/HM-16.5/origCfP/cropped/BlowingBubbles_384x192_50.yuv -o str.bin
