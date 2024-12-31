import svgwrite

def create_simple_logo():
    # Create new SVG drawing
    dwg = svgwrite.Drawing('logo.svg', size=(200, 200))

    # Add background circle
    dwg.add(dwg.circle(center=(100, 100), r=80,
            fill='#2196F3'))

    # Add text
    dwg.add(dwg.text('LOGO', insert=(50, 110),
            fill='white', font_size=40))

    dwg.save()

create_simple_logo()