import math
# IMPORTANT: Displayed numbers in MHR are ROUNDED DOWN.

###############################################################################
# RAW ATTACK CALCULATIONS
###############################################################################

def compute_display_raw(
                        base_raw,
                        atk_boost_lvl,
                        power_sheathe_uptime,                     
                        has_charm_talon,
                        has_attack_buffs,
                        ):                                       
  display_raw =(math.floor(
    base_raw * (1 + atk_boost_skill[atk_boost_lvl][1]) *
    (power_sheathe_uptime * power_sheathe_raw[0] + 1) +
    atk_boost_skill[atk_boost_lvl][0] +
    charm_talon[has_charm_talon] +
    attack_buffs[has_attack_buffs])
  )
  
  return display_raw                    


def compute_crit_chance(
                        base_affinity,
                        wex_lvl,
                        crit_eye_lvl,
                        latent_power_lvl,
                        latent_power_uptime
                       ):
  crit_chance_base = base_affinity + wex_skill[wex_lvl] + crit_eye_skill[crit_eye_lvl]
  
  if(crit_chance_base > 1):
    crit_chance_base = 1
  
  crit_chance_lp = crit_chance_base + latent_power_skill[latent_power_lvl]
  
  if(crit_chance_lp > 1):
    crit_chance_lp = 1
  
  crit_chance = (crit_chance_base * (1 - latent_power_uptime) + 
                crit_chance_lp * (latent_power_uptime))

  return crit_chance

def compute_crit_raw(
                      crit_chance,
                      crit_boost_lvl
                      ):
  if crit_chance < 0:
    crit_raw = (1 + crit_chance) + (- crit_chance * .75)
  else:
    crit_raw = (1 - crit_chance ) + (crit_chance * crit_boost_skill[crit_boost_lvl])

  return crit_raw

def compute_total_raw(weapon,build,params):
  display_raw = compute_display_raw(
    weapon.base_raw,
    build.attack_boost_level,
    params.power_sheathe_uptime,
    params.has_charm_talon,
    params.has_attack_buffs
  )
  crit_chance = compute_crit_chance(
    weapon.base_affinity,
    build.weakness_exploit_level,
    build.critical_eye_level,
    build.latent_power_level,
    params.latent_power_uptime
  )
  crit_raw = compute_crit_raw(
    crit_chance, 
    build.critical_boost_level
  )

  total_raw = display_raw * crit_raw * sharpness_raw[weapon.sharpness_level]

  return total_raw

def compute_display_element(
                      base_element,
                      element_atk_lvl
                      ):
  ele_attack = (base_element * (1 + element_atk_skill[element_atk_lvl][1]) +
      element_atk_skill[element_atk_lvl][0])

  return ele_attack

def compute_crit_ele(
                      crit_chance,
                      crit_element_lvl
                      ):
  if(crit_element_lvl <= 0):
    return 1

  else:
    crit_ele = (1 - crit_chance ) + (crit_chance * crit_element_skill[crit_element_lvl])

  return crit_ele 

def compute_total_ele(weapon,build,params):
  display_element = compute_display_element(
    weapon.base_element,
    build.element_attack_level
  )
  crit_chance = compute_crit_chance(
    weapon.base_affinity,
    build.weakness_exploit_level,
    build.critical_eye_level,
    build.latent_power_level,
    params.latent_power_uptime
  )
  crit_ele = compute_crit_ele(
    crit_chance,
    build.critical_element_level
  )

  total_ele = display_element * crit_ele

  return total_ele


# Attack Buffs
# Assume attack buffs: Might Seed +10, Demon Powder +10, Mega Demondrug +7,
#                      Booster +9

# 0 is no buffs, 1 is Booster, 2 is Booster + MegaDrug + Powder + Seed
attack_buffs = [0, 9, 36]

# 0 is no charm or talon, 1 is charm, 2 is talon, and 3 is both
charm_talon = [0, 6, 9, 15]


# Attack Boost 0 - 7
atk_boost_skill = [
        (0, 0),
        (3, 0),
        (6, 0),
        (9, 0),
        (7, .05),
        (8, .06),
        (9, .08),
        (10, .10)
]

# For Long Sword only
ls_spirit_raw = [1.0, 1.05, 1.1, 1.2];

# For GS only
power_sheathe_raw = [.1]

# 0: Red
# 1: Orange
# 2: Yellow
# 3: Green
# 4: Blue
# 5: White
# 6: Purple
sharpness_raw = [0.50, 0.75, 1.00, 1.05, 1.20, 1.32, 1.39]
sharpness_element = [0.25, 0.50, 0.75, 1.00, 1.0625, 1.15, 1.25]

# Critical boost
# CB 0 - 3
crit_boost_skill = [1.25, 1.30, 1.35, 1.40]

# Critical Eye
# CE 0-7
crit_eye_skill = [0, .05, .10, .15, .20, .25, .30, .40]

# Weakness Exploit
# WEX 0-3
wex_skill = [0, .15, .30, .50]

# Latent Power 0 - 5
latent_power_skill = [0, 0.10, 0.20, 0.30, 0.40, 0.50]

# Critical Element Skill
crit_element_skill = [0.00, 0.05, 0.10, 0.15]

# Element Attack 0 - 5
element_atk_skill = [
        (0, 0),
        (2, 0),
        (3, 0),
        (4, 0.05),
        (4, 0.10),
        (4, 0.20)
]