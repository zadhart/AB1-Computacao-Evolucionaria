from secrets import randbelow

operands = ["p", "q", "r"]
operators = [" and ", " or "]


class Population:
    def __init__(self, size):
        self.pop_size = size
        self.pop_gen = 0
        self.individuals = []
        self.ogtable = [False, True, False, False, False, False, False, False]

    def genIndividual(self):
        stack = []
        expression = []
        n = randbelow(5) + 3
        for j in range(n):
            k = randbelow(3)
            no = randbelow(100)
            p = randbelow(100)
            o = randbelow(2)
            if no % 4 == 0:
                expression.append(" not ")
            expression.append("(")
            expression.append(operands[k])
            stack.append("(")
            if p % 4 == 0 and stack != []:
                expression.append(")")
                stack.pop()

            if j == n - 1:
                if len(stack) > 0:
                    for i in stack:
                        expression.append(")")
            else:
                expression.append(operators[o])

        individual = Individual(expression)
        if not individual.pqrMonster():
            self.individuals.append(individual)

    def firtsGen(self):
        index = 0
        while index < self.pop_size:
                self.genIndividual()
                index += 1

    def solveExpressions(self):
        for individual in self.individuals:
            individual.atributePQR(1)
            individual.getAdaptation(self.ogtable)
            self.sort()
            if individual.adaptation == 8:
                print("".join(individual.table_op))
                print(individual.table_results)
                return True
            return False

    def crossing(self):
        pass

    def mutating(self, individual):
        aux1 = [" and ", " or "]
        aux2 = ["p", "q", "r"]
        i = randbelow(len(individual.table_op))
        if individual.table_op[i] in aux1:
            aux1.remove(individual.table_op[i])
            individual.table_op[i] = aux1[0]
        elif individual.table_op[i] in aux2:
            aux2.remove(individual.table_op[i])
            n = randbelow(2)
            individual.table_op[i] = aux2[n]
        elif individual.table_op[i] == "not":
            del (individual.table_op[i])

        else:
            return self.mutating(individual)

        if individual.pqrMonster():
            return self.mutating(individual)
        return individual.table_op

    def sort(self):
        aux = []
        new = []
        for individual in self.individuals:
            aux.append(individual.adaptation)
        aux.sort(reverse=True)
        for a in aux:
            for individual in self.individuals:
                if individual.adaptation == a:
                    new.append(individual)
                    self.individuals.remove(individual)
                    break
        self.individuals = new

    def eliteSelection(self):
        topfive = []
        new = []
        for i in range(5):
            topfive.append(self.individuals[i])
            j = 0
            while j < 10:
                nindivididual = Individual(self.mutating(self.individuals[i]))
                if nindivididual not in new:
                    new.append(nindivididual)
                    j += 1
        self.individuals = new

        for x in range(50):
            self.genIndividual()

        self.pop_size = len(new)
        self.pop_gen += 1



class Individual:
    def __init__(self, table):
        self.table_results = []
        self.table_op = table
        self.adaptation = 0
        self.p = True
        self.q = True
        self.r = True

    def calcExpression(self):
        expression = []
        for i in self.table_op:
            expression.append(i)
        for i in range(len(expression)):
            if expression[i] == "p":
                expression[i] = " " + str(self.p) + " "
            elif expression[i] == "q":
                expression[i] = " " + str(self.q) + " "
            elif expression[i] == "r":
                expression[i] = " " + str(self.r) + " "
        string = "".join(expression)
        # print(string)
        result = eval(string)
        # print(result)
        self.table_results.append(result)

    def atributePQR(self, n):
        self.p = True
        self.q = True
        self.r = True
        if n <= 8:
            if n > 4:
                self.p = False
                # print("testep")
            if n in range(3, 5) or n in range(7, 9):
                self.q = False
                # print("testeq")
            if n % 2 == 0:
                self.r = False
                # print("tester")
            self.calcExpression()
            self.atributePQR(n + 1)
        else:
            return

    def parenthesisMonster(self):
        stack = []
        for i in self.table_op:
            if i == "(":
                stack.append(i)
            elif i == ")":
                if len(stack) == 0:
                    return 1
                else:
                    stack.pop()
        if len(stack) > 0:
            return 1
        return 0

    def pqrMonster(self):
        if "p" not in self.table_op:
            return True
        elif "q" not in self.table_op:
            return True
        elif "r" not in self.table_op:
            return True
        else:
            return False

    def getAdaptation(self, ogtable):
        for i in range(0, 8):
            # print(ogtable[i], self.table_results[i])
            if ogtable[i] == self.table_results[i]:
                self.adaptation += 1


# individualteste = Individual(["(", "p", "and", "q", ")", "or", " not ", "r"])
# individualteste.atributePQR(1)
# print(individualteste.table_results)
def main(size):
    pop = Population(size)
    pop.firtsGen()
    while not pop.solveExpressions():
        print(f"geração {pop.pop_gen} tamanho{pop.pop_size}")
        pop.eliteSelection()


main(100)