disp('Begin Shock from Matlab');

% pe = pyenv("ExecutionMode","OutOfProcess");
% pe = pyenv

% pyversion
% path = fileparts(which(test.py));
shock_file = ' Stimulation_files/shock.py';
num_shocks = 5;
terminal_input = strcat('python', ' ', shock_file, ' ', num_shocks);
disp(terminal_input);

system('python Stimulation_files/shock.py 5')

disp('Finished');