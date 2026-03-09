#!/usr/bin/env python3
"""
Generate a light SysML2 ontology focused on ownership relationships.
This script extracts classes and properties related to ownership from the full ontology.
"""

import json
import xml.etree.ElementTree as ET
from datetime import datetime

# Namespaces
NS = {
    "owl": "http://www.w3.org/2002/07/owl#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "sysml": "https://www.omg.org/spec/SysML#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
}


def load_ownership_properties():
    """Load ownership properties from JSON file."""
    with open("ownership_props.json", "r") as f:
        return json.load(f)


def extract_classes_from_properties(properties):
    """Extract unique classes from property domains and ranges."""
    classes = set()
    for prop in properties:
        if prop.get("domain"):
            classes.add(prop["domain"])
        if prop.get("range"):
            classes.add(prop["range"])
    return sorted(classes)


def parse_full_ontology():
    """Parse the full SysML ontology to extract class definitions."""
    tree = ET.parse("sysml2/owl/www.omg.org/spec/SysML.owl")
    root = tree.getroot()

    # Register namespaces
    for prefix, uri in NS.items():
        ET.register_namespace(prefix, uri)

    classes_info = {}

    # Find all owl:Class elements
    for cls in root.findall(".//{http://www.w3.org/2002/07/owl#}Class"):
        about = cls.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about")
        if about:
            label = cls.find("{http://www.w3.org/2000/01/rdf-schema#}label")
            comment = cls.find("{http://www.w3.org/2000/01/rdf-schema#}comment")
            subclasses = cls.findall(
                "{http://www.w3.org/2000/01/rdf-schema#}subClassOf"
            )

            classes_info[about] = {
                "uri": about,
                "label": label.text if label is not None else about.split("#")[-1],
                "comment": comment.text if comment is not None else "",
                "subClassOf": [
                    sc.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
                    for sc in subclasses
                    if sc.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
                ],
            }

    return classes_info


def clean_comment(comment):
    """Clean HTML tags from comments."""
    import re

    # Remove HTML tags
    comment = re.sub(r"<[^>]+>", "", comment)
    # Unescape HTML entities
    comment = comment.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    return comment.strip()


def generate_turtle(properties, classes_info, output_file):
    """Generate Turtle format ontology."""

    with open(output_file, "w", encoding="utf-8") as f:
        # Header
        f.write("# SysML2 Light Ontology - Ownership Relationships\n")
        f.write(f"# Generated: {datetime.now().isoformat()}\n")
        f.write("# Focus: Ownership and containment relationships\n")
        f.write(f"# Classes: {len(classes_info)} | Properties: {len(properties)}\n\n")

        # Prefixes
        f.write("@prefix : <https://www.omg.org/spec/SysML#> .\n")
        f.write("@prefix owl: <http://www.w3.org/2002/07/owl#> .\n")
        f.write("@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n")
        f.write("@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n")
        f.write("@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\n")

        # Ontology declaration
        f.write("<https://www.omg.org/spec/SysML-Light-Ownership>\n")
        f.write("    a owl:Ontology ;\n")
        f.write('    rdfs:label "SysML2 Light Ontology - Ownership" ;\n')
        f.write(
            '    rdfs:comment "A lightweight version of the SysML2 ontology focused on querying ownership and containment relationships." ;\n'
        )
        f.write('    owl:versionInfo "1.0" .\n\n')

        # Classes
        f.write("#\n# Classes\n#\n\n")

        for class_uri in sorted(classes_info.keys()):
            cls = classes_info[class_uri]
            short_name = class_uri.split("#")[-1]

            f.write(f":{short_name}\n")
            f.write(f"    a owl:Class ;\n")
            f.write(f'    rdfs:label "{cls["label"]}" ;\n')

            if cls["comment"]:
                comment = clean_comment(cls["comment"])
                # Escape quotes and newlines
                comment = (
                    comment.replace("\\", "\\\\")
                    .replace('"', '\\"')
                    .replace("\n", "\\n")
                )
                f.write(f'    rdfs:comment "{comment}" ;\n')

            if cls["subClassOf"]:
                for parent in cls["subClassOf"]:
                    parent_short = parent.split("#")[-1]
                    f.write(f"    rdfs:subClassOf :{parent_short} ;\n")

            # Remove trailing semicolon and add period
            f.seek(f.tell() - 3)
            f.write(" .\n\n")

        # Properties
        f.write("#\n# Object Properties - Ownership Relationships\n#\n\n")

        for prop in sorted(properties, key=lambda p: p["uri"]):
            short_name = prop["uri"].split("#")[-1]

            f.write(f":{short_name}\n")
            f.write(f"    a owl:ObjectProperty ;\n")

            if prop.get("label"):
                f.write(f'    rdfs:label "{prop["label"]}" ;\n')

            if prop.get("comment"):
                comment = clean_comment(prop["comment"])
                comment = (
                    comment.replace("\\", "\\\\")
                    .replace('"', '\\"')
                    .replace("\n", "\\n")
                )
                f.write(f'    rdfs:comment "{comment}" ;\n')

            if prop.get("domain"):
                domain_short = prop["domain"].split("#")[-1]
                f.write(f"    rdfs:domain :{domain_short} ;\n")

            if prop.get("range"):
                range_short = prop["range"].split("#")[-1]
                f.write(f"    rdfs:range :{range_short} ;\n")

            if prop.get("subPropertyOf"):
                for parent in prop["subPropertyOf"]:
                    parent_short = parent.split("#")[-1]
                    f.write(f"    rdfs:subPropertyOf :{parent_short} ;\n")

            if prop.get("inverseOf"):
                inverse_short = prop["inverseOf"].split("#")[-1]
                f.write(f"    owl:inverseOf :{inverse_short} ;\n")

            if prop.get("isFunctional"):
                f.write(f"    a owl:FunctionalProperty ;\n")

            if prop.get("isInverseFunctional"):
                f.write(f"    a owl:InverseFunctionalProperty ;\n")

            # Remove trailing semicolon and add period
            f.seek(f.tell() - 3)
            f.write(" .\n\n")


def generate_rdfxml(properties, classes_info, output_file):
    """Generate RDF/XML format ontology."""

    # Register namespaces first
    for prefix, uri in NS.items():
        ET.register_namespace(prefix, uri)

    # Create root element
    root = ET.Element("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF")
    root.set("xmlns", "https://www.omg.org/spec/SysML#")
    root.set("xml:base", "https://www.omg.org/spec/SysML-Light-Ownership")

    # Ontology declaration
    ontology = ET.SubElement(root, "{http://www.w3.org/2002/07/owl#}Ontology")
    ontology.set(
        "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about",
        "https://www.omg.org/spec/SysML-Light-Ownership",
    )

    label = ET.SubElement(ontology, "{http://www.w3.org/2000/01/rdf-schema#}label")
    label.text = "SysML2 Light Ontology - Ownership"

    comment = ET.SubElement(ontology, "{http://www.w3.org/2000/01/rdf-schema#}comment")
    comment.text = "A lightweight version of the SysML2 ontology focused on querying ownership and containment relationships."

    version = ET.SubElement(ontology, "{http://www.w3.org/2002/07/owl#}versionInfo")
    version.text = "1.0"

    # Add comment about generation
    root_comment = ET.Comment(f" Generated: {datetime.now().isoformat()} ")
    root.insert(1, root_comment)
    root.insert(
        2, ET.Comment(f" Classes: {len(classes_info)} | Properties: {len(properties)} ")
    )

    # Classes
    for class_uri in sorted(classes_info.keys()):
        cls = classes_info[class_uri]

        cls_elem = ET.SubElement(root, "{http://www.w3.org/2002/07/owl#}Class")
        cls_elem.set("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about", class_uri)

        label = ET.SubElement(cls_elem, "{http://www.w3.org/2000/01/rdf-schema#}label")
        label.text = cls["label"]

        if cls["comment"]:
            comment = ET.SubElement(
                cls_elem, "{http://www.w3.org/2000/01/rdf-schema#}comment"
            )
            comment.text = clean_comment(cls["comment"])

        for parent in cls["subClassOf"]:
            subclass = ET.SubElement(
                cls_elem, "{http://www.w3.org/2000/01/rdf-schema#}subClassOf"
            )
            subclass.set(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource", parent
            )

    # Properties
    for prop in sorted(properties, key=lambda p: p["uri"]):
        prop_elem = ET.SubElement(
            root, "{http://www.w3.org/2002/07/owl#}ObjectProperty"
        )
        prop_elem.set("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about", prop["uri"])

        if prop.get("label"):
            label = ET.SubElement(
                prop_elem, "{http://www.w3.org/2000/01/rdf-schema#}label"
            )
            label.text = prop["label"]

        if prop.get("comment"):
            comment = ET.SubElement(
                prop_elem, "{http://www.w3.org/2000/01/rdf-schema#}comment"
            )
            comment.text = clean_comment(prop["comment"])

        if prop.get("domain"):
            domain = ET.SubElement(
                prop_elem, "{http://www.w3.org/2000/01/rdf-schema#}domain"
            )
            domain.set(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource", prop["domain"]
            )

        if prop.get("range"):
            range_elem = ET.SubElement(
                prop_elem, "{http://www.w3.org/2000/01/rdf-schema#}range"
            )
            range_elem.set(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource", prop["range"]
            )

        for parent in prop.get("subPropertyOf", []):
            subprop = ET.SubElement(
                prop_elem, "{http://www.w3.org/2000/01/rdf-schema#}subPropertyOf"
            )
            subprop.set("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource", parent)

        if prop.get("inverseOf"):
            inverse = ET.SubElement(
                prop_elem, "{http://www.w3.org/2002/07/owl#}inverseOf"
            )
            inverse.set(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource",
                prop["inverseOf"],
            )

        if prop.get("isFunctional"):
            rdf_type = ET.SubElement(
                prop_elem, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}type"
            )
            rdf_type.set(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource",
                "http://www.w3.org/2002/07/owl#FunctionalProperty",
            )

        if prop.get("isInverseFunctional"):
            rdf_type = ET.SubElement(
                prop_elem, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}type"
            )
            rdf_type.set(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource",
                "http://www.w3.org/2002/07/owl#InverseFunctionalProperty",
            )

    # Pretty print and write
    ET.indent(root, space="    ")
    tree = ET.ElementTree(root)
    tree.write(output_file, encoding="utf-8", xml_declaration=True)


def main():
    print("Loading ownership properties...")
    properties = load_ownership_properties()
    print(f"Loaded {len(properties)} ownership properties")

    print("\nExtracting classes from properties...")
    class_uris = extract_classes_from_properties(properties)
    print(f"Found {len(class_uris)} unique classes")

    print("\nParsing full ontology for class definitions...")
    all_classes_info = parse_full_ontology()
    print(f"Parsed {len(all_classes_info)} class definitions from full ontology")

    # Filter to only classes involved in ownership
    classes_info = {
        uri: info for uri, info in all_classes_info.items() if uri in class_uris
    }
    print(f"Using {len(classes_info)} classes for light ontology")

    print("\nGenerating Turtle format...")
    generate_turtle(properties, classes_info, "sysml2-light-ownership.ttl")
    print("✓ Created sysml2-light-ownership.ttl")

    print("\nGenerating RDF/XML format...")
    generate_rdfxml(properties, classes_info, "sysml2-light-ownership.owl")
    print("✓ Created sysml2-light-ownership.owl")

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Classes:    {len(classes_info)}")
    print(f"Properties: {len(properties)}")
    print(f"  - Functional: {sum(1 for p in properties if p.get('isFunctional'))}")
    print(
        f"  - Inverse Functional: {sum(1 for p in properties if p.get('isInverseFunctional'))}"
    )
    print(f"  - With inverseOf: {sum(1 for p in properties if p.get('inverseOf'))}")
    print(
        f"  - With subPropertyOf: {sum(1 for p in properties if p.get('subPropertyOf'))}"
    )
    print("=" * 60)


if __name__ == "__main__":
    main()
