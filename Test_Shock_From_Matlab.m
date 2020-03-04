disp('Begin Shock from Matlab');

% pe = pyenv("ExecutionMode","OutOfProcess");
% pe = pyenv

% pyversion
% path = fileparts(which(test.py));
shock_file = ' Stimulation_files/shock.py';
num_shocks = 5;
terminal_input = strcat('python', ' ', shock_file, {' '}, num2str(num_shocks));
% terminal_input2 = strcat(terminal_input, {' '}, num_shocks);
% disp('testing');
% disp(terminal_input);

% system(char(terminal_input));

pyversion
path_to_u6 = fileparts(which('u6.py'));
if count(py.sys.path, path_to_u6) == 0
    insert(py.sys.path, int32(0), path_to_u6);
end
% system('python Stimulation_files/shock.py 10');
% make_sound(30000);

disp('Finished');
