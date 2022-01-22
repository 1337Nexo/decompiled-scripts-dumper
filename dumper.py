import re, sys

sys.stdout = open('decompiled-scripts-dumper.log', 'w')
        
def del_chars(string, b, e):
    begin = string[:b]
    end = string[e+1:]
    return begin + end

def dump_regex(regex_name, regex, file_name):
    matches = re.finditer(regex, open(file_name).read(), re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):   
        print('\n[{regex_name}]: {match}'.format(regex_name = regex_name, match = match.group()))
        return match.group()

def find_regex(regex, file_name):
    matches = re.finditer(regex, open(file_name).read(), re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):   
        return match.group()

def print_regex(regex_name, regex_found_value):
    print('\n[{regex_name}]: {value}'.format(regex_name = regex_name, value = regex_found_value))

decompiled_scripts_directory = 'GTA-V-Decompiled-Scripts/decompiled_scripts/'
freemode_directory = decompiled_scripts_directory + 'freemode.c'
three_card_poker_directory = decompiled_scripts_directory + 'three_card_poker.c'
net_rank_tunable_loader_directory = decompiled_scripts_directory + 'net_rank_tunable_loader.c'
casino_slots_directory = decompiled_scripts_directory + 'casino_slots.c'
tuneables_processing_directory = decompiled_scripts_directory + 'tuneables_processing.c'
fm_mission_controller_2020_directory = decompiled_scripts_directory + 'fm_mission_controller_2020.c'

tuneables = dump_regex('tuneables', r'if \(Global_.*\.f_.* == 1 && !func_.*\(PLAYER::PLAYER_ID\(\), 1\)\)', freemode_directory )
tuneables = dump_regex('tuneables', r'if \(Global_.*\.f_.* == 1 && !func_.*\(unk_.*\(\), 1\)\)', freemode_directory )

spawn_activities = dump_regex('spawn_activities', r'func_.*\(PLAYER::PLAYER_PED_ID\(\), func_.*\(\), -1, 0\);\n						Global_.*.f_8 = 0;', freemode_directory )
spawn_activities = dump_regex('spawn_activities', r'func_.*\(unk_.*\(\), func_.*\(\), -1, 0\);\n						Global_.*.f_8 = 0;', freemode_directory )

playerid = dump_regex('playerid', r'Global_.*\.f_.* = { 9999\.9f, 9999\.9f, 9999\.9f };', three_card_poker_directory )
three_card_poker_table = dump_regex('three_card_poker_table', r'Local_.*\[iVar1 .*\].f_.* == iParam0', three_card_poker_directory )
three_card_poker_cur_deck = dump_regex('three_card_poker_cur_deck', r'Local_.*\.f_.* = { Local_.*\.f_.*\[iParam0 .*] };', three_card_poker_directory )
three_card_poker_ac_deck = dump_regex('three_card_poker_ac_deck', r'Local_.*\.f_.* = { Local_.*\.f_.*\[iParam0 .*] };', three_card_poker_directory )

net_rank_tunable_loader_regex = r'func_.*\(iLocal_.*, .*, .*, &\(Global_.*\[8000]\), 1\);'
net_rank_tunable_loader = find_regex(net_rank_tunable_loader_regex, net_rank_tunable_loader_directory )
net_rank_tunable_loader = del_chars(net_rank_tunable_loader, 0, 42)
net_rank_tunable_loader = del_chars(net_rank_tunable_loader, 6, 20)
print_regex('get_rp_required_for_rank', net_rank_tunable_loader)

casino_slots_regex = r'struct<279> Local_.* = { 64, 3, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 8, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 16, 3, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10 } ;'
casino_slots = find_regex(casino_slots_regex, casino_slots_directory )
casino_slots = del_chars(casino_slots, 22, 7331)
casino_slots = del_chars(casino_slots, 0, 17)
print_regex('casino_slots', casino_slots)

player_stats_regex = r'Global_.*\[PLAYER::PLAYER_ID\(\) .*\].f_.*.f_.* = func_.*\(joaat\("mpply_total_races_won"\)\);'
player_stats_ = find_regex(player_stats_regex, freemode_directory )
print_regex('player_stats', player_stats_)

ballistic_equipment = dump_regex('ballistic_equipment', r'func_8\(iParam0, iParam1, -156036296, &\(Global_.*\.f_.*\), 1\);', tuneables_processing_directory )

contract_value = dump_regex('contract_value', r'func_.*\(iParam0, iParam1, -2108119120, &\(Global_.*\.f_.*\), 1\);', tuneables_processing_directory )

cayo_perico_team_lives_regex = r'Local_.*\.f_.*\[iVar4\] = Global_.*\.f_.*\[iVar3 .*\]\[iVar4\];'
cayo_perico_team_lives = dump_regex('cayo_perico_team_lives', cayo_perico_team_lives_regex, fm_mission_controller_2020_directory )