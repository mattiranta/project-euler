
export X=1
echo -n "$X;" | tee -a data.csv; /cygdrive/c/Python32/python.exe 0${X}.py | tail -n1 | cut -c 7- | tee -a data.csv; export X=$((X+1));

python generate_graph.py && /cygdrive/c/Program\ Files\ \(x86\)/IrfanView/i_view32.exe plot.png