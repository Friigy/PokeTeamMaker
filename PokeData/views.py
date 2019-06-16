from django.shortcuts import render

from .models import *

import csv
import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


def index(request):
    context = { 'message' : PROJECT_ROOT, }

    return render(request, "PokeData/index.html", context)

def parsePokeCSV(request):
    # Contest Types
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/contest_types.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        ContestType(id=int(row['id']), 
                    identifier=row['identifier']).save()

    # Move Damage Class
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/move_damage_classes.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        MoveDamageClass(id=int(row['id']),
                        identifier=row['identifier']).save()

    # Stat
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/stats.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        print(row['identifier'])
        print(row['damage_class_id'])
        Stat(   id=int(row['id']),
                damageClassId=None if row['damage_class_id'] == '' else MoveDamageClass.objects.get(id=int(row['damage_class_id'])),
                identifier=row['identifier'],
                isBattleOnly=row['is_battle_only'],
                gameIndex=None if row['game_index'] == '' else int(row['game_index'])).save()

    # Characteristic
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/characteristics.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        Characteristic( id=int(row['id']),
                        statId=Stat.objects.get(id=int(row['stat_id'])),
                        geneMod5=row['gene_mod_5']).save()
    
    # Berry Firmness
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/berry_firmness.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        BerryFirmness(  id=int(row['id']),
                        identifier=row['identifier']).save()
    
    # Item Fling Effect
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/item_fling_effects.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        ItemFlingEffect(id=int(row['id']),
                        identifier=row['identifier']).save()
    
    # Item Pocket
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/item_pockets.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        ItemPocket( id=int(row['id']),
                    identifier=row['identifier']).save()
    
    # Item Category
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/item_categories.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        ItemCategory(   id=int(row['id']),
                        pocketId=ItemPocket.objects.get(id=int(row['pocket_id'])),
                        identifier=row['identifier']).save()
    
    # Item
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/items.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        Item(   id=int(row['id']),
                identifier=row['identifier'],
                categoryId=ItemCategory.objects.get(id=int(row['category_id'])),
                cost=row['cost'],
                flingPower=None if row['fling_power'] == '' else int(row['fling_power']),
                flingEffectId=None if row['fling_effect_id'] == '' else ItemFlingEffect.objects.get(id=int(row['fling_effect_id']))).save()
    
    # Language
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/languages.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        Language(   id=int(row['id']),
                    iso639=row['iso639'],
                    iso3166=row['iso3166'],
                    identifier=row['identifier'],
                    official=row['official'],
                    order=row['order']).save()
    
    # Region
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/regions.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        Region(id=int(row['id']), identifier=row['identifier']).save()

    # Generation
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/generations.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        Generation( id=int(row['id']),
                    mainRegionId=Region.objects.get(id=int(row['main_region_id'])),
                    identifier=row['identifier']).save()
    
    # Type
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/types.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        Type(   id=int(row['id']),
                identifier=row['identifier'],
                generationId=Generation.objects.get(id=int(row['generation_id'])),
                damageClassId=None if row['damage_class_id'] == '' else MoveDamageClass.objects.get(id=int(row['damage_class_id']))).save()
    
    # VersionGroup
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/version_groups.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        VersionGroup(id=int(row['id']), identifier=row['identifier'], generationId=Generation.objects.get(id=int(row['generation_id'])), order=row['order']).save()
    
    # Ability
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/abilities.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        Ability(id=int(row['id']), identifier=row['identifier'], generationId=Generation.objects.get(id=int(row['generation_id']))).save()
    
    # AbilityChangelog
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/ability_changelog.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        AbilityChangelog(   id=int(row['id']), 
                            abilityId=Ability.objects.get(id=int(row['ability_id'])),
                            changedInVersionGroupId=VersionGroup.objects.get(id=int(row['changed_in_version_group_id']))).save()
    
    # AbilityChangelogProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/ability_changelog_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        AbilityChangelogProse(  abilityChangelogId=AbilityChangelog.objects.get(id=int(row['ability_changelog_id'])), 
                                localLanguageId=Language.objects.get(id=int(row['local_language_id'])),
                                effect=row['effect']).save()
    
    # AbilityFlavorText
    ''' broken CSV
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/ability_flavor_text.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        AbilityFlavorText(  abilityId=Ability.objects.get(id=int(row['ability_id'])),
                            versionGroupdId=VersionGroup.objects.get(id=int(row['version_group_id'])),
                            languageId=Language.objects.get(id=int(row['language_id'])),
                            flavorText=row['flavor_text']).save()
    '''
    # AbilityName
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/ability_names.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        AbilityName(abilityId=Ability.objects.get(id=int(row['ability_id'])),
                    localLanguageId=Language.objects.get(id=int(row['local_language_id'])),
                    name=row['name']).save()
    
    # AbilityProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/ability_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        AbilityProse(abilityId=Ability.objects.get(id=int(row['ability_id'])), localLanguageId=Language.objects.get(id=int(row['local_language_id'])), shortEffect=row['short_effect']).save()
    
    # Berry
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/berries.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        Berry(  id=int(row['id']),
                itemId=Item.objects.get(id=int(row['item_id'])),
                firmnessId=BerryFirmness.objects.get(id=int(row['firmness_id'])),
                naturalGiftPower=row['natural_gift_power'],
                naturalGiftTypeId=Type.objects.get(id=int(row['natural_gift_type_id'])),
                size=row['size'], 
                maxHarvest=row['max_harvest'],
                growthTime=row['growth_time'],
                soilDryness=row['soil_dryness'],
                smoothness=row['smoothness']).save()
    
    # BeryFirmnessName
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/berry_firmness_names.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        BerryFirmnessName(  berryFirmnessId=BerryFirmness.objects.get(id=int(row['berry_firmness_id'])),
                            localLanguageId=Language.objects.get(id=int(row['local_language_id'])),
                            name=row['name']).save()
    
    # BerryFlavor
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/berry_flavors.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        BerryFlavor(berryId=Berry.objects.get(id=int(row['berry_id'])),
                    contestTypeId=ContestType.objects.get(id=int(row['contest_type_id'])),
                    flavor=row['flavor']).save()
    
    # CharacteristicText
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/characteristic_text.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        CharacteristicText( characteristicId=Characteristic.objects.get(id=int(row['characteristic_id'])),
                            localLanguageId=Language.objects.get(id=int(row['local_language_id'])),
                            message=row['message']).save()
    
    # EvolutionChain
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/evolution_chains.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        EvolutionChain( id=int(row['id']),
                        babyTriggerItemId=None if row['baby_trigger_item_id'] == '' else Item.objects.get(id=int(row['baby_trigger_item_id']))).save()
    
    # PokemonColor
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_colors.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonColor(id=int(row['id']), identifier=row['identifier']).save()
    
    # PokemonShape
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_shapes.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonShape(id=int(row['id']), identifier=row['identifier']).save()
    
    # PokemonHabitat
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_habitats.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonHabitat(id=int(row['id']), identifier=row['identifier']).save()
    
    # GrowthRate
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/growth_rates.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        GrowthRate(id=int(row['id']), identifier=row['identifier'], formula=row['formula']).save()
    
    # PokemonSpecies
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_species.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonSpecies( id=int(row['id']),
                        identifier=row['identifier'],
                        evolvesFromSpeciesId=None if row['evolves_from_species_id'] == '' else PokemonSpecies.objects.get(id=int(row['evolves_from_species_id'])),
                        evolutionChainId=EvolutionChain.objects.get(id=int(row['evolution_chain_id'])),
                        colorId=PokemonColor.objects.get(id=int(row['color_id'])),
                        shapeId=PokemonShape.objects.get(id=int(row['shape_id'])),
                        habitatId=PokemonHabitat.objects.get(id=int(row['habitat_id'])),
                        genderRate=row['gender_rate'],
                        captureRate=row['capture_rate'],
                        baseHappiness=row['base_happiness'],
                        isBaby=row['is_baby'],
                        hatchCounter=row['hatch_counter'],
                        hasGenderDifferences=row['has_gender_differences'],
                        growthRateId=GrowthRate.objects.get(id=int(row['growth_rate_id'])),
                        formsSwitchable=row['forms_switchable'],
                        order=row['order']).save()
    
    # Pokemon
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        Pokemon(id=int(row['id']), identifier=row['identifier'], speciesId=PokemonSpecies.objects.get(id=int(row['species_id'])), height=row['height'], weight=row['weight'], baseExperience=row['base_experience'], order=row['order'], isDefault=row['is_default']).save()
    
    # MoveEffect
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/move_effects.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        MoveEffect(id=int(row['id'])).save()
    
    # ContestEffect
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/contest_effects.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        ContestEffect(id=int(row['id']), appeal=row['appeal'], jam=row['jam']).save()
    
    # SuperContestEffect
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/super_contest_effects.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        SuperContestEffect(id=int(row['id']), appeal=row['appeal']).save()

    # MoveTarget
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/move_targets.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        MoveTarget(id=int(row['id']), identifier=row['identifier']).save()
    
    # Move
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/moves.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        Move(id=int(row['id']), identifier=row['identifier'], generationId=Generation.objects.get(id=int(row['generation_id'])), typeId=row['type_id'], power=row['power'], pp=row['pp'], accuracy=row['accuracy'], targetId=row['target_id'], damageClassId=int(row['damage_class_id']), effect=row['effect_id'], effectChance=row['effect_chance'], contestTypeId=ContestType.objects.get(id=int(row['contest_type_id'])), contestEffectId=row['contest_effect_id'], superContestEffectId=row['super_contest_effect_id']).save()
    
    # ContestCombo
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/contest_combos.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        ContestCombo(firstMoveId=row['first_move_id'], secondMoveId=row['second_move_id']).save()
    
    # ContestEffectProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/contest_effect_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        ContestEffectProse(contestEffectId=row['contest_effect_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), flavorText=['flavor_text'], effect=row['effect']).save()
    
    # ContestTypeName
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/contest_type_names.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        ContestTypeName(contestTypeId=ContestType.objects.get(id=int(row['contest_type_id'])), localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name'], flavor=row['flavor'], color=row['color']).save()
    
    # EggGroup
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/egg_groups.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        EggGroup(id=int(row['id']), identifier=row['identifier']).save()
    
    # EggGroupProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/egg_group_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        EggGroupProse(eggGroupId=row['egg_group_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name']).save()
    
    # EncounterCondition
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/encounter_conditions.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        EncounterCondition(id=int(row['id']), identifier=row['identifier']).save()
    
    # EncounterConditionProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/encounter_condition_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        EncounterConditionProse(encounterConditionId=row['encounter_condition_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name']).save()
    
    # Version
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/versions.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        Version(id=int(row['id']), versionGroupId=VersionGroup.objects.get(id=int(row['version_group_id'])), identifier=row['identifier']).save()
    
    # Location
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/locations.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        Location(   id=int(row['id']), 
                    regionId=Region.objects.get(id=int(row['region_id']),
                    identifier=row['identifier'])).save()
    
    # LocationArea
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/location_areas.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        LocationArea(id=int(row['id']), locationId=row['location_id'], gameIndex=None if row['game_index'] == '' else int(row['game_index']), identifier=row['identifier']).save()
    
    # EncounterMethod
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/encounter_methods.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        EncounterMethod(id=int(row['id']), identifier=row['identifier'], order=row['order']).save()
    
    # EncounterSlot
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/encounter_slots.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        EncounterSlot(id=int(row['id']), versionGroupId=VersionGroup.objects.get(id=int(row['version_group_id'])), encounterMethodId=row['encounter_method_id'], slot=row['slot'], rarity=row['rarity']).save()
    
    # Encounter
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/encounters.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        Encounter(id=int(row['id']), versionId=row['version_id'], locationAreaId=row['location_area_id'], encounterSlotId=row['encounter_slot_id'], pokemonId=row['pokemon_id'], minLevel=row['min_level'], maxLevel=row['max_level']).save()
    
    # EncounterConditionValue
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/encounter_condition_values.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        EncounterConditionValue(id=int(row['id']), encounterConditionId=row['encounter_condition_id'], identifier=row['identifier'], isDefault=row['is_default']).save()
    
    # EncounterConditionValueMap
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/evolution_condition_value_map.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        EncounterConditionValueMap(encounterId=row['encounter_id'], encounterConditionValueId=row['encounter_condition_value_id']).save()
    
    # EncounterConditionValueProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/encounter_condition_value_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        EncounterConditionValueProse(encounterConditionValueId=row['encounter_condition_value_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name']).save()
    
    # EncounterMethodProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/encounter_method_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        EncounterMethodProse(encounterMethodId=row['encounter_method_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name']).save()
    
    # EvolutionTrigger
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/evolution_triggers.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        EvolutionTrigger(id=int(row['id']), identifier=row['identifier']).save()
    
    # EvolutionTriggerProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/evolution_trigger_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        EvolutionTriggerProse(evolutionTriggerId=row['evolution_trigger_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name']).save()
    
    # Experience
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/experience.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        Experience(growthRateId=GrowthRate.objects.get(id=int(row['growth_rate_id'])), level=row['level'], experience=row['experience']).save()
    
    # Gender
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/genders.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        Gender(id=int(row['id']), identifier=row['identifier']).save()
    
    # GenerationName
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/generation_names.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        GenerationName(generationId=Generation.objects.get(id=int(row['generation_id'])), localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name']).save()
    
    # GrowthRateProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/growth_rate_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        GrowthRateProse(growthRateId=GrowthRate.objects.get(id=int(row['growth_rate_id'])), localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name']).save()
    
    # ItemCategoryProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/item_category_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        ItemCategoryProse(itemCategoryId=row['item_category_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name']).save()
    
    # ItemFlag
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/item_flags.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        ItemFlag(id=int(row['id']), identifier=row['identifier']).save()
    
    # ItemFlagMap
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/item_flag_map.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        ItemFlagMap(itemId=Item.objects.get(id=int(row['item_id'])), itemFlagId=row['item_flag_id']).save()
    
    # ItemFlagProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/item_flag_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        ItemFlagProse(itemFlagId=row['item_flag_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name'], description=row['description']).save()
    
    # ItemFlavorText
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/item_flavor_text.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        ItemFlavorText(itemId=Item.objects.get(id=int(row['item_id'])), versionGroupId=VersionGroup.objects.get(id=int(row['version_group_id'])), languageId=Language.objects.get(id=int(row['language_id'])), flavorText=row['flavor_text']).save()
    
    # ItemFlingEffectProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/item_fling_effect_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        ItemFlingEffectProse(itemFlingEffectId=row['item_fling_effect_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name'], description=row['description']).save()
    
    # ItemGameIndice
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/item_gmae_indices.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        ItemGameIndice(itemId=Item.objects.get(id=int(row['item_id'])), generationId=Generation.objects.get(id=int(row['generation_id'])), gmaeIndex=row['gmae_index']).save()
    
    # ItemName
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/item_names.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        ItemName(itemId=Item.objects.get(id=int(row['item_id'])), localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name']).save()
    
    # ItemPocketName
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/item_pocket_names.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        ItemPocketName(itemPocketId=row['item_pocket_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name']).save()
    
    # ItemProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/item_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        ItemProse(itemId=Item.objects.get(id=int(row['item_id'])), localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name']).save()
    
    # LanguageName
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/language_names.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        LanguageName(languageId=Language.objects.get(id=int(row['language_id'])), localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name']).save()
    
    # LocationAreaEncounterEncounterRate
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/location_area_encounter_rates.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        LocationAreaEncounterEncounterRate(locationAreaId=row['location_area_id'], encounterMethodId=row['encounter_method_id'], versionId=row['version_id'], rate=row['rate']).save()
    
    # LocationAreaProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/location_area_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        LocationAreaProse(locationAreaId=row['location_area_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name']).save()
    
    # LocationGameIndice
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/location_game_indices.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        LocationGameIndice(locationId=row['location_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name'], subtitle=row['subtitle']).save()
    
    # LocationName
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/location_names.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        LocationName(locationId=row['location_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name'], subtitle=row['subtitle']).save()
    
    # Machine
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/machines.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        Machine(machineNumber=row['machine_number'], versionGroupId=VersionGroup.objects.get(id=int(row['version_group_id'])), itemId=Item.objects.get(id=int(row['item_id'])), moveId=row['move_id']).save()
    
    # MoveBattleStyle
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/move_battle_styles.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        MoveBattleStyle(id=int(row['id']), identifier=row['identifier']).save()
    
    # MoveBattleStyle
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/move_battle_style_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        MoveBattleStyle(id=int(row['id']), identifier=row['identifier']).save()
    
    # MoveChangelog
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/move_changelog.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        MoveChangelog(moveId=row['move_id'], changedInVersionGroupId=row['changed_in_version_group_id'], typeId=row['type_id'], power=row['power'], pp=row['pp'], accuracy=row['accuracy'], priority=row['priority'], targetId=row['target_id'], effectId=row['effect_id'], effectChange=row['effect_change']).save()
    
    # MoveDamaClassProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/move_damage_class_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        MoveDamaClassProse(moveDamageClassId=row['move_damage_class_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name'], description=row['description']).save()
    
    # MoveEffectChangelog
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/move_effect_changelog.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        MoveEffectChangelog(id=int(row['id']), effectId=row['effect_id'], changedInVersionGroupId=row['changed_in_version_group_id']).save()
    
    # MoveEffectChangelogProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/move_effect_changelog_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        MoveEffectChangelogProse(moveEffectChangelogId=row['move_effect_changelog_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), effect=row['effect']).save()
    
    # MoveEffectProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/move_effect_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        MoveEffectProse(moveEffectId=row['move_effect_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), shortEffect=row['short_effect']).save()
    
    # MoveFlag
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/move_flags.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        MoveFlag(id=int(row['id']), identifier=row['identifier']).save()
    
    # MoveFlagMap
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/move_flag_map.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        MoveFlagMap(moveId=row['move_id'], moveFlagId=row['move_flag_id']).save()
    
    # MoveFlagProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/move_flag_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        MoveFlagProse(moveFlagId=int(row['id']), localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name'], description=row['description']).save()
    
    # MoveFlavorText
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/move_flavor_text.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        MoveFlavorText(moveId=row['move_id'], versionGroupId=VersionGroup.objects.get(id=int(row['version_group_id'])), languageId=Language.objects.get(id=int(row['language_id'])), flavorText=row['flavor_text']).save()
    
    # MoveMetaCategory
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/move_categories.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        MoveMetaCategory(id=int(row['id']), identifier=row['identifier']).save()
    
    # MoveMetaAilment
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/move_meta_ailments.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        MoveMetaAilment(id=int(row['id']), identifier=row['identifier']).save()
    
    # MoveMeta
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/move_meta.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        MoveMeta(id=row['moveId'], metaCategoryId=row['meta_category_id'], metaAilmentId=row['meta_ailment_id'], minHits=row['min_hits'], maxHits=row['max_hits'], minTurns=row['min_turns'], maxTurns=row['max_turns'], drain=row['drain'], healing=row['healing'],ailmentChance=row['ailment_chance'], flingChance=row['fling_chance'], statChance=row['stat_chance']).save()
    
    # MoveMetaAilmentName
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/move_meta_ailment_names.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        MoveMetaAilmentName(moveId=row['move_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name']).save()
    
    # MoveMetaCategoryProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/move_meta_category_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        MoveMetaCategoryProse(moveMetaCategoryId=row['move_meta_category_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), description=row['description']).save()
    
    # MoveMetaStatChange
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/move_meta_stat_changes.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        MoveMetaStatChange(moveId=row['move_id'], statId=row['sat_id'], change=row['change']).save()
    
    # MoveName
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/move_names.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        MoveName(moveId=row['move_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name']).save()
    
    # MoveTargetProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/move_target_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        MoveTargetProse(moveTargetId=row['move_target_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name'], description=row['description']).save()
    
    # Nature
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/natures.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        Nature(id=int(row['id']), identifier=row['identifier'], decreasedStatId=row['decreased_stat_id'], increasedStatId=row['increased_stat_id'], hatesFlavorId=row['hates_flavor_id'], likesFlavorId=row['likes_flavor_id'], gameIndex=None if row['game_index'] == '' else int(row['game_index'])).save()
    
    # NatureBattleStylePreference
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/nature_battle_style_preferences.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        NatureBattleStylePreference(natureId=row['nature_id'], moveBattleStyleId=row['move_battle_style_id'], lowHpPreference=row['low_hp_preference'], highHpPreference=row['high_hp_preference']).save()
    
    # NatureName
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/nature_names.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        NatureName(natureId=row['nature_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name']).save()
    
    # PokeathlonStat
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokeathlon_stats.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokeathlonStat(id=int(row['id']), identifier=row['identifier']).save()
    
    # NaturePokeathlonStat
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/nature_pokeathlon_stats.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        NaturePokeathlonStat(natureId=row['nature_id'], pokeathlonStatId=row['pokeathlon_stat_id'], maxChange=row['max_change']).save()
    
    # PalParkArea
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pal_park_areas.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PalParkArea(id=int(row['id']), identifier=row['identifier']).save()
    
    # PalPark
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pal_park.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PalPark(speciesId=PokemonSpecies.objects.get(id=int(row['species_id'])), areaId=row['area_id'], baseScore=row['base_score'], rate=row['rate']).save()
    
    # PalParkAreaName
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pal_park_area_names.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PalParkAreaName(palParkAreaId=row['pal_park_area_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name']).save()
    
    # PokeathlonStatName
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokeathlon_stat_names.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokeathlonStatName(pokeathlonStatId=row['pokeathlon_stat_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=['name']).save()
    
    # Pokedex
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokedexes.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        Pokedex(id=int(row['id']),
                regionId=Region.objects.get(id=int(row['region_id']),
                identifier=row['identifier'],
                isMainSeries=row['is_main_series'])).save()
    
    # PokedexProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokedex_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokedexProse(pokedexId=row['pokedex_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name'], description=row['description']).save()
    
    # PokedexVersionGroup
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokedex_version_groups.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokedexVersionGroup(pokedexId=row['pokedex_id'], versionGroupId=VersionGroup.objects.get(id=int(row['version_group_id']))).save()
    
    # PokemonAbility
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_abilities.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonAbility(pokemonId=row['pokemon_id'], abilityId=Ability.objects.get(id=int(row['ability_id'])), isHidden=row['is_hidden'], slot=row['slot']).save()
    
    # PokemonColorName
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_color_names.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonColorName(pokemonColorId=row['pokemon_color_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name']).save()
    
    # PokemonDexNumber
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_dex_numbers.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonDexNumber(speciesId=PokemonSpecies.objects.get(id=int(row['species_id'])), pokedexId=row['pokedex_id'], pokedexNumber=row['pokedex_number']).save()
    
    # PokemonEggGroup
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_egg_groups.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonEggGroup(speciesId=PokemonSpecies.objects.get(id=int(row['species_id'])), eggGroupId=row['egg_group_id']).save()
    
    # PokemonEvolution
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_evolutions.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonEvolution(id=int(row['id']), evolvedSpeciesId=row['evolved_species_id'], evolutionTriggerId=row['evolution_triger_id'], triggerItemId=row['trigger_item_id'], minimumLevel=row['minimum_level'], genderId=row['gender_id'], locationId=row['location_id'], heldItemId=row['held_item_id'], timeOfDay=row['time_of_day'], knownMoveId=row['known_move_id'], minimumHappiness=row['minimum_happiness'], minimumBeauty=row['minimum_beauty'], minimumAffection=row['minimum_affection'], relativePhysicalStat=row['relative_physical_stat'], partySpeciesId=row['party_species_id'], partyTypeId=row['party_type_id'], tradeSpecies=row['trade_species'], needsOverworldRain=row['needs_overworld_rain'], turnUpsideDown=row['turn_upside_down']).save()
    
    # PokemonForm
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_forms.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonForm(id=int(row['id']), formIdentifier=row['form_identifier'], pokemonId=row['pokemon_id'], introducedInVersionGroupId=['introduced_in_version_group_id'], isDefault=row['is_default'], isBattleOnly=row['is_battle_only'], isMega=row['is_mega'], formOrder=row['form_order'], order=row['order']).save()
    
    # PokemonFormGeneration
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_form_generations.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonFormGeneration(pokemonFromId=row['pokemon_form_id'], generationId=Generation.objects.get(id=int(row['generation_id'])), gameIndex=None if row['game_index'] == '' else int(row['game_index'])).save()
    
    # PokemonFormName
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_form_names.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonFormName(pokemonFormId=row['pokemon_form_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), formName=row['form_name'], pokemonName=row['pokemon_name']).save()
    
    # PokemonFormPokeathlonStat
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_form_pokeathlon_stats.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonFormPokeathlonStat(pokemonFormId=row['pokemon_form_id'], pokeathlonStatId=row['pokeathlon_stat_id'], minimumStat=row['minimum_stat'], baseStat=row['base_stat'], maximumStat=row['maximum_stat']).save()
    
    # PokemonGameIndice
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_game_indices.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonGameIndice(pokemonId=row['pokemon_id'], versionId=row['version_id'], gameIndex=None if row['game_index'] == '' else int(row['game_index'])).save()
    
    # PokemonHabitatName
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_habitat_names.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonHabitatName(pokemonHabitatId=int(row['id']), localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name']).save()
    
    # PokemonItem
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_items.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonItem(pokemonId=row['pokemon_id'], versionId=row['version_id'], itemId=Item.objects.get(id=int(row['item_id'])), rarity=row['rarity']).save()
    
    # PokemonMoveMethod
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_move_methods.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonMoveMethod(id=int(row['id']), identifier=row['identifier']).save()
    
    # PokemonMoveMethodProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_move_method_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonMoveMethodProse(pokemonMoveMethodId=row['pokemon_move_method_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name'], description=row['description']).save()
    
    # PokemonMove
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_moves.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonMove(pokemonId=row['pokemon_id'], versionGroupId=VersionGroup.objects.get(id=int(row['version_group_id'])), moveId=row['move_id'], pokemonMoveMethodId=row['pokemon_move_method_id'], level=row['level'], order=row['order']).save()
    
    # PokemonShapeProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_shape_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonShapeProse(pokemonShapeId=row['pokemon_shape_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name'], awesomeName=row['awesomeName'], description=row['description']).save()
    
    # PokemonSpeciesFlavorText
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_species_flavor_text.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonSpeciesFlavorText(speciesId=PokemonSpecies.objects.get(id=int(row['species_id'])), versionId=row['version_id'], languageId=Language.objects.get(id=int(row['language_id'])), flavorText=row['flavor_text']).save()
    
    # PokemonSpeciesName
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_species_names.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonSpeciesName(pokemonSpeciesId=row['pokemon_species_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name'], genus=row['genus']).save()
    
    # PokemonSpeciesProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_species_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonHabitat(pokemonSpeciesId=row['pokemon_species_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), formDescription=row['form_description']).save()
    
    # PokemonStat
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_stats.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonStat(pokemonId=row['pokemon_id'], statId=Stat.objects.get(id=int(row['stat_id'])), baseStat=row['base_stat'], effort=row['effort']).save()
    
    # PokemonType
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/pokemon_types.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        PokemonHabitat(pokemonId=row['pokemon_id'], typeId=row['type_id'], slot=row['slot']).save()
    
    # RegionName
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/region_names.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        RegionName( regionId=Region.objects.get(id=int(row['region_id']),
                    localLanguageId=Language.objects.get(id=int(row['local_language_id'])),
                    name=row['name'])).save()
    
    # StatName
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/stat_names.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        StatName(   statId=Stat.objects.get(id=int(row['stat_id'])),
                    localLanguageId=Language.objects.get(id=int(row['local_language_id'])),
                    name=row['name']).save()
    
    # SuperContestCombo
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/super_contest_combos.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        SuperContestCombo(firstMoveId=row['first_move_id'], secondMoveId=row['second_move_id']).save()
    
    # SuperContestEffectProse
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/super_contest_effect_prose.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        SuperContestEffectProse(superContestEffectId=row['super_contest_combo_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), flavorText=row['flavor_text']).save()
    
    # TypeEfficacy
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/type_efficacy.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        TypeEfficacy(damageTypeId=row['damage_type_id'], targetTypeId=row['target_type_id'], damageFactor=row['damage_factor']).save()
    
    # TypeGameIndices
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/type_game_indices.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        TypeGameIndices(typeId=row['type_id'], generationId=Generation.objects.get(id=int(row['generation_id'])), gameIndex=None if row['game_index'] == '' else int(row['game_index'])).save()
    
    # TypeName
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/type_names.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        TypeName(typeId=row['type_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name']).save()
    
    # VersionGroupPokemonMoveMethod
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/version_group_pokemon_move_methods.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        VersionGroupPokemonMoveMethod(versionGroupId=VersionGroup.objects.get(id=int(row['version_group_id'])), pokemonMoveMethodId=row['pokemon_move_method_id']).save()
    
    # VersionGroupRegion
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/version_group_regions.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        VersionGroupRegion( versionGroupId=int(row['id']),
                            regionId=Region.objects.get(id=int(row['region_id']))).save()
    
    # VersionName
    dictReader = csv.DictReader(open(PROJECT_ROOT + '/Data/csv/version_names.csv', 'r+'),
                                delimiter = ',',
                                quotechar='"')
                                
    for row in dictReader:
        VersionName(versionId=row['version_id'], localLanguageId=Language.objects.get(id=int(row['local_language_id'])), name=row['name']).save()
    


    context = { 'message' : 'boom', }

    return render(request, "PokeData/index.html", context)
