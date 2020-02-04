disp('Begin Shock from Matlab');

% pe = pyenv("ExecutionMode","OutOfProcess");
% pe = pyenv

% pyversion
% path = fileparts(which(test.py));
system('python Stimulation_files/test.py')

disp('Finished');