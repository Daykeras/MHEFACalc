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
                        flat_attack_buffs,
                        ):                    
  display_raw = math.floor(
    base_raw * atk_boost_skill[atk_boost_lvl][1] *
    power_sheathe_uptime * power_sheathe_raw[0] +
    atk_boost_skill[atk_boost_lvl][0] +
    dict.get(has_charm_talon) +
    dict.get(flat_attack_buffs)
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

# Attack Buffs
# Assume attack buffs: Might Seed +10, Demon Powder +10, Mega Demondrug +7,
#                      Booster +9

flat_attack_buffs = {
                    'None' : 1,
                    'Booster' : 9,
                    'Full' : 36
                    }

has_charm_talon = {
                  'Neither': 0,
                  'Charm' : 6,
                  'Talon' : 9,
                  'Both': 15
                  }

# Attack Boost 0 - 7
atk_boost_skill = [
        (0, 0),
        (3, 0),
        (6, 0),
        (9, 0),
        (7, 0.05),
        (8, 0.06),
        (9, 0.08),
        (10, 0.10)
]

# For Long Sword only
ls_spirit_raw = [1.0, 1.05, 1.1, 1.2];

# For GS only
power_sheathe_raw = [1.1]

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
crit_boost_skill = [0.25, 0.30, 0.35, 0.40]

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