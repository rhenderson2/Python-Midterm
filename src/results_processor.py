# This module processes the winner

def process_results(master_state_map):
    """
    This function processes the election results
    :type master_state_map: object
    :return:
    """
   # for state_num, state_data in master_state_map.items():
   #     print(state_data)

    for state_num, state_data in master_state_map.items():
        #print(f"state_num: {state_num}, this represents the item number in the dictionary.")
        #print(f"state_data: {state_data}, this contains all the state data")
        # print(state_data)
        dem_elect = {'democratic': 0}
        rep_elect = {'republican': 0}
        lib_elect = {'libertarian': 0}
        ind_elect = {'independent': 0}
        for key, value in state_data.items():
            if key == 'party':
                if value == 'democratic':
                    if key == 'electorate':
                        for key,value in dem_elect:
                            Democratic = key
                            Electors = value
                            print(dem_elect)
                elif 'party' == 'republican':
                        if key == 'electorate':
                            for key, value in rep_elect:
                                Republican = key
                                Electors = value
                                print(rep_elect)
                elif 'party' == 'libertarian':
                        if key == 'electorate':
                            for key, value in lib_elect:
                                Libertarian = key
                                Electors = value
                                print(lib_elect)
                elif 'party' == 'Independent':
                        if key == 'electorate':
                            for key, value in ind_elect:
                                Libertarian = key
                                Electors = value
                                print(ind_elect)

                print(f"state: {value}")
            elif key == 'num_voters':
                print(f"num_voters: {value}")
            elif key == 'party':
                print(f"party: {value}")
            elif key == 'votes':
                print(f"votes: {value}")
            elif key == 'electorate':
                print(f"electorate: {value}")







