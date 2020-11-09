def hdr(pm_trials, var=0, ent=0, attr1=0, attr2=0, round_off= 15):
        """Hubbard Decision Research counter-based PRNG"""

        values = []
        for pm_index in range(1, pm_trials+1):
            eq = ((((
                (((999999999999989 % ((
                (pm_index * 2499997 + (var) * 1800451 + (ent) * 2000371 + (attr1) * 1796777 + attr2 * 2299603)
                    % 7450589) * 4658 + 7450581)) * 383) % 99991) * 7440893 +
                (((999999999999989 % ((
                (pm_index * 2246527 + var * 2399993 + ent * 2100869 + (attr1) * 1918303 + (attr2) * 1624729)
                    % 7450987) * 7580 + 7560584)) * 17669) % 7440893)) * 1343)
                    % 4294967296) + 0.5) / 4294967296

            eq = round(eq, ndigits=round_off)

            values.append(eq)

        return values

