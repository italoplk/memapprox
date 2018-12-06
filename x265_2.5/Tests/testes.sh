#../../pin -t ../../source/tools/ManualExamples/obj-intel64/memapprox.so -- 


#./build/linux/x265 --input-res 384x192 --wber-me 0 --rber-me 0  --no-asm  --frame-threads 1 --no-wpp --no-pmode  --no-pme --lookahead-slices 0 --bframes  0 --b-adapt  0 --keyint -1 --tune psnr --psnr --frames 10 --fps 50 --qp 32 --ctu 64 --min-cu-size  8  --max-merge  5 --rc-lookahead  60 --rd  6 --rdoq-level  2 --tu-intra  4 --tu-inter  4 --scenecut  40 --ref  5 --limit-refs  0 --merange  92 --subme  5 --me  star  --rect  --amp  --no-limit-modes  --no-early-skip  --no-fast-intra  --b-intra  --sao  --signhide  --weightp  --weightb --aq-mode  1 --log-level 4 --csv-log-level 2  --psnr --csv x265_BlowingBubbles_2560x1600_FPS-30_Fr-10_QP-32_teste_0.csv --input /home/italo/Documentos/HM-16.5/origCfP/cropped/BlowingBubbles_384x192_50.yuv -o str.bin >> x265_BlowingBubbles_2560x1600_FPS-30_Fr-10_QP-32_teste_0.txt


./../pin -t ../source/tools/ManualExamples/obj-intel64/memapprox.so -- ./build/linux/x265 --input-res 384x192 --wber-me 1E-1 --rber-me 0  --no-asm --no-wpp --no-pmode  --no-pme --lookahead-slices 0 --bframes  0 --b-adapt  0 --keyint -1 --tune psnr --psnr --frames 4 --fps 50 --qp 32 --ctu 64 --min-cu-size  8  --max-merge  5 --rc-lookahead  60 --rd  6 --rdoq-level  2 --tu-intra  4 --tu-inter  4 --scenecut  40 --ref  5 --limit-refs  0 --merange  92 --subme  5 --me  star  --rect  --amp  --no-limit-modes  --no-early-skip  --no-fast-intra  --b-intra  --sao  --signhide  --weightp  --weightb --aq-mode  1 --log-level 4 --csv-log-level 2  --psnr --csv x265_BlowingBubbles_2560x1600_FPS-30_Fr-200_QP-32_TesteWER2_picYUV.csv --input /home/italo/Documentos/HM-16.5/origCfP/cropped/BlowingBubbles_384x192_50.yuv -o str.bin >> x265_BlowingBubbles_2560x1600_FPS-30_Fr-200_QP-32_TesteWER2_picYUV.txt



./../pin-memapprox/pin -t ./../source/tools/ManualExamples/obj-intel64/memapprox.so     -- ./build/linux/x265 -input-res 384x192 --fps 50 --preset 5 -f 4 --qp 37 --input /home/italo/Documentos/HM-16.5/origCfP/cropped/BlowingBubbles_384x192_50.yuv --no-wpp --no-pmode  --no-pme --lookahead-slices 0 -o ./Cactus_1920x1080_50/videos/Cactus_1920x1080_50_qp37_1E-6_0.265 --wber-me 1E-6 --rber-me 0 --psnr  --csv-log-level 2 --csv ./Cactus_1920x1080_50/csv/Cactus_1920x1080_50_qp37_1E-6_0.csv --tune psnr --tune ssim
#> x265_BlowingBubbles_2560x1600_FPS-30_Fr-200_QP-32_teste_BuffTransformadas.txt


taskset -c 11 ./../pin-memapprox/pin -t ./../source/tools/ManualExamples/obj-intel64/memapprox.so     -- ./build/linux/x265 --input-res 1920x1080 --fps 50 --preset 5 -f 8 --qp 37 --input /home/italo/Documentos/HM-16.5/origCfP/cropped/Cactus_1920x1080_50.yuv --no-wpp --no-pmode  --no-pme --lookahead-slices 0 -o ./Cactus_1920x1080_50_qp37_0_0.265 --wber-trans 0 --rber-trans 0 --psnr  --csv-log-level 2 --csv ./Cactus_1920x1080_50_qp37_0_0.csv --tune psnr --tune ssim
