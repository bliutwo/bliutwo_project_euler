# Author: Brian Liu
# File:   chemoUtils.py
# Description: utilities file containing class and function definitions

from sets import *
import random

DEFAULT_ITERATIONS = 100
DEFAULT_SEED = 214

# Inputs:
#  -allFingerprintsAndTargets: a list of drugs matched to its fingerprints and
#   targets, both parsed correctly (i.e. into correct ints and formatting)
# Returns:
#  -dictionary containing indexes for drugs for fast access
def generateFingerprintsAndTargetsIndexDictionary(allFingerprintsAndTargets):
    dictionary = {}
    for i in range(len(allFingerprintsAndTargets)):
        dictionary[allFingerprintsAndTargets[i][0]] = i
    return dictionary

# Input:
#  -output: a opened file to which we will write
#  -outputGrid: a grid containing the information that we will write to output
#  -stringSeparator: the string that separates the elements in each element in
#   outputGrid
# simply writes to output
def writeToOutput(output, outputGrid, stringSeparator):
    # try writing one line to output
    for i in range(len(outputGrid)):
        output.write(stringSeparator.join(map(str, outputGrid[i])))
        output.write("\n")

# Input:
#  -outputGrid: a grid containing the information that we will write to output
#  -filename: name of the file to be outputted
#  -stringSeparator: the string that separates the elements in each element in
#   outputGrid
# outputs a file with filename
def outputFile(outputGrid, filename, stringSeparator, title):
    output = open(filename, "w")
    if (title != ""):
        output.write(title)
        output.write("\n")
    writeToOutput(output, outputGrid, stringSeparator)
    output.close()

# takes in a rawFingerprint (string from drugs.csv) and outputs a list
# containing the numbers as ints rather than one string
def parseFingerprint(rawFingerprint):
    fingerprint = rawFingerprint.split()
    fingerprint = map(int, fingerprint)
    return fingerprint

# takes in a drug (string), allFingerprintsAndTargets (maps drugs to
# fingerprints and targets), and the drugIndexDictionary (for easy access to
# drugs)
# returns the fingerprint from allFingerprintsAndTargets
def getFingerprint(drug, allFingerprintsAndTargets, drugIndexDictionary):
    index = drugIndexDictionary[drug]
    fingerprint = allFingerprintsAndTargets[index][1]
    return fingerprint

# takes in two lists and returns the length of the intersected set
def findIntersect(fpA, fpB):
    intersectSet = set(fpA) & set(fpB)
    return len(intersectSet)

# takes in two lists and returns the length of the union of the sets
def findUnion(fpA, fpB):
    unionSet = list(set(fpA) | set(fpB))
    return len(unionSet)

# returns Tanimoto score given two drug IDs and allFingerprintsAndTargets (maps
# drugs to fingerprints and targets) and drugIndexDictionary (for easy index
# access to drugs)
def getTanimotoScore(drugA, drugB, allFingerprintsAndTargets, drugIndexDictionary):
    if drugA == drugB:
        return 1
    fingerprintA = getFingerprint(drugA, allFingerprintsAndTargets, drugIndexDictionary)
    fingerprintB = getFingerprint(drugB, allFingerprintsAndTargets, drugIndexDictionary)
    intersection = findIntersect(fingerprintA, fingerprintB)
    union = findUnion(fingerprintA, fingerprintB)
    tScore = float(intersection) / union
    return tScore

# Inputs:
#  -drug: string containing ID of drug in question
#  -targetsGrid: grid containing info from targets.csv
# returns a list of targets
def getTargetList(drug, targetsGrid):
    targetList = []
    for targetinfolist in targetsGrid:
        if targetinfolist[0] == drug:
            targetList.append(targetinfolist[1])
    return targetList

# Inputs:
#  -drug: a string containing ID of drug in question
#  -allFingerprintsAndTargets: a list mapping drugs to their fingerprints and
#   targets
#  -drugIndexDictionary: dictionary mapping drugs to their indices in 
#   allFingerprintsAndTargets
# returns a drug's target list
def getTargetListFromAFAT(drug, allFingerprintsAndTargets, drugIndexDictionary):
    index = drugIndexDictionary[drug]
    targetlist = allFingerprintsAndTargets[index][2]
    return targetlist

# Inputs:
#  -drugA: string with ID of first drug in question
#  -drugB: string with ID of second drug in question
#  -allFingerprintsAndTargets: a list mapping drugs to their fingerprints and
#   targets
#  -drugIndexDictionary: dictionary mapping drugs to their indices in 
#   allFingerprintsAndTargets
# returns 1 or 0 based on whether two drugs share target(s)
def determineShareTargets(drugA, drugB, allFingerprintsAndTargets, drugIndexDictionary):
    targetListA = getTargetListFromAFAT(drugA, allFingerprintsAndTargets, drugIndexDictionary)
    targetListB = getTargetListFromAFAT(drugB, allFingerprintsAndTargets, drugIndexDictionary)
    intersection = findIntersect(targetListA, targetListB)
    if intersection == 0:
        return 0
    else:
        return 1

# returns a grid with all information given an opened file of the csv file
def getGrid(opened):
    # use opened to obtain the list of pairs
    # read first line of file since the first line is a "key/legend"
    opened.readline()
    grid = []
    for line in opened:
        # parse line to get first part of pair
        line = line.strip()
        lineList = line.split(",")
        grid.append(lineList)
    return grid

# sorts a grid given a grid
def sortGrid(grid):
    return sorted(grid)

# returns a list of all pairs of drugs given a drugGrid, which contains info
# from drugs.csv
def getAllPairs(drugGrid):
    # use grid to construct listOfPairs
    listOfPairs = []
    for i in range(len(drugGrid)):
        for j in range (i+1, len(drugGrid)):
            pair = []
            # add first drug to pair
            pair.append(drugGrid[i][0])
            # add second drug to pair
            pair.append(drugGrid[j][0])
            listOfPairs.append(pair)
    return listOfPairs

# returns a list of all fingerprints and protein targets matched with drugs
# given a drugGrid and targetsGrid, containing info from drugs.csv and
# targets.csv, respectively
def getFingerprintsAndProteinTargets(drugGrid, targetsGrid):
    allFingerprintsAndProteinTargets = []
    for druglist in drugGrid:
        singleFingerprintAndProteinTargets = []
        singleFingerprintAndProteinTargets.append(druglist[0])
        fingerprint = parseFingerprint(druglist[2])
        singleFingerprintAndProteinTargets.append(fingerprint)
        targetlist = getTargetList(druglist[0], targetsGrid)
        singleFingerprintAndProteinTargets.append(targetlist)
        allFingerprintsAndProteinTargets.append(singleFingerprintAndProteinTargets)
    return allFingerprintsAndProteinTargets

# returns a list of drugs that bind to a protein given the protein and
# allFingerprintsAndProteinTargets (maps drugs to its fingerprints and protein
# targets)
def getDrugsBindProtein(protein, allFingerprintsAndProteinTargets):
    drugsBindProtein = []
    for druglist in allFingerprintsAndProteinTargets:
        if protein in druglist[2]:
            drugsBindProtein.append(druglist[0])
    return drugsBindProtein

# returns a list of proteins mapped to drugs that bind each protein in that
# list given a list of proteins (proteinList), a list that maps drugs to each
# drug's fingerprint and protein targets (allFingerprintsAndProteinTargets),
# and a dictionary mapping drugs to its index in allFingerprintsAndProteinTargets
# (drugIndexDictionary)
def getProteinsToDrugs(proteinList, allFingerprintsAndProteinTargets, drugIndexDictionary):
    proteinsToDrugs = []
    for protein in proteinList:
        singleProteinToDrug = []
        drugsBindProtein = getDrugsBindProtein(protein, allFingerprintsAndProteinTargets)
        singleProteinToDrug.append(protein)
        singleProteinToDrug.append(drugsBindProtein)
        proteinsToDrugs.append(singleProteinToDrug)
    return proteinsToDrugs

# Inputs:
#  -drugsBindProteinA: a list of drugs that bind to proteinA
#  -drugsBindProteinB: a list of drugs that bind to proteinB
#  -allFingerprintsAndTargets: a list of drugs mapped to its fingerprints
#   and targets
#  -drugIndexDictionary: a dictionary containing drugs mapped to index for
#   easy drug access in allFingerprintsAndTargets
# Returns:
#  -TSummary, a floating point number
def getTSummary(drugsBindProteinA, drugsBindProteinB, allFingerprintsAndTargets, drugIndexDictionary):
    TSummary = float(0.0)
    listOfTScores = [getTanimotoScore(drugA, drugB, allFingerprintsAndTargets, drugIndexDictionary) for drugA in drugsBindProteinA for drugB in drugsBindProteinB]
    TSummary += sum([tScore if tScore > 0.5 else 0 for tScore in listOfTScores])
    return TSummary

# Inputs:
#  -size: size of the drug list
#  -drugGrid: a grid containing drugs.csv info
# Returns:
#  -randomDrugList: a list of drugs randomly selected from drugGrid
def generateRandomDrugList(size, drugGrid):
    randomDrugList = []
    for i in range(0, size):
        randIndex = random.randint(0, len(drugGrid) - 1)
        randomDrugList.append(drugGrid[randIndex][0])
    return randomDrugList

# Inputs:
#  -drugGrid: a grid containing drugs.csv info
# Returns:
#  -list of drugs in drugGrid
def generateDrugList(drugGrid):
    drugList = []
    for druginfolist in drugGrid:
        drugList.append(druginfolist[0])
    return drugList

# Inputs:
#  -drugGrid: a grid containing drugs.csv info
#  -na: length of list of drugs binding proteinA
#  -nb: length of list of drugs binding proteinB
#  -allFingerprintsAndProteinTargets: a list of drugs mapped to its fingerprints
#   and protein targets
#  -drugIndexDictionary: a dictionary mapping drugs to indices in
#   allFingerprintsAndProteinTargets for easy access to drugs
# Returns:
#  -TBSummary, a double
def getTBSummary(drugGrid, na, nb, allFingerprintsAndProteinTargets, drugIndexDictionary):
    randDrugListA = generateRandomDrugList(na, drugGrid)
    randDrugListB = generateRandomDrugList(nb, drugGrid)
    TBSummary = getTSummary(randDrugListA, randDrugListB, allFingerprintsAndProteinTargets, drugIndexDictionary)
    return TBSummary

# Inputs:
#  -allFingerprintsAndProteinTargets: a list of drugs mapped to its fingerprints
#   and protein targets
#  -drugIndexDictionary: a dictionary mapping drugs to its index in
#   allFingerprintsAndProteinTargets
#  -proteinsToDrugs: a list of proteins mapped to a list of drugs that bind to
#   that protein
#  -proteinsToDrugsIndexDict: a dictionary mapping proteins to their indices in
#  -proteinsToDrugs
#  -drugGrid: a grid containing information in drugs.csv
#  -proteinA: a string with the ID of the first protein in question
#  -proteinB: a string with the ID of the second protein in question
#  -iterations: an int referencing the number of iterations to perform this
#   algorithm
# returns a bootstrap p-value, a double
# random number generator already seeded
def generateBootstrapPValue(allFingerprintsAndProteinTargets, drugIndexDictionary, proteinsToDrugs, proteinsToDrugsIndexDict, drugGrid, proteinA, proteinB, iterations):
    drugsBindProteinA = proteinsToDrugs[proteinsToDrugsIndexDict[proteinA]][1]
    drugsBindProteinB = proteinsToDrugs[proteinsToDrugsIndexDict[proteinB]][1]
    Tsummary = getTSummary(drugsBindProteinA, drugsBindProteinB, allFingerprintsAndProteinTargets, drugIndexDictionary)
    na = len(drugsBindProteinA)
    nb = len(drugsBindProteinB)
    TBSummarySum = 0
    listOfTBSummaries = [getTBSummary(drugGrid, na, nb, allFingerprintsAndProteinTargets, drugIndexDictionary) for i in range(0, iterations)]
    TBSummarySum += sum([1 if TBSummary >= Tsummary else 0 for TBSummary in listOfTBSummaries])
    pbootstrap = float(TBSummarySum) / iterations
    return pbootstrap

# Input:
#  -proteinNodesGrid: grid containing information from protein_nodes.csv
# Returns:
#  -a list of proteins
def generateListOfProteinsFromProteinNodesGrid(proteinNodesGrid):
    return [proteininfolist[0] for proteininfolist in proteinNodesGrid]
