"""
Draft where we solve the problem.
Given the input Payload, compute response
"""

import pprint


def solve(eenput_data):
    PAYLOAD = eenput_data
    LOAD = PAYLOAD["load"]
    result = []

    # ALGORITHM
    # for each power plants,
    # 1. compute the merit order
    # 2. down the merit order, fill the power needed until matching load

    # mapping type ==> fuels
    mapping_type_to_fuel = {
        "gasfired": "gas(euro/MWh)",
        "turbojet": "kerosine(euro/MWh)",
        "windturbine": "wind(%)"
    }

    # array of tuples(name_of_powerplants: price/MWh
    compute_buffer = []

    # 1. compute the merit order
    for powerplant in PAYLOAD["powerplants"]:
        powerplant_name = powerplant["name"]

        if powerplant["type"] is not "windturbine":
            # price of fuel given the type of powerplants
            price_of_fuel = PAYLOAD["fuels"][mapping_type_to_fuel[powerplant["type"]]]

            # new price with efficiency
            new_price = price_of_fuel * 100 / powerplant["efficiency"]
            new_price = "{:.1f}".format(new_price)
            print("Power plant [{0}] new_price with efficiency = {1}".format(powerplant_name, new_price))
            compute_buffer.append((powerplant_name, new_price))
        else:
            # Wind-turbines do not consume 'fuel' and thus are considered to generate power at zero price.
            compute_buffer.append((powerplant_name, 0))

    pprint.pprint(compute_buffer)

    print("Sorting....")

    # we sort according to price
    sorted_results = sorted(compute_buffer, key=lambda element: float(element[1]))
    pprint.pprint(sorted_results)

    current_power = 0

    # 2. down the merit order, fill the power needed until matching load
    for elem in sorted_results:
        powerplant_name = elem[0]
        current_pmax = 0
        for pow_plant in PAYLOAD["powerplants"]:
            if pow_plant["name"] == powerplant_name:
                if pow_plant["type"] == "windturbine":
                    current_pmax = pow_plant["pmax"] * (PAYLOAD["fuels"]["wind(%)"] / 100)
                else:
                    current_pmax = pow_plant["pmax"] * pow_plant["efficiency"]

        if current_pmax + current_power < LOAD:
            # here we add to result
            tmp_dict = {
                "name": powerplant_name,
                "p": "{:.1f}".format(current_pmax)
            }
            result.append(tmp_dict)
            current_power += current_pmax

        elif current_pmax + current_power > LOAD:
            power_lacking = LOAD - current_power
            if power_lacking <= current_pmax:
                # if True we have enough to use from that powerplant
                tmp_dict = {
                    "name": powerplant_name,
                    "p": "{:.1f}".format(power_lacking)
                }
                result.append(tmp_dict)
                current_power += power_lacking

        if current_power == LOAD:
            break

    ##########################################################################################
    # here we finish the reponse array. The p: 0, those that do nothing. Fill the result array
    for powerplant in PAYLOAD["powerplants"]:
        found = False
        for res_powerplant in result:
            if powerplant["name"] == res_powerplant["name"]:
                found = True
                break

        if not found:
            tmp_dict = {
                "name": powerplant["name"],
                "p": 0
            }
            result.append(tmp_dict)

    print("######### Results #########")
    print("Current total POWER = ", current_power)
    pprint.pprint(result)

    return result
