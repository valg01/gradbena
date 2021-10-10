<html>
    <body>
    <h1>Gradbena dela</h1>
        <h2>Urejenje in pregled nad delom na objektu</h2>
            % if neopravljena > 0:
                <p>{{neopravljena}} del je neopravljenih, od tega jih zamuja {zamujena}.</p>
            % elif neopravljena > 2 and zamujena == 0:
                <p>{{neopravljena}} del je neopravljenih, vendat Vam nobeno ne zamuja.</p>
            % elif neopravljena == 2 and zamujena == 2:
                <p>2 deli sta neopravljeni in zamujata.</p>
            % elif neopravljena == 2 and zamujena == 1:
                <p>2 deli sta neopravljeni, 1 delo že zamuja.</p>
            % elif neopravljena == 2 and zamujena == 0:
                <p>2 deli sta neopravljeni.</p>
            % elif neopravljena == 1 and zamujena == 1:
                <p>1 delo je neopravljeno in zamuja.</p>
            % elif neopravljena == 1 and zamujena == 0:
                <p>1 delo je neopravljeno.</p>
            % else:
                <p>Super! Vsa dela so opravljena.</p>
            % end
        <h3>Aktualna dela:</h3>
            <ul>
                % for delo in dela:
                    <li>{{delo.ime}}</li>
                % end
            </ul>
    </body>
</html>