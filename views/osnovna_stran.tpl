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
                <p>{{neopravljena}} dela so neopravljena, od tega jih zamuja {{zamujena}}</p>
            %elif neopravljena == 4 or neopravljena == 3 and zamujena == 2:
                <p>{{neopravljena}} dela so neopravljena, od tega 2 deli zamujata.</p>
            %elif neopravljena == 4 or neopravljena == 3 and zamujena == 1:
                <p>{{neopravljena}} dela so neopravljena, od tega 1 del0 zamuja.</p>
            %elif neopravljena == 4 or neopravljena == 3 and zamujena == 0:
                <p>{{neopravljena}} dela so neopravljena, vendar nobeno ne zamuja.</p>
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
                <li> <b>Opravljena dela:</b>
                    <ul>
                    % for delo in kretenizem:
                        % if delo.opravljeno:
                            <li>{{delo.ime}}</li>
                        % end
                    % end
                    </ul>
                <li> <b>Neopravljena dela:</b>
                    <ul>
                    % for indeks, delo in enumerate(kretenizem):
                        % if not delo.opravljeno:
                            <li>{{delo.ime}}</li>
                            <form method="POST" action="/opravi/">
                                <input type="hidden" name="indeks" value="{{indeks}}">
                                <input type="submit" value="Opravi!">
                            </form>
                        % end
                     % end
                    </ul>
             </ul>
            <form method="POST" action="/dodaj/">
                ime : <input type="text" name="ime">
                opis : <input type="text" name="opis">
                tezavnost : <input type="text" name="tezavnost">
                cena : <input type="number" name="cena">
                material : <input type="text" name="material">
                rok : <input type="date" id="rok" name="rok">
                <input type="submit" value="Oddaj!">
            </form>
    </body>
</html>