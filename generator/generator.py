import re
import os


def parse_dotUML(file_path):
    classes = {}
    relations = []
    with open(file_path, 'r') as file:
        content = file.read()
        class_matches = re.findall(r'class (\w+) {([\s\S]*?)\}', content)
        for class_name, class_body in class_matches:
            attributes = re.findall(r'private (\w+) : (\w+)', class_body)
            methods = re.findall(r'public (\w+)\((.*?)\)', class_body)
            classes[class_name] = {'attributes': attributes, 'methods': methods}
            relations.extend(re.findall(r'(\w+) ("[\d\*]+")?--("[\d\*]+")? (\w+)', class_body))
    return classes, relations


def generate_java_class(class_name, attributes=[]):
    package = 'package com.trodieng.parisportif.model\n\n'
    imports = ("import javax.persistence.*;\nimport org.openxava.annotations.*;\nimport lombok.*;\nimport "
               "org.openxava.model.*;\n")
    lombok_annotations = '\n@Entity @Getter @Setter\n'
    java_code = f'{package}{imports}{lombok_annotations}public class {class_name} extends Identifiable' + ' {\n'
    for attribute_name, attribute_type in attributes:
        if attribute_name.lower() != 'identifiant' and not (
                attribute_name.lower().startswith('id') or attribute_name.lower().endswith(
                'id') or 'identifiant' in attribute_name.lower()):
            if attribute_type.lower() == 'string':
                attribute_type = 'String'
            java_code += f'    @Column\n    private {attribute_type} {attribute_name};\n'
    java_code += '}\n'
    return java_code


def generate_java_files(classes, relations, output_directory):
    for class_name, class_info in classes.items():
        class_content = generate_java_class(class_name, class_info['attributes'])
        classes[class_name] = class_content

    for class_name, class_content in classes.items():
        file_name = f'{class_name}.java'
        file_path = os.path.join(output_directory, file_name)
        with open(file_path, 'w') as file:
            file.write(class_content)

    for relation in relations:
        relation_type = relation[1].replace('"', '')
        if relation_type == '1':
            field_type = class_name.capitalize()
        elif relation_type == '*':
            field_type = f'List<{class_name.capitalize()}>'
        else:
            continue
        field_name = relation[3]
        with open(os.path.join(output_directory, f'{field_name.capitalize()}.java'), 'a') as file:
            file.write(f'\n    @ManyToOne\n    private {field_type} {field_name};\n')


def main(input_file, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    classes, relations = parse_dotUML(input_file)
    generate_java_files(classes, relations, output_directory)
    print("Java files generated successfully!")


if __name__ == "__main__":
    input_file = '../diagrams/class.dotuml'
    output_directory = 'java_classes'
    main(input_file, output_directory)
