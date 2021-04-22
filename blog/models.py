

from django.conf import settings
from django.db import models
from django.utils import timezone



class character(models.Model):

    # description - описание
    character_name = models.TextField()
    worldview = models.TextField()
    nameperson = models.TextField()
    lvlcharacter = models.TextField()
    thedeity = models.TextField()
    homeland = models.TextField()
    race = models.TextField()
    size = models.TextField()
    floor = models.TextField()
    age = models.TextField()
    height = models.TextField()
    weight = models.TextField()
    hair = models.TextField()
    eye = models.TextField()
    # abilities - характеристики
    srtength_ability_score = models.TextField()
    srtength_ability_modifier = models.TextField()
    srtength_temp_adjustment = models.TextField()
    srtength_temp_modifier = models.TextField()
    dexterity_ability_score = models.TextField()
    dexterity_ability_modifier = models.TextField()
    dexterity_temp_adjustment = models.TextField()
    dexterity_temp_modifier = models.TextField()
    constitution_ability_score = models.TextField()
    constitution_ability_modifier = models.TextField()
    constitution_temp_adjustment = models.TextField()
    constitution_temp_modifier = models.TextField()
    intelligence_ability_score = models.TextField()
    intelligence_ability_modifier = models.TextField()
    intelligence_temp_adjustment = models.TextField()
    intelligence_temp_modifier = models.TextField()
    wisdom_ability_score = models.TextField()
    wisdom_ability_modifier = models.TextField()
    wisdom_temp_adjustment = models.TextField()
    wisdom_temp_modifier = models.TextField()
    charisma_ability_score = models.TextField()
    charisma_ability_modifier = models.TextField()
    charisma_temp_adjustment = models.TextField()
    charisma_temp_modifier = models.TextField()
    # armor-класс брони
    armor_class_total = models.TextField()
    armor_class_bonus = models.TextField()
    armor_class_shield_bonus = models.TextField()
    armor_class_dex_modifier = models.TextField()
    armor_class_size_modifier = models.TextField()
    armor_class_natural_armor = models.TextField()
    armor_class_deflection_modifier = models.TextField()
    armor_class_misc_modifier = models.TextField()
    touch_armor_class = models.TextField()
    flat_footed_armor_class = models.TextField()
    armor_class_modifier = models.TextField()
    # HP - здоровье
    hit_points_total = models.TextField()
    hit_points_damage_reduction = models.TextField()
    hit_points_wounds_current_HP = models.TextField()
    hit_points_nonlethal_damage = models.TextField()
    # инициативы
    initiative_modifier_total = models.TextField()
    initiative_modifier_dex_modifier = models.TextField()
    initiative_modifier_misc_modifier = models.TextField()
    # наземная скорость
    speed_land_base_speed_FT_SQ = models.TextField()
    speed_land_with_armor_FT_SQ = models.TextField()
    speed_land_fly_FT = models.TextField()
    speed_land_maneuverability_FT = models.TextField()
    speed_land_swim_FT = models.TextField()
    speed_land_climb_FT = models.TextField()
    speed_land_burrow_FT = models.TextField()
    speed_land_temp_modifiers = models.TextField()
    # испытания
    fortitude_total = models.TextField()  # стойкость
    fortitude_base_save = models.TextField()  # стойкость
    fortitude_ability_modifier = models.TextField()  # стойкость
    fortitude_magic_modifier = models.TextField()  # стойкость
    fortitude_misc_modifier = models.TextField()  # стойкость
    fortitude_temporary_modifier = models.TextField()  # стойкость
    reflex_total = models.TextField()  # реакция
    reflex_base_save = models.TextField()  # реакция
    reflex_ability_modifier = models.TextField()  # реакция
    reflex_magic_modifier = models.TextField()  # реакция
    reflex_misc_modifier = models.TextField()  # реакция
    reflex_temporary_modifier = models.TextField()  # реакция
    will_total = models.TextField()  # воля
    will_base_save = models.TextField()  # воля
    will_ability_modifier = models.TextField()  # воля
    will_magic_modifier = models.TextField()  # воля
    will_misc_modifier = models.TextField()  # воля
    will_temporary_modifier = models.TextField()  # воля
    saving_throws_modifier = models.TextField()  # общая модель для всех испытаний
    # other
    base_attack_bonus = models.TextField()
    spell_resistance = models.TextField()
    # cmb
    cmb_total = models.TextField()
    cmb_base_attack_bonus = models.TextField()
    cmb_strength_modifier = models.TextField()
    cmb_size_modifier = models.TextField()
    cmb_modifier = models.TextField()
    # cmd
    cmd_total = models.TextField()
    cmd_base_attack_bonus = models.TextField()
    cmd_strength_modifier = models.TextField()
    cmd_dexterity_modifier = models.TextField()
    cmd_size_modifier = models.TextField()
    # weapon_one
    weapon_one_name = models.TextField()
    weapon_one_attack_bonus = models.TextField()
    weapon_one_critical = models.TextField()
    weapon_one_type = models.TextField()
    weapon_one_range = models.TextField()
    weapon_one_ammunition = models.TextField()
    weapon_one_damage = models.TextField()
    # weapon_two
    weapon_two_name = models.TextField()
    weapon_two_attack_bonus = models.TextField()
    weapon_two_critical = models.TextField()
    weapon_two_type = models.TextField()
    weapon_two_range = models.TextField()
    weapon_two_ammunition = models.TextField()
    weapon_two_damage = models.TextField()
    # weapon_three
    weapon_three_name = models.TextField()
    weapon_three_attack_bonus = models.TextField()
    weapon_three_critical = models.TextField()
    weapon_three_type = models.TextField()
    weapon_three_range = models.TextField()
    weapon_three_ammunition = models.TextField()
    weapon_three_damage = models.TextField()
    # weapon_four
    weapon_four_name = models.TextField()
    weapon_four_attack_bonus = models.TextField()
    weapon_four_critical = models.TextField()
    weapon_four_type = models.TextField()
    weapon_four_range = models.TextField()
    weapon_four_ammunition = models.TextField()
    weapon_four_damage = models.TextField()
    # weapon_five
    weapon_five_name = models.TextField()
    weapon_five_attack_bonus = models.TextField()
    weapon_five_critical = models.TextField()
    weapon_five_type = models.TextField()
    weapon_five_range = models.TextField()
    weapon_five_ammunition = models.TextField()
    weapon_five_damage = models.TextField()
    # skills
    skill_acrobatics_total_bonus = models.TextField()  # 1
    skill_acrobatics_ranks = models.TextField()
    skill_acrobatics_misc_mod = models.TextField()
    skill_acrobatics_class_skill = models.TextField()
    skill_acrobatics_trained_only = models.TextField()
    skill_appraise_total_bonus = models.TextField()  # 2
    skill_appraise_ranks = models.TextField()
    skill_appraise_misc_mod = models.TextField()
    skill_appraise_class_skill = models.TextField()
    skill_appraise_trained_only = models.TextField()
    skill_bluff_total_bonus = models.TextField()  # 3
    skill_bluff_ranks = models.TextField()
    skill_bluff_misc_mod = models.TextField()
    skill_bluff_class_skill = models.TextField()
    skill_bluff_trained_only = models.TextField()
    skill_climb_total_bonus = models.TextField()  # 4
    skill_climb_ranks = models.TextField()
    skill_climb_misc_mod = models.TextField()
    skill_climb_class_skill = models.TextField()
    skill_climb_trained_only = models.TextField()
    skill_craft_one_total_bonus = models.TextField()  # 5
    skill_craft_one_ranks = models.TextField()
    skill_craft_one_misc_mod = models.TextField()
    skill_craft_one_class_skill = models.TextField()
    skill_craft_one_trained_only = models.TextField()
    skill_craft_two_total_bonus = models.TextField()  # 6
    skill_craft_two_ranks = models.TextField()
    skill_craft_two_misc_mod = models.TextField()
    skill_craft_two_class_skill = models.TextField()
    skill_craft_two_trained_only = models.TextField()
    skill_craft_three_total_bonus = models.TextField()  # 7
    skill_craft_three_ranks = models.TextField()
    skill_craft_three_misc_mod = models.TextField()
    skill_craft_three_class_skill = models.TextField()
    skill_craft_three_trained_only = models.TextField()
    skill_diplomacy_total_bonus = models.TextField()  # 8
    skill_diplomacy_ranks = models.TextField()
    skill_diplomacy_misc_mod = models.TextField()
    skill_diplomacy_class_skill = models.TextField()
    skill_diplomacy_trained_only = models.TextField()
    skill_disable_device_total_bonus = models.TextField()  # 9
    skill_disable_device_ranks = models.TextField()
    skill_disable_device_misc_mod = models.TextField()
    skill_disable_device_class_skill = models.TextField()
    skill_disable_device_trained_only = models.TextField()
    skill_disguese_total_bonus = models.TextField()  # 10
    skill_disguese_ranks = models.TextField()
    skill_disguese_misc_mod = models.TextField()
    skill_disguese_class_skill = models.TextField()
    skill_disguese_trained_only = models.TextField()
    skill_escape_artist_total_bonus = models.TextField()  # 11
    skill_escape_artist_ranks = models.TextField()
    skill_escape_artist_misc_mod = models.TextField()
    skill_escape_artist_class_skill = models.TextField()
    skill_escape_artist_trained_only = models.TextField()
    skill_fly_total_bonus = models.TextField()  # 12
    skill_fly_ranks = models.TextField()
    skill_fly_misc_mod = models.TextField()
    skill_fly_class_skill = models.TextField()
    skill_fly_trained_only = models.TextField()
    skill_handle_animal_total_bonus = models.TextField()  # 13
    skill_handle_animal_ranks = models.TextField()
    skill_handle_animal_misc_mod = models.TextField()
    skill_handle_animal_class_skill = models.TextField()
    skill_handle_animal_trained_only = models.TextField()
    skill_heal_total_bonus = models.TextField()  # 14
    skill_heal_ranks = models.TextField()
    skill_heal_misc_mod = models.TextField()
    skill_heal_class_skill = models.TextField()
    skill_heal_trained_only = models.TextField()
    skill_intimidate_total_bonus = models.TextField()  # 15
    skill_intimidate_ranks = models.TextField()
    skill_intimidate_misc_mod = models.TextField()
    skill_intimidate_class_skill = models.TextField()
    skill_intimidate_trained_only = models.TextField()
    # knowledge
    skill_arcana_total_bonus = models.TextField()  # 16
    skill_arcana_ranks = models.TextField()
    skill_arcana_misc_mod = models.TextField()
    skill_arcana_class_skill = models.TextField()
    skill_arcana_trained_only = models.TextField()
    skill_dungeoneering_total_bonus = models.TextField()  # 17
    skill_dungeoneering_ranks = models.TextField()
    skill_dungeoneering_misc_mod = models.TextField()
    skill_dungeoneering_class_skill = models.TextField()
    skill_dungeoneering_trained_only = models.TextField()
    skill_engineering_total_bonus = models.TextField()  # 18
    skill_engineering_ranks = models.TextField()
    skill_engineering_misc_mod = models.TextField()
    skill_engineering_class_skill = models.TextField()
    skill_engineering_trained_only = models.TextField()
    skill_geography_total_bonus = models.TextField()  # 19
    skill_geography_ranks = models.TextField()
    skill_geography_misc_mod = models.TextField()
    skill_geography_class_skill = models.TextField()
    skill_geography_trained_only = models.TextField()
    skill_history_total_bonus = models.TextField()  # 20
    skill_history_ranks = models.TextField()
    skill_history_misc_mod = models.TextField()
    skill_history_class_skill = models.TextField()
    skill_history_trained_only = models.TextField()
    skill_local_total_bonus = models.TextField()  # 21
    skill_local_ranks = models.TextField()
    skill_local_misc_mod = models.TextField()
    skill_local_class_skill = models.TextField()
    skill_local_trained_only = models.TextField()
    skill_nature_total_bonus = models.TextField()  # 22
    skill_nature_ranks = models.TextField()
    skill_nature_misc_mod = models.TextField()
    skill_nature_class_skill = models.TextField()
    skill_nature_trained_only = models.TextField()
    skill_nobility_total_bonus = models.TextField()  # 23
    skill_nobility_ranks = models.TextField()
    skill_nobility_misc_mod = models.TextField()
    skill_nobility_class_skill = models.TextField()
    skill_nobility_trained_only = models.TextField()
    skill_planes_total_bonus = models.TextField()  # 24
    skill_planes_ranks = models.TextField()
    skill_planes_misc_mod = models.TextField()
    skill_planes_class_skill = models.TextField()
    skill_planes_trained_only = models.TextField()
    skill_religion_total_bonus = models.TextField()  # 25
    skill_religion_ranks = models.TextField()
    skill_religion_misc_mod = models.TextField()
    skill_religion_class_skill = models.TextField()
    skill_religion_trained_only = models.TextField()
    # скилы после knowledge
    skill_linguistics_total_bonus = models.TextField()  # 26
    skill_linguistics_ranks = models.TextField()
    skill_linguistics_misc_mod = models.TextField()
    skill_linguistics_class_skill = models.TextField()
    skill_linguistics_trained_only = models.TextField()
    skill_perception_total_bonus = models.TextField()  # 27
    skill_perception_ranks = models.TextField()
    skill_perception_misc_mod = models.TextField()
    skill_perception_class_skill = models.TextField()
    skill_perception_trained_only = models.TextField()
    skill_perform_one_total_bonus = models.TextField()  # 28  тут еще есть строка которую нужно заполнить, я не сделал доп модель для неё
    skill_perform_one_ranks = models.TextField()
    skill_perform_one_misc_mod = models.TextField()
    skill_perform_one_class_skill = models.TextField()
    skill_perform_one_trained_only = models.TextField()
    skill_perform_two_total_bonus = models.TextField()  # 29  тут еще есть строка которую нужно заполнить, я не сделал доп модель для неё
    skill_perform_two_ranks = models.TextField()
    skill_perform_two_misc_mod = models.TextField()
    skill_perform_two_class_skill = models.TextField()
    skill_perform_two_trained_only = models.TextField()
    skill_profession_one_total_bonus = models.TextField()  # 30 тут еще есть строка которую нужно заполнить, я не сделал доп модель для неё
    skill_profession_one_ranks = models.TextField()
    skill_profession_one_misc_mod = models.TextField()
    skill_profession_one_class_skill = models.TextField()
    skill_profession_one_trained_only = models.TextField()
    skill_profession_two_total_bonus = models.TextField()  # 31 тут еще есть строка которую нужно заполнить, я не сделал доп модель для неё
    skill_profession_two_ranks = models.TextField()
    skill_profession_two_misc_mod = models.TextField()
    skill_profession_two_class_skill = models.TextField()
    skill_profession_two_trained_only = models.TextField()
    skill_ride_total_bonus = models.TextField()  # 32
    skill_ride_ranks = models.TextField()
    skill_ride_misc_mod = models.TextField()
    skill_ride_class_skill = models.TextField()
    skill_ride_trained_only = models.TextField()
    skill_sense_motive_total_bonus = models.TextField()  # 33
    skill_sense_ranks = models.TextField()
    skill_sense_misc_mod = models.TextField()
    skill_sense_class_skill = models.TextField()
    skill_sense_trained_only = models.TextField()
    skill_sleight_of_hand_total_bonus = models.TextField()  # 33
    skill_sleight_of_hand_ranks = models.TextField()
    skill_sleight_of_hand_misc_mod = models.TextField()
    skill_sleight_of_hand_class_skill = models.TextField()
    skill_sleight_of_hand_trained_only = models.TextField()
    skill_spellcraft_total_bonus = models.TextField()  # 34
    skill_spellcraft_ranks = models.TextField()
    skill_spellcraft_misc_mod = models.TextField()
    skill_spellcraft_class_skill = models.TextField()
    skill_spellcraft_trained_only = models.TextField()
    skill_stealth_total_bonus = models.TextField()  # 35
    skill_stealth_ranks = models.TextField()
    skill_stealth_misc_mod = models.TextField()
    skill_stealth_class_skill = models.TextField()
    skill_stealth_trained_only = models.TextField()
    skill_survival_total_bonus = models.TextField()  # 36
    skill_survival_ranks = models.TextField()
    skill_survival_misc_mod = models.TextField()
    skill_survival_class_skill = models.TextField()
    skill_survival_trained_only = models.TextField()
    skill_swim_total_bonus = models.TextField()  # 37
    skill_swim_ranks = models.TextField()
    skill_swim_misc_mod = models.TextField()
    skill_swim_class_skill = models.TextField()
    skill_swim_trained_only = models.TextField()
    skill_use_magic_device_total_bonus = models.TextField()  # 37
    skill_use_magic_device_ranks = models.TextField()
    skill_use_magic_device_misc_mod = models.TextField()
    skill_use_magic_device_class_skill = models.TextField()
    skill_use_magic_device_trained_only = models.TextField()

    # предметы
    ac_items_one = models.TextField()
    ac_items_two = models.TextField()
    ac_items_three = models.TextField()
    ac_items_four = models.TextField()
    ac_items_five = models.TextField()
    # bonus
    bonus_one = models.TextField()
    bonus_two = models.TextField()
    bonus_three = models.TextField()
    bonus_four = models.TextField()
    bonus_five = models.TextField()
    bonus_totals = models.TextField()
    # type
    type_one = models.TextField()
    type_two = models.TextField()
    type_three = models.TextField()
    type_four = models.TextField()
    type_five = models.TextField()
    type_totals = models.TextField()
    # check_penalty
    check_penalty_one = models.TextField()
    check_penalty_two = models.TextField()
    check_penalty_three = models.TextField()
    check_penalty_four = models.TextField()
    check_penalty_five = models.TextField()
    check_penalty_totals = models.TextField()
    # spell_failure
    spell_failure_one = models.TextField()
    spell_failure_two = models.TextField()
    spell_failure_three = models.TextField()
    spell_failure_four = models.TextField()
    spell_failure_five = models.TextField()
    spell_failure_totals = models.TextField()
    # weight
    weight_one = models.TextField()
    weight_two = models.TextField()
    weight_three = models.TextField()
    weight_four = models.TextField()
    weight_five = models.TextField()
    weight_totals = models.TextField()
    light_load =  models.TextField()
    middle_load =  models.TextField()
    big_load =  models.TextField()
    raise_overhead =  models.TextField()
    tear_off_the_ground = models.TextField()
    push_or_drag = models.TextField()
    # properties
    properties_one = models.TextField()
    properties_two = models.TextField()
    properties_three = models.TextField()
    properties_four = models.TextField()
    properties_five = models.TextField()
    properties_totals = models.TextField()
    # feats
    feats_1 = models.TextField()
    feats_2 = models.TextField()
    feats_3 = models.TextField()
    feats_4 = models.TextField()
    feats_5 = models.TextField()
    feats_6 = models.TextField()
    feats_7 = models.TextField()
    feats_8 = models.TextField()
    feats_9 = models.TextField()
    feats_10 = models.TextField()
    feats_11 = models.TextField()
    feats_12 = models.TextField()
    feats_13 = models.TextField()
    feats_14 = models.TextField()
    # special_abilities
    special_abilities = models.TextField()
    special_abilities_1 = models.TextField()
    special_abilities_2 = models.TextField()
    special_abilities_3 = models.TextField()
    special_abilities_4 = models.TextField()
    special_abilities_5 = models.TextField()
    special_abilities_6 = models.TextField()
    special_abilities_7 = models.TextField()
    special_abilities_8 = models.TextField()
    special_abilities_9 = models.TextField()
    special_abilities_10 = models.TextField()
    special_abilities_11 = models.TextField()
    special_abilities_12 = models.TextField()
    special_abilities_13 = models.TextField()
    special_abilities_14 = models.TextField()
    special_abilities_15 = models.TextField()
    special_abilities_16 = models.TextField()
    special_abilities_17 = models.TextField()
    special_abilities_18 = models.TextField()
    special_abilities_19 = models.TextField()
    special_abilities_20 = models.TextField()
    special_abilities_21 = models.TextField()
    special_abilities_22 = models.TextField()
    special_abilities_23 = models.TextField()
    special_abilities_24 = models.TextField()
    special_abilities_25 = models.TextField()
    special_abilities_26 = models.TextField()
    # spells
    # lvl0
    spells_known_lvl0 = models.TextField()
    spell_save_dc_lvl0 = models.TextField()
    spells_per_day_lvl0 = models.TextField()
    spells_bonus_lvl0 = models.IntegerField()
    # lvl1
    spells_known_lvl1 = models.TextField()
    spell_save_dc_lvl1 = models.TextField()
    spells_per_day_lvl1 = models.TextField()
    spells_bonus_lvl1 = models.TextField()
    # lvl2
    spells_known_lvl2 = models.TextField()
    spell_save_dc_lvl2 = models.TextField()
    spells_per_day_lvl2 = models.TextField()
    spells_bonus_lvl2 = models.TextField()
    # lvl3
    spells_known_lvl3 = models.TextField()
    spell_save_dc_lvl3 = models.TextField()
    spells_per_day_lvl3 = models.TextField()
    spells_bonus_lvl3 = models.TextField()
    # lvl4
    spells_known_lvl4 = models.TextField()
    spell_save_dc_lvl4 = models.TextField()
    spells_per_day_lvl4 = models.TextField()
    spells_bonus_lvl4 = models.TextField()
    # lvl5
    spells_known_lvl5 = models.TextField()
    spell_save_dc_lvl5 = models.TextField()
    spells_per_day_lvl5 = models.TextField()
    spells_bonus_lvl5 = models.TextField()
    # lvl6
    spells_known_lvl6 = models.TextField()
    spell_save_dc_lvl6 = models.TextField()
    spells_per_day_lvl6 = models.TextField()
    spells_bonus_lvl6 = models.TextField()
    # lvl7
    spells_known_lvl7 = models.TextField()
    spell_save_dc_lvl7 = models.TextField()
    spells_per_day_lvl7 = models.TextField()
    spells_bonus_lvl7 = models.TextField()
    # lvl8
    spells_known_lvl8 = models.TextField()
    spell_save_dc_lvl8 = models.TextField()
    spells_per_day_lvl8 = models.TextField()
    spells_bonus_lvl8 = models.TextField()
    # lvl9
    spells_known_lvl9 = models.TextField()
    spell_save_dc_lvl9 = models.TextField()
    spells_per_day_lvl9 = models.TextField()
    spells_bonus_lvl9 = models.TextField()
    conditional_modifiers = models.TextField()
    #spheres/specializations_sсhool
    Circumstance_modifiers = models.TextField()
    #School_of_Incarnation-0
    School_of_Incarnation_1 = models.TextField()
    School_of_Incarnation_2 = models.TextField()
    School_of_Incarnation_3 = models.TextField()
    School_of_Incarnation_4 = models.TextField()
    School_of_Incarnation_5 = models.TextField()
    School_of_Incarnation_6 = models.TextField()
    School_of_Incarnation_7 = models.TextField()
    School_of_Incarnation_8 = models.TextField()
    #School_of_illusion-1
    School_of_illusion_1 = models.TextField()
    School_of_illusion_2 = models.TextField()
    School_of_illusion_3 = models.TextField()
    School_of_illusion_4 = models.TextField()
    School_of_illusion_5 = models.TextField()
    School_of_illusion_6 = models.TextField()
    School_of_illusion_7 = models.TextField()
    School_of_illusion_8 = models.TextField()
    #School_of_Necromancy-2
    School_of_Necromancy_1 = models.TextField()
    School_of_Necromancy_2 = models.TextField()
    School_of_Necromancy_3 = models.TextField()
    School_of_Necromancy_4 = models.TextField()
    School_of_Necromancy_5 = models.TextField()
    School_of_Necromancy_6 = models.TextField()
    School_of_Necromancy_7 = models.TextField()
    School_of_Necromancy_8 = models.TextField()
    #School_of_charm-3
    School_of_charm_1 = models.TextField()
    School_of_charm_2 = models.TextField()
    School_of_charm_3 = models.TextField()
    School_of_charm_4 = models.TextField()
    School_of_charm_5 = models.TextField()
    School_of_charm_6 = models.TextField()
    School_of_charm_7 = models.TextField()
    School_of_charm_8 = models.TextField()
    #School_of_transformation
    School_of_transformation_1 = models.TextField()
    School_of_transformation_2 = models.TextField()
    School_of_transformation_3 = models.TextField()
    School_of_transformation_4 = models.TextField()
    School_of_transformation_5 = models.TextField()
    School_of_transformation_6 = models.TextField()
    School_of_transformation_7 = models.TextField()
    School_of_transformation_8 = models.TextField()
    #Obstruction_school
    Obstruction_school_1 = models.TextField()
    Obstruction_school_2 = models.TextField()
    Obstruction_school_3 = models.TextField()
    Obstruction_school_4 = models.TextField()
    Obstruction_school_5 = models.TextField()
    Obstruction_school_6 = models.TextField()
    Obstruction_school_7 = models.TextField()
    Obstruction_school_8 = models.TextField()
    #School_of_Divination
    School_of_Divination_1 = models.TextField()
    School_of_Divination_2 = models.TextField()
    School_of_Divination_3 = models.TextField()
    School_of_Divination_4 = models.TextField()
    School_of_Divination_5 = models.TextField()
    School_of_Divination_6 = models.TextField()
    School_of_Divination_7 = models.TextField()
    School_of_Divination_8 = models.TextField()
    #School_of_destruction
    School_of_destruction_1 = models.TextField()
    School_of_destruction_2 = models.TextField()
    School_of_destruction_3 = models.TextField()
    School_of_destruction_4 = models.TextField()
    School_of_destruction_5 = models.TextField()
    School_of_destruction_6 = models.TextField()
    School_of_destruction_7 = models.TextField()
    School_of_destruction_8 = models.TextField()
    #School_of_Universalism
    School_of_Universalism_1 = models.TextField()
    School_of_Universalism_2 = models.TextField()
    School_of_Universalism_3 = models.TextField()
    School_of_Universalism_4 = models.TextField()
    School_of_Universalism_5 = models.TextField()
    School_of_Universalism_6 = models.TextField()
    School_of_Universalism_7 = models.TextField()
    School_of_Universalism_8 = models.TextField()
    #money
    money_MM = models.TextField()
    money_CM = models.TextField()
    money_3M =  models.TextField()
    money_PM =  models.TextField()
    experience =  models.TextField()
    following_experience =  models.TextField()

