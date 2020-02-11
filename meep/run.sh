conda activate pmp

if [ $1 = run_diff_dist ]; then
    python main.py 0.0 meep_out/cube_dis_0.0.bin &
    python main.py 0.1 meep_out/cube_dis_0.1.bin &
    python main.py 0.2 meep_out/cube_dis_0.2.bin &
    python main.py 0.3 meep_out/cube_dis_0.3.bin &
    python main.py 0.4 meep_out/cube_dis_0.4.bin &
    python main.py 0.5 meep_out/cube_dis_0.5.bin &
    python main.py 0.6 meep_out/cube_dis_0.6.bin &
    python main.py 0.7 meep_out/cube_dis_0.7.bin &
    python main.py 0.8 meep_out/cube_dis_0.8.bin &
    python main.py 0.9 meep_out/cube_dis_0.9.bin &
    python main.py 1.0 meep_out/cube_dis_1.0.bin &
else
    python main.py 0.5 meep_out/cube_dis_0.5_absorb.bin &
fi
wait
