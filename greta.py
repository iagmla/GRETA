# GRETA (Gated Rotor Encryption Algorithm) by Karl Zander
# Each rotor equates to 26 cards of a single color

class GRETA:
    G = 0
    Q = 0
    def __init__(
        self,
        sub_rotor : list,
        control_rotor : list
        ):
        self.sub_rotor = sub_rotor
        self.control_rotor = control_rotor

    def step_rotors(self):
        self.G = self.control_rotor[self.G]
        self.Q = self.sub_rotor[self.Q]
        self.sub_rotor.append(self.sub_rotor.pop(self.Q))
        self.control_rotor.append(self.control_rotor.pop(self.G))
        for x in range(self.G):
            self.sub_rotor.append(self.sub_rotor.pop(0))
        for x in range(self.Q):
            self.control_rotor.append(self.control_rotor.pop(0))

    def encrypt_letter(
        self,
        letter : str
        ) -> str:
        self.step_rotors()
        return chr(self.sub_rotor[ord(letter) - 65] + 65)
    
    def decrypt_letter(
        self,
        letter : str
        ) -> str:
        self.step_rotors()
        return chr(self.sub_rotor.index(ord(letter) - 65) + 65)

    def encrypt(
        self,
        msg : str
        ) -> str:
        ctxt = []
        for letter in msg:
            ctxt.append(self.encrypt_letter(letter))
        return "".join(ctxt)
    
    def decrypt(
        self,
        ctxt : str
        ) -> str:
        ptxt = []
        for letter in ctxt:
            ptxt.append(self.decrypt_letter(letter))
        return "".join(ptxt)
