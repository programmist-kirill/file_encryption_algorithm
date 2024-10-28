import sys

def check_english(characters):
    sys.path.append("/home/kirill/file_encryption/algorithm/dictionary/eng")

    if 'a' in characters:
        import a
        a.check_and_write(characters)
    
    elif 'b' in characters:
        import b
        b.check_and_write(characters)
    
    elif 'c' in characters:
        import c
        c.check_and_write(characters)
    
    elif 'd' in characters:
        import d
        d.check_and_write(characters)
    
    elif 'e' in characters:
        import syse
        syse.check_and_write(characters)

    elif 'f' in characters:
        import f
        f.check_and_write(characters)
    
    elif 'g' in characters:
        import g
        g.check_and_write(characters)
    
    elif 'h' in characters:
        import h
        h.check_and_write(characters)
    
    elif 'i' in characters:
        import i
        i.check_and_write(characters)
    
    elif 'j' in characters:
        import j
        j.check_and_write(characters)

    elif 'k' in characters:
        import k
        k.check_and_write(characters)
    
    elif 'l' in characters:
        import l
        l.check_and_write(characters)
    
    elif 'm' in characters:
        import m
        m.check_and_write(characters)
    
    elif 'n' in characters:
        import dictionary.eng.n
        n.check_and_write(characters)
    
    elif 'o' in characters:
        import o
        o.check_and_write(characters)
    
    elif 'p' in characters:
        import p
        p.check_and_write(characters)
    
    elif 'q' in characters:
        import q
        q.check_and_write(characters)
    
    elif 'r' in characters:
        import r
        r.check_and_write(characters)
    
    elif 's' in characters:
        import s
        s.check_and_write(characters)
    
    elif 't' in characters:
        import t
        t.check_and_write(characters)
    
    elif 'u' in characters:
        import u
        u.check_and_write(characters)
    
    elif 'v' in characters:
        import v
        v.check_and_write(characters)
    
    elif 'w' in characters:
        import w
        w.check_and_write(characters)
    
    elif 'x' in characters:
        import x
        x.check_and_write(characters)
    
    elif 'y' in characters:
        import y
        y.check_and_write(characters)
    
    elif 'z' in characters:
        import z
        z.check_and_write(characters)


    def check_simwol(characters):
        sys.path.append('dictionary/simwol/')

        if '&' in characters:
            import ampersand
            ampersand.check_and_write(characters)
        
        elif "'" in characters:
            import apostrophe
            apostrophe.check_and_write(characters)
        
        elif '*' in characters:
            import asterisk
            asterisk.check_and_write(characters)
        
        elif '@' in characters:
            import At_symbol
            At_symbol.check_and_write(characters)
        
        elif '^' in characters:
            import circumflex
            circumflex.check_and_write(characters)
        
        elif ':' in characters:
            import colon
            colon.check_and_write(characters)
        
        elif ',' in characters:
            import comma
            comma.check_and_write(characters)
        
        elif '$' in characters:
            import dollar_sign
            dollar_sign.check_and_write(characters)
        
        elif '=' in characters:
            import equals
            equals.check_and_write(characters)
        
        elif '!' in characters:
            import exclamation
            exclamation.check_and_write(characters)
        
        elif '>' in characters:
            import greater_than
            greater_than.check_and_write(characters)
        
        elif '{' in characters:
            import left_curcli_brace
            left_curcli_brace.check_and_write(characters)
        
        elif '(' in characters:
            import left_parenthesis
            left_parenthesis.check_and_write(characters)
        
        elif '[' in characters:
            import left_square_bracket
            left_square_bracket.check_and_write(characters)
        
        elif '<' in characters:
            import less_than
            less_than.check_and_write(characters)
        
        elif '-' in characters:
            import minus
            minus.check_and_write(characters)
        
        elif '#' in characters:
            import number_sign
            number_sign.check_and_write(characters)
        
        elif '№' in characters:
            import numero_sign
            numero_sign.check_and_write(characters)
        
        elif '.' in characters:
            import period
            period.check_and_write(characters)
        
        elif '+' in characters:
            import plus
            plus.check_and_write(characters)
        
        elif '%' in characters:
            import procent
            procent.check_and_write(characters)
        
        elif '?' in characters:
            import question
            question.check_and_write(characters)
        
        elif '"' in characters:
            import quotation_mark
            quotation_mark.check_and_write(characters)
        
        elif '}' in characters:
            import right_curcly_brace
            right_curcly_brace.check_and_write(characters)
        
        elif ')' in characters:
            import right_parenthesis
            right_parenthesis.check_and_write(characters)
        
        elif ']' in characters:
            import right_square_bracket
            right_square_bracket.check_and_write(characters)
        
        elif ';' in characters:
            import semicolon
            semicolon.check_and_write(characters)
    
        elif '~' in characters:
            import tilde
            tilde.check_and_write(characters)
        
        elif ' ' in characters:
            import probel
            probel.check_and_write(characters)
