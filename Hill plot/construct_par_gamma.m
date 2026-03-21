%% Generate random parameter sets

%% Set number of parameter sets to be samples
nr_par=900000;

%% Define the parameter space
range = [log10(0.0001) log10(5);log10(0.0001) log10(5);log10(0.0001) log10(5);log10(0.0001) log10(5); ... % p1-p4
log10(0.01) log10(5);1 3;log10(0.01) log10(10);log10(0.0001) log10(1);0.2 3.5;1 1;0.01 5;... % p5-p11, xXF1 %gamma!=1
log10(0.01) log10(5);1 3;log10(0.01) log10(10);log10(0.0001) log10(1);0.2 3.5;1 1;0.01 5;... % p12-p18, xXF2
log10(0.01) log10(5);1 3;log10(0.01) log10(10);log10(0.0001) log10(1);0.2 3.5;0.01 5;0.01 5;... % p19-p25, xXF3
log10(0.01) log10(5);1 3;log10(0.01) log10(10);log10(0.0001) log10(1);0.2 3.5;log10(0.01) log10(3);0.01 5]; % p26-p32, xXF4

%% Sample parameters
pars = lhsu(range(:,1)',range(:,2)',nr_par);

%% Generate parameters
for i = 1:nr_par
    % Log-sample p8 and p5 (p5 > p8)
    log_p8 = pars(i,8);
    log_p5 = rand * (log10(5) - (log_p8 + 0.001)) + (log_p8 + 0.001);
    pars(i, 5) = log_p5; % p5
    pars(i, 8) = log_p8; % p8
    
    % Log-sample p15 and p12 (p12 > p15)
    log_p15 = pars(i,15);
    log_p12 = rand * (log10(5) - (log_p15 + 0.001)) + (log_p15 + 0.001);
    pars(i, 12) = log_p12; % p12
    pars(i, 15) = log_p15; % p15

    % Log-sample p22 and p19 (p19 > p22)
    log_p22 = pars(i,22);
    log_p19 = rand * (log10(5) - (log_p22 + 0.001)) + (log_p22 + 0.001);
    pars(i, 19) = log_p19; % p19
    pars(i, 22) = log_p22; % p22

    % Log-sample p29 and p26 (p26 > p29)
    log_p29 = pars(i,29);
    log_p26 = rand * (log10(5) - (log_p29 + 0.001)) + (log_p29 + 0.001);
    pars(i, 26) = log_p26; % p26
    pars(i, 29) = log_p29; % p29
end

%% Convert back from log10
pars(:,[1,2,3,4,5,7,8,12,14,15,19,21,22,26,28,29,31]) = 10.^(pars(:,[1,2,3,4,5,7,8,12,14,15,19,21,22,26,28,29,31]));

%% Write parameter sets to output file
dlmwrite('/home/madhusud/modeling_gene_expression/Screens/three_cascade.txt', pars);
