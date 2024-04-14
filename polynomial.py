"""The polinom"""

class Mono:
    """
    Represents a monomial in a polynomial.
    """

    def __init__(self, coefficient, degree) -> None:
        """
        Initializes a Mono object.

        """
        if not coefficient:
            self.coefficient = 0
            self.degree = 0
        else:
            self.coefficient = coefficient
            self.degree = degree
        self.next = None

    def __str__(self) -> str:
        """
        Returns a string representation of the monomial.

        """
        if not self.coefficient:
            return "Mono: 0"
        if not self.degree:
            return f"Mono: {self.coefficient}"
        output_str = "Mono: "
        output_str += "-" if self.coefficient == -1 else str(self.coefficient) \
        if self.coefficient != 1 else ''
        output_str += f"x**{self.degree}" if self.degree != 1 else "x"
        return output_str

    def __repr__(self) -> str:
        """
        Returns a string representation of the monomial for debugging.

        """
        return f"Mono(coeff={self.coefficient}, degree={self.degree})"

    def __eq__(self, value: object) -> bool:
        """
        Checks if two monomials are equal.

        """
        return (self.coefficient, self.degree) == (value.coefficient, value.degree)

    def __lt__(self, value: object) -> bool:
        """
        Checks if one monomial is less than another.

        """
        if self.degree == 0 and value.degree == 0:
            return self.coefficient < value.coefficient
        return self.degree < value.degree


class Polynomial:
    """
    Represents a polynomial.

    """

    def __init__(self, *args) -> None:
        """
        Initializes a Polynomial object.

        """
        self.head = Mono(666, 666)
        def get_monos(args, head):
            node = head
            for i in args:
                if isinstance(i, Polynomial):
                    while node.next:
                        node = node.next
                    node.next = another_copy(i.head)
                else:
                    while node.next:
                        node = node.next
                    node.next = Mono(i.coefficient, i.degree)
            return head.next

        def another_copy(node):
            output_node = node
            output_head = Mono(666, 666)
            current_output = output_head
            while output_node:
                current_output.next = Mono(output_node.coefficient, output_node.degree)
                current_output = current_output.next
                output_node = output_node.next
            return output_head.next

        self.head = get_monos(args, another_copy(self.head))
        # degree = 0
        # node = self.head
        # while node:
        #     if node.degree > degree:
        #         degree = node.degree
        #     node = node.next
        # self.degree = degree
        # print(self.degree)

    @property
    def degree(self):
        degree = 0
        node = self.head
        while node:
            if node.degree > degree:
                degree = node.degree
            node = node.next
        # print(degree)
        return degree

    def __str__(self) -> str:
        """
        Returns a string representation of the polynomial.

        """
        node, output_str = self.head, ""
        while node:
            if node.coefficient == 0:
                node = node.next
                continue
            output_str += str(node)[6:] + "+"
            node = node.next
        if not output_str:
            return "Polynomial: 0"
        if output_str[0] == "0":
            output_str = output_str[1:]
        return f"Polynomial: {output_str[:-1].replace('+-', '-')}"

    def __repr__(self) -> str:
        """
        Returns a string representation of the polynomial for debugging.

        """
        node, output_str= self.head, ""
        while node:
            output_str += repr(node) + " -> "
            node = node.next
        return "Polynomial(" + output_str[:-4] + ")"

    def copy(self):
        """
        Creates a deep copy of the polynomial.

        """
        output_node = self.head
        mmm = Polynomial(Mono(666, 666))
        output_head = Mono(666, 666)
        current_output = output_head
        while output_node:
            current_output.next = Mono(output_node.coefficient, output_node.degree)
            current_output = current_output.next
            output_node = output_node.next
        mmm.head = output_head.next
        return mmm

    def sort(self):
        """
        Sorts the polynomial by degree.

        """
        current_head = self.copy()
        current_node = current_head.head
        output_head = Polynomial(Mono(666, 666))
        count = 0
        while current_node:
            # print(current_node)
            if current_node.coefficient == 0:
                count += 1
                current_head.head = delete_node(current_head.head, Mono(0, 0))
                # current_node = current_node.next
            else:
                max_node = current_node
                next_node = current_node.next
                while next_node:
                    if next_node > max_node:
                        max_node = next_node
                    next_node = next_node.next
                output_head.append(Mono(max_node.coefficient, max_node.degree))
                current_head.head = delete_node(current_head.head, max_node)
            current_node = current_head.head
        for _ in range(count):
            output_head.append(Mono(0, 0))
        self.head = output_head.head.next





    def append(self, mono):
        """
        Appends a monomial to the polynomial.

        """
        node = self.head
        while node.next:
            node = node.next
        node.next = mono


    def simplify(self):
        """
        Simplifies the polynomial by combining like terms.
        """
        self.sort()
        node = self.head
        while node.next:
            if node.degree == node.next.degree:
                node.coefficient += node.next.coefficient
                if node.coefficient == 0:
                    node.degree = 0
                node.next = node.next.next
            elif node.next.coefficient == 0:
                node.next = node.next.next
                node = node.next
            else:
                node = node.next
            if not node:
                break
        current_node = self.head
        if not current_node:
            return
        while current_node.next:
            if current_node.next.coefficient == 0:
                current_node.next = current_node.next.next
            current_node = current_node.next
            if not current_node:
                return
    def eval_at(self, number):
        """
        Evaluates the polynomial at a given number.


        """
        output = 0
        node = self.head
        while node:
            output += node.coefficient*(number**node.degree)
            node = node.next
        return output

    def __eq__(self, value: object) -> bool:
        """
        Checks if two polynomials are equal.

        """
        if isinstance(value, Polynomial):
            return self.eval_at(100) == value.eval_at(100)
        return False

    def __hash__(self) -> int:
        """
        Returns the hash value of the polynomial.

        """
        return hash(self.eval_at(69))

    @property
    def derivative(self):
        """
        Returns the derivative of the polynomial.

        """
        copy_head = self.copy()
        node = copy_head.head
        while node:
            node.coefficient *= node.degree
            node.degree -= 1
            node = node.next
        copy_head.simplify()
        return copy_head

    def __add__(self, other):
        """
        Adds two polynomials.

        """
        copy_self, copy_other = self.copy(), other.copy()
        output = Polynomial(copy_self, copy_other)
        output.simplify()
        return output

    def __sub__(self, other):
        """
        Subtracts one polynomial from another.

        """
        copy_self, copy_other = self.copy(), other.copy()
        current_other = copy_other.head
        while current_other:
            current_other.coefficient *= -1
            current_other = current_other.next
        output = Polynomial(copy_other) + copy_self
        return output

    def __mul__(self, other):
        """
        Multiplies two polynomials or a polynomial by a scalar.

        """
        if isinstance(other, Polynomial):
            copy_self, copy_other = self.copy(), other.copy()
            output_mono = Polynomial(Mono(666, 666))
            curr_output_mono = output_mono.head
            current_node = copy_self.head
            while current_node:
                mul_node = copy_other.head
                while mul_node:
                    curr_output_mono.next = Mono(current_node.coefficient * mul_node.coefficient, \
            current_node.degree + mul_node.degree if mul_node.degree != 0 else current_node.degree)
                    mul_node = mul_node.next
                    curr_output_mono = curr_output_mono.next
                current_node = current_node.next
            output_mono.head = output_mono.head.next
            output_mono.simplify()
            return output_mono
        copy_self = self.copy()
        current_node = copy_self.head
        while current_node:
            current_node.coefficient *= other
            current_node = current_node.next
        return copy_self

    def __rmul__(self, other):
        """
        Multiplies a scalar by a polynomial.

        """
        return self.__mul__(other)

    def __truediv__(self, other):
        output_pol = Polynomial(Mono(0, 0))
        copy_other, copy_self = other.copy(), self.copy()
        copy_other.simplify()
        copy_self.simplify()
        other_lenght = 0
        current_other = copy_other.head

        while current_other:
            other_lenght += 1
            current_other = current_other.next

        while copy_other.degree <= copy_self.degree:
            cache_self = Polynomial(Mono(0, 0))
            count = 0
            current_self = copy_self.head

            while count != other_lenght:
                cache_self += Polynomial(Mono(current_self.coefficient, current_self.degree))
                current_self = current_self.next
                count += 1
            
            div_poli = Polynomial(Mono(cache_self.head.coefficient / copy_other.head.coefficient, cache_self.degree - copy_other.degree))
            copy_self = copy_self - (div_poli * other)
            copy_self.simplify()
            output_pol += div_poli
            if output_pol == self:
                return output_pol, Polynomial(Mono(0, 0))
        return output_pol, copy_self

            
            



def delete_node(head, value):
    if head is None:
        return head

    if head.coefficient == value.coefficient and head.degree == value.degree:
        return head.next

    current = head
    while current.next is not None:
        if current.next.coefficient == value.coefficient and current.next.degree == value.degree:
            current.next = current.next.next
            break
        current = current.next

    return head

def test_polynomial():
    """
    Test Polynomial Basics
    """
    # Firstly, let's create Mono class
    # (a polynomial which has only one term).
    # It has similar structure as Node
    # for LinkedList.
    # For 5x^2 it would be:
    m1 = Mono(5, 2)
    assert m1.coefficient == 5
    assert m1.degree == 2
    assert m1.next is None
    assert str(m1) == "Mono: 5x**2"
    assert repr(m1) == 'Mono(coeff=5, degree=2)'

    m2 = Mono(5, 0)
    assert m2.coefficient == 5
    assert m2.degree == 0
    assert m2.next is None
    assert str(m2) == "Mono: 5"
    assert repr(m2) == 'Mono(coeff=5, degree=0)'

    m3 = Mono(1, 1)
    assert m3.coefficient == 1
    assert m3.degree == 1
    assert m3.next is None
    assert str(m3) == "Mono: x"
    assert repr(m3) == 'Mono(coeff=1, degree=1)'

    # If monomial has a zero coefficient,
    # it is always has 0 degree.
    m4 = Mono(0, 2)
    assert m4.coefficient == 0
    assert m4.degree == 0
    assert m4.next is None
    assert str(m4) == "Mono: 0"
    assert repr(m4) == 'Mono(coeff=0, degree=0)'

    # now we are ready to create polynomial
    p1 = Polynomial(m1, m2, m3)
    assert p1.head == m1
    assert p1.head.next == m2
    assert p1.head.next.next == m3
    assert str(p1) == "Polynomial: 5x**2+5+x"
    assert repr(p1) == 'Polynomial(Mono(coeff=5, degree=2) -> Mono(coeff=5, degree=0) -> Mono(coeff=1, degree=1))'

    # The degree of polynomial is the largest power
    # of x.
    assert p1.degree == 2

    # The polynomial constructor must be non-destructive
    assert m1.next is None
    assert m2.next is None
    assert m3.next is None

    p2 = Polynomial(Mono(-5, 2), Mono(-3, 1))
    assert str(p2) == "Polynomial: -5x**2-3x"
    assert p2.degree == 2

    p3 = Polynomial(Mono(-5, 1), Mono(3, 1))
    assert str(p3) == "Polynomial: -5x+3x"
    assert p3.degree == 1

    p4 = Polynomial(Mono(0, 2), Mono(-3, 1))
    assert str(p4) == "Polynomial: -3x"
    assert p4.degree == 1

    # we also can use polynomials to create
    # the new polynomial
    p5 = Polynomial(m1, Polynomial(m2, m3))
    assert p5.head == m1
    assert p5.head.next == m2
    # print(p5)
    assert p5.head.next.next == m3
    assert str(p5) == "Polynomial: 5x**2+5+x"

    # or even polynomial in polynomial inside
    p6 = Polynomial(m1, Polynomial(m2, Polynomial(m3)))
    assert p6.head == m1
    assert p6.head.next == m2
    assert p6.head.next.next == m3
    assert str(p6) == "Polynomial: 5x**2+5+x"

    # We can create the copy of Polynomial
    p_6 = p6.copy()
    assert repr(p_6) == repr(p6), (repr(p_6), repr(p6))
    assert p_6 is not p6

    # Also we can write the polynomial in a
    # canonical way, where the degrees of x are
    # in descending order. This action is
    # destructive one.
    assert str(p1) == "Polynomial: 5x**2+5+x"
    p1.sort()
    assert str(p1) == "Polynomial: 5x**2+x+5", str(p1)

    assert str(p3) == "Polynomial: -5x+3x"
    p3.sort()
    assert str(p3) == "Polynomial: -5x+3x", str(p3)


    # all Mono with 0 degree and 0 coefficient
    # must be at the end after sorting.
    p7 = Polynomial(m1, m4, m3)
    assert str(p7) == "Polynomial: 5x**2+x"
    assert repr(p7) == 'Polynomial(Mono(coeff=5, degree=2) -> Mono(coeff=0, degree=0) -> Mono(coeff=1, degree=1))'
    p7.sort()
    assert repr(p7) == 'Polynomial(Mono(coeff=5, degree=2) -> Mono(coeff=1, degree=1) -> Mono(coeff=0, degree=0))'

    # Also for a lot of operations (as +, -, *)
    # it is better to simplify the polynomial
    # (combine like terms). This action destructive
    # too.
    assert str(p3) == "Polynomial: -5x+3x"
    p3.simplify()
    assert str(p3) == "Polynomial: -2x"
    # also all Mono with 0 degree and 0 coefficient
    # should be deleted by simplifying method.
    assert repr(p7) == 'Polynomial(Mono(coeff=5, degree=2) -> Mono(coeff=1, degree=1) -> Mono(coeff=0, degree=0))'
    p7.simplify()
    assert repr(p7) == 'Polynomial(Mono(coeff=5, degree=2) -> Mono(coeff=1, degree=1))'

    # Just a few more examples
    p8 = Polynomial(Mono(-5, 2), Mono(-3, 1), Mono(-3, 2), Mono(2, 1), Mono(1, 1))
    assert str(p8) == "Polynomial: -5x**2-3x-3x**2+2x+x"
    assert p8.degree == 2
    p8.sort()
    assert str(p8) == "Polynomial: -5x**2-3x**2-3x+2x+x"
    p8.simplify()
    assert str(p8) == "Polynomial: -8x**2"

    # p.eval_at(x) returns the polynomial evaluated at that value of x
    assert str(p1) == "Polynomial: 5x**2+x+5"
    assert p1.eval_at(0) == 5
    assert p1.eval_at(2) == 27
    assert str(p2) == "Polynomial: -5x**2-3x"
    assert p2.eval_at(0) == 0
    assert p2.eval_at(2) == -26

    # Use mathematical reason for two polynomials
    # to be equal.
    assert Polynomial(m1, m2, m3) == Polynomial(m3, m2, m1)
    assert Polynomial(m1, m2, m3) == p1
    assert Polynomial(m1, m1, m2) == Polynomial(m2, Polynomial(m1, m1))

    assert Polynomial(m1, m2, m3) != Polynomial(m1, m2)
    assert Polynomial(m1, m2, m3) != 42
    assert Polynomial(Mono(0, 2), Mono(0, 0), Mono(0, 1)) == Polynomial(Mono(0, 1))

    # It can be par of the set
    s = set()
    p6 = Polynomial(m1, m2, m3)
    p7 = Polynomial(m3, m2, m1)
    assert p6 not in s
    s.add(p6)
    assert p6 in s
    assert p7 in s

    # p.derivative will return a new polynomial that is the derivative
    # of the original, using the power rule.
    assert str(p1) == "Polynomial: 5x**2+x+5"
    p8 = p1.derivative
    assert isinstance(p8, Polynomial)
    assert str(p8) == "Polynomial: 10x+1"

    p9 = p2.derivative
    assert str(p9) == 'Polynomial: -10x-3'

    # Derivative is always in a canonical
    # (simplified) form.
    assert str(p5) == "Polynomial: 5x**2+5+x"
    assert str(p5.derivative) == "Polynomial: 10x+1"
    #but it doesn't change the origin polynomial.
    assert str(p5) == "Polynomial: 5x**2+5+x"

    # we can add polynomials together, which will add the coefficients
    # of any terms with the same degree, and return a new polynomial.
    # And it is not distructive.
    p10 = p1 + p9  # (5x**2+x+5) + (-10x-3) == (5x**2-9x+2)
    assert isinstance(p10, Polynomial)
    assert repr(p10) == "Polynomial(Mono(coeff=5, degree=2) -> Mono(coeff=-9, degree=1) -> Mono(coeff=2, degree=0))"
    assert str(p10) == "Polynomial: 5x**2-9x+2"
    assert str(p1) == "Polynomial: 5x**2+x+5"

    p10 = p1 - p9
    assert isinstance(p10, Polynomial)
    assert str(p10) == "Polynomial: 5x**2+11x+8"
    assert str(p1) == "Polynomial: 5x**2+x+5"

    # We can multiply polynomials, which will multiply the
    # coefficients of two polynomials and return a new polynomial with the
    # correct coefficients.
    p11 = p1*p9 # (5x**2+x+5) * (-10x-3) == (-50x**3-25x**2-53*x-15)
    assert isinstance(p11, Polynomial)
    assert str(p11) == "Polynomial: -50x**3-25x**2-53x-15"

    #And, of course, we can multiply by numbers
    p12 = p9*3
    assert isinstance(p11, Polynomial)
    assert str(p12) == "Polynomial: -30x-9"

    p13 = 3*p9
    assert p13 == p12


    assert Polynomial(m1, m1) == 2*Polynomial(m1)
    assert Polynomial(m1, m1, m1) == 3*Polynomial(m1)

    p14 = Polynomial(p1*p9)
    assert p14 == p11

        # we also can divide polynomials
    # and as a result obtain the tuple
    # of two polynomials: the quotient
    # and the remainder.
    # For example

    assert str(p14) == 'Polynomial: -50x**3-25x**2-53x-15'
    assert str(p9) == 'Polynomial: -10x-3'
    #
    p15, p16 = p9/p14
    assert str(p15) == 'Polynomial: 0'
    assert p16 == p9

    p15, p16 = p9/Polynomial(Mono(1, 0))
    assert p15 == p9
    assert str(p16) == 'Polynomial: 0'

    p15, p16 = p14/p9
    assert p15 == p1
    assert str(p15) == 'Polynomial: 5.0x**2+x+5.0'
    assert str(p16) == 'Polynomial: 0'

    assert str(p8) == 'Polynomial: 10x+1'
    p15, p16 = p14/p8
    assert str(p15) == 'Polynomial: -5.0x**2-2.0x-5.1'
    assert str(p16) == 'Polynomial: -9.9'

    assert str(p1-Polynomial(Mono(2, 0))) == 'Polynomial: 5x**2+x+3'
    p15, p16 = p14/(p1-Polynomial(Mono(2, 0)))
    assert str(p15) == 'Polynomial: -10.0x-3.0'
    assert str(p16) == 'Polynomial: -20.0x-6.0'



if __name__== '__main__':
    print('Testing Polynomial class...')
    test_polynomial()
    print('Passed!')
