import calcefa

class obj(object):
    def __init__(self, d):
        self.__dict__ = d

# base raw and affinity are after ramp up
# affinity is percentage as decimal. negative allowed
# sharpness_level =
# # 0: Red
# 1: Orange
# 2: Yellow
# 3: Green
# 4: Blue
# 5: White
# 6: Purple

Dark_of_Night_Attack_Boost_III = obj({
    "base_raw" : 188,
    "base_affinity" : .35,
    "sharpness_level" : 5,
    "base_element" : 0
})

Abominable_Great_Sword_Affinity_Boost_II = obj({
    "base_raw" : 230,
    "base_affinity" : -.09,
    "sharpness_level" : 4,
    "base_element" : 20
})

Tigrex_Great_Sword_Attack_Boost_III = obj({
    "base_raw" : 218,
    "base_affinity" : -.15,
    "sharpness_level" : 5,
    "base_element" : 0 
})


# example usage:

# example usage test:
build1 = obj({
    "attack_boost_level" : 7,
    "weakness_exploit_level" : 3,
    "critical_eye_level" : 3,
    "latent_power_level" : 0,
    "critical_boost_level" : 3,
    "element_attack_level" : 0,
    "critical_element_level" : 0

})

build2 = obj({
    "attack_boost_level" : 4,
    "weakness_exploit_level" : 3,
    "critical_eye_level" : 6,
    "latent_power_level" : 0,
    "critical_boost_level" : 3,
    "element_attack_level" : 5,
    "critical_element_level" : 0
})

build3 = obj({
    "attack_boost_level" : 4,
    "weakness_exploit_level" : 3,
    "critical_eye_level" : 7,
    "latent_power_level" : 0,
    "critical_boost_level" : 3,
    "element_attack_level" : 5,
    "critical_element_level" : 0
})

# has_charm_talon = 0: none, 1: charm, 2: talon, 3: both
# has_attack_buffs = 0: none, 1: booster, 2: booster + megadrug + seed + powder
# uptime is a percentage as a decimal
# hit_zone_ratio is the Elemental HZ / Raw HZ being tested
# elemental_mod_ratio is Ele MOD/ MV of a given run, or estimate
# 1.4 is close to the Olay GS Freestyle Rajang WR
params1 = obj({
    "power_sheathe_uptime" : 0.4,
    "has_charm_talon" : 3,
    "has_attack_buffs" : 2,
    "latent_power_uptime" : .5,
    "maximum_might_uptime" : 0,
    "weak_spot_uptime" : 1,
    "hit_zone_ratio" : 0.0,
    "elemental_mod_ratio" : 1.4
})

#print(mhefacalc.evaluate_build(build1, params_ls1))

# Best weapon
print(calcefa.compute_total_efa(Dark_of_Night_Attack_Boost_III,build1,params1))
print(calcefa.compute_total_efa(Dark_of_Night_Attack_Boost_III,build3,params1))
# 3rd best + ice
print(calcefa.compute_total_efa(Abominable_Great_Sword_Affinity_Boost_II,build2,params1))

print(calcefa.compute_total_efa(Tigrex_Great_Sword_Attack_Boost_III,build3,params1))