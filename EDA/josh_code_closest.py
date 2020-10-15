# pop_table = 1.4 million row
# village_table = village and coords

#scidist
def assign_vil_pop(pop, vil):

    # [1] for element in pop_table:
    for i in pop.index:

        # lowest is a distance
        lowest = 0
        # d is the index in the village dataframe that a pop segment belongs to
        d = 0

        # debug
        # print(pop.loc[i, 'latitude'])
    

        # [2] find distance between pop table instance and each village:
        for k in vil.index:
            # distance formula
            distance = math.sqrt( ((pop.loc[i, 'latitude'] - vil.loc[k, 'lat'])**2) + 
                                  ((pop.loc[i, 'longitude'] - vil.loc[k, 'long'])**2))
            # maybe consider the scidist formula instead, might be faster

            # lowest is only 0 if it's the first loop
            if lowest == 0:
                # initial lowest distance
                lowest = distance
                # this doesn't need to be recalculated
                # just indicating a temporary lowest distance of the 0th index
                d = 0
            # this happens every other time
            else:
                if distance < lowest:
                    # set new lowest distance
                    lowest = distance
                    # increment counter (which represents index)
                    d += 1
                else:
                    # no lowest distance update
                    # increment counter
                    d += 1
        
        # create a new column called 'closest_village' and set it equal to the value
        # of vilage_id at the index 'd'
        pop.loc[i, 'closest_village'] = vil.loc[d, 'village']