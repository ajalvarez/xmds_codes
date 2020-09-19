echo Iniciando Simulacion ...
rm lorenz.cc
rm lorenz.h5
rm lorenz.xsil
xmmd2 lorenz.xmmd
./lorenz
python plotify.py&
