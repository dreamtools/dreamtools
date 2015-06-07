%  How to use:
%
%  subchallenge2_missing_connections takes 3 inputs and returns 3 outputs.
%
%  [t x rInfo] = subchallenge2_missing_connections(tspan,solver,options)
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
%     [t x rInfo] = subchallenge2_missing_connections(linspace(0,100,100),@ode23s,options);
%
function [t x rInfo] = subchallenge2_missing_connections(tspan,solver,options)
    % initial conditions
    [x rInfo] = model();

    % initial assignments

    % assignment rules

    % run simulation
    [t x] = feval(solver,@model,tspan,x,options);

    % assignment rules

function [xdot rInfo] = model(time,x)
%  x(1)        p1
%  x(2)        p2
%  x(3)        p3
%  x(4)        p4
%  x(5)        p5
%  x(6)        p6
%  x(7)        p11
%  x(8)        p7
%  x(9)        p8
%  x(10)        p9
%  x(11)        p10

% List of Compartments 
vol__compartment = 1;		%compartment

% Global Parameters 
rInfo.g_p1 = 1;		% p1_synthesis_rate
rInfo.g_p2 = 1;		% r1_Kd
rInfo.g_p3 = 1;		% r1_h
rInfo.g_p4 = 1;		% p1_degradation_rate
rInfo.g_p5 = 1;		% p2_synthesis_rate
rInfo.g_p6 = 1;		% r2_Kd
rInfo.g_p7 = 1;		% r2_h
rInfo.g_p8 = 1;		% r5_Kd
rInfo.g_p9 = 1;		% r5_h
rInfo.g_p10 = 1;		% p2_degradation_rate
rInfo.g_p11 = 1;		% p3_synthesis_rate_1
rInfo.g_p12 = 1;		% r4_Kd
rInfo.g_p13 = 1;		% r4_h
rInfo.g_p14 = 1;		% p3_synthesis_rate_2
rInfo.g_p15 = 1;		% r3_Kd
rInfo.g_p16 = 1;		% r3_h
rInfo.g_p17 = 1;		% p3_degradation_rate
rInfo.g_p18 = 1;		% p4_synthesis_rate_1
rInfo.g_p19 = 1;		% p4_synthesis_rate_2
rInfo.g_p20 = 1;		% r8_Kd
rInfo.g_p21 = 1;		% r8_h
rInfo.g_p22 = 1;		% p4_degradation_rate
rInfo.g_p23 = 1;		% r6_basal
rInfo.g_p24 = 1;		% p5_synthesis_rate_1
rInfo.g_p25 = 1;		% r6_Kd
rInfo.g_p26 = 1;		% r6_h
rInfo.g_p27 = 1;		% p5_synthesis_rate_3
rInfo.g_p28 = 1;		% r7_Kd
rInfo.g_p29 = 1;		% r7_h
rInfo.g_p30 = 1;		% p5_synthesis_rate_2
rInfo.g_p31 = 1;		% p5_degradation_rate
rInfo.g_p32 = 1;		% p6_synthesis_rate
rInfo.g_p33 = 1;		% p6_degradation_rate
rInfo.g_p34 = 1;		% r11_basal
rInfo.g_p35 = 1;		% p11_synthesis_rate_1
rInfo.g_p36 = 1;		% r11_Kd
rInfo.g_p37 = 1;		% r11_h
rInfo.g_p38 = 1;		% p11_degradation_rate
rInfo.g_p39 = 1;		% p7_synthesis_rate
rInfo.g_p40 = 1;		% p7_degradation_rate
rInfo.g_p41 = 1;		% p8_synthesis_rate
rInfo.g_p42 = 1;		% r14_Kd
rInfo.g_p43 = 1;		% r14_h
rInfo.g_p44 = 1;		% p8_degradation_rate
rInfo.g_p45 = 1;		% p9_synthesis_rate
rInfo.g_p46 = 1;		% r15_Kd
rInfo.g_p47 = 1;		% r15_h
rInfo.g_p48 = 1;		% p9_degradation_rate
rInfo.g_p49 = 1;		% p10_synthesis_rate
rInfo.g_p50 = 1;		% r16_Kd
rInfo.g_p51 = 1;		% r16_h
rInfo.g_p52 = 1;		% r13_Kd
rInfo.g_p53 = 1;		% r13_h
rInfo.g_p54 = 1;		% p10_degradation_rate

% Boundary Conditions 
rInfo.g_p55 = 1;		% X = X[Concentration]
rInfo.g_p56 = 1;		% __src__ = __src__[Concentration]
rInfo.g_p57 = 1;		% __waste__ = __waste__[Concentration]

if (nargin == 0)

    % set initial conditions
   xdot(1) = 1*vol__compartment;		% p1 = p1 [Concentration]
   xdot(2) = 1*vol__compartment;		% p2 = p2 [Concentration]
   xdot(3) = 1*vol__compartment;		% p3 = p3 [Concentration]
   xdot(4) = 1*vol__compartment;		% p4 = p4 [Concentration]
   xdot(5) = 1*vol__compartment;		% p5 = p5 [Concentration]
   xdot(6) = 1*vol__compartment;		% p6 = p6 [Concentration]
   xdot(7) = 1*vol__compartment;		% p11 = p11 [Concentration]
   xdot(8) = 1*vol__compartment;		% p7 = p7 [Concentration]
   xdot(9) = 1*vol__compartment;		% p8 = p8 [Concentration]
   xdot(10) = 1*vol__compartment;		% p9 = p9 [Concentration]
   xdot(11) = 1*vol__compartment;		% p10 = p10 [Concentration]

   % reaction info structure
   rInfo.stoich = [
      1 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 1 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 1 -1 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 1 1 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 1 -1 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 1 -1 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 1 -1 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -1 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -1 0 0 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -1 0 0
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 -1
   ];

   rInfo.floatingSpecies = {		% Each row: [Species Name, Initial Value, isAmount (1 for amount, 0 for concentration)]
      'p1' , 1, 0
      'p2' , 1, 0
      'p3' , 1, 0
      'p4' , 1, 0
      'p5' , 1, 0
      'p6' , 1, 0
      'p11' , 1, 0
      'p7' , 1, 0
      'p8' , 1, 0
      'p9' , 1, 0
      'p10' , 1, 0
   };

   rInfo.compartments = {		% Each row: [Compartment Name, Value]
      'compartment' , 1
   };

   rInfo.params = {		% Each row: [Parameter Name, Value]
      'p1_synthesis_rate' , 1
      'r1_Kd' , 1
      'r1_h' , 1
      'p1_degradation_rate' , 1
      'p2_synthesis_rate' , 1
      'r2_Kd' , 1
      'r2_h' , 1
      'r5_Kd' , 1
      'r5_h' , 1
      'p2_degradation_rate' , 1
      'p3_synthesis_rate_1' , 1
      'r4_Kd' , 1
      'r4_h' , 1
      'p3_synthesis_rate_2' , 1
      'r3_Kd' , 1
      'r3_h' , 1
      'p3_degradation_rate' , 1
      'p4_synthesis_rate_1' , 1
      'p4_synthesis_rate_2' , 1
      'r8_Kd' , 1
      'r8_h' , 1
      'p4_degradation_rate' , 1
      'r6_basal' , 1
      'p5_synthesis_rate_1' , 1
      'r6_Kd' , 1
      'r6_h' , 1
      'p5_synthesis_rate_3' , 1
      'r7_Kd' , 1
      'r7_h' , 1
      'p5_synthesis_rate_2' , 1
      'p5_degradation_rate' , 1
      'p6_synthesis_rate' , 1
      'p6_degradation_rate' , 1
      'r11_basal' , 1
      'p11_synthesis_rate_1' , 1
      'r11_Kd' , 1
      'r11_h' , 1
      'p11_degradation_rate' , 1
      'p7_synthesis_rate' , 1
      'p7_degradation_rate' , 1
      'p8_synthesis_rate' , 1
      'r14_Kd' , 1
      'r14_h' , 1
      'p8_degradation_rate' , 1
      'p9_synthesis_rate' , 1
      'r15_Kd' , 1
      'r15_h' , 1
      'p9_degradation_rate' , 1
      'p10_synthesis_rate' , 1
      'r16_Kd' , 1
      'r16_h' , 1
      'r13_Kd' , 1
      'r13_h' , 1
      'p10_degradation_rate' , 1
   };

   rInfo.boundarySpecies = {		% Each row: [Species Name, Initial Value, isAmount (1 for amount, 0 for concentration)]
      'X' , 1, 0
      '__src__' , 1, 0
      '__waste__' , 1, 0
   };

   rInfo.rateRules = { 		 % List of variables involved in a rate rule 
   };

else

    % calculate rates of change
   R0 = rInfo.g_p1*pow((rInfo.g_p55)/rInfo.g_p2,rInfo.g_p3)/(1+pow((rInfo.g_p55)/rInfo.g_p2,rInfo.g_p3));
   R1 = rInfo.g_p4*(x(1));
   R2 = rInfo.g_p5*pow((x(1))/rInfo.g_p6,rInfo.g_p7)/(1+pow((x(1))/rInfo.g_p6,rInfo.g_p7))/(1+pow((x(6))/rInfo.g_p8,rInfo.g_p9));
   R3 = rInfo.g_p10*(x(2));
   R4 = rInfo.g_p11*pow((x(2))/rInfo.g_p12,rInfo.g_p13)/(1+pow((x(2))/rInfo.g_p12,rInfo.g_p13))+rInfo.g_p14*pow((x(1))/rInfo.g_p15,rInfo.g_p16)/(1+pow((x(1))/rInfo.g_p15,rInfo.g_p16));
   R5 = rInfo.g_p17*(x(3));
   R6 = rInfo.g_p18*(x(3));
   R7 = rInfo.g_p19/(1+pow((x(8))/rInfo.g_p20,rInfo.g_p21));
   R8 = rInfo.g_p22*(x(4));
   R9 = rInfo.g_p23+rInfo.g_p24*pow((x(4))/rInfo.g_p25,rInfo.g_p26)/(1+pow((x(4))/rInfo.g_p25,rInfo.g_p26))+rInfo.g_p27*pow((x(5))/rInfo.g_p28,rInfo.g_p29)/(1+pow((x(5))/rInfo.g_p28,rInfo.g_p29))+rInfo.g_p30;
   R10 = rInfo.g_p31*(x(5));
   R11 = rInfo.g_p32;
   R12 = rInfo.g_p33*(x(6));
   R13 = rInfo.g_p34+rInfo.g_p35*pow((x(5))/rInfo.g_p36,rInfo.g_p37)/(1+pow((x(5))/rInfo.g_p36,rInfo.g_p37));
   R14 = rInfo.g_p38*(x(7));
   R15 = rInfo.g_p39*(rInfo.g_p34+rInfo.g_p35*pow((x(5))/rInfo.g_p36,rInfo.g_p37)/(1+pow((x(5))/rInfo.g_p36,rInfo.g_p37)));
   R16 = rInfo.g_p40*(x(8));
   R17 = rInfo.g_p41/(1+pow((x(8))/rInfo.g_p42,rInfo.g_p43));
   R18 = rInfo.g_p44*(x(9));
   R19 = rInfo.g_p45*pow((x(9))/rInfo.g_p46,rInfo.g_p47)/(1+pow((x(9))/rInfo.g_p46,rInfo.g_p47));
   R20 = rInfo.g_p48*(x(10));
   R21 = rInfo.g_p49/(1+pow((x(10))/rInfo.g_p50,rInfo.g_p51))/(1+pow((x(8))/rInfo.g_p52,rInfo.g_p53));
   R22 = rInfo.g_p54*(x(11));

   xdot = [
      + R0 - R1
      + R2 - R3
      + R4 - R5 - R6
      + R6 + R7 - R8
      + R9 - R10
      + R11 - R12
      + R13 - R14
      + R15 - R16
      + R17 - R18
      + R19 - R20
      + R21 - R22
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
 

