#!/usr/bin/python
import os
import xml.etree.ElementTree as ET

def change_svg_color(svg_file, new_color):
    try:
        tree = ET.parse(svg_file)
        root = tree.getroot()
        for element in root.iter():
            if 'fill' in element.attrib:
                element.attrib['fill'] = new_color
            if 'stroke' in element.attrib:
                element.attrib['stroke'] = new_color
        tree.write(svg_file)
        print(f"Color changed in: {svg_file}")
    except Exception as e:
        print(f"Error processing {svg_file}: {e}")

def batch_change_color_in_directory(directory_path, new_color):
    for filename in os.listdir(directory_path):
        if filename.endswith('.svg'):
            svg_file_path = os.path.join(directory_path, filename)
            change_svg_color(svg_file_path, new_color)

if __name__ == "__main__":
    svg_files_directory = os.getcwd()
    new_color = '#ffffff'
    batch_change_color_in_directory(svg_files_directory, new_color)
