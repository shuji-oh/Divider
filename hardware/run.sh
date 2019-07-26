#!/bin/sh

EXE=main

iverilog -o $EXE clk_based_tdc.v out_hex.v testbench.v

if [ $? -eq 0 ]; then
  vvp $EXE
fi
