from collections import defaultdict
from intcode import Intcode
import os

code = [2,380,379,385,1008,2119,899068,381,1005,381,12,99,109,2120,1101,0,0,383,1101,0,0,382,20101,0,382,1,20101,0,383,2,21101,37,0,0,1105,1,578,4,382,4,383,204,1,1001,382,1,382,1007,382,37,381,1005,381,22,1001,383,1,383,1007,383,20,381,1005,381,18,1006,385,69,99,104,-1,104,0,4,386,3,384,1007,384,0,381,1005,381,94,107,0,384,381,1005,381,108,1105,1,161,107,1,392,381,1006,381,161,1101,-1,0,384,1106,0,119,1007,392,35,381,1006,381,161,1101,0,1,384,20102,1,392,1,21102,1,18,2,21102,0,1,3,21101,0,138,0,1105,1,549,1,392,384,392,20102,1,392,1,21101,18,0,2,21101,0,3,3,21102,1,161,0,1105,1,549,1102,0,1,384,20001,388,390,1,20102,1,389,2,21101,0,180,0,1106,0,578,1206,1,213,1208,1,2,381,1006,381,205,20001,388,390,1,21002,389,1,2,21101,205,0,0,1105,1,393,1002,390,-1,390,1102,1,1,384,21002,388,1,1,20001,389,391,2,21102,1,228,0,1106,0,578,1206,1,261,1208,1,2,381,1006,381,253,20102,1,388,1,20001,389,391,2,21102,1,253,0,1106,0,393,1002,391,-1,391,1102,1,1,384,1005,384,161,20001,388,390,1,20001,389,391,2,21102,279,1,0,1106,0,578,1206,1,316,1208,1,2,381,1006,381,304,20001,388,390,1,20001,389,391,2,21102,1,304,0,1106,0,393,1002,390,-1,390,1002,391,-1,391,1102,1,1,384,1005,384,161,20101,0,388,1,20102,1,389,2,21101,0,0,3,21102,338,1,0,1106,0,549,1,388,390,388,1,389,391,389,21002,388,1,1,20101,0,389,2,21102,4,1,3,21102,1,365,0,1105,1,549,1007,389,19,381,1005,381,75,104,-1,104,0,104,0,99,0,1,0,0,0,0,0,0,251,16,15,1,1,18,109,3,22102,1,-2,1,21202,-1,1,2,21102,1,0,3,21101,0,414,0,1106,0,549,21201,-2,0,1,22102,1,-1,2,21102,1,429,0,1105,1,601,2102,1,1,435,1,386,0,386,104,-1,104,0,4,386,1001,387,-1,387,1005,387,451,99,109,-3,2106,0,0,109,8,22202,-7,-6,-3,22201,-3,-5,-3,21202,-4,64,-2,2207,-3,-2,381,1005,381,492,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,481,21202,-4,8,-2,2207,-3,-2,381,1005,381,518,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,507,2207,-3,-4,381,1005,381,540,21202,-4,-1,-1,22201,-3,-1,-3,2207,-3,-4,381,1006,381,529,22101,0,-3,-7,109,-8,2105,1,0,109,4,1202,-2,37,566,201,-3,566,566,101,639,566,566,1202,-1,1,0,204,-3,204,-2,204,-1,109,-4,2105,1,0,109,3,1202,-1,37,593,201,-2,593,593,101,639,593,593,21001,0,0,-2,109,-3,2105,1,0,109,3,22102,20,-2,1,22201,1,-1,1,21101,373,0,2,21102,698,1,3,21101,740,0,4,21101,630,0,0,1106,0,456,21201,1,1379,-2,109,-3,2106,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,2,2,0,2,2,0,2,2,2,2,2,2,2,2,2,2,0,0,2,0,0,2,2,0,2,0,2,2,2,0,1,1,0,2,2,2,0,2,2,0,2,2,2,2,2,2,2,2,2,2,2,2,0,2,0,2,2,2,2,2,2,0,2,0,0,0,0,1,1,0,0,0,0,2,2,2,2,0,2,0,0,2,2,0,0,2,2,2,0,2,2,2,0,2,2,0,2,0,2,0,2,0,2,0,1,1,0,2,2,2,2,0,2,2,2,2,2,2,0,2,2,2,2,2,2,2,0,2,2,0,0,2,2,2,0,0,0,2,2,2,0,1,1,0,0,2,2,2,2,2,2,2,2,0,2,0,2,2,0,0,2,2,2,0,2,2,0,2,2,2,0,2,0,0,0,0,2,0,1,1,0,2,2,0,2,0,0,2,2,0,2,2,0,2,2,0,2,2,2,2,2,2,2,2,0,0,0,2,2,2,0,2,2,0,0,1,1,0,2,2,2,0,0,2,2,2,2,0,2,2,0,0,2,2,2,2,0,2,0,2,2,2,2,2,2,2,2,0,2,0,0,0,1,1,0,0,0,2,2,2,2,0,2,2,2,0,2,2,0,2,2,0,2,2,2,0,2,2,0,0,0,2,2,0,2,2,0,0,0,1,1,0,0,2,0,2,0,0,0,2,2,0,2,0,0,0,2,0,0,2,2,0,2,2,2,0,2,2,2,0,2,0,2,2,0,0,1,1,0,2,2,2,2,2,0,0,2,0,2,2,0,2,2,2,0,0,0,2,2,2,0,0,2,2,0,2,2,2,0,2,2,0,0,1,1,0,0,2,2,2,2,0,0,2,0,0,2,2,2,2,0,2,2,2,0,0,0,2,0,0,0,2,2,0,2,0,2,2,2,0,1,1,0,2,2,0,0,0,2,2,2,0,0,2,0,0,0,0,2,2,2,2,0,2,0,2,2,0,0,2,0,0,2,2,2,2,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,7,6,62,46,97,31,39,45,95,95,98,48,29,84,17,69,15,63,97,49,94,40,66,35,55,30,26,68,72,37,25,72,98,71,57,16,63,47,30,4,9,59,42,34,51,23,13,79,75,82,84,39,54,12,3,73,15,28,7,59,29,93,5,36,1,53,52,40,32,60,96,1,35,3,79,92,40,97,77,29,86,62,31,66,46,29,45,96,18,38,8,65,28,74,37,96,59,46,7,41,47,11,94,49,74,67,5,64,14,75,50,61,42,93,61,4,75,42,56,36,38,49,24,58,81,2,25,62,68,27,94,81,65,54,8,36,56,5,97,27,78,78,94,33,75,11,1,1,41,52,92,8,26,66,58,10,85,33,34,87,41,81,24,4,5,11,18,97,65,25,47,39,36,61,59,21,75,5,29,93,81,33,17,96,58,3,22,67,87,87,4,96,37,11,74,21,55,51,67,47,40,29,96,49,89,72,96,64,31,88,47,49,51,91,46,42,37,27,58,40,73,49,3,36,98,19,65,14,78,96,97,70,58,45,66,67,43,66,65,44,84,40,85,39,87,57,90,72,77,38,59,90,91,67,19,14,63,1,89,21,53,40,53,16,62,20,74,62,72,45,29,87,48,81,39,89,21,14,49,56,53,76,58,75,40,96,11,12,60,41,13,53,53,77,3,66,6,16,7,64,75,22,21,29,22,78,63,15,2,66,53,19,2,1,83,11,61,34,53,53,40,66,88,78,40,59,46,49,21,38,69,54,52,20,89,27,82,54,2,69,27,35,65,37,13,27,84,69,64,49,95,36,88,58,16,86,74,82,45,33,27,81,16,10,3,33,62,80,37,40,24,60,27,27,72,53,89,45,48,42,80,96,27,81,22,25,39,70,31,29,50,38,96,30,7,66,93,20,83,57,57,98,10,16,58,63,8,26,72,94,67,55,1,98,4,50,51,88,97,95,97,40,58,97,97,36,72,58,76,64,48,11,94,1,97,34,30,13,36,8,14,6,70,86,91,18,41,66,37,59,71,38,86,74,89,96,19,69,85,26,68,86,59,31,90,76,82,11,74,83,29,34,74,37,25,31,6,85,60,44,43,11,73,24,6,91,7,96,3,41,58,9,29,3,89,36,19,66,66,12,35,46,14,24,56,87,71,16,94,27,88,7,18,22,30,52,90,42,18,39,45,68,54,50,74,27,42,1,24,30,5,60,24,20,91,33,57,55,60,6,58,52,27,13,85,98,27,8,67,66,33,16,33,15,88,73,75,51,90,90,27,88,32,60,20,34,86,67,38,83,76,19,67,36,63,50,56,41,37,40,37,34,75,52,82,60,25,57,62,82,34,53,82,1,49,9,24,35,22,86,60,14,75,63,14,5,37,75,96,21,64,39,74,7,59,8,42,96,7,14,43,76,62,70,16,30,3,36,62,77,68,95,60,19,45,7,62,14,24,30,91,91,26,11,73,2,74,8,60,17,96,74,5,88,72,85,41,57,47,22,42,4,52,42,48,73,52,43,87,49,29,49,24,97,76,30,34,75,24,58,23,54,4,73,56,84,11,77,60,59,78,5,5,79,45,94,47,49,84,38,54,48,86,76,27,23,42,73,42,2,64,33,63,70,1,86,5,1,77,43,16,34,61,44,28,76,34,76,16,89,56,72,12,28,37,38,5,23,13,49,899068]
#code = [2,380,379,385,1008,2655,455702,381,1005,381,12,99,109,2656,1101,0,0,383,1101,0,0,382,20102,1,382,1,21002,383,1,2,21101,37,0,0,1105,1,578,4,382,4,383,204,1,1001,382,1,382,1007,382,42,381,1005,381,22,1001,383,1,383,1007,383,24,381,1005,381,18,1006,385,69,99,104,-1,104,0,4,386,3,384,1007,384,0,381,1005,381,94,107,0,384,381,1005,381,108,1106,0,161,107,1,392,381,1006,381,161,1101,-1,0,384,1106,0,119,1007,392,40,381,1006,381,161,1102,1,1,384,21002,392,1,1,21102,1,22,2,21102,1,0,3,21101,138,0,0,1106,0,549,1,392,384,392,21001,392,0,1,21102,22,1,2,21102,3,1,3,21101,0,161,0,1106,0,549,1102,0,1,384,20001,388,390,1,20102,1,389,2,21102,180,1,0,1105,1,578,1206,1,213,1208,1,2,381,1006,381,205,20001,388,390,1,20101,0,389,2,21101,0,205,0,1106,0,393,1002,390,-1,390,1102,1,1,384,21002,388,1,1,20001,389,391,2,21101,0,228,0,1106,0,578,1206,1,261,1208,1,2,381,1006,381,253,21002,388,1,1,20001,389,391,2,21102,253,1,0,1105,1,393,1002,391,-1,391,1102,1,1,384,1005,384,161,20001,388,390,1,20001,389,391,2,21101,0,279,0,1106,0,578,1206,1,316,1208,1,2,381,1006,381,304,20001,388,390,1,20001,389,391,2,21102,304,1,0,1105,1,393,1002,390,-1,390,1002,391,-1,391,1102,1,1,384,1005,384,161,20102,1,388,1,21001,389,0,2,21101,0,0,3,21101,0,338,0,1106,0,549,1,388,390,388,1,389,391,389,20101,0,388,1,20102,1,389,2,21101,4,0,3,21102,365,1,0,1106,0,549,1007,389,23,381,1005,381,75,104,-1,104,0,104,0,99,0,1,0,0,0,0,0,0,268,19,19,1,1,21,109,3,21201,-2,0,1,21202,-1,1,2,21102,0,1,3,21101,0,414,0,1105,1,549,22101,0,-2,1,22102,1,-1,2,21101,0,429,0,1105,1,601,1202,1,1,435,1,386,0,386,104,-1,104,0,4,386,1001,387,-1,387,1005,387,451,99,109,-3,2105,1,0,109,8,22202,-7,-6,-3,22201,-3,-5,-3,21202,-4,64,-2,2207,-3,-2,381,1005,381,492,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,481,21202,-4,8,-2,2207,-3,-2,381,1005,381,518,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,507,2207,-3,-4,381,1005,381,540,21202,-4,-1,-1,22201,-3,-1,-3,2207,-3,-4,381,1006,381,529,22102,1,-3,-7,109,-8,2106,0,0,109,4,1202,-2,42,566,201,-3,566,566,101,639,566,566,2101,0,-1,0,204,-3,204,-2,204,-1,109,-4,2106,0,0,109,3,1202,-1,42,593,201,-2,593,593,101,639,593,593,21001,0,0,-2,109,-3,2105,1,0,109,3,22102,24,-2,1,22201,1,-1,1,21101,0,509,2,21102,684,1,3,21102,1,1008,4,21102,630,1,0,1106,0,456,21201,1,1647,-2,109,-3,2106,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,2,2,0,0,0,0,0,2,0,2,0,0,0,2,0,0,0,0,0,2,2,2,0,0,2,0,0,2,2,0,2,2,0,2,2,0,0,0,0,1,1,0,2,0,2,0,2,0,2,0,0,2,0,2,0,0,2,0,2,0,0,0,0,2,2,0,0,0,0,0,2,0,0,2,2,2,0,2,0,2,0,1,1,0,2,2,2,0,0,2,0,2,0,2,2,0,0,0,2,2,2,2,0,0,0,0,2,0,2,2,0,2,2,2,0,0,0,2,0,2,2,2,0,1,1,0,0,0,0,2,2,2,2,0,0,0,2,2,2,0,2,2,2,0,2,0,2,2,0,0,0,2,2,2,0,0,0,0,0,2,2,2,0,0,0,1,1,0,2,0,2,0,0,0,0,0,0,0,2,2,0,2,0,2,2,2,2,2,2,0,2,0,0,2,0,2,0,0,2,2,2,0,0,2,0,0,0,1,1,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,2,0,2,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,2,2,2,2,2,0,2,2,2,2,2,0,0,0,2,0,2,0,0,2,0,0,2,2,0,2,0,2,0,2,0,2,2,2,2,0,2,0,0,1,1,0,2,0,0,2,2,2,2,0,2,2,2,0,0,0,0,2,0,2,0,0,2,0,0,2,2,0,0,0,0,0,2,2,0,0,0,2,0,0,0,1,1,0,2,0,0,0,0,2,0,2,0,2,0,2,0,2,2,0,0,2,0,0,0,0,2,2,2,2,0,2,0,0,2,2,0,0,2,0,0,0,0,1,1,0,0,2,0,0,0,2,0,2,2,2,0,2,2,0,2,2,2,0,0,0,2,0,2,0,2,2,0,0,2,0,0,0,0,2,0,2,2,0,0,1,1,0,0,0,0,0,0,2,0,2,0,2,0,0,0,2,2,0,2,0,2,0,2,2,2,2,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0,1,1,0,2,2,2,2,2,0,0,0,0,0,2,0,2,0,2,0,0,0,0,2,0,2,0,0,2,2,0,0,2,2,0,2,0,0,2,0,0,2,0,1,1,0,2,0,0,0,2,0,0,0,2,2,0,2,2,0,0,0,0,0,0,0,0,2,0,2,0,0,2,2,0,2,0,0,2,0,0,2,2,2,0,1,1,0,0,0,0,0,2,2,2,0,0,0,0,0,2,0,2,2,0,2,2,0,2,0,2,0,0,0,0,0,2,0,2,2,0,0,0,2,2,2,0,1,1,0,2,2,2,0,0,0,2,0,2,2,0,0,0,2,2,0,2,0,0,0,2,2,2,0,2,0,2,0,0,2,0,2,0,2,2,0,0,0,0,1,1,0,2,2,0,2,0,0,2,2,2,0,2,2,0,0,0,0,2,0,2,0,0,0,2,0,2,2,0,0,0,0,0,0,2,2,2,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,23,82,82,16,37,71,32,87,51,93,33,83,22,21,23,36,43,97,16,24,33,77,54,2,88,59,72,36,26,90,26,4,4,44,42,14,5,40,27,7,27,96,27,74,43,17,90,6,85,69,21,28,82,82,81,53,95,14,84,70,92,51,29,86,83,44,37,36,54,77,1,26,33,92,46,74,43,10,96,73,31,32,22,66,14,89,2,72,97,3,16,22,31,24,90,87,18,18,42,55,82,38,2,64,38,22,49,39,32,23,14,58,15,24,65,7,28,88,15,81,20,18,70,5,98,56,60,9,47,94,7,51,18,90,27,74,50,45,81,86,73,75,89,56,63,34,15,72,48,86,77,66,47,91,18,89,25,51,41,2,57,52,84,84,44,76,7,15,97,56,59,50,73,94,81,7,4,95,32,82,97,36,60,38,5,51,60,65,51,27,45,5,82,35,7,30,63,44,9,95,29,70,88,63,48,56,12,40,44,28,94,25,48,72,28,95,83,46,48,67,42,23,23,76,34,25,84,40,39,69,6,40,28,42,15,19,92,9,91,94,22,51,31,19,39,42,60,63,16,29,46,69,52,7,79,59,33,90,93,61,59,9,98,1,13,24,74,70,35,12,50,54,67,83,18,88,52,49,40,19,59,54,33,62,66,82,65,63,29,93,14,7,57,56,87,52,41,28,46,14,70,69,94,25,88,59,7,45,18,73,11,41,20,42,7,25,36,88,76,42,57,65,84,21,12,71,25,94,38,5,71,60,61,92,24,32,18,36,12,74,57,95,59,30,94,88,30,30,9,96,25,80,88,27,89,89,48,84,23,11,50,45,53,81,18,57,94,50,57,26,87,33,3,50,71,96,71,89,49,29,45,6,74,32,98,23,27,7,92,29,93,82,84,95,98,1,74,59,10,92,63,60,54,34,70,4,60,59,7,30,70,8,53,52,23,46,7,26,88,40,51,77,12,32,33,34,46,79,4,33,33,10,16,7,23,90,74,90,93,78,6,21,40,77,64,76,74,58,7,26,18,74,90,82,40,68,60,18,45,16,59,96,48,7,96,49,60,48,88,42,63,30,18,8,96,88,36,38,82,96,17,72,76,23,98,45,74,26,42,69,11,56,26,59,67,33,98,62,73,7,59,22,17,48,89,14,1,47,28,43,95,91,33,62,15,77,81,29,6,81,20,55,1,51,19,40,25,52,43,19,91,47,59,21,88,73,80,65,62,57,19,80,1,40,74,33,30,95,73,68,92,26,86,22,12,33,30,23,14,79,52,42,2,61,32,3,55,10,10,4,71,4,6,22,36,39,8,14,11,92,61,74,12,15,16,77,50,8,7,1,38,40,11,87,11,96,52,74,69,34,63,48,45,92,71,60,6,58,47,23,25,64,50,98,48,80,27,76,31,66,91,3,74,9,59,97,45,98,18,74,45,9,7,29,97,64,57,54,19,61,37,41,14,62,55,92,79,16,85,53,78,85,93,30,94,5,51,34,25,64,21,21,79,16,59,12,68,50,39,59,62,17,40,51,42,26,51,60,87,21,37,97,45,23,43,27,7,9,25,48,54,37,45,34,7,58,86,8,48,91,88,56,94,7,80,80,15,83,91,23,92,23,29,36,62,50,2,45,9,94,96,93,60,18,96,83,40,13,19,28,69,26,66,75,36,98,35,39,70,58,67,72,78,59,57,60,18,60,41,97,94,39,11,18,70,63,24,5,19,41,92,27,88,81,28,37,36,92,51,23,32,69,95,8,66,67,59,49,31,16,65,17,23,57,71,75,20,63,36,62,32,82,26,73,57,93,69,27,20,91,72,23,44,86,94,59,23,49,15,7,4,69,64,59,77,37,50,42,64,88,3,4,23,47,60,46,72,22,78,46,12,18,30,18,19,74,80,93,43,10,73,15,59,47,37,53,16,57,43,72,81,4,55,40,33,14,16,85,61,90,72,40,79,96,24,94,75,14,59,7,76,52,13,87,53,10,87,95,4,51,13,89,68,34,68,15,31,60,64,21,41,84,12,90,6,5,85,77,94,10,8,18,61,39,80,90,78,13,16,13,36,48,28,71,91,90,35,20,60,98,44,18,88,69,22,71,27,79,54,38,25,8,6,94,36,3,57,10,58,92,6,88,62,19,67,47,79,95,71,6,68,37,16,28,89,34,72,56,65,11,35,10,83,24,51,41,40,31,12,84,68,41,44,56,73,46,59,93,98,3,71,12,90,26,80,88,97,64,18,24,75,34,85,53,39,62,69,58,13,17,91,53,89,58,34,87,64,43,455702]
seen = set()
tiles = dict()

index = 0
X = 0
Y = 0
outputCounter = 0

computer = Intcode(code)

walls = set()
blocks = set()
blocks.add((-1, -1))
paddle = (0, 0)
ball = (0, 0)
score = 0
started = False

def output():
    os.system('cls')
    for y in range(100):
        l = ""
        for x in range(50):
            if (x,y) == ball: l += "O"
            elif (x,y) in blocks: l += "#"
            elif (x,y) in walls: l += "X"
            elif (x,y) == paddle: l += "-"
            else: l += " "
        print(l)

while True:
    out = ""
    inp = 0
    if (ball[0] < paddle[0]): inp = -1
    elif (ball[0] > paddle[0]): inp = 1

    while out == "" and not computer.isTerminated():
        out = computer.next(inp)[1]
    x = out
    out = ""
    while out == "" and not computer.isTerminated():
        out = computer.next(inp)[1]
    y = out
    out = ""
    while out == "" and not computer.isTerminated():
        out = computer.next(inp)[1]
    t = out

    if (x == -1):
        print("SCORE:", t)
        score = t
    elif (t == 1): walls.add((x,y))
    elif (t == 2):
        blocks.add((x,y))
        started = True
    elif (t == 3): paddle = (x,y)
    elif (t == 4): ball = (x, y)

#    if ball in blocks: blocks.remove(ball)
#    print(ball)

#    output()

    if (started and len(blocks) == 0): break

print(score)
#print(min())