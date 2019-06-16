from django.db import models

class ContestType(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)

class MoveDamageClass(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)

class Stat(models.Model):
    id = models.IntegerField(primary_key=True)
    damageClassId = models.ForeignKey(MoveDamageClass, on_delete=models.CASCADE, blank=True, null=True)
    identifier = models.CharField(max_length=250)
    isBattleOnly = models.BooleanField()
    gameIndex = models.IntegerField(blank=True, null=True)

class Characteristic(models.Model):
    id = models.IntegerField(primary_key=True)
    statId = models.ForeignKey(Stat, on_delete=models.CASCADE)
    geneMod5 = models.IntegerField()

class BerryFirmness(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)

class ItemFlingEffect(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)

class ItemPocket(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)

class ItemCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    pocketId = models.ForeignKey(ItemPocket, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=250)

class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)
    categoryId = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    cost = models.IntegerField()
    flingPower = models.IntegerField(blank=True, null=True)
    flingEffectId = models.ForeignKey(ItemFlingEffect, on_delete=models.CASCADE, blank=True, null=True)

class Language(models.Model):
    id = models.IntegerField(primary_key=True)
    iso639 = models.CharField(max_length=250)
    iso3166 = models.CharField(max_length=250)
    identifier = models.CharField(max_length=250)
    official = models.IntegerField()
    order = models.IntegerField()

class Region(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)

class Generation(models.Model):
    id = models.IntegerField(primary_key=True)
    mainRegionId = models.ForeignKey(Region, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=250)

class Type(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)
    generationId = models.ForeignKey(Generation, on_delete=models.CASCADE)
    damageClassId = models.ForeignKey(MoveDamageClass, on_delete=models.CASCADE, blank=True, null=True)

class VersionGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)
    generationId = models.ForeignKey(Generation, on_delete=models.CASCADE)
    order = models.IntegerField()

class Ability(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)
    generationId = models.ForeignKey(Generation, on_delete=models.CASCADE)

class AbilityChangelog(models.Model):
    id = models.IntegerField(primary_key=True)
    abilityId = models.ForeignKey(Ability, on_delete=models.CASCADE)
    changedInVersionGroupId = models.ForeignKey(VersionGroup, on_delete=models.CASCADE)

class AbilityChangelogProse(models.Model):
    abilityChangelogId = models.ForeignKey(AbilityChangelog, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    effect = models.CharField(max_length=250)

class AbilityFlavorText(models.Model):
    abilityId = models.ForeignKey(Ability, on_delete=models.CASCADE)
    versionGroupId = models.ForeignKey(VersionGroup, on_delete=models.CASCADE)
    languageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    flavorText = models.CharField(max_length=250)

class AbilityName(models.Model):
    abilityId = models.ForeignKey(Ability, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class AbilityProse(models.Model):
    abilityId = models.ForeignKey(Ability, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    shortEffect = models.CharField(max_length=250)

class Berry(models.Model):
    id = models.IntegerField(primary_key=True)
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE)
    firmnessId = models.ForeignKey(BerryFirmness, on_delete=models.CASCADE)
    naturalGiftPower = models.IntegerField()
    naturalGiftTypeId = models.ForeignKey(Type, on_delete=models.CASCADE)
    size = models.IntegerField()
    maxHarvest = models.IntegerField()
    growthTime = models.IntegerField()
    soilDryness = models.IntegerField()
    smoothness = models.IntegerField()

class BerryFirmnessName(models.Model):
    berryFirmnessId = models.ForeignKey(BerryFirmness, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class BerryFlavor(models.Model):
    berryId = models.ForeignKey(Berry, on_delete=models.CASCADE)
    contestTypeId = models.ForeignKey(ContestType, on_delete=models.CASCADE)
    flavor = models.IntegerField()

class CharacteristicText(models.Model):
    characteristicId = models.ForeignKey(Characteristic, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    message = models.CharField(max_length=250)

class EvolutionChain(models.Model):
    id = models.IntegerField(primary_key=True)
    babyTriggerItemId = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)

class PokemonColor(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)

class PokemonShape(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)

class PokemonHabitat(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)

class GrowthRate(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)
    formula = models.CharField(max_length=250)

class PokemonSpecies(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)
    evolvesFromSpeciesId = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    evolutionChainId = models.ForeignKey(EvolutionChain, on_delete=models.CASCADE)
    colorId = models.ForeignKey(PokemonColor, on_delete=models.CASCADE)
    shapeId = models.ForeignKey(PokemonShape, on_delete=models.CASCADE)
    habitatId = models.ForeignKey(PokemonHabitat, on_delete=models.CASCADE)
    genderRate = models.IntegerField()
    captureRate = models.IntegerField()
    baseHappiness = models.IntegerField()
    isBaby = models.BooleanField()
    hatchCounter = models.IntegerField()
    hasGenderDifferences = models.BooleanField()
    growthRateId = models.ForeignKey(GrowthRate, on_delete=models.CASCADE)
    formsSwitchable = models.BooleanField()
    order = models.IntegerField()

class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)
    speciesId = models.ForeignKey(PokemonSpecies, on_delete=models.CASCADE)
    height = models.IntegerField()
    weight = models.IntegerField()
    baseExperience = models.IntegerField()
    order = models.IntegerField()
    isDefault = models.BooleanField()

class MoveEffect(models.Model):
    id = models.IntegerField(primary_key=True)

class ContestEffect(models.Model):
    id = models.IntegerField(primary_key=True)
    appeal = models.IntegerField()
    jam = models.IntegerField()

class SuperContestEffect(models.Model):
    id = models.IntegerField(primary_key=True)
    appeal = models.IntegerField()

class MoveTarget(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)

class Move(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)
    generationId = models.ForeignKey(Generation, on_delete=models.CASCADE)
    typeId = models.ForeignKey(Type, on_delete=models.CASCADE)
    power = models.IntegerField(blank=True, null=True)
    pp = models.IntegerField(blank=True, null=True)
    accuracy = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    targetId = models.ForeignKey(MoveTarget, on_delete=models.CASCADE)
    damageClassId = models.ForeignKey(MoveDamageClass, on_delete=models.CASCADE)
    effectId = models.ForeignKey(MoveEffect, on_delete=models.CASCADE)
    effectChance = models.IntegerField(blank=True, null=True)
    contestTypeId = models.ForeignKey(ContestType, on_delete=models.CASCADE, blank=True, null=True)
    contestEffectId = models.ForeignKey(ContestEffect, on_delete=models.CASCADE, blank=True, null=True)
    superContestEffectId = models.ForeignKey(SuperContestEffect, on_delete=models.CASCADE)

class ContestCombo(models.Model):
    firstMoveId = models.ForeignKey(Move, on_delete=models.CASCADE, related_name='first_move')
    secondMoveId = models.ForeignKey(Move, on_delete=models.CASCADE, related_name='second_move')

class ContestEffectProse(models.Model):
    contestEffectId = models.ForeignKey(ContestEffect, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    flavorText = models.CharField(max_length=250)
    effect = models.CharField(max_length=250)

class ContestTypeName(models.Model):
    contestTypeId = models.ForeignKey(ContestType, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    flavor = models.CharField(max_length=250)
    color = models.CharField(max_length=250)

class EggGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)

class EggGroupProse(models.Model):
    eggGroupId = models.ForeignKey(EggGroup, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class EncounterCondition(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)

class EncounterConditionProse(models.Model):
    encounterConditionId = models.ForeignKey(EncounterCondition, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class Version(models.Model):
    id = models.IntegerField(primary_key=True)
    versionGroupId = models.ForeignKey(VersionGroup, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=250)

class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    regionId = models.ForeignKey(Region, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=250)

class LocationArea(models.Model):
    id = models.IntegerField(primary_key=True)
    locationId = models.ForeignKey(Location, on_delete=models.CASCADE)
    gameIndex = models.IntegerField()
    identifier = models.CharField(max_length=250, blank=True, null=True)

class EncounterMethod(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)
    order = models.IntegerField()

class EncounterSlot(models.Model):
    id = models.IntegerField(primary_key=True)
    versionGroupId = models.ForeignKey(VersionGroup, on_delete=models.CASCADE)
    encounterMethodId = models.ForeignKey(EncounterMethod, on_delete=models.CASCADE)
    slot = models.IntegerField()
    rarity = models.IntegerField()

class Encounter(models.Model):
    id = models.IntegerField(primary_key=True)
    versionId = models.ForeignKey(Version, on_delete=models.CASCADE)
    locationAreaId = models.ForeignKey(LocationArea, on_delete=models.CASCADE)
    encounterSlotId = models.ForeignKey(EncounterSlot, on_delete=models.CASCADE)
    pokemonId = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    minLevel = models.IntegerField()
    maxLevel = models.IntegerField()

class EncounterConditionValue(models.Model):
    id = models.IntegerField(primary_key=True)
    encounterConditionId = models.ForeignKey(EncounterCondition, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=250)
    isDefault = models.BooleanField()

class EncounterConditionValueMap(models.Model):
    encounterId = models.ForeignKey(Encounter, on_delete=models.CASCADE)
    encounterConditionValueId = models.ForeignKey(EncounterConditionValue, on_delete=models.CASCADE)

class EncounterConditionValueProse(models.Model):
    encounterConditionValueId = models.ForeignKey(EncounterConditionValue, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class EncounterMethodProse(models.Model):
    encounterMethodId = models.ForeignKey(EncounterMethod, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class EvolutionTrigger(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)

class EvolutionTriggerProse(models.Model):
    evolutionTriggerId = models.ForeignKey(EvolutionTrigger, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class Experience(models.Model):
    growthRateId = models.ForeignKey(GrowthRate, on_delete=models.CASCADE)
    level = models.IntegerField()
    experience = models.IntegerField()

class Gender(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)

class GenerationName(models.Model):
    generationId = models.ForeignKey(Generation, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class GrowthRateProse(models.Model):
    growthRateId = models.ForeignKey(GrowthRate, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class ItemCategoryProse(models.Model):
    itemCategoryId = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class ItemFlag(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)

class ItemFlagMap(models.Model):
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE)
    itemFlagId = models.ForeignKey(ItemFlag, on_delete=models.CASCADE)

class ItemFlagProse(models.Model):
    itemFlagId = models.ForeignKey(ItemFlag, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

class ItemFlavorText(models.Model):
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE)
    versionGroupId = models.ForeignKey(VersionGroup, on_delete=models.CASCADE)
    languageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    flavorText = models.CharField(max_length=250)

class ItemFlingEffectProse(models.Model):
    itemFlingEffectId = models.ForeignKey(ItemFlingEffect, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

class ItemGameIndice(models.Model):
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE)
    generationId = models.ForeignKey(Generation, on_delete=models.CASCADE)
    gameIndex = models.IntegerField()

class ItemName(models.Model):
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class ItemPocketName(models.Model):
    itemPocketId = models.ForeignKey(ItemPocket, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class ItemProse(models.Model):
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    shortEffect = models.CharField(max_length=250)

class LanguageName(models.Model):
    languageId = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language_id')
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='local_language_id')
    name = models.CharField(max_length=250)

class LocationAreaEncounterRate(models.Model):
    locationAreaId = models.ForeignKey(LocationArea, on_delete=models.CASCADE)
    encounterMethodId = models.ForeignKey(EncounterMethod, on_delete=models.CASCADE)
    versionId = models.ForeignKey(Version, on_delete=models.CASCADE)
    rate = models.IntegerField()

class LocationAreaProse(models.Model):
    locationAreaId = models.ForeignKey(LocationArea, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, blank=True, null=True)

class LocationGameIndice(models.Model):
    locationId = models.ForeignKey(Location, on_delete=models.CASCADE)
    generationId = models.ForeignKey(Generation, on_delete=models.CASCADE)
    gameIndex = models.IntegerField()

class LocationName(models.Model):
    locationId = models.ForeignKey(Location, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250, blank=True, null=True)

class Machine(models.Model):
    machineNumber = models.IntegerField()
    versionGroupId = models.ForeignKey(VersionGroup, on_delete=models.CASCADE)
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE)
    moveId = models.ForeignKey(Move, on_delete=models.CASCADE)

class MoveBattleStyle(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)

class MoveBattleStyleProse(models.Model):
    moveBattleStyleId = models.ForeignKey(MoveBattleStyle, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class MoveChangelog(models.Model):
    moveId = models.ForeignKey(Move, on_delete=models.CASCADE)
    changedInVersionGroupId = models.ForeignKey(VersionGroup, on_delete=models.CASCADE)
    typeId = models.ForeignKey(Type, on_delete=models.CASCADE)
    power = models.IntegerField(blank=True, null=True)
    pp = models.IntegerField(blank=True, null=True)
    accuracy = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    targetId = models.ForeignKey(Pokemon, on_delete=models.CASCADE, blank=True, null=True)
    effectId = models.ForeignKey(MoveEffect, on_delete=models.CASCADE, blank=True, null=True)
    effectChange = models.IntegerField(blank=True, null=True)

class MoveDamageClassProse(models.Model):
    moveDamageClassId = models.ForeignKey(MoveDamageClass, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

class MoveEffectChangelog(models.Model):
    id = models.IntegerField(primary_key=True)
    effectId = models.ForeignKey(MoveEffect, on_delete=models.CASCADE)
    changedInVersionGroupId = models.ForeignKey(VersionGroup, on_delete=models.CASCADE)

class MoveEffectChangelogProse(models.Model):
    moveEffectChangelogId = models.ForeignKey(MoveEffectChangelog, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    effect = models.CharField(max_length=250)

class MoveEffectProse(models.Model):
    moveEffectId = models.ForeignKey(MoveEffect, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    shortEffect = models.CharField(max_length=250)

class MoveFlag(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)

class MoveFlagMap(models.Model):
    moveId = models.ForeignKey(Move, on_delete=models.CASCADE)
    moveFlagId = models.ForeignKey(MoveFlag, on_delete=models.CASCADE)

class MoveFlagProse(models.Model):
    moveFlagId = models.ForeignKey(MoveFlag, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

class MoveFlavorText(models.Model):
    moveId = models.ForeignKey(Move, on_delete=models.CASCADE)
    versionGroupId = models.ForeignKey(VersionGroup, on_delete=models.CASCADE)
    languageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    flavorText = models.CharField(max_length=250)

class MoveMetaCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)

class MoveMetaAilment(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)

class MoveMeta(models.Model):
    moveId = models.ForeignKey(Move, on_delete=models.CASCADE)
    metaCategoryId = models.ForeignKey(MoveMetaCategory, on_delete=models.CASCADE)
    metaAilmentId = models.ForeignKey(MoveMetaAilment, on_delete=models.CASCADE)
    minHits = models.IntegerField(blank=True, null=True)
    maxHits = models.IntegerField(blank=True, null=True)
    minTurns = models.IntegerField(blank=True, null=True)
    maxTurns = models.IntegerField(blank=True, null=True)
    drain = models.IntegerField()
    healing = models.IntegerField()
    ailmentChance = models.IntegerField()
    flinchChance = models.IntegerField()
    statChance = models.IntegerField()

class MoveMetaAilmentName(models.Model):
    moveId = models.ForeignKey(Move, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class MoveMetaCategoryProse(models.Model):
    moveMetaCategoryId = models.ForeignKey(MoveMetaCategory, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)

class MoveMetaStatChange(models.Model):
    moveId = models.ForeignKey(Move, on_delete=models.CASCADE)
    statId = models.ForeignKey(Stat, on_delete=models.CASCADE)
    change = models.IntegerField()

class MoveName(models.Model):
    moveId = models.ForeignKey(Move, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class MoveTargetProse(models.Model):
    moveTargetId = models.ForeignKey(MoveTarget, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

class Nature(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)
    decreasedStatId = models.ForeignKey(Stat, on_delete=models.CASCADE, related_name='decreased_stat_id')
    increasedStatId = models.ForeignKey(Stat, on_delete=models.CASCADE, related_name='increased_stat_id')
    hatesFlavorId = models.ForeignKey(BerryFlavor, on_delete=models.CASCADE, related_name='hates_flavor_id')
    likesFlavorId = models.ForeignKey(BerryFlavor, on_delete=models.CASCADE, related_name='likes_flavor_id')
    gameIndex = models.IntegerField()

class NatureBattleStylePreference(models.Model):
    natureId = models.ForeignKey(Nature, on_delete=models.CASCADE)
    moveBattleStyleId = models.ForeignKey(MoveBattleStyle, on_delete=models.CASCADE)
    lowHpPreference = models.IntegerField()
    highHpPreference = models.IntegerField()

class NatureName(models.Model):
    natureId = models.ForeignKey(Nature, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class PokeathlonStat(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)

class NaturePokeathlonStat(models.Model):
    natureId = models.ForeignKey(Nature, on_delete=models.CASCADE)
    pokeathlonStatId = models.ForeignKey(PokeathlonStat, on_delete=models.CASCADE)
    maxChange = models.IntegerField()

class PalParkArea(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)

class PalPark(models.Model):
    speciesId = models.ForeignKey(PokemonSpecies, on_delete=models.CASCADE)
    areaId = models.ForeignKey(PalParkArea, on_delete=models.CASCADE)
    baseScore = models.IntegerField()
    rate = models.IntegerField()

class PalParkAreaName(models.Model):
    palParkAreaId = models.ForeignKey(PalParkArea, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class PokeathlonStatName(models.Model):
    pokeathlonStatId = models.ForeignKey(PokeathlonStat, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class Pokedex(models.Model):
    id = models.IntegerField(primary_key=True)
    regionId = models.ForeignKey(Region, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=250)
    isMainSeries = models.BooleanField()

class PokedexProse(models.Model):
    pokedexId = models.ForeignKey(Pokedex, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

class PokedexVersionGroup(models.Model):
    pokedexId = models.ForeignKey(Pokedex, on_delete=models.CASCADE)
    versionGroupId = models.ForeignKey(VersionGroup, on_delete=models.CASCADE)

class PokemonAbility(models.Model):
    pokemonId = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    abilityId = models.ForeignKey(Ability, on_delete=models.CASCADE)
    isHidden = models.BooleanField()
    slot = models.IntegerField()

class PokemonColorName(models.Model):
    pokemonColorId = models.ForeignKey(PokemonColor, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class PokemonDexNumber(models.Model):
    speciesId = models.ForeignKey(PokemonSpecies, on_delete=models.CASCADE)
    pokedexId = models.ForeignKey(Pokedex, on_delete=models.CASCADE)
    pokedexNumber = models.IntegerField()

class PokemonEggGroup(models.Model):
    speciesId = models.ForeignKey(PokemonSpecies, on_delete=models.CASCADE)
    eggGroupId = models.ForeignKey(EggGroup, on_delete=models.CASCADE)

class PokemonEvolution(models.Model):
    id = models.IntegerField(primary_key=True)
    evolvedSpeciesId = models.ForeignKey(PokemonSpecies, on_delete=models.CASCADE, related_name='evolved_species_id')
    evolutionTriggerId = models.ForeignKey(EvolutionTrigger, on_delete=models.CASCADE)
    triggerItemId = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True, related_name='trigger_item_id')
    minimumLevel = models.IntegerField(blank=True, null=True)
    genderId = models.ForeignKey(Gender, on_delete=models.CASCADE, blank=True, null=True)
    locationId = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    heldItemId = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True, related_name='held_item_id')
    timeOfDay = models.CharField(max_length=250, blank=True, null=True)
    knownMoveId = models.ForeignKey(Move, on_delete=models.CASCADE, blank=True, null=True)
    knownMoveTypeId = models.ForeignKey(Type, on_delete=models.CASCADE, blank=True, null=True, related_name='known_move_id')
    minimumHappiness = models.IntegerField(blank=True, null=True)
    minimumBeauty = models.IntegerField(blank=True, null=True)
    minimumAffection = models.IntegerField(blank=True, null=True)
    relativePhysicalStat = models.IntegerField(blank=True, null=True)
    partySpeciesId = models.ForeignKey(PokemonSpecies, on_delete=models.CASCADE, blank=True, null=True, related_name='party_species_id')
    partyTypeId = models.ForeignKey(Type, on_delete=models.CASCADE, blank=True, null=True, related_name='party_type_id')
    tradeSpecies= models.ForeignKey(PokemonSpecies, on_delete=models.CASCADE, blank=True, null=True, related_name='trade_species_id')
    needsOverworldRain = models.BooleanField()
    turnUpsideDown = models.BooleanField()

class PokemonForm(models.Model):
    id = models.IntegerField(primary_key=True)
    formIdentifier = models.CharField(max_length=250, blank=True, null=True)
    pokemonId = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    introducedInVersionGroupId = models.ForeignKey(VersionGroup, on_delete=models.CASCADE)
    isDefault = models.BooleanField()
    isBattleOnly = models.BooleanField()
    isMega = models.BooleanField()
    formOrder = models.IntegerField()
    order = models.IntegerField()

class PokemonFormGeneration(models.Model):
    pokemonFormId = models.ForeignKey(PokemonForm, on_delete=models.CASCADE)
    generationId = models.ForeignKey(Generation, on_delete=models.CASCADE)
    gameIndex = models.IntegerField()

class PokemonFormName(models.Model):
    pokemonFormId = models.ForeignKey(PokemonForm, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    formName = models.CharField(max_length=250, blank=True, null=True)
    pokemonName = models.CharField(max_length=250, blank=True, null=True)

class PokemonFormPokeathlonStat(models.Model):
    pokemonFormId = models.ForeignKey(PokemonForm, on_delete=models.CASCADE)
    pokeathlonStatId = models.ForeignKey(PokeathlonStat, on_delete=models.CASCADE)
    minimumStat = models.IntegerField()
    baseStat = models.IntegerField()
    maximumStat = models.IntegerField()

class PokemonGameIndice(models.Model):
    pokemonId = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    versionId = models.ForeignKey(Version, on_delete=models.CASCADE)
    gameIndex = models.IntegerField()

class PokemonHabitatName(models.Model):
    pokemonHabitatId = models.ForeignKey(PokemonHabitat, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class PokemonItem(models.Model):
    pokemonId = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    versionId = models.ForeignKey(Version, on_delete=models.CASCADE)
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE)
    rarity = models.IntegerField()

class PokemonMoveMethod(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=250)

class PokemonMoveMethodProse(models.Model):
    pokemonMoveMethodId = models.ForeignKey(PokemonMoveMethod, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

class PokemonMove(models.Model):
    pokemonId = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    versionGroupId = models.ForeignKey(VersionGroup, on_delete=models.CASCADE)
    moveId = models.ForeignKey(Move, on_delete=models.CASCADE)
    pokemonMoveMethodId = models.ForeignKey(PokemonMoveMethod, on_delete=models.CASCADE)
    level = models.IntegerField()
    order = models.IntegerField()

class PokemonShapeProse(models.Model):
    pokemonShapeId = models.ForeignKey(PokemonShape, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    awesomeName = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

class PokemonSpeciesFlavorText(models.Model):
    speciesId = models.ForeignKey(PokemonSpecies, on_delete=models.CASCADE)
    versionId = models.ForeignKey(Version, on_delete=models.CASCADE)
    languageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    flavorText = models.CharField(max_length=250)

class PokemonSpeciesName(models.Model):
    pokemonSpeciesId = models.ForeignKey(PokemonSpecies, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    genus = models.CharField(max_length=250, blank=True, null=True)

class PokemonSpeciesProse(models.Model):
    pokemonSpeciesId = models.ForeignKey(PokemonSpecies, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    formDescription = models.CharField(max_length=250)

class PokemonStat(models.Model):
    pokemonId = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    statId = models.ForeignKey(Stat, on_delete=models.CASCADE)
    baseStat = models.IntegerField()
    effort = models.IntegerField()

class PokemonType(models.Model):
    pokemonId = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    typeId = models.ForeignKey(Type, on_delete=models.CASCADE)
    slot = models.IntegerField()

class RegionName(models.Model):
    regionId = models.ForeignKey(Region, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class StatName(models.Model):
    statId = models.ForeignKey(Stat, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class SuperContestCombo(models.Model):
    firstMoveId = models.ForeignKey(Move, on_delete=models.CASCADE, related_name='first_move_id')
    secondMoveId = models.ForeignKey(Move, on_delete=models.CASCADE, related_name='second_move_id')

class SuperContestEffectProse(models.Model):
    superContestEffectId = models.ForeignKey(SuperContestEffect, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    flavorText = models.CharField(max_length=250)

class TypeEfficacy(models.Model):
    damageTypeId = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='damage_type_id')
    targetTypeId = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='target_type_id')
    damageFactor = models.IntegerField()

class TypeGameIndice(models.Model):
    typeId = models.ForeignKey(Type, on_delete=models.CASCADE)
    generationId = models.ForeignKey(Generation, on_delete=models.CASCADE)
    gameIndex = models.IntegerField()

class TypeName(models.Model):
    typeId = models.ForeignKey(Type, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    
class VersionGroupPokemonMoveMethod(models.Model):
    versionGroupId = models.ForeignKey(VersionGroup, on_delete=models.CASCADE)
    pokemonMoveMethodId = models.ForeignKey(PokemonMoveMethod, on_delete=models.CASCADE)

class VersionGroupRegion(models.Model):
    versionGroupId = models.ForeignKey(VersionGroup, on_delete=models.CASCADE)
    regionId = models.ForeignKey(Region, on_delete=models.CASCADE)

class VersionName(models.Model):
    versionId = models.ForeignKey(Version, on_delete=models.CASCADE)
    localLanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
