% script to make .tgt files
clc
clear
close all

namefile = 'Savings_AntiClampWash_';
% group = 'NE_ccw_c2'; 
% group = 'NE_cw_c2'; 
% group = 'NW_ccw_c2'; 
% group = 'NW_cw_c2'; 
% group = 'SW_ccw_c2'; 
% group = 'SW_cw_c2'; 
% group = 'SE_ccw_c2'; 
% group = 'SE_cw_c2'; 

% group = 'NE_ccw_c15';
% group = 'NE_cw_c15'; 
% group = 'NW_ccw_c15'; 
% group = 'NW_cw_c15'; 
% group = 'SW_ccw_c15'; 
group = 'SW_cw_c15'; 
% group = 'SE_ccw_c15'; 
% group = 'SE_cw_c15'; 

n_landmarks = 0;

target_dist = 80;

if strcmp(group(end),'2')
    rot_size = 2;
else
    rot_size = 15;
end

if strcmp(group(4:5),'cw')
    rot_size=(-1)*rot_size;
else
    rot_size=rot_size;
end

probe_tgt_angles = 10:10:80;  % target set (for NE. for the other quarter, add the appropriate angle)
if strcmp(group(1:2),'NE')
    tgt_wedges = probe_tgt_angles;
elseif strcmp(group(1:2),'NW')
    tgt_wedges = 90+probe_tgt_angles;
elseif strcmp(group(1:2),'SW')
    tgt_wedges = 180+probe_tgt_angles;
else
    tgt_wedges = 270+probe_tgt_angles;
end

% a cycle includes a trial for each target
tpc = length(probe_tgt_angles); % trials per cycle

% different blocks of experiment: number of cycles

% for testing
% nC_noFbPre=1; % no feedback pre adaptation
% nC_base=1; % baseline (veridical feedback)
% nC_clamp1=10; % 1st clamp

nC_noFbPre=3; % no feedback pre adaptation
nC_base=5; % baseline (veridical feedback)
nC_clamp1=60; % 1st clamp
nC_antiClamp=30; % washout using anticlamp (transition to veridical feedback is adjusted for each participant)
nC_wash=20; % washout using anticlamp and then veridical 
nC_clamp2=60; % 2nd clamp
nC_noFbPost=3; % no feedback post adaptation

% different blocks of experiment: number of trials
nT_noFbPre=nC_noFbPre*tpc; % no feedback pre adaptation
nT_illustrate=[2 2 2 2 2]; % practice trials that illustrate the veridical or clamp (number of elements is for number of sessions), each value is the number of illustration trials 
nT_base=nC_base*tpc; % baseline (veridical feedback)
nT_clamp1=nC_clamp1*tpc; % 1st clamp
nT_antiClamp=nC_antiClamp*tpc; % anti-clamp
nT_wash=nC_wash*tpc; % washout
nT_clamp2=nC_clamp2*tpc; % 2nd clamp
nT_noFbPost=nC_noFbPost*tpc; % no feedback post adaptation

nT_tot = nT_noFbPre + sum(nT_illustrate) + nT_base + nT_clamp1 + nT_antiClamp + nT_wash + nT_clamp2 + nT_noFbPost;

% tgt_wedges_row=reshape(tgt_wedges,1,[]);
% tgt_perms_noFb_base=nan(nC_noFbPre+nC_base+nC_noFbPost,tpc);
% for i=1:(nC_noFbPre+nC_base+nC_noFbPost)
%     tgt_perms_noFb_base(i,:)=tgt_wedges_row(randperm(tpc));
% end
possible_tgt_perms=perms(tgt_wedges); % for 8 targets - 40,320 perms

itgt_perms_noFbPre=randperm(size(possible_tgt_perms,1),nC_noFbPre);
itgt_perms_base=randperm(size(possible_tgt_perms,1),nC_base);
itgt_perms_clamp1=randperm(size(possible_tgt_perms,1),nC_clamp1);
itgt_perms_antiClamp=randperm(size(possible_tgt_perms,1),nC_antiClamp);
itgt_perms_wash=randperm(size(possible_tgt_perms,1),nC_wash);
itgt_perms_clamp2=randperm(size(possible_tgt_perms,1),nC_clamp2);
itgt_perms_noFbPost=randperm(size(possible_tgt_perms,1),nC_noFbPost);

tgt_perms_noFbPre=reshape(possible_tgt_perms(itgt_perms_noFbPre,:)',[],1);
tgt_perms_base=reshape(possible_tgt_perms(itgt_perms_base,:)',[],1);
tgt_perms_clamp1=reshape(possible_tgt_perms(itgt_perms_clamp1,:)',[],1);
tgt_perms_antiClamp=reshape(possible_tgt_perms(itgt_perms_antiClamp,:)',[],1);
tgt_perms_wash=reshape(possible_tgt_perms(itgt_perms_wash,:)',[],1);
tgt_perms_clamp2=reshape(possible_tgt_perms(itgt_perms_clamp2,:)',[],1);
tgt_perms_noFbPost=reshape(possible_tgt_perms(itgt_perms_noFbPost,:)',[],1);

% indices of start and end of the different experimental blocks (i-initial; f-final)
noFbPre_f=nT_noFbPre;
illustrate1_i=noFbPre_f+1;
illustrate1_f=illustrate1_i-1+nT_illustrate(1);
base_i=illustrate1_f+1;
base_f=base_i-1+nT_base;
illustrate2_i=base_f+1;
illustrate2_f=illustrate2_i-1+nT_illustrate(2);
clamp1_i=illustrate2_f+1;
clamp1_f=clamp1_i-1+nT_clamp1;
illustrate3_i=clamp1_f+1;
illustrate3_f=illustrate3_i-1+nT_illustrate(3);
antiClamp_i=illustrate3_f+1;
antiClamp_f=antiClamp_i-1+nT_antiClamp;
illustrate4_i=antiClamp_f+1;
illustrate4_f=illustrate4_i-1+nT_illustrate(4);
wash_i=illustrate4_f+1;
wash_f=wash_i-1+nT_wash;
illustrate5_i=wash_f+1;
illustrate5_f=illustrate5_i-1+nT_illustrate(5);
clamp2_i=illustrate5_f+1;
clamp2_f=clamp2_i-1+nT_clamp2;
noFbPost_i=clamp2_f+1;

% Constant values
T.trialnum = (1:nT_tot)';
T.tgt_dist = ones(nT_tot, 1)*target_dist;
T.tgt_angle = [tgt_perms_noFbPre; mean(tgt_wedges)*ones(2,1); tgt_perms_base; mean(tgt_wedges)*ones(2,1);...
              tgt_perms_clamp1; mean(tgt_wedges)*ones(2,1); tgt_perms_antiClamp; mean(tgt_wedges)*ones(2,1);...
              tgt_perms_wash; mean(tgt_wedges)*ones(2,1); tgt_perms_clamp2; tgt_perms_noFbPost];
T.rotation = zeros(nT_tot, 1); T.rotation([illustrate2_i:clamp1_f illustrate5_i:clamp2_f])=rot_size; T.rotation(illustrate3_i:antiClamp_f)=-rot_size;
T.num_landmarks = ones(nT_tot, 1)*n_landmarks;
T.aiming_landmarks = zeros(nT_tot, 1);
T.online_fb = zeros(nT_tot, 1); T.online_fb(illustrate1_i:clamp2_f)=1;
T.endpoint_fb = zeros(nT_tot, 1);T.endpoint_fb(illustrate1_i:clamp2_f)=1;
T.clamped_fb = zeros(nT_tot, 1); T.clamped_fb([illustrate2_i:clamp1_f illustrate3_i:antiClamp_f illustrate5_i:clamp2_f])=1;
T.between_blocks = zeros(nT_tot, 1);
T.breaks = zeros(nT_tot, 1);

% decide here where you want to place between block messages
T.between_blocks(noFbPre_f) = 1;
T.between_blocks(illustrate1_f) = 4;
T.between_blocks(base_f) = 1;
T.between_blocks(illustrate2_f) = 2;
T.between_blocks(illustrate2_f+(nC_clamp1/2)*tpc) = 2;
T.between_blocks(clamp1_f) = 1;
T.between_blocks(illustrate3_f) = 2;
T.between_blocks(antiClamp_f) = 1;
% T.between_blocks(illustrate4_f) = 4;
for b=1:3
    T.between_blocks(illustrate4_f+b*5*tpc) = 4;
end
T.between_blocks(wash_f) = 1;
T.between_blocks(illustrate5_f) = 2;
T.between_blocks(illustrate5_f+(nC_clamp2/2)*tpc) = 2;
T.between_blocks(clamp2_f) = 3;

T.breaks(illustrate2_f+(nC_clamp1/2)*tpc) = 1; % break duration
T.breaks(clamp1_f) = 2;
for b=1:3
    T.breaks(illustrate4_f+b*5*tpc) = 1;
end
T.breaks(illustrate5_f+(nC_clamp2/2)*tpc) = 1; % break duration

T.stage=[ones(nT_noFbPre,1); zeros(nT_illustrate(1),1); 2*ones(nT_base,1); zeros(nT_illustrate(2),1);...
        3*ones(nT_clamp1,1); zeros(nT_illustrate(3),1); 4*ones(nT_antiClamp,1); zeros(nT_illustrate(4),1);...
        5*ones(nT_wash,1); zeros(nT_illustrate(5),1); 6*ones(nT_clamp2,1); 7*ones(nT_noFbPost,1)];

dummy = struct2dataset(T); %%% These two lines are to convert structure into double
set = double(dummy);

set(:,1) = 1:size(set,1);
%Add in last Betweenblocks
%set(end,15) = 1;
%Variables header file

header = {'trialnum','tgt_distance','tgt_angle','rotation',...
    'num_landmarks','aiming_landmarks','online_fb', 'endpoint_feedback',...
    'clamped_fb','between_blocks','breaks','stage'};

filename = strcat([namefile group],'_1','.tgt');

%If you ever need strings in here use this way
fid = fopen(filename,'wt');
[rows,cols] = size(set);
fprintf(fid,'%s\t',header{:});
for i = 1:rows
    fprintf(fid,'\n');
    for j = 1:cols
        fprintf(fid,'%3.2f\t',set(i,j));
    end
end
fclose(fid);
