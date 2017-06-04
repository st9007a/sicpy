class OpTable:

    op_codes = {
        'ADD': '18',
        'ADDF': '58',
        'ADDR': '90',
        'AND': '40',
        'CLEAR': 'b4',
        'COMP': '28',
        'COMPF': '88',
        'DIV': '24',
        'DIVF': '64',
        'DIVR': '9c',
        'FIX': 'c4',
        'FLOAT': 'c0',
        'HIO': 'f4',
        'J': '3c',
        'JEQ': '30',
        'JGT': '34',
        'JLT': '38',
        'JSUB': '48',
        'LDA': '00',
        'LDB': '68',
        'LDCH': '50',
        'LDF': '70',
        'LDL': '08',
        'LDS': '6c',
        'LDT': '74',
        'LDX': '04',
        'LPS': 'd0',
        'MUL': '20',
        'MULF': '60',
        'MULR': '98',
        'NORM': 'c8',
        'OR': '44',
        'RD': 'd8',
        'RMO': 'ac',
        'RSUB': '4c',
        'SHIFTL': 'a4',
        'SHIFTR': 'a8',
        'SIO': 'f0',
        'SSK': 'ec',
        'STA': '0c',
        'STB': '78',
        'STCH': '54',
        'STF': '80',
        'STI': 'd4',
        'STL': '14',
        'STS': '7c',
        'STSW': 'e8',
        'STT': '84',
        'STX': '10',
        'SUB': '1C',
        'SUBF': '5c',
        'SUBR': '94',
        'SVC': 'b0',
        'TD': 'e0',
        'TIO': 'f8',
        'TIX': '2c',
        'TIXR': 'b8',
        'WD': 'dc',

    }

    pseudo_op_codes = [ 'RESB', 'RESW', 'BYTE', 'WORD', 'START', 'END' ]

    def __init__(self):
        self.op_to_code = {}
        self.code_to_op = {}
        for elem in OpTable.op_codes:
            self.op_to_code[elem] = OpTable.op_codes[elem]
            self.code_to_op[OpTable.op_codes[elem]] = elem

    def is_exist(self, op):
        return True if op in OpTable.op_codes or op in OpTable.pseudo_op_codes else False

    def is_op_exist(self, op):
        return True if op in OpTable.op_codes else False

    def is_pseudo_op_exist(self, op):
        return True if op in OpTable.pseudo_op_codes else False

if __name__ == '__main__':
    op_table = OpTable()