import sys

def check_russian(characters):
    sys.path.append('dictionary/rus/')

    if 'а' in characters:
        import A
        A.check_and_write(characters)
    
    elif 'б' in characters:
        import B
        B.check_and_write(characters)

    elif 'в' in characters:
        import V
        V.check_and_write(characters)
    
    elif 'г' in characters:
        import G
        G.check_and_write(characters)
    
    elif 'д' in characters:
        import D
        D.check_and_write(characters)
    
    elif 'е' in characters:
        import E
        E.check_and_write(characters)
    
    elif 'ё' in characters:
        import EE
        EE.check_and_write(characters)
    
    elif 'ж' in characters:
        import ZZ
        ZZ.check_and_write(characters)

    elif 'з' in characters:
        import Z
        Z.check_and_write(characters)
    
    elif 'и' in characters:
        import I
        I.check_and_write(characters)
    
    elif 'й' in characters:
        import II
        II.check_and_write(characters)
    
    elif 'к' in characters:
        import K
        K.check_and_write(characters)
    
    elif 'л' in characters:
        import L
        L.check_and_write(characters)
    
    elif 'м' in characters:
        import M
        M.check_and_write(characters)
    
    elif 'н' in characters:
        import N
        N.check_and_write(characters)
    
    elif 'о' in characters:
        import O
        O.check_and_write(characters)
    
    elif 'п' in characters:
        import P
        P.check_and_write(characters)
    
    elif 'р' in characters:
        import R
        R.check_and_write(characters)
    
    elif 'с' in characters:
        import S
        S.check_and_write(characters)
    
    elif 'т' in characters:
        import T
        T.check_and_write(characters)
    
    elif 'у' in characters:
        import Y
        Y.check_and_write(characters)

    elif 'ф' in characters:
        import F
        F.check_and_write(characters)
    
    elif 'х' in characters:
        import X
        X.check_and_write(characters)
    
    elif 'ц' in characters:
        import C
        C.check_and_write(characters)

    elif 'ч' in characters:
        import CC
        CC.check_and_write(characters)
    
    elif 'ш' in characters:
        import SS
        SS.check_and_write(characters)
    
    elif 'щ' in characters:
        import SH
        SH.check_and_write(characters)
    
    elif 'ъ' in characters:
        import KI
        KI.check_and_write(characters)
    
    elif 'ы' in characters:
        import UL
        UL.check_and_write(characters)
    
    elif 'ь' in characters:
        import HI
        HI.check_and_write(characters)
    
    elif 'э' in characters:
        import AU
        AU.check_and_write(characters)
    
    elif 'ю' in characters:
        import IU
        IU.check_and_write(characters)
    
    elif 'я' in characters:
        import IA
        IA.check_and_write(characters)

    