##The authors are Olivia and Lily

class Fabric:
    def __init__(self, countryOFOrigin, color):
        self.countryOFOrigin = countryOFOrigin
        self.color = color

    def __str__(self):
        return self.countryOFOrigin + "("+ str(self.color)+ ")"

fab1= Fabric("Bolivia", "pink")
print(fab1)
