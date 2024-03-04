class Term(object) :
    def __init__(self, coefficient : int, exponent : int)->None:
        self.coefficient=coefficient
        self.exponent=exponent
        self.next=None
        
        
class Polynomial(object):
    def __init__(self) -> None:
        self.headTerm=None
        
    def insert(self, coefficient: int, exponent:int):
        if coefficient == 0:
            return
        
        newTerm=Term(coefficient=coefficient, exponent=exponent)
        
        if not self.headTerm:
            self.headTerm=newTerm
        else:
            currentTerm=self.headTerm
            while(currentTerm.next!=None):
                currentTerm=currentTerm.next
            
            currentTerm.next=newTerm
            newTerm.next=None
            
    def build(self, terms):
        for term in terms:
            coefficient, exponent = term
            self.insert(coefficient=coefficient, exponent=exponent)
            
    def display(self):
        currentTerm=self.headTerm
        while(currentTerm!=None):
            if currentTerm.exponent==0:
                print(currentTerm.coefficient, end=" ")
            else:
                print(f"{currentTerm.coefficient}x^{currentTerm.exponent}", end=" ")
            if currentTerm.next is not None:
                print(f"+", end=" ")
            currentTerm=currentTerm.next
        print()
        
        
        
    def add(self, polynomialExpression):
        result = Polynomial()
        currentSelf = self.headTerm
        currentOther = polynomialExpression.headTerm

        while currentSelf and currentOther:
            if currentSelf.exponent == currentOther.exponent:
                result.insert(currentSelf.coefficient + currentOther.coefficient, currentSelf.exponent)
                currentSelf = currentSelf.next
                currentOther = currentOther.next
            elif currentSelf.exponent > currentOther.exponent:
                result.insert(currentSelf.coefficient, currentSelf.exponent)
                currentSelf = currentSelf.next
            else:
                result.insert(currentOther.coefficient, currentOther.exponent)
                currentOther = currentOther.next
        
        while currentSelf:
            result.insert(currentSelf.coefficient, currentSelf.exponent)
            currentSelf = currentSelf.next
        
        while currentOther:
            result.insert(currentOther.coefficient, currentOther.exponent)
            current_other = current_other.next
        
        return result
    
    def sub(self, polynomialExpression):
        result = Polynomial()
        currentSelf = self.headTerm
        currentOther = polynomialExpression.headTerm

        while currentSelf and currentOther:
            if currentSelf.exponent == currentOther.exponent:
                result.insert(currentSelf.coefficient - currentOther.coefficient, currentSelf.exponent)
                currentSelf = currentSelf.next
                currentOther = currentOther.next
            elif currentSelf.exponent > currentOther.exponent:
                result.insert(currentSelf.coefficient, currentSelf.exponent)
                currentSelf = currentSelf.next
            else:
                result.insert(-currentOther.coefficient, currentOther.exponent)
                currentOther = currentOther.next
        
        while currentSelf:
            result.insert(currentSelf.coefficient, currentSelf.exponent)
            currentSelf = currentSelf.next
        
        while currentOther:
            result.insert(-currentOther.coefficient, currentOther.exponent)
            current_other = current_other.next
        
        return result
        
        
    def mul(self, polynomialExpression):
        result = Polynomial()

        currentSelf = self.headTerm
        while currentSelf:
            currentOther = polynomialExpression.headTerm
            while currentOther:
                coefficient = currentSelf.coefficient * currentOther.coefficient
                exponent = currentSelf.exponent + currentOther.exponent
                result.insert(coefficient, exponent)
                currentOther = currentOther.next
            currentSelf = currentSelf.next

        return result
        
        
        



P = Polynomial()
Q = Polynomial()

terms_P = [(2, 2), (3, 1), (4, 0)]
terms_Q = [(2, 3), (3, 2), (4, 1), (9, 0)]

P.build(terms_P)
Q.build(terms_Q)

R = P.mul(Q)
print("Polynomial R(x) after  P(x) - Q(x): ", end='')
R.display()




