from pathlib import Path
import zipfile,re,html

zip_path=Path('docs/main.min.53XkBRxF.zip')
out=Path('docs/client-js-layout-report.md')
patterns=[
 ('inline-style',r'\.style\.(?:left|right|top|bottom|width|height|transform|display|position|zIndex)'),
 ('set-attribute-style',r'setAttribute\([^\n]{0,80}["\']style["\']'),
 ('css-text',r'cssText'),
 ('positioner',r'positioner'),
 ('game-window-positioner',r'game-window-positioner'),
 ('hud-container',r'hud-container'),
 ('bottom-panel',r'bottom-panel'),
 ('left-column',r'left-column'),
 ('right-column',r'right-column'),
 ('mini-map',r'mini-map'),
 ('inventory',r'inventory[_-](?:wrapper|grid)|equipment-wrapper|stats-wrapper'),
 ('classlist',r'classList\.(?:add|remove|toggle)'),
 ('transform',r'transform'),
]
with zipfile.ZipFile(zip_path) as z:
    names=z.namelist()
    jsname=next((n for n in names if n.endswith('.js')),None)
    if not jsname: raise SystemExit('No JS in archive')
    data=z.read(jsname).decode('utf-8','replace')

lines=['# Client JS layout analysis','',f'- Archive: `{zip_path}`',f'- JS entry: `{jsname}`',f'- JS bytes: {len(data.encode("utf-8"))}',f'- Characters: {len(data)}','']
for title,pat in patterns:
    ms=list(re.finditer(pat,data,re.I))
    lines.append(f'## {title}')
    lines.append(f'Matches: **{len(ms)}**')
    lines.append('')
    for i,m in enumerate(ms[:40],1):
        a=max(0,m.start()-260); b=min(len(data),m.end()+360)
        s=data[a:b].replace('\n',' ')
        lines.append(f'### {i}')
        lines.append('```js')
        lines.append(s)
        lines.append('```')
    if len(ms)>40: lines.append(f'_Only first 40 of {len(ms)} matches shown._')
    lines.append('')

# Extract likely literal class/selector strings related to layout.
terms=['hud','positioner','inventory','equipment','stats','mini-map','left-column','right-column','bottom-panel','chat','game-window']
strings=re.findall(r'(["\'])(.{1,180}?)\1',data)
vals=[]
for _,s in strings:
    sl=s.lower()
    if any(t in sl for t in terms) and s not in vals:
        vals.append(s)
lines += ['## Relevant string literals',f'Unique matches: **{len(vals)}**','']
for s in vals[:300]: lines.append(f'- `{s.replace("`","\\`")}`')
out.write_text('\n'.join(lines),encoding='utf-8')
print(out)
