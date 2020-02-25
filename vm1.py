compNum = 0
def fullTrans(vmL):
    asmFinal=[]
    temp=[]
    for x in range(len(vmL)):
        vmL[x] = strip(vmL[x])
        if not ''==vmL[x]:
            temp.append(vmL[x])
    vmL=temp
    for p in range(len(vmL)):
        asmFinal.extend(trans(vmL[p]))
    asmFinal.extend([
    '(END)', 
	'@END',
	'0;JMP'
    ])
    for x in asmFinal:
        print(x)
        pass
    return asmFinal

def strip(vm):
    if len(vm)>=1:
        char = vm[0]
        if char == '\n' or char == '/':
            return ''
        elif char == ' ':
            return strip(vm[1:])
        else:
            return char + strip(vm[1:])
    else:
        return ''

def trans(vm):
    global compNum
    asm = []
    if len(vm) == 2:
        if vm == 'or':
            asm.extend([
            '@SP',
            'M=M-1',
            'A=M',
            'D=M',
            'A=A-1',
            'M=M|D'
            ])
        elif vm == 'eq':
            asm.extend([
            '@SP',
            'M=M-1',
            'A=M',
            'D=M',
            'A=A-1',
            'D=M-D',
            '@L'+str(compNum),
            'D;JEQ',
            '@SP',
            'A=M-1',
            'M=0',
            '@L'+str(compNum+1),
            '0;JMP',
            '(L'+str(compNum)+')',
            '@SP',
            'A=M-1',
            'M=-1',
            '(L'+str(compNum+1)+')'
            ])
            compNum+=2
        elif vm == 'gt':
            asm.extend([
            '@SP',
            'M=M-1',
            'A=M',
            'D=M',
            'A=A-1',
            'D=M-D',
            '@L'+str(compNum),
            'D;JGT',
            '@SP',
            'A=M-1',
            'M=0',
            '@L'+str(compNum+1),
            '0;JMP',
            '(L'+str(compNum)+')',
            '@SP',
            'A=M-1',
            'M=-1',
            '(L'+str(compNum+1)+')'
            ])
            compNum+=2
        elif vm == 'lt':
            asm.extend([
            '@SP',
            'M=M-1',
            'A=M',
            'D=M',
            'A=A-1',
            'D=M-D',
            '@L'+str(compNum),
            'D;JLT',
            '@SP',
            'A=M-1',
            'M=0',
            '@L'+str(compNum+1),
            '0;JMP',
            '(L'+str(compNum)+')',
            '@SP',
            'A=M-1',
            'M=-1',
            '(L'+str(compNum+1)+')'
            ])
            compNum+=2
    elif len(vm) == 3:
        if vm == 'add':
            asm.extend([
            '@SP',
            'M=M-1',
            'A=M',
            'D=M',
            'A=A-1',
            'M=M+D'
            ])
        elif vm == 'sub':
            asm.extend([
            '@SP',
            'M=M-1',
            'A=M',
            'D=M',
            'A=A-1',
            'M=M-D'
            ])
        elif vm == 'neg':
            asm.extend([
            '@SP',
            'A=M-1',
            'M=-M'
            ])
        elif vm == 'and':
            asm.extend([
            '@SP',
            'M=M-1',
            'A=M',
            'D=M',
            'A=A-1',
            'M=M&D'
            ])
        elif vm == 'not':
            asm.extend([
            '@SP',
            'A=M-1',
            'M=!M'
            ])
    elif len(vm) > 3:
        if vm[0:4] == 'push':
            if 'constant' in vm:
                u=vm[vm.index('constant')+8:]
                asm.extend([
                    '@'+str(u),
                    'D=A',
                    '@SP',
                    'M=M+1',
                    'A=M-1',
                    'M=D'
                ])
            elif 'static' in vm:
                u=vm[vm.index('static')+6:]
                asm.extend([
                    '@16',
                    'D=A',
                    '@'+str(u),
                    'A=D+A',
                    'D=M',
                    '@SP',
                    'M=M+1',
                    'A=M-1',
                    'M=D'
                ])
            elif 'local' in vm:
                u=vm[vm.index('local')+5:]
                asm.extend([
                    '@'+str(u),
                    'D=A',
                    '@LCL',
                    'A=D+M',
                    'D=M',
                    '@SP',
                    'M=M+1',
                    'A=M-1',
                    'M=D'
                ])
            elif 'argument' in vm:
                u=vm[vm.index('argument')+8:]
                asm.extend([
                    '@'+str(u),
                    'D=A',
                    '@ARG',
                    'A=D+M',
                    'D=M',
                    '@SP',
                    'M=M+1',
                    'A=M-1',
                    'M=D'
                ])
            elif 'this' in vm:
                u=vm[vm.index('this')+4:]
                asm.extend([
                    '@'+str(u),
                    'D=A',
                    '@THIS',
                    'A=D+M',
                    'D=M',
                    '@SP',
                    'M=M+1',
                    'A=M-1',
                    'M=D'
                ])
            elif 'that' in vm:
                u=vm[vm.index('that')+4:]
                asm.extend([
                    '@'+str(u),
                    'D=A',
                    '@THAT',
                    'A=D+M',
                    'D=M',
                    '@SP',
                    'M=M+1',
                    'A=M-1',
                    'M=D'
                ])
            elif 'pointer' in vm:
                u=vm[vm.index('pointer')+7:]
                asm.extend([
                    '@3',
                    'D=A',
                    '@'+str(u),
                    'A=D+A',
                    'D=M',
                    '@SP',
                    'M=M+1',
                    'A=M-1',
                    'M=D'
                ])
            elif 'temp' in vm:
                u=vm[vm.index('temp')+4:]
                asm.extend([
                    '@5',
                    'D=A',
                    '@'+str(u),
                    'A=D+A',
                    'D=M',
                    '@SP',
                    'M=M+1',
                    'A=M-1',
                    'M=D'
                ])
                
        elif vm[0:3] == 'pop':
            if 'static' in vm:
                u=vm[vm.index('static')+6:]
                asm.extend([
                    '@16',
                    'D=A',
                    '@'+str(u),
                    'D=D+A'
                ])
            elif 'local' in vm:
                u=vm[vm.index('local')+5:]
                asm.extend([
                    '@'+str(u),
                    'D=A',
                    '@LCL',
                    'D=D+A'
                ])
            elif 'argument' in vm:
                u=vm[vm.index('argument')+8:]
                asm.extend([
                    '@'+str(u),
                    'D=A',
                    '@ARG',
                    'D=D+A'
                ])
            elif 'this' in vm:
                u=vm[vm.index('this')+4:]
                asm.extend([
                    '@'+str(u),
                    'D=A',
                    '@THIS',
                    'D=D+A'
                ])
            elif 'that' in vm:
                u=vm[vm.index('that')+4:]
                asm.extend([
                    '@'+str(u),
                    'D=A',
                    '@THAT',
                    'D=D+A'
                ])
            elif 'pointer' in vm:
                u=vm[vm.index('pointer')+7:]
                asm.extend([
                    '@3',
                    'D=A',
                    '@'+str(u),
                    'D=D+A'
                ])
            elif 'temp' in vm:
                u=vm[vm.index('temp')+4:]
                asm.extend([
                    '@5',
                    'D=A',
                    '@'+str(u),
                    'D=D+A'
                ])
            asm.extend([
                '@R13',
                'M=D',
                '@SP',
                'M=M-1',
                'A=M',
                'D=M',
                '@R13',
                'A=M',
                'M=D'
            ])
    return asm
'''
sourceFile=open('D:\\CSII\\projects\\07\\MemoryAccess\\BasicTest\\BasicTest.vm',mode='r')
fileName = 'BasicTest'
f=open('D:\\CSII\\projects\\07\\MemoryAccess\\BasicTest\\BasicTest.asm',mode='w+')
'''
'''
sourceFile=open('D:\\CSII\\projects\\07\\MemoryAccess\\PointerTest\\PointerTest.vm',mode='r')
fileName = 'PointerTest'
f=open('D:\\CSII\\projects\\07\\MemoryAccess\\PointerTest\\PointerTest.asm',mode='w+')
'''
'''
sourceFile=open('D:\\CSII\\projects\\07\\MemoryAccess\\StaticTest\\StaticTest.vm',mode='r')
fileName = 'StaticTest'
f=open('D:\\CSII\\projects\\07\\MemoryAccess\\StaticTest\\StaticTest.asm',mode='w+')
'''
'''
sourceFile=open('D:\\CSII\\projects\\07\\StackArithmetic\\SimpleAdd\\SimpleAdd.vm',mode='r')
fileName = 'SimpleAdd'
f=open('D:\\CSII\\projects\\07\\StackArithmetic\\SimpleAdd\\SimpleAdd.asm',mode='w+')
'''

sourceFile=open('D:\\CSII\\projects\\07\\StackArithmetic\\StackTest\\StackTest.vm',mode='r')
fileName = 'StackTest'
f=open('D:\\CSII\\projects\\07\\StackArithmetic\\StackTest\\StackTest.asm',mode='w+')


vmL=sourceFile.readlines()
out=fullTrans(vmL)
for x in out:
    f.write(x+'\n')
f.close()