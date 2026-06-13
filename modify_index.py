import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The slides we want to insert (6 slides total)
new_slides = """
        <!-- ═══ 5: NEW BRIDGE — HOW AI THINKS ═══ -->
        <div class="slide" id="s5" data-num="05 / 30">
            <h2 class="slide-title a1"><i class="fa-solid fa-microchip"></i> מתחת למכסה המנוע: איך AI "חושב"?</h2>
            <div class="content-area">
                <div class="a2">
                    <span class="def-term">AI ≠ מוח. AI = מנוע ניבוי הסתברותי.</span>
                    <p style="font-size:21px; margin-bottom:18px;">
                        דמיינו <strong>מתמחה שקרא כל ספר, תקן וחוזה שנכתבו אי-פעם</strong> — וכל מה שהוא עושה זה לנחש את המילה הסבירה הבאה. הוא לא "מבין" מאזן. הוא <strong>משלים תבניות</strong> — בצורה מבריקה.
                    </p>
                </div>
                <div class="callout a3">
                    <h4><i class="fa-solid fa-bullseye"></i> התובנה שמשנה הכל:</h4>
                    <p>המכונה <strong>גאונית בתבניות, אך עיוורת לאמת.</strong> זה מסביר גם את הכוח העצום שלה — וגם את הסכנה. שתי השקופיות הבאות מפרקות בדיוק את זה.</p>
                </div>
            </div>
        </div>

        <!-- ═══ 6: HOW AI THINKS IMAGE ═══ -->
        <div class="slide" id="s6" data-num="06 / 30">
            <div class="image-hero">
                <img src="assets/ai_brain_predict.png" alt="AI Prediction Engine" class="aimg">
                <p class="cap a2">
                    <i class="fa-solid fa-microchip" style="color:var(--accent-cyan); margin-left:8px;"></i>
                    הוא לא מבין את המספרים, אבל מזהה את התבנית שלהם טוב מכל בן אנוש.
                </p>
            </div>
        </div>

        <!-- ═══ 7: NEW BRIDGE — THREE GEARS ═══ -->
        <div class="slide" id="s7" data-num="07 / 30">
            <h2 class="slide-title a1"><i class="fa-solid fa-gears"></i> שלושה הילוכים: מצ'אט ועד סוכן</h2>
            <div class="content-area">
                <div class="flow a2">
                    <div class="flow-node course">
                        <span class="flow-tag">הילוך 1 · פסיבי</span>
                        <h4>צ'אט = יועץ</h4>
                        <p>שואלים, הוא עונה בטקסט. נחמד — אבל לא עושה כלום בעצמו.</p>
                    </div>
                    <div class="flow-arrow"><i class="fa-solid fa-circle-arrow-left"></i></div>
                    <div class="flow-node tool">
                        <span class="flow-tag">הילוך 2 · כלים</span>
                        <h4>מחשבון + אינטרנט</h4>
                        <p>מריץ קוד, סורק את הרשת, מנתח אקסל של מיליון שורות.</p>
                    </div>
                    <div class="flow-arrow"><i class="fa-solid fa-circle-arrow-left"></i></div>
                    <div class="flow-node result">
                        <span class="flow-tag">הילוך 3 · אוטונומי</span>
                        <h4>סוכן = ידיים</h4>
                        <p>נכנס למערכות, מקליד, ולוחץ "שלח" — לבד.</p>
                    </div>
                </div>
                <div class="callout a3">
                    <h4><i class="fa-solid fa-gauge-high"></i> מפת הדרכים לכל הערב:</h4>
                    <p>כל כלי שנראה היום יושב באחד משלושת ההילוכים. ככל שעולים הילוך — עולה הכוח, וגם הצורך בבקרת CFO.</p>
                </div>
            </div>
        </div>

        <!-- ═══ 8: THREE GEARS IMAGE ═══ -->
        <div class="slide" id="s8" data-num="08 / 30">
            <div class="image-hero">
                <img src="assets/ai_three_gears.png" alt="AI Three Gears" class="aimg">
                <p class="cap a2">
                    <i class="fa-solid fa-layer-group" style="color:var(--accent-emerald); margin-left:8px;"></i>
                    מהתייעצות פסיבית בממשק צ'אט (הילוך 1) ועד לסוכן שמבצע פעולות בעצמו (הילוך 3).
                </p>
            </div>
        </div>

        <!-- ═══ 9: NEW BRIDGE — HALLUCINATION ═══ -->
        <div class="slide" id="s9" data-num="09 / 30">
            <h2 class="slide-title a1"><i class="fa-solid fa-wand-magic-sparkles"></i> זה לא באג — זו תכונה: למה AI "ממציא"?</h2>
            <div class="content-area">
                <p class="a2" style="font-size:23px; font-weight:700; color:var(--text-primary); margin-bottom:18px;">
                    אותו מנוע ניבוי שהופך את ה-AI לגאון — הוא זה שגורם לו לשקר בביטחון מלא.
                </p>
                <p class="a3" style="font-size:20px; max-width:1000px;">
                    כשה-AI לא יודע, הוא <strong>לא אומר "אינני יודע".</strong> הוא מנבא את התשובה ה<em>סבירה ביותר</em> — מנוסחת היטב, משכנעת, ולעיתים פשוט לא נכונה. בדיוק כמו סטודנט שלעולם לא משאיר שאלה ריקה במבחן.
                </p>
                <div class="callout rose a4">
                    <h4><i class="fa-solid fa-triangle-exclamation"></i> כלל הברזל של ה-CFO:</h4>
                    <p>ה-AI ממקסם ל<strong>"נשמע נכון"</strong> — לא ל<strong>"נכון".</strong> לכן כל פלט פיננסי חייב לעבור דרך עין מקצועית. זו בדיוק הסיבה שההכשרה שלכם קריטית מתמיד.</p>
                </div>
            </div>
        </div>

        <!-- ═══ 10: HALLUCINATION IMAGE ═══ -->
        <div class="slide" id="s10" data-num="10 / 30">
            <div class="image-hero">
                <img src="assets/ai_hallucination.png" alt="AI Hallucination" class="aimg">
                <p class="cap a2">
                    <i class="fa-solid fa-triangle-exclamation" style="color:var(--accent-rose); margin-left:8px;"></i>
                    הנתון נראה מושלם ורהוט, אך עלול להיות מומצא לחלוטין.
                </p>
            </div>
        </div>
"""

# Find the insertion point (right after slide 4 closes, before slide 5 comment)
# We look for the closing div of slide 4
parts = re.split(r'(<!-- ═══ 5: EXPERTISE FIRST \(reframed\) ═══ -->)', content, maxsplit=1)
if len(parts) == 3:
    header = parts[0]
    tail = parts[1] + parts[2]
else:
    print("Could not find insertion point!")
    exit(1)

# Now we need to re-number all the slides in the tail
# We need to add 6 to the numbering of s5 to s24
# Find all occurrences of `id="sX"` and `data-num="XX / 24"`
# Also update all slides to out of 30, including the header
header = re.sub(r'data-num="\d+ / \d+"', lambda m: m.group(0).split('/')[0] + '/ 30"', header)

def renumber_tail(match):
    # This matches 'id="s5" data-num="05 / 24"' and increments it
    s_id = int(match.group(1))
    new_id = s_id + 6
    return f'id="s{new_id}" data-num="{new_id:02d} / 30"'

# Replace all id="s..." data-num="..." in the tail
tail = re.sub(r'id="s(\d+)"\s+data-num="\d+\s*/\s*\d+"', renumber_tail, tail)
# Also fix any remaining data-num without id (if any)
tail = re.sub(r'data-num="\d+ / \d+"', lambda m: m.group(0).split('/')[0] + '/ 30"', tail)
# And the comments: <!-- ═══ 5: EXPERTISE FIRST...
def renumber_comment(match):
    c_id = int(match.group(1))
    new_id = c_id + 6
    return f'<!-- ═══ {new_id}:'
tail = re.sub(r'<!-- ═══ (\d+):', renumber_comment, tail)


# Now update the JS array
# First, update total=24 to total=30
tail = tail.replace('total = 24', 'total = 30')
tail = tail.replace('const totalElement = document.getElementById(\'totalSlides\');', '') # if exists

names_start = tail.find('const names = [')
if names_start != -1:
    names_end = tail.find('];', names_start)
    if names_end != -1:
        names_str = tail[names_start:names_end+2]
        
        # We want to insert 6 items after "ההמחשה: מטוס F-35 בסופר",
        new_names_items = '''
        "איך AI חושב?",
        "ההמחשה: מנוע ניבוי",
        "שלושה הילוכים",
        "ההמחשה: האבולוציה",
        "הזיות: לא באג אלא תכונה",
        "ההמחשה: דאטה מסולף",'''
        
        new_names_str = names_str.replace('"ההמחשה: מטוס F-35 בסופר",', '"ההמחשה: מטוס F-35 בסופר",' + new_names_items)
        tail = tail.replace(names_str, new_names_str)

new_content = header + new_slides + "\n" + tail

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("index.html modified successfully.")
