# generate_pdf.py
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, ListFlowable, ListItem, PageBreak
from reportlab.lib.units import inch
from aws_content import aws_pages
import os

def create_pdf(filename):
    # Reduced margins to fit more on one page
    doc = SimpleDocTemplate(filename, pagesize=letter, topMargin=20, bottomMargin=20, leftMargin=40, rightMargin=40)
    story = []
    
    styles = getSampleStyleSheet()
    
    # Custom Styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=20, # Reduced from 24
        textColor=colors.darkblue,
        spaceAfter=6, # Reduced
        alignment=1 # Center
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=12,
        textColor=colors.darkgray,
        spaceAfter=15, # Reduced
        alignment=1
    )
    
    header_style = ParagraphStyle(
        'CustomHeader',
        parent=styles['Heading2'],
        fontSize=14, # Reduced from 18
        textColor=colors.black,
        spaceBefore=10, # Reduced
        spaceAfter=5, # Reduced
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=10, # Reduced from 12
        leading=14, # Reduced from 18
        spaceAfter=6,
        fontName='Helvetica'
    )

    q_style = ParagraphStyle(
        'Question',
        parent=styles['Normal'],
        fontSize=10, # Reduced
        leading=12,
        textColor=colors.darkblue,
        spaceBefore=0,
        fontName='Helvetica-Bold'
    )

    a_style = ParagraphStyle(
        'Answer',
        parent=styles['Normal'],
        fontSize=10, # Reduced
        leading=12,
        textColor=colors.black,
        spaceAfter=0,
        fontName='Helvetica'
    )

    # Loop through each page in the content
    for text_page in aws_pages:
        # Title Section
        story.append(Paragraph(text_page['title'], title_style))
        story.append(Paragraph(text_page['subtitle'], subtitle_style))
        story.append(Spacer(1, 0.1*inch))
        
        # Process Sections
        for section in text_page['sections']:
            # Header
            if 'header' in section:
                story.append(Paragraph(section['header'], header_style))
            
            # Body text
            if 'body' in section:
                story.append(Paragraph(section['body'], body_style))
            
            # Bullet Points
            if 'items' in section:
                bullet_list = []
                for item in section['items']:
                    bullet_list.append(ListItem(Paragraph(item, body_style)))
                story.append(ListFlowable(bullet_list, bulletType='bullet', start='circle', leftIndent=20))
                story.append(Spacer(1, 4))
                
            # Subsections
            if 'subsections' in section:
                data = []
                for sub in section['subsections']:
                    title_p = Paragraph(f"<b>{sub['title']}</b>", body_style)
                    text_p = Paragraph(sub['text'], body_style)
                    data.append([title_p, text_p])
                
                t = Table(data, colWidths=[1.5*inch, 5*inch])
                t.setStyle(TableStyle([
                    ('VALIGN', (0,0), (-1,-1), 'TOP'),
                    ('LEFTPADDING', (0,0), (-1,-1), 0),
                    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
                ]))
                story.append(t)

            # Interview Section
            if 'interview' in section:
                q_text = section['interview']['question']
                a_text = section['interview']['answer']
                
                # Create a "Card" effect using a Table
                q_para = Paragraph(f"{q_text}", q_style)
                a_para = Paragraph(f"{a_text}", a_style)
                
                # Table data: [Question], [Answer]
                data = [[q_para], [a_para]]
                
                t_interview = Table(data, colWidths=[7*inch]) # Wider table since margins are smaller
                t_interview.setStyle(TableStyle([
                    ('BOX', (0,0), (-1,-1), 1, colors.darkblue), # Blue border
                    ('BACKGROUND', (0,0), (-1,-1), colors.aliceblue), # Light background
                    ('TOPPADDING', (0,0), (-1,-1), 5), # Reduced padding
                    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
                    ('LEFTPADDING', (0,0), (-1,-1), 5),
                    ('RIGHTPADDING', (0,0), (-1,-1), 5),
                    ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey), # Divider line
                ]))
                
                story.append(Spacer(1, 5)) # Reduced spacer
                story.append(t_interview)

            story.append(Spacer(1, 6)) # Reduced section spacer
            
        # Just a visual spacer between topics
        story.append(Spacer(1, 20))
        
    # Build
    try:
        doc.build(story)
        print(f"Successfully created {filename}")
    except Exception as e:
        print(f"Error creating PDF: {e}")

if __name__ == "__main__":
    output_path = "AWS_Notes_Sample.pdf"
    create_pdf(output_path)
