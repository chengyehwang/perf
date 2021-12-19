#!/usr/bin/env python3
from perfetto.trace_processor import TraceProcessor

def slice():
        tp = TraceProcessor(file_path='trace.proto')

        qr_it = tp.query('SELECT name FROM slice')
        for row in qr_it:
            print(row.name)
slice()
