"""
build_comprehensive_docx_report.py
Generates the comprehensive 7,000–8,000 word academic project report
in Microsoft Word (.docx) format for Course ES1.101 (Project 25).
Follows all syllabus instructions, unslop-writing rules, and the formatting standard of Negi & Prasad.
"""

import os
import sys
import re
from pathlib import Path
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

from report_sections.section1_intro import (
    TITLE, AUTHORS, AFFILIATION, CORRESPONDING_NOTE, ABSTRACT_TEXT, KEYWORDS, INTRO_PARAGRAPHS
)
from report_sections.section2_study_area import STUDY_AREA_PARAGRAPHS
from report_sections.section3_methods import METHODS_PARAGRAPHS, TABLE_1_DATA
from report_sections.section4_results import (
    RESULTS_PARAGRAPHS, TABLE_2_DATA, TABLE_3_DATA, TABLE_4_DATA, TABLE_5_DATA, TABLE_6_DATA
)
from report_sections.section5_discussion import DISCUSSION_PARAGRAPHS
from report_sections.section6_limitations_conclusions import (
    LIMITATIONS_PARAGRAPHS, CONCLUSIONS_PARAGRAPHS, ACKNOWLEDGEMENTS_TEXT, DECLARATIONS
)
from report_sections.references import REFERENCES_DB

ROOT = Path("C:/Users/vivek/EST")
EST_PROJ = ROOT / "EST-Project"
FIG_DIR = EST_PROJ / "data" / "outputs" / "figures_standalone"

# Palette: Clean Academic
COLOR_PRIMARY = RGBColor(16, 44, 87)     # Deep Navy
COLOR_SECONDARY = RGBColor(53, 95, 142)  # Steel Blue
COLOR_TEXT = RGBColor(20, 20, 20)        # Off-black Charcoal
COLOR_MUTED = RGBColor(90, 90, 90)       # Muted Slate
COLOR_LINK = "1A5276"                    # Academic Link Blue

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def format_three_line_table(table):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="12" w:space="0" w:color="1A2B4C"/>'
        f'  <w:bottom w:val="single" w:sz="12" w:space="0" w:color="1A2B4C"/>'
        f'  <w:insideH w:val="none"/>'
        f'  <w:insideV w:val="none"/>'
        f'  <w:left w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)
    
    # Header bottom border & formatting
    for cell in table.rows[0].cells:
        tcPr = cell._tc.get_or_add_tcPr()
        tcPr.append(parse_xml(f'<w:tcBorders {nsdecls("w")}><w:bottom w:val="single" w:sz="8" w:space="0" w:color="1A2B4C"/></w:tcBorders>'))
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
        tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="F4F6F9"/>'))
        
    for row in table.rows[1:]:
        for cell in row.cells:
            set_cell_margins(cell, top=70, bottom=70, left=120, right=120)

def add_p(doc, text="", style='Normal', space_before=0, space_after=6, line_spacing=1.5, align=WD_ALIGN_PARAGRAPH.LEFT, bold=False, italic=False, color=COLOR_TEXT, font_size=10):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    if text:
        r = p.add_run(text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(font_size)
        r.bold = bold
        r.italic = italic
        r.font.color.rgb = color
    return p

def add_h1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11.5)
    r.bold = True
    r.font.color.rgb = COLOR_PRIMARY
    return p

def add_h2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(10.5)
    r.bold = True
    r.font.color.rgb = COLOR_SECONDARY
    return p

def add_h3(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(7)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(10)
    r.bold = True
    r.italic = True
    r.font.color.rgb = COLOR_TEXT
    return p

def create_omml_eq1():
    # Equation 1: Pearson cross-correlation r(k)
    xml = (
        f'<m:oMathPara {nsdecls("m")}>'
        '  <m:oMath>'
        '    <m:r><m:t>r(k) = </m:t></m:r>'
        '    <m:f>'
        '      <m:num>'
        '        <m:nary>'
        '          <m:naryPr><m:chr m:val="∑"/><m:limLoc m:val="undOvr"/><m:grow m:val="1"/></m:naryPr>'
        '          <m:sub><m:r><m:t>t</m:t></m:r></m:sub>'
        '          <m:sup/>'
        '          <m:e>'
        '            <m:d>'
        '              <m:e>'
        '                <m:sSub><m:e><m:r><m:t>ΔP</m:t></m:r></m:e><m:sub><m:r><m:t>t-k</m:t></m:r></m:sub></m:sSub>'
        '                <m:r><m:t> - ΔP̄</m:t></m:r>'
        '              </m:e>'
        '            </m:d>'
        '            <m:d>'
        '              <m:e>'
        '                <m:sSub><m:e><m:r><m:t>ΔT</m:t></m:r></m:e><m:sub><m:r><m:t>t</m:t></m:r></m:sub></m:sSub>'
        '                <m:r><m:t> - ΔT̄</m:t></m:r>'
        '              </m:e>'
        '            </m:d>'
        '          </m:e>'
        '        </m:nary>'
        '      </m:num>'
        '      <m:den>'
        '        <m:rad>'
        '          <m:radPr><m:degHide m:val="1"/></m:radPr>'
        '          <m:deg/>'
        '          <m:e>'
        '            <m:nary>'
        '              <m:naryPr><m:chr m:val="∑"/><m:limLoc m:val="undOvr"/><m:grow m:val="1"/></m:naryPr>'
        '              <m:sub><m:r><m:t>t</m:t></m:r></m:sub><m:sup/>'
        '              <m:e>'
        '                <m:sSup>'
        '                  <m:e>'
        '                    <m:d><m:e><m:sSub><m:e><m:r><m:t>ΔP</m:t></m:r></m:e><m:sub><m:r><m:t>t-k</m:t></m:r></m:sub></m:sSub><m:r><m:t> - ΔP̄</m:t></m:r></m:e></m:d>'
        '                  </m:e>'
        '                  <m:sup><m:r><m:t>2</m:t></m:r></m:sup>'
        '                </m:sSup>'
        '              </m:e>'
        '            </m:nary>'
        '            <m:nary>'
        '              <m:naryPr><m:chr m:val="∑"/><m:limLoc m:val="undOvr"/><m:grow m:val="1"/></m:naryPr>'
        '              <m:sub><m:r><m:t>t</m:t></m:r></m:sub><m:sup/>'
        '              <m:e>'
        '                <m:sSup>'
        '                  <m:e>'
        '                    <m:d><m:e><m:sSub><m:e><m:r><m:t>ΔT</m:t></m:r></m:e><m:sub><m:r><m:t>t</m:t></m:r></m:sub></m:sSub><m:r><m:t> - ΔT̄</m:t></m:r></m:e></m:d>'
        '                  </m:e>'
        '                  <m:sup><m:r><m:t>2</m:t></m:r></m:sup>'
        '                </m:sSup>'
        '              </m:e>'
        '            </m:nary>'
        '          </m:e>'
        '        </m:rad>'
        '      </m:den>'
        '    </m:f>'
        '    <m:r><m:t>        (1)</m:t></m:r>'
        '  </m:oMath>'
        '</m:oMathPara>'
    )
    return parse_xml(xml)

def create_omml_eq2():
    # Equation 2: Squared Chord Distance SCD_ij
    xml = (
        f'<m:oMathPara {nsdecls("m")}>'
        '  <m:oMath>'
        '    <m:sSub><m:e><m:r><m:t>SCD</m:t></m:r></m:e><m:sub><m:r><m:t>ij</m:t></m:r></m:sub></m:sSub>'
        '    <m:r><m:t> = </m:t></m:r>'
        '    <m:nary>'
        '      <m:naryPr><m:chr m:val="∑"/><m:limLoc m:val="undOvr"/><m:grow m:val="1"/></m:naryPr>'
        '      <m:sub><m:r><m:t>t=1</m:t></m:r></m:sub>'
        '      <m:sup><m:r><m:t>M</m:t></m:r></m:sup>'
        '      <m:e>'
        '        <m:sSup>'
        '          <m:e>'
        '            <m:d>'
        '              <m:e>'
        '                <m:rad><m:radPr><m:degHide m:val="1"/></m:radPr><m:deg/><m:e><m:sSub><m:e><m:r><m:t>p</m:t></m:r></m:e><m:sub><m:r><m:t>it</m:t></m:r></m:sub></m:sSub></m:e></m:rad>'
        '                <m:r><m:t> - </m:t></m:r>'
        '                <m:rad><m:radPr><m:degHide m:val="1"/></m:radPr><m:deg/><m:e><m:sSub><m:e><m:r><m:t>q</m:t></m:r></m:e><m:sub><m:r><m:t>jt</m:t></m:r></m:sub></m:sSub></m:e></m:rad>'
        '              </m:e>'
        '            </m:d>'
        '          </m:e>'
        '          <m:sup><m:r><m:t>2</m:t></m:r></m:sup>'
        '        </m:sSup>'
        '      </m:e>'
        '    </m:nary>'
        '    <m:r><m:t>        (2)</m:t></m:r>'
        '  </m:oMath>'
        '</m:oMathPara>'
    )
    return parse_xml(xml)

def create_omml_eq3():
    # Equation 3: Taxon SCD Contribution C_it
    xml = (
        f'<m:oMathPara {nsdecls("m")}>'
        '  <m:oMath>'
        '    <m:sSub><m:e><m:r><m:t>C</m:t></m:r></m:e><m:sub><m:r><m:t>it</m:t></m:r></m:sub></m:sSub>'
        '    <m:r><m:t> = </m:t></m:r>'
        '    <m:sSup>'
        '      <m:e>'
        '        <m:d>'
        '          <m:e>'
        '            <m:rad><m:radPr><m:degHide m:val="1"/></m:radPr><m:deg/><m:e><m:sSub><m:e><m:r><m:t>p</m:t></m:r></m:e><m:sub><m:r><m:t>it</m:t></m:r></m:sub></m:sSub></m:e></m:rad>'
        '            <m:r><m:t> - </m:t></m:r>'
        '            <m:rad><m:radPr><m:degHide m:val="1"/></m:radPr><m:deg/><m:e><m:sSub><m:e><m:r><m:t>q</m:t></m:r></m:e><m:sub><m:r><m:t>j*t</m:t></m:r></m:sub></m:sSub></m:e></m:rad>'
        '          </m:e>'
        '        </m:d>'
        '      </m:e>'
        '      <m:sup><m:r><m:t>2</m:t></m:r></m:sup>'
        '    </m:sSup>'
        '    <m:r><m:t>,  where  j* = argmin </m:t></m:r>'
        '    <m:sSub><m:e><m:r><m:t>SCD</m:t></m:r></m:e><m:sub><m:r><m:t>ij</m:t></m:r></m:sub></m:sSub>'
        '    <m:r><m:t>        (3)</m:t></m:r>'
        '  </m:oMath>'
        '</m:oMathPara>'
    )
    return parse_xml(xml)

def create_omml_eq4():
    # Equation 4: 2D Planar Migration Velocity v_mig(x, y)
    xml = (
        f'<m:oMathPara {nsdecls("m")}>'
        '  <m:oMath>'
        '    <m:sSub><m:e><m:r><m:t>v</m:t></m:r></m:e><m:sub><m:r><m:t>mig</m:t></m:r></m:sub></m:sSub>'
        '    <m:r><m:t>(x, y) = </m:t></m:r>'
        '    <m:f>'
        '      <m:num><m:r><m:t>1</m:t></m:r></m:num>'
        '      <m:den><m:r><m:t>‖∇Age(x, y)‖</m:t></m:r></m:den>'
        '    </m:f>'
        '    <m:r><m:t> = </m:t></m:r>'
        '    <m:f>'
        '      <m:num><m:r><m:t>1</m:t></m:r></m:num>'
        '      <m:den>'
        '        <m:rad>'
        '          <m:radPr><m:degHide m:val="1"/></m:radPr><m:deg/>'
        '          <m:e>'
        '            <m:sSup>'
        '              <m:e>'
        '                <m:d><m:e>'
        '                  <m:f>'
        '                    <m:num><m:r><m:t>∂Age</m:t></m:r></m:num>'
        '                    <m:den><m:r><m:t>∂x</m:t></m:r></m:den>'
        '                  </m:f>'
        '                </m:e></m:d>'
        '              </m:e>'
        '              <m:sup><m:r><m:t>2</m:t></m:r></m:sup>'
        '            </m:sSup>'
        '            <m:r><m:t> + </m:t></m:r>'
        '            <m:sSup>'
        '              <m:e>'
        '                <m:d><m:e>'
        '                  <m:f>'
        '                    <m:num><m:r><m:t>∂Age</m:t></m:r></m:num>'
        '                    <m:den><m:r><m:t>∂y</m:t></m:r></m:den>'
        '                  </m:f>'
        '                </m:e></m:d>'
        '              </m:e>'
        '              <m:sup><m:r><m:t>2</m:t></m:r></m:sup>'
        '            </m:sSup>'
        '          </m:e>'
        '        </m:rad>'
        '      </m:den>'
        '    </m:f>'
        '    <m:r><m:t>        (4)</m:t></m:r>'
        '  </m:oMath>'
        '</m:oMathPara>'
    )
    return parse_xml(xml)

def add_omml_eq(doc, omml_elem):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.15
    p._p.append(omml_elem)
    return p

def add_hyperlink(paragraph, url, text, color=COLOR_LINK, underline=True):
    part = paragraph.part
    r_id = part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)

    hyperlink = parse_xml(f'<w:hyperlink {nsdecls("w")} r:id="{r_id}" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"/>')
    new_run = parse_xml(f'<w:r {nsdecls("w")}><w:rPr/></w:r>')
    rPr = new_run.find(qn('w:rPr'))
    
    if color:
        c = parse_xml(f'<w:color {nsdecls("w")} w:val="{color}"/>')
        rPr.append(c)
    if underline:
        u = parse_xml(f'<w:u {nsdecls("w")} w:val="single"/>')
        rPr.append(u)
    font = parse_xml(f'<w:rFonts {nsdecls("w")} w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>')
    rPr.append(font)
    sz = parse_xml(f'<w:sz {nsdecls("w")} w:val="18"/>') # 9pt
    rPr.append(sz)
    
    t = OxmlElement('w:t')
    t.text = text
    new_run.append(t)
    
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)
    return hyperlink

def add_fig(doc, img_path, caption_title, caption_text, width=Inches(6.2)):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(10)
    p_img.paragraph_format.space_after = Pt(4)
    p_img.paragraph_format.keep_with_next = True
    if os.path.exists(img_path):
        run = p_img.add_run()
        run.add_picture(str(img_path), width=width)
    else:
        r = p_img.add_run(f"[FIGURE NOT FOUND: {img_path}]")
        r.font.color.rgb = RGBColor(200, 0, 0)
        
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_cap.paragraph_format.space_before = Pt(2)
    p_cap.paragraph_format.space_after = Pt(10)
    p_cap.paragraph_format.line_spacing = 1.15
    r_title = p_cap.add_run(caption_title + " ")
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(9.5)
    r_title.bold = True
    r_desc = p_cap.add_run(caption_text)
    r_desc.font.name = 'Times New Roman'
    r_desc.font.size = Pt(9.5)
    return p_cap

def add_tbl(doc, tbl_data):
    # Caption first (above table)
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_cap.paragraph_format.space_before = Pt(10)
    p_cap.paragraph_format.space_after = Pt(3)
    p_cap.paragraph_format.line_spacing = 1.15
    p_cap.paragraph_format.keep_with_next = True
    r_title = p_cap.add_run(tbl_data["title"] + " ")
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(9.5)
    r_title.bold = True
    r_desc = p_cap.add_run(tbl_data["caption"])
    r_desc.font.name = 'Times New Roman'
    r_desc.font.size = Pt(9.5)
    
    headers = tbl_data["headers"]
    rows = tbl_data["rows"]
    table = doc.add_table(rows=len(rows)+1, cols=len(headers))
    format_three_line_table(table)
    
    # Header cells
    for j, h in enumerate(headers):
        cell = table.cell(0, j)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.05
        r = p.add_run(h)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9)
        r.bold = True
        r.font.color.rgb = COLOR_PRIMARY
        
    # Data cells
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            cell = table.cell(i+1, j)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.05
            r = p.add_run(str(val))
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_TEXT
            
    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_before = Pt(0)
    p_spacer.paragraph_format.space_after = Pt(6)
    p_spacer.paragraph_format.line_spacing = 1.0
    return table

def build_full_manuscript():
    print("Initializing document...")
    doc = docx.Document()
    
    # 1. Page Margins: 1 inch all around
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        
    # Base Normal Style: Times New Roman 10pt
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(10)
    font.color.rgb = COLOR_TEXT
    
    # 2. Title Block
    p_title = add_p(doc, TITLE, space_before=6, space_after=6, align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, font_size=16, color=COLOR_PRIMARY)
    
    # Authors with typographic superscripts
    p_auth = doc.add_paragraph()
    p_auth.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_auth.paragraph_format.space_before = Pt(2)
    p_auth.paragraph_format.space_after = Pt(2)
    p_auth.paragraph_format.line_spacing = 1.15
    for i, (name, email, aff_num) in enumerate(AUTHORS):
        r_name = p_auth.add_run(name)
        r_name.font.name = 'Times New Roman'
        r_name.font.size = Pt(11)
        r_name.bold = True
        r_aff = p_auth.add_run(aff_num)
        r_aff.font.name = 'Times New Roman'
        r_aff.font.size = Pt(11)
        r_aff.bold = True
        r_aff.font.superscript = True
        if i < len(AUTHORS) - 2:
            r_sep = p_auth.add_run(", ")
        elif i == len(AUTHORS) - 2:
            r_sep = p_auth.add_run(", and ")
        if i < len(AUTHORS) - 1:
            r_sep.font.name = 'Times New Roman'
            r_sep.font.size = Pt(11)
            r_sep.bold = True
            
    # Email IDs
    p_email = doc.add_paragraph()
    p_email.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_email.paragraph_format.space_before = Pt(0)
    p_email.paragraph_format.space_after = Pt(4)
    p_email.paragraph_format.line_spacing = 1.15
    for i, (name, email, aff_num) in enumerate(AUTHORS):
        r_em = p_email.add_run(email)
        r_em.font.name = 'Times New Roman'
        r_em.font.size = Pt(9.5)
        r_em.italic = True
        r_em.font.color.rgb = COLOR_MUTED
        if i < len(AUTHORS) - 1:
            r_com = p_email.add_run(", ")
            r_com.font.name = 'Times New Roman'
            r_com.font.size = Pt(9.5)
            r_com.italic = True
            r_com.font.color.rgb = COLOR_MUTED

    # Affiliation with typographic superscript
    p_aff = doc.add_paragraph()
    p_aff.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_aff.paragraph_format.space_before = Pt(0)
    p_aff.paragraph_format.space_after = Pt(6)
    p_aff.paragraph_format.line_spacing = 1.15
    r_aff_num = p_aff.add_run("1")
    r_aff_num.font.name = 'Times New Roman'
    r_aff_num.font.size = Pt(9)
    r_aff_num.font.superscript = True
    r_aff_text = p_aff.add_run(AFFILIATION)
    r_aff_text.font.name = 'Times New Roman'
    r_aff_text.font.size = Pt(9)
    r_aff_text.italic = True
    
    # Corresponding author note
    add_p(doc, CORRESPONDING_NOTE, space_before=2, space_after=12, align=WD_ALIGN_PARAGRAPH.LEFT, italic=True, font_size=8.5, color=COLOR_MUTED)
    
    # Abstract
    add_h2(doc, "Abstract")
    add_p(doc, ABSTRACT_TEXT, space_before=2, space_after=6, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    
    # Keywords
    p_kw = add_p(doc, "Keywords: ", space_before=2, space_after=14, bold=True, font_size=9.5)
    r_kw = p_kw.add_run("; ".join(KEYWORDS))
    r_kw.font.name = 'Times New Roman'
    r_kw.font.size = Pt(9.5)
    r_kw.italic = True
    
    # -------------------------------------------------------------
    # Section 1. Introduction
    # -------------------------------------------------------------
    add_h1(doc, "1. Introduction")
    for p_text in INTRO_PARAGRAPHS:
        add_p(doc, p_text, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
        
    # -------------------------------------------------------------
    # Section 2. Study Area and Paleoenvironmental Setting
    # -------------------------------------------------------------
    add_h1(doc, "2. Study Area and Paleoenvironmental Setting")
    for i, p_text in enumerate(STUDY_AREA_PARAGRAPHS):
        add_p(doc, p_text, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
        if i == 0:
            add_fig(
                doc,
                FIG_DIR / "fig1_study_sites.png",
                "Figure 1.",
                "Spatial distribution of the 69 retained sedimentary fossil pollen cores (1,706 temporal bins) across Eastern North America (34°–52° N, 100°–60° W). Blue filled circles denote cores with direct LegacyAge 1.0 Bayesian chronologies (n = 57); amber circles denote cores with Neotoma depth-calibrated fallback chronologies (n = 12); red crosses mark excluded cores with <100 woody grains (n = 4)."
            )
            
    # -------------------------------------------------------------
    # Section 3. Data and Methods
    # -------------------------------------------------------------
    add_h1(doc, "3. Data and Methodology")
    
    add_h2(doc, "3.1. Fossil Pollen and Modern Analogue Datasets")
    for p_text in METHODS_PARAGRAPHS["3.1"]:
        add_p(doc, p_text, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
        
    add_h2(doc, "3.2. Independent Paleoclimate Simulation (TraCE-21ka)")
    for p_text in METHODS_PARAGRAPHS["3.2"]:
        add_p(doc, p_text, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
        
    add_h2(doc, "3.3. Chronological Harmonization and Bayesian Depth-Age Models")
    for p_text in METHODS_PARAGRAPHS["3.3"]:
        add_p(doc, p_text, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
        
    add_h2(doc, "3.4. Taxonomic Isolation and REVEALS Pollen Productivity Normalization")
    for p_text in METHODS_PARAGRAPHS["3.4"]:
        add_p(doc, p_text, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    add_tbl(doc, TABLE_1_DATA)
    
    add_h2(doc, "3.5. Stationary First-Differenced Lags and Ebisuzaki Autocorrelation Controls")
    add_p(doc, METHODS_PARAGRAPHS["3.5"][0], align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    add_p(doc, METHODS_PARAGRAPHS["3.5"][1], align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    add_omml_eq(doc, create_omml_eq1())
    
    add_h2(doc, "3.6. Squared Chord Distance and Taxon Attribution of No-Analogue Communities")
    add_p(doc, METHODS_PARAGRAPHS["3.6"][0], align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    add_omml_eq(doc, create_omml_eq2())
    add_p(doc, METHODS_PARAGRAPHS["3.6"][1], align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    add_omml_eq(doc, create_omml_eq3())
    add_p(doc, METHODS_PARAGRAPHS["3.6"][2], align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    
    add_h2(doc, "3.7. Two-Dimensional Planar Migration Velocity and Climate Tracking Deficit")
    add_p(doc, METHODS_PARAGRAPHS["3.7"][0], align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    add_p(doc, METHODS_PARAGRAPHS["3.7"][1], align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    add_omml_eq(doc, create_omml_eq4())
    add_p(doc, METHODS_PARAGRAPHS["3.7"][2], align=WD_ALIGN_PARAGRAPH.JUSTIFY)

    # -------------------------------------------------------------
    # Section 4. Results (Separate Section)
    # -------------------------------------------------------------
    add_h1(doc, "4. Results")
    
    add_h2(doc, "4.1. Deglacial Climatic Dynamics and Community Turnover")
    for p_text in RESULTS_PARAGRAPHS["4.1"]:
        add_p(doc, p_text, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    add_fig(
        doc,
        FIG_DIR / "fig2_climate_and_turnover.png",
        "Figure 2.",
        "Late-Quaternary climate dynamics and community turnover across Eastern North America from TraCE-21ka and Neotoma (15,000–0 cal yr BP). Top panel: Regional mean annual temperature (TREFHT, °C, solid line) and annual precipitation (PRECT, mm/day, dashed line). Middle panel: Thermal warming rate (°C/century) highlighting abrupt warming pulses at 14.5 ka BP and 12.0 ka BP. Bottom panel: Median Hellinger vegetation turnover rate per century (solid line) with interquartile range (shaded ribbon)."
    )
    
    add_h2(doc, "4.2. Climate–Vegetation Lags, Polarity, and Ecological Speed Tiers (RQ1)")
    for p_text in RESULTS_PARAGRAPHS["4.2"]:
        add_p(doc, p_text, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    add_fig(
        doc,
        FIG_DIR / "fig3_genus_lags_raincloud.png",
        "Figure 3.",
        "Postglacial forest response lag dynamics and warming polarity across 13 tree genera. (A) Response delay (median lag ± 95% bootstrap confidence interval) structured into three ecological speed tiers: fast pioneers (<1,000 yr), canopy reorganization taxa (1,000–2,000 yr), and late climax seeders (>2,000 yr). (B) Fossil site response polarity showing percentage of cores exhibiting cold-retreating negative correlations (-r, blue) versus warm-expanding positive correlations (+r, orange), with dark shading indicating Ebisuzaki p < 0.05 significance."
    )
    add_tbl(doc, TABLE_2_DATA)
    
    add_h2(doc, "4.3. Trajectory, Timing, and Taxonomic Drivers of No-Analogue Forests (RQ2)")
    for p_text in RESULTS_PARAGRAPHS["4.3"]:
        add_p(doc, p_text, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    add_fig(
        doc,
        FIG_DIR / "fig4_noanalogue_drivers.png",
        "Figure 4.",
        "Temporal dynamics and taxonomic drivers of late-Quaternary no-analogue forest communities. Top panel: Percentage of fossil pollen samples classified as no-analogue (blue line, exceeding modern 5th percentile SCD threshold = 0.1060) overlaid with absolute climate warming rate (|dT/dt|, orange dashed line). Bottom panel: Taxonomic decomposition of mean Squared Chord Distance (SCD) contributions across 15,000 years, showing elevated deglacial contributions from Quercus, Alnus, Betula, Populus, and Picea."
    )
    add_tbl(doc, TABLE_3_DATA)
    
    add_h2(doc, "4.4. Two-Dimensional Migration Isochrones and Topographic Steering (RQ3)")
    for p_text in RESULTS_PARAGRAPHS["4.4"]:
        add_p(doc, p_text, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    add_fig(
        doc,
        FIG_DIR / "fig5_migration_isochrones.png",
        "Figure 5.",
        "Two-dimensional postglacial arrival age isochrones (ka BP) and local migration vectors across the five tree genera passing the 2D planar regression significance gate (p_2d <= 0.05). Contours represent arrival surfaces interpolated via thin-plate splines clipped strictly to observed convex hulls. Black arrows indicate local dispersal vectors and mean azimuths: Carya (azimuth 65.0° ENE), Alnus (308.2° WNW), Fagus (344.4° NNW), Tsuga (344.3° NNW), and Larix (1.2° N)."
    )
    add_tbl(doc, TABLE_4_DATA)
    
    add_h2(doc, "4.5. Empirical Migration Ceilings and the 9.3x Velocity Tracking Deficit")
    for p_text in RESULTS_PARAGRAPHS["4.5"]:
        add_p(doc, p_text, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    add_fig(
        doc,
        FIG_DIR / "fig6_velocity_deficit.png",
        "Figure 6.",
        "Log-scale comparison of empirical 2D postglacial tree migration speeds against past deglacial climate velocity and projected 21st-century anthropogenic climate velocity. Green circles mark median migration velocities; horizontal whiskered bars show spatial surface ranges (min–max). Blue dashed line indicates 95th-percentile deglacial climate velocity (332.1 m/yr); orange dashed-dotted line marks projected contemporary climate velocity (1,573.8 m/yr for 1.9 °C/century warming), illustrating the 9.3x continental velocity deficit."
    )
    add_tbl(doc, TABLE_6_DATA)
    
    add_h2(doc, "4.6. Chronological Uncertainty, Bin-Resolution, and Planted-Truth Sensitivity")
    for p_text in RESULTS_PARAGRAPHS["4.6"]:
        add_p(doc, p_text, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    add_tbl(doc, TABLE_5_DATA)

    # -------------------------------------------------------------
    # Section 5. Discussion (Separate Section)
    # -------------------------------------------------------------
    add_h1(doc, "5. Discussion")
    
    add_h2(doc, "5.1. Biophysical Mechanisms Driving Century-to-Millennial Response Lags")
    for p_text in DISCUSSION_PARAGRAPHS["5.1"]:
        add_p(doc, p_text, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
        
    add_h2(doc, "5.2. Genesis and Dissolution of No-Analogue Communities: Seasonality vs Herbivore Loss")
    for p_text in DISCUSSION_PARAGRAPHS["5.2"]:
        add_p(doc, p_text, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
        
    add_h2(doc, "5.3. The 9.3x Velocity Tracking Deficit in Fragmented Anthropocene Landscapes")
    for p_text in DISCUSSION_PARAGRAPHS["5.3"]:
        add_p(doc, p_text, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
        
    add_h2(doc, "5.4. Methodological Synthesis: Calibration, Autocorrelation, and Model Independence")
    for p_text in DISCUSSION_PARAGRAPHS["5.4"]:
        add_p(doc, p_text, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
        
    add_h2(doc, "5.5. Implications for 21st-Century Forest Conservation and Assisted Migration")
    for p_text in DISCUSSION_PARAGRAPHS["5.5"]:
        add_p(doc, p_text, align=WD_ALIGN_PARAGRAPH.JUSTIFY)

    # -------------------------------------------------------------
    # Section 6. Limitations and Future Directions
    # -------------------------------------------------------------
    add_h1(doc, "6. Limitations and Future Directions")
    for p_text in LIMITATIONS_PARAGRAPHS:
        add_p(doc, p_text, align=WD_ALIGN_PARAGRAPH.JUSTIFY)

    # -------------------------------------------------------------
    # Section 7. Conclusions
    # -------------------------------------------------------------
    add_h1(doc, "7. Conclusions")
    for p_text in CONCLUSIONS_PARAGRAPHS:
        add_p(doc, p_text, align=WD_ALIGN_PARAGRAPH.JUSTIFY)

    # -------------------------------------------------------------
    # Acknowledgements & Declarations
    # -------------------------------------------------------------
    add_h1(doc, "Acknowledgements")
    add_p(doc, ACKNOWLEDGEMENTS_TEXT, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    
    add_h1(doc, "Declarations")
    for dec_title, dec_text in DECLARATIONS.items():
        add_h2(doc, dec_title)
        add_p(doc, dec_text, align=WD_ALIGN_PARAGRAPH.JUSTIFY)

    # -------------------------------------------------------------
    # References (Author-Date, Alphabetical, Unnumbered, Clickable Hyperlinks)
    # -------------------------------------------------------------
    add_h1(doc, "References")
    sorted_ref_keys = sorted(REFERENCES_DB.keys(), key=lambda k: k.lower())
    for k in sorted_ref_keys:
        ref_text = REFERENCES_DB[k]
        p_ref = doc.add_paragraph()
        p_ref.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_ref.paragraph_format.space_before = Pt(2)
        p_ref.paragraph_format.space_after = Pt(4)
        p_ref.paragraph_format.line_spacing = 1.15
        p_ref.paragraph_format.left_indent = Inches(0.3)
        p_ref.paragraph_format.first_line_indent = Inches(-0.3)
        
        # Parse out URL/DOI for clickable hyperlink
        m = re.search(r'(https?://[^\s]+)', ref_text)
        if m:
            prefix = ref_text[:m.start()]
            url = m.group(1)
            suffix = ref_text[m.end():]
            
            r_pre = p_ref.add_run(prefix)
            r_pre.font.name = 'Times New Roman'
            r_pre.font.size = Pt(9)
            r_pre.font.color.rgb = COLOR_TEXT
            
            add_hyperlink(p_ref, url, url, color=COLOR_LINK, underline=True)
            
            if suffix:
                r_suf = p_ref.add_run(suffix)
                r_suf.font.name = 'Times New Roman'
                r_suf.font.size = Pt(9)
                r_suf.font.color.rgb = COLOR_TEXT
        else:
            r = p_ref.add_run(ref_text)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9)
            r.font.color.rgb = COLOR_TEXT

    output_path = ROOT / "TBD2_Comprehensive_Project_Report.docx"
    doc.save(str(output_path))
    print(f"Report successfully built and saved to: {output_path}")
    return output_path

if __name__ == "__main__":
    build_full_manuscript()
