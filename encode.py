#! /usr/bin/env python
import sys
import dftext
args = dftext.ArgParser().parse_args()
sys.stdout.write(dftext.Parser().encode(args.filename, index=args.index))