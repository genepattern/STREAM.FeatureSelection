docker run  -v ${PWD}:$PWD -w $PWD/job_1 genepattern/stream_featureselection python /stream/featureselection_command_line.py -m $PWD/test/data/foo_stream_result.pkl -lf 0.1 -per 95 -n_j 8 -of bar --flag_variable