import xlsxwriter

class Xlsx:

    def __init__(self, name, resknown=False):
        self.resknown = resknown
        self.name = "Saves/" + name
        self.name += ".xlsx"
        self.workbook = xlsxwriter.Workbook(self.name)
        worksheet1 = self.workbook.add_worksheet("PLOT")
        worksheet1.insert_image("A1", "plots/temp/tempplot.jpeg")
        self.mainworksheet = self.workbook.add_worksheet("main")
        self.mainworksheet.write("A1", "Roll no")
        if resknown == True:
            self.mainworksheet.write("B1", "Required force Magnitude")
            self.mainworksheet.write("C1", "Required force Direction")
        else:
            self.mainworksheet.write("B1", "Resultant Magnitude")
            self.mainworksheet.write("C1", "Resultant Direction")


    def save(self, arr, i):
        if self.resknown == False:
            i += 2
        else:
            i += 1
        a = "A" + str(i)
        b = "B" + str(i)
        c = "C" + str(i)
        self.mainworksheet.write(a, i-1)
        self.mainworksheet.write(b, arr[0])
        self.mainworksheet.write(c, arr[1])

    def main_save(self):
        self.workbook.close()