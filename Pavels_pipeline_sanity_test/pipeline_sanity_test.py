#!/usr/bin/env python3
"""
Tests all possible algorithm combinations in the pipeline.
8 * 8 * 1 * 5 = 320 combinations tested.
"""

import sys
import os
import pipeline_generator
import subprocess as sb
import shutil


def sanity_test():
    pips, chain = pipeline_generator.generate_pips()
    test_json_path = os.path.join('assets', 'json', 'test.json')
    test_img_path = os.path.join('samples', 'test.jpg')
    nefi2_call = ' '.join(['python3', 'nefi2.py', '-p', test_json_path, '-f',
                           test_img_path])
    os.chdir(os.path.join(os.path.pardir, 'nefi2'))
    failed_chains = {}
    failed_chains_short = {}
    for it in range(len(pips)):
        with open(test_json_path, 'w') as fjson:
            fjson.write(pips[it])
            nefi2_run = sb.Popen(nefi2_call, shell=True, stdout=sb.PIPE,
                                 stderr=sb.PIPE,
                                 close_fds=True)
        stdout, stderr = nefi2_run.communicate()
        failed_chains[chain[it]] = stderr.decode('utf-8')
        failed_chains_short[chain[it]] = False if stderr else True
        stdou, stderr = '', ''
    os.remove(test_json_path)
    shutil.rmtree('output')
    os.mkdir('output')
    output = ['\n'.join([k, v]) for k, v in failed_chains.items()]
    output_short = [' '.join([str(v) + ',', k]) for k, v in failed_chains_short.items()]
    with open('pipeline_sanity.log', 'w') as flog:
        flog.write('\n'.join(output_short))
        flog.write('\n\n##### DETAILS #####\n\n')
        flog.write(''.join(output))


if __name__ == '__main__':
    sanity_test()
