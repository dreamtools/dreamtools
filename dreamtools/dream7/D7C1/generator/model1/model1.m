%  How to use:
%
%  _model_9_genes_tic takes 3 inputs and returns 3 outputs.
%
%  [t x rInfo] = _model_9_genes_tic(tspan,solver,options)
%  INPUTS: 
%  tspan - the time vector for the simulation. It can contain every time point, 
%  or just the start and end (e.g. [0 1 2 3] or [0 100]).
%  solver - the function handle for the odeN solver you wish to use (e.g. @ode23s).
%  options - this is the options structure returned from the MATLAB odeset
%  function used for setting tolerances and other parameters for the solver.
%  
%  OUTPUTS: 
%  t - the time vector that corresponds with the solution. If tspan only contains
%  the start and end times, t will contain points spaced out by the solver.
%  x - the simulation results.
%  rInfo - a structure containing information about the model. The fields
%  within rInfo are: 
%     stoich - the stoichiometry matrix of the model 
%     floatingSpecies - a cell array containing floating species name, initial
%     value, and indicator of the units being inconcentration or amount
%     compartments - a cell array containing compartment names and volumes
%     params - a cell array containing parameter names and values
%     boundarySpecies - a cell array containing boundary species name, initial
%     value, and indicator of the units being inconcentration or amount
%     rateRules - a cell array containing the names of variables used in a rate rule
%
%  Sample function call:
%     options = odeset('RelTol',1e-12,'AbsTol',1e-9);
%     [t x rInfo] = _model_9_genes_tic(linspace(0,100,100),@ode23s,options);
%
function [t x rInfo] = _model_9_genes_tic(tspan,solver,options)
    % initial conditions
    [x rInfo] = model();

    % initial assignments

    % assignment rules

    % run simulation
    [t x] = feval(solver,@model,tspan,x,options);

    % assignment rules

function [xdot rInfo] = model(time,x)
%  x(1)        g6
%  x(2)        p1
%  x(3)        p2
%  x(4)        p3
%  x(5)        p4
%  x(6)        p5
%  x(7)        p6
%  x(8)        p7
%  x(9)        p8
%  x(10)        p9
%  x(11)        pro1
%  x(12)        pro2
%  x(13)        pro3
%  x(14)        pro4
%  x(15)        pro5
%  x(16)        pro6
%  x(17)        pro7
%  x(18)        pro8
%  x(19)        pro9
%  x(20)        rbs1
%  x(21)        rbs2
%  x(22)        rbs3
%  x(23)        rbs4
%  x(24)        rbs5
%  x(25)        rbs6
%  x(26)        rbs7
%  x(27)        rbs8
%  x(28)        rbs9
%  x(29)        v1_mrna
%  x(30)        v2_mrna
%  x(31)        v3_mrna
%  x(32)        v4_mrna
%  x(33)        v5_mrna
%  x(34)        v6_mrna
%  x(35)        v7_mrna
%  x(36)        v8_mrna
%  x(37)        v9_mrna

% List of Compartments 
vol__DefaultCompartment = 1;		%DefaultCompartment

% Global Parameters 
rInfo.g_p1 = 1;		% v8_mrna_degradation_rate
rInfo.g_p2 = 1;		% v9_mrna_degradation_rate
rInfo.g_p3 = 1;		% p1_degradation_rate
rInfo.g_p4 = 1;		% p2_degradation_rate
rInfo.g_p5 = 1;		% p3_degradation_rate
rInfo.g_p6 = 1;		% p4_degradation_rate
rInfo.g_p7 = 1;		% p5_degradation_rate
rInfo.g_p8 = 1;		% p6_degradation_rate
rInfo.g_p9 = 1;		% p7_degradation_rate
rInfo.g_p10 = 1;		% p8_degradation_rate
rInfo.g_p11 = 1;		% p9_degradation_rate
rInfo.g_p12 = 1;		% r1_Kd
rInfo.g_p13 = 1;		% r1_h
rInfo.g_p14 = 1;		% r2_Kd
rInfo.g_p15 = 1;		% r2_h
rInfo.g_p16 = 1;		% r3_Kd
rInfo.g_p17 = 1;		% r3_h
rInfo.g_p18 = 1;		% r4_Kd
rInfo.g_p19 = 1;		% r4_h
rInfo.g_p20 = 1;		% r5_Kd
rInfo.g_p21 = 1;		% r5_h
rInfo.g_p22 = 1;		% r6_Kd
rInfo.g_p23 = 1;		% r6_h
rInfo.g_p24 = 1;		% r7_Kd
rInfo.g_p25 = 1;		% r7_h
rInfo.g_p26 = 1;		% r8_Kd
rInfo.g_p27 = 1;		% r8_h
rInfo.g_p28 = 1;		% r9_Kd
rInfo.g_p29 = 1;		% r9_h
rInfo.g_p30 = 1;		% v1_mrna_degradation_rate
rInfo.g_p31 = 1;		% v2_mrna_degradation_rate
rInfo.g_p32 = 1;		% pro1_strength
rInfo.g_p33 = 1;		% pro2_strength
rInfo.g_p34 = 1;		% pro3_strength
rInfo.g_p35 = 1;		% pro4_strength
rInfo.g_p36 = 1;		% pro5_strength
rInfo.g_p37 = 1;		% v3_mrna_degradation_rate
rInfo.g_p38 = 1;		% pro6_strength
rInfo.g_p39 = 1;		% pro7_strength
rInfo.g_p40 = 1;		% pro8_strength
rInfo.g_p41 = 1;		% pro9_strength
rInfo.g_p42 = 1;		% v4_mrna_degradation_rate
rInfo.g_p43 = 1;		% r10_Kd
rInfo.g_p44 = 1;		% r10_h
rInfo.g_p45 = 1;		% r11_Kd
rInfo.g_p46 = 1;		% r11_h
rInfo.g_p47 = 1;		% r12_Kd
rInfo.g_p48 = 1;		% r12_h
rInfo.g_p49 = 1;		% r13_Kd
rInfo.g_p50 = 1;		% r13_h
rInfo.g_p51 = 1;		% v5_mrna_degradation_rate
rInfo.g_p52 = 1;		% rbs1_strength
rInfo.g_p53 = 1;		% rbs2_strength
rInfo.g_p54 = 1;		% rbs3_strength
rInfo.g_p55 = 1;		% rbs4_strength
rInfo.g_p56 = 1;		% rbs5_strength
rInfo.g_p57 = 1;		% v6_mrna_degradation_rate
rInfo.g_p58 = 1;		% rbs6_strength
rInfo.g_p59 = 1;		% rbs7_strength
rInfo.g_p60 = 1;		% rbs8_strength
rInfo.g_p61 = 1;		% rbs9_strength
rInfo.g_p62 = 1;		% v7_mrna_degradation_rate

% Boundary Conditions 
rInfo.g_p63 = 1;		% as1 = as1[Concentration]
rInfo.g_p64 = 1;		% as2 = as2[Concentration]
rInfo.g_p65 = 1;		% as3 = as3[Concentration]
rInfo.g_p66 = 1;		% as5 = as5[Concentration]
rInfo.g_p67 = 1;		% as6 = as6[Concentration]
rInfo.g_p68 = 1;		% as7 = as7[Concentration]
rInfo.g_p69 = 1;		% as9 = as9[Concentration]
rInfo.g_p70 = 1;		% g1 = g1[Concentration]
rInfo.g_p71 = 1;		% g2 = g2[Concentration]
rInfo.g_p72 = 1;		% g3 = g3[Concentration]
rInfo.g_p73 = 1;		% g4 = g4[Concentration]
rInfo.g_p74 = 1;		% g5 = g5[Concentration]
rInfo.g_p75 = 1;		% g7 = g7[Concentration]
rInfo.g_p76 = 1;		% g8 = g8[Concentration]
rInfo.g_p77 = 1;		% g9 = g9[Concentration]
rInfo.g_p78 = 1;		% rs1a = rs1a[Concentration]
rInfo.g_p79 = 1;		% rs1b = rs1b[Concentration]
rInfo.g_p80 = 1;		% rs2 = rs2[Concentration]
rInfo.g_p81 = 1;		% rs3 = rs3[Concentration]
rInfo.g_p82 = 1;		% rs7 = rs7[Concentration]
rInfo.g_p83 = 1;		% rs8 = rs8[Concentration]

if (nargin == 0)

    % set initial conditions
   xdot(1) = 1*vol__DefaultCompartment;		% g6 = g6 [Concentration]
   xdot(2) = 1*vol__DefaultCompartment;		% p1 = p1 [Concentration]
   xdot(3) = 1*vol__DefaultCompartment;		% p2 = p2 [Concentration]
   xdot(4) = 1*vol__DefaultCompartment;		% p3 = p3 [Concentration]
   xdot(5) = 1*vol__DefaultCompartment;		% p4 = p4 [Concentration]
   xdot(6) = 1*vol__DefaultCompartment;		% p5 = p5 [Concentration]
   xdot(7) = 1*vol__DefaultCompartment;		% p6 = p6 [Concentration]
   xdot(8) = 1*vol__DefaultCompartment;		% p7 = p7 [Concentration]
   xdot(9) = 1*vol__DefaultCompartment;		% p8 = p8 [Concentration]
   xdot(10) = 1*vol__DefaultCompartment;		% p9 = p9 [Concentration]
   xdot(11) = 1*vol__DefaultCompartment;		% pro1 = pro1 [Concentration]
   xdot(12) = 1*vol__DefaultCompartment;		% pro2 = pro2 [Concentration]
   xdot(13) = 1*vol__DefaultCompartment;		% pro3 = pro3 [Concentration]
   xdot(14) = 1*vol__DefaultCompartment;		% pro4 = pro4 [Concentration]
   xdot(15) = 1*vol__DefaultCompartment;		% pro5 = pro5 [Concentration]
   xdot(16) = 1*vol__DefaultCompartment;		% pro6 = pro6 [Concentration]
   xdot(17) = 1*vol__DefaultCompartment;		% pro7 = pro7 [Concentration]
   xdot(18) = 1*vol__DefaultCompartment;		% pro8 = pro8 [Concentration]
   xdot(19) = 1*vol__DefaultCompartment;		% pro9 = pro9 [Concentration]
   xdot(20) = 1*vol__DefaultCompartment;		% rbs1 = rbs1 [Concentration]
   xdot(21) = 1*vol__DefaultCompartment;		% rbs2 = rbs2 [Concentration]
   xdot(22) = 1*vol__DefaultCompartment;		% rbs3 = rbs3 [Concentration]
   xdot(23) = 1*vol__DefaultCompartment;		% rbs4 = rbs4 [Concentration]
   xdot(24) = 1*vol__DefaultCompartment;		% rbs5 = rbs5 [Concentration]
   xdot(25) = 1*vol__DefaultCompartment;		% rbs6 = rbs6 [Concentration]
   xdot(26) = 1*vol__DefaultCompartment;		% rbs7 = rbs7 [Concentration]
   xdot(27) = 1*vol__DefaultCompartment;		% rbs8 = rbs8 [Concentration]
   xdot(28) = 1*vol__DefaultCompartment;		% rbs9 = rbs9 [Concentration]
   xdot(29) = 0*vol__DefaultCompartment;		% v1_mrna = v1_mrna [Concentration]
   xdot(30) = 0*vol__DefaultCompartment;		% v2_mrna = v2_mrna [Concentration]
   xdot(31) = 0*vol__DefaultCompartment;		% v3_mrna = v3_mrna [Concentration]
   xdot(32) = 0*vol__DefaultCompartment;		% v4_mrna = v4_mrna [Concentration]
   xdot(33) = 0*vol__DefaultCompartment;		% v5_mrna = v5_mrna [Concentration]
   xdot(34) = 0*vol__DefaultCompartment;		% v6_mrna = v6_mrna [Concentration]
   xdot(35) = 0*vol__DefaultCompartment;		% v7_mrna = v7_mrna [Concentration]
   xdot(36) = 0*vol__DefaultCompartment;		% v8_mrna = v8_mrna [Concentration]
   xdot(37) = 0*vol__DefaultCompartment;		% v9_mrna = v9_mrna [Concentration]

   % reaction info structure
   rInfo.stoich = [
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -1
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -1 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -1 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -1 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 1 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 1 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 1 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -1 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -1 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -1 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 1 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 1 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 1 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      1 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
   ];

   rInfo.floatingSpecies = {		% Each row: [Species Name, Initial Value, isAmount (1 for amount, 0 for concentration)]
      'g6' , 1, 0
      'p1' , 1, 0
      'p2' , 1, 0
      'p3' , 1, 0
      'p4' , 1, 0
      'p5' , 1, 0
      'p6' , 1, 0
      'p7' , 1, 0
      'p8' , 1, 0
      'p9' , 1, 0
      'pro1' , 1, 0
      'pro2' , 1, 0
      'pro3' , 1, 0
      'pro4' , 1, 0
      'pro5' , 1, 0
      'pro6' , 1, 0
      'pro7' , 1, 0
      'pro8' , 1, 0
      'pro9' , 1, 0
      'rbs1' , 1, 0
      'rbs2' , 1, 0
      'rbs3' , 1, 0
      'rbs4' , 1, 0
      'rbs5' , 1, 0
      'rbs6' , 1, 0
      'rbs7' , 1, 0
      'rbs8' , 1, 0
      'rbs9' , 1, 0
      'v1_mrna' , 0, 0
      'v2_mrna' , 0, 0
      'v3_mrna' , 0, 0
      'v4_mrna' , 0, 0
      'v5_mrna' , 0, 0
      'v6_mrna' , 0, 0
      'v7_mrna' , 0, 0
      'v8_mrna' , 0, 0
      'v9_mrna' , 0, 0
   };

   rInfo.compartments = {		% Each row: [Compartment Name, Value]
      'DefaultCompartment' , 1
   };

   rInfo.params = {		% Each row: [Parameter Name, Value]
      'v8_mrna_degradation_rate' , 1
      'v9_mrna_degradation_rate' , 1
      'p1_degradation_rate' , 1
      'p2_degradation_rate' , 1
      'p3_degradation_rate' , 1
      'p4_degradation_rate' , 1
      'p5_degradation_rate' , 1
      'p6_degradation_rate' , 1
      'p7_degradation_rate' , 1
      'p8_degradation_rate' , 1
      'p9_degradation_rate' , 1
      'r1_Kd' , 1
      'r1_h' , 1
      'r2_Kd' , 1
      'r2_h' , 1
      'r3_Kd' , 1
      'r3_h' , 1
      'r4_Kd' , 1
      'r4_h' , 1
      'r5_Kd' , 1
      'r5_h' , 1
      'r6_Kd' , 1
      'r6_h' , 1
      'r7_Kd' , 1
      'r7_h' , 1
      'r8_Kd' , 1
      'r8_h' , 1
      'r9_Kd' , 1
      'r9_h' , 1
      'v1_mrna_degradation_rate' , 1
      'v2_mrna_degradation_rate' , 1
      'pro1_strength' , 1
      'pro2_strength' , 1
      'pro3_strength' , 1
      'pro4_strength' , 1
      'pro5_strength' , 1
      'v3_mrna_degradation_rate' , 1
      'pro6_strength' , 1
      'pro7_strength' , 1
      'pro8_strength' , 1
      'pro9_strength' , 1
      'v4_mrna_degradation_rate' , 1
      'r10_Kd' , 1
      'r10_h' , 1
      'r11_Kd' , 1
      'r11_h' , 1
      'r12_Kd' , 1
      'r12_h' , 1
      'r13_Kd' , 1
      'r13_h' , 1
      'v5_mrna_degradation_rate' , 1
      'rbs1_strength' , 1
      'rbs2_strength' , 1
      'rbs3_strength' , 1
      'rbs4_strength' , 1
      'rbs5_strength' , 1
      'v6_mrna_degradation_rate' , 1
      'rbs6_strength' , 1
      'rbs7_strength' , 1
      'rbs8_strength' , 1
      'rbs9_strength' , 1
      'v7_mrna_degradation_rate' , 1
   };

   rInfo.boundarySpecies = {		% Each row: [Species Name, Initial Value, isAmount (1 for amount, 0 for concentration)]
      'as1' , 1, 0
      'as2' , 1, 0
      'as3' , 1, 0
      'as5' , 1, 0
      'as6' , 1, 0
      'as7' , 1, 0
      'as9' , 1, 0
      'g1' , 1, 0
      'g2' , 1, 0
      'g3' , 1, 0
      'g4' , 1, 0
      'g5' , 1, 0
      'g7' , 1, 0
      'g8' , 1, 0
      'g9' , 1, 0
      'rs1a' , 1, 0
      'rs1b' , 1, 0
      'rs2' , 1, 0
      'rs3' , 1, 0
      'rs7' , 1, 0
      'rs8' , 1, 0
   };

   rInfo.rateRules = { 		 % List of variables involved in a rate rule 
   };

else

    % listOfRules
   rInfo.g_p68 = (1+pow((x(7))/rInfo.g_p47,rInfo.g_p48)-1)/(1+pow((x(7))/rInfo.g_p47,rInfo.g_p48));
   rInfo.g_p67 = (1+pow((x(10))/rInfo.g_p28,rInfo.g_p29)-1)/(1+pow((x(10))/rInfo.g_p28,rInfo.g_p29));
   rInfo.g_p66 = (1+pow((x(9))/rInfo.g_p49,rInfo.g_p50)-1)/(1+pow((x(9))/rInfo.g_p49,rInfo.g_p50));
   rInfo.g_p65 = (1+pow((x(5))/rInfo.g_p20,rInfo.g_p21)-1)/(1+pow((x(5))/rInfo.g_p20,rInfo.g_p21));
   rInfo.g_p64 = (1+pow((x(2))/rInfo.g_p14,rInfo.g_p15)-1)/(1+pow((x(2))/rInfo.g_p14,rInfo.g_p15));
   rInfo.g_p63 = (1+pow((x(2))/rInfo.g_p12,rInfo.g_p13)-1)/(1+pow((x(2))/rInfo.g_p12,rInfo.g_p13));
   rInfo.g_p83 = 1/(1+pow((x(10))/rInfo.g_p43,rInfo.g_p44));
   rInfo.g_p82 = 1/(1+pow((x(8))/rInfo.g_p22,rInfo.g_p23));
   rInfo.g_p81 = 1/(1+pow((x(6))/rInfo.g_p24,rInfo.g_p25));
   rInfo.g_p80 = 1/(1+pow((x(4))/rInfo.g_p16,rInfo.g_p17));
   rInfo.g_p79 = 1/(1+pow((x(7))/rInfo.g_p26,rInfo.g_p27));
   rInfo.g_p78 = 1/(1+pow((x(3))/rInfo.g_p18,rInfo.g_p19));
   rInfo.g_p77 = (1+pow((x(7))/rInfo.g_p45,rInfo.g_p46)-1)/(1+pow((x(7))/rInfo.g_p45,rInfo.g_p46));
   rInfo.g_p76 = 1/(1+pow((x(10))/rInfo.g_p43,rInfo.g_p44));
   rInfo.g_p75 = (1+pow((x(7))/rInfo.g_p47,rInfo.g_p48)-1)/(1+pow((x(7))/rInfo.g_p47,rInfo.g_p48))*(1/(1+pow((x(8))/rInfo.g_p22,rInfo.g_p23)));
   rInfo.g_p74 = (1+pow((x(9))/rInfo.g_p49,rInfo.g_p50)-1)/(1+pow((x(9))/rInfo.g_p49,rInfo.g_p50));
   rInfo.g_p73 = (1+pow((x(10))/rInfo.g_p28,rInfo.g_p29)-1)/(1+pow((x(10))/rInfo.g_p28,rInfo.g_p29));
   rInfo.g_p72 = (1+pow((x(5))/rInfo.g_p20,rInfo.g_p21)-1)/(1+pow((x(5))/rInfo.g_p20,rInfo.g_p21))*(1/(1+pow((x(6))/rInfo.g_p24,rInfo.g_p25)));
   rInfo.g_p71 = (1+pow((x(2))/rInfo.g_p14,rInfo.g_p15)-1)/(1+pow((x(2))/rInfo.g_p14,rInfo.g_p15))*(1/(1+pow((x(4))/rInfo.g_p16,rInfo.g_p17)));
   rInfo.g_p70 = (1+pow((x(2))/rInfo.g_p12,rInfo.g_p13)-1)/(1+pow((x(2))/rInfo.g_p12,rInfo.g_p13))*(1/(1+pow((x(3))/rInfo.g_p18,rInfo.g_p19))*1/(1+pow((x(7))/rInfo.g_p26,rInfo.g_p27)));
   rInfo.g_p69 = (1+pow((x(7))/rInfo.g_p45,rInfo.g_p46)-1)/(1+pow((x(7))/rInfo.g_p45,rInfo.g_p46));

    % calculate rates of change
   R0 = rInfo.g_p40*(rInfo.g_p76);
   R1 = rInfo.g_p2*(x(37));
   R2 = rInfo.g_p61*(x(37));
   R3 = rInfo.g_p11*(x(10));
   R4 = rInfo.g_p41*(rInfo.g_p75);
   R5 = rInfo.g_p1*(x(36));
   R6 = rInfo.g_p59*(x(36));
   R7 = rInfo.g_p10*(x(9));
   R8 = rInfo.g_p39*(rInfo.g_p77);
   R9 = rInfo.g_p62*(x(35));
   R10 = rInfo.g_p60*(x(35));
   R11 = rInfo.g_p9*(x(8));
   R12 = rInfo.g_p38*(x(1));
   R13 = rInfo.g_p57*(x(34));
   R14 = rInfo.g_p58*(x(34));
   R15 = rInfo.g_p8*(x(7));
   R16 = rInfo.g_p36*(rInfo.g_p74);
   R17 = rInfo.g_p51*(x(33));
   R18 = rInfo.g_p56*(x(33));
   R19 = rInfo.g_p7*(x(6));
   R20 = rInfo.g_p35*(rInfo.g_p73);
   R21 = rInfo.g_p42*(x(32));
   R22 = rInfo.g_p55*(x(32));
   R23 = rInfo.g_p6*(x(5));
   R24 = rInfo.g_p34*(rInfo.g_p72);
   R25 = rInfo.g_p37*(x(31));
   R26 = rInfo.g_p54*(x(31));
   R27 = rInfo.g_p5*(x(4));
   R28 = rInfo.g_p33*(rInfo.g_p71);
   R29 = rInfo.g_p31*(x(30));
   R30 = rInfo.g_p53*(x(30));
   R31 = rInfo.g_p4*(x(3));
   R32 = rInfo.g_p32*(rInfo.g_p70);
   R33 = rInfo.g_p30*(x(29));
   R34 = rInfo.g_p52*(x(29));
   R35 = rInfo.g_p3*(x(2));

   xdot = [
        0
      + R34 - R35
      + R30 - R31
      + R26 - R27
      + R22 - R23
      + R18 - R19
      + R14 - R15
      + R10 - R11
      + R6 - R7
      + R2 - R3
        0
        0
        0
        0
        0
        0
        0
        0
        0
        0
        0
        0
        0
        0
        0
        0
        0
        0
      + R32 - R33
      + R28 - R29
      + R24 - R25
      + R20 - R21
      + R16 - R17
      + R12 - R13
      + R8 - R9
      + R4 - R5
      + R0 - R1
   ];
end;


%listOfSupportedFunctions
function z = pow (x,y) 
    z = x^y; 


function z = sqr (x) 
    z = x*x; 


function z = piecewise(varargin) 
		numArgs = nargin; 
		result = 0; 
		foundResult = 0; 
		for k=1:2: numArgs-1 
			if varargin{k+1} == 1 
				result = varargin{k}; 
				foundResult = 1; 
				break; 
			end 
		end 
		if foundResult == 0 
			result = varargin{numArgs}; 
		end 
		z = result; 


function z = gt(a,b) 
   if a > b 
   	  z = 1; 
   else 
      z = 0; 
   end 


function z = lt(a,b) 
   if a < b 
   	  z = 1; 
   else 
      z = 0; 
   end 


function z = geq(a,b) 
   if a >= b 
   	  z = 1; 
   else 
      z = 0; 
   end 


function z = leq(a,b) 
   if a <= b 
   	  z = 1; 
   else 
      z = 0; 
   end 


function z = neq(a,b) 
   if a ~= b 
   	  z = 1; 
   else 
      z = 0; 
   end 


function z = and(varargin) 
		result = 1;		 
		for k=1:nargin 
		   if varargin{k} ~= 1 
		      result = 0; 
		      break; 
		   end 
		end 
		z = result; 


function z = or(varargin) 
		result = 0;		 
		for k=1:nargin 
		   if varargin{k} ~= 0 
		      result = 1; 
		      break; 
		   end 
		end 
		z = result; 


function z = xor(varargin) 
		foundZero = 0; 
		foundOne = 0; 
		for k = 1:nargin 
			if varargin{k} == 0 
			   foundZero = 1; 
			else 
			   foundOne = 1; 
			end 
		end 
		if foundZero && foundOne 
			z = 1; 
		else 
		  z = 0; 
		end 
		 


function z = not(a) 
   if a == 1 
   	  z = 0; 
   else 
      z = 1; 
   end 


function z = root(a,b) 
	z = a^(1/b); 
 

