module main (
	output [31:0] out_data,
	input CLK,
    input RST,
    input SW,
    input CAN_logic,
    output reg [6:0] HEX5,
    output reg [6:0] HEX4,
    output reg [6:0] HEX3,
    output reg [6:0] HEX2,
    output reg [6:0] HEX1,
    output reg [6:0] HEX0,
    output can_sample_clk,

    input SCK,
    input SSEL,
    input MOSI,
    output MISO,

    output LEDR0,
    output LEDR1
);
reg [31:0] in_data;
wire WR;
wire RD;
reg FULL;
reg EMPTY;

spi spi(.CLK(CLK), .SCK(SCK), .SSEL(SSEL), .MOSI(MOSI), .MISO(MISO), .out_data(out_data), .read_request(RD), .read_error(EMPTY));
fifo fifo(.CLK(CLK), .nRST(RST), .D(in_data), .Q(out_data), .WR(WR), .RD(RD), .FULL(FULL), .EMPTY(EMPTY));
measure_time measure_time(.out_data(in_data), .CLK(CLK), .SW(SW), .CAN_logic(CAN_logic), .HEX5(HEX5), .HEX4(HEX4), .HEX3(HEX3), .HEX2(HEX2), .HEX1(HEX1), .HEX0(HEX0), .can_sample_clk(can_sample_clk), .write_request(WR));

assign LEDR0 = FULL;
assign LEDR1 = EMPTY;

endmodule
