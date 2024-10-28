import sys

class main:
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
