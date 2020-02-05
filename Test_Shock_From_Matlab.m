disp('Begin Shock from Matlab');

% pe = pyenv("ExecutionMode","OutOfProcess");
% pe = pyenv

% pyversion
% path = fileparts(which(test.py));
system('python Stimulation_files/shock.py 5')

disp('Finished');