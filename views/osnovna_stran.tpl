<html>
    <body>
    <h1>Gradbena dela</h1>
        <h2>Urejenje in pregled nad delom na objektu</h2>
            % if neopravljena > 4 and zamujena > 2:
                <p>{{neopravljena}} del je neopravljenih, od tega jih zamuja {{zamujena}}.</p>
            % elif neopravljena > 4 and zamujena == 2:
                <p>{{neopravljena}} del je neopravljenih, od tega 2 deli zamujata.</p>
            % elif neopravljena > 4 and zamujena == 1:
                <p>{{neopravljena}} del je neopravljenih, od tega 1 delo zamuja.</p>
            % elif neopravljena > 4 and zamujena == 0:
                <p>{{neopravljena}} del je neopravljenih, vendat Vam nobeno ne zamuja.</p>
            %elif neopravljena == 4 or neopravljena == 3 and zamujena > 2:
                <p>{{neopravljena}} dela so neopravljena, od tega jih zamuja {zamujena}</p>
            %elif neopravljena == 4 or neopravljena == 3 and zamujena = 2:
                <p>{{neopravljena}} del so neopravljena, od tega 2 deli zamujata.</p>
            %elif neopravljena == 4 or neopravljena == 3 and zamujena = 1:
                <p>{{neopravljena}} del so neopravljena, od tega 1 del0 zamuja.</p>
            %elif neopravljena == 4 or neopravljena == 3 and zamujena = 0:
                <p>{{neopravljena}} del so neopravljena, vendar nobeno ne zamuja.</p>
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
    </body>
</html>