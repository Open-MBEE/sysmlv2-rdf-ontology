# SysML2 Light Ontology - File Guide

## 📁 Generated Files Overview

All files generated for the SysML2 Light Ontology project, organized by category.

---

## 🎯 Primary Ontology Files (USE THESE!)

### Light Ontology - Two Formats

| File | Size | Format | Description |
|------|------|--------|-------------|
| **sysml2-light-ownership.ttl** | 93 KB | Turtle | **Recommended**: Human-readable, compact format |
| **sysml2-light-ownership.owl** | 127 KB | RDF/XML | For Protégé and other OWL tools |

**Content**: 68 classes, 86 ownership properties, validated syntax

**Choose**:
- `.ttl` for: Python (rdflib), SPARQL endpoints, version control
- `.owl` for: Protégé, OWL tools, XML-based systems

---

## 📚 Documentation Files (START HERE!)

### Main Documentation

| File | Size | Purpose | Audience |
|------|------|---------|----------|
| **LIGHT-ONTOLOGY-SUMMARY.md** | 9 KB | **Start here** - Project overview | All users |
| **LIGHT-ONTOLOGY-README.md** | 11 KB | Complete documentation | Developers |
| **SPARQL-QUERY-EXAMPLES.md** | 11 KB | 50 practical query examples | Query writers |
| **OWNERSHIP_PROPERTIES_QUICK_REF.md** | 11 KB | Property reference tables | Quick lookup |
| **LIGHT-ONTOLOGY-FILES.md** | This file | File guide | Navigation |

**Reading Order**:
1. LIGHT-ONTOLOGY-SUMMARY.md - Get the big picture
2. LIGHT-ONTOLOGY-README.md - Understand details
3. SPARQL-QUERY-EXAMPLES.md - Learn to query
4. OWNERSHIP_PROPERTIES_QUICK_REF.md - Reference when needed

---

## 🔧 Generation & Analysis Files

### Property Extraction Data

| File | Size | Format | Use Case |
|------|------|--------|----------|
| **ownership_props.json** | 52 KB | JSON | Raw property data, programmatic access |
| **ownership_props_summary.json** | 59 KB | JSON | Structured with categories |
| **ownership_props.csv** | 26 KB | CSV | Import to spreadsheet tools |
| **ownership_props_report.md** | 31 KB | Markdown | Detailed human-readable report |
| **ownership_properties_summary.txt** | 11 KB | Text | Plain text summary |

### Generation Script

| File | Size | Purpose |
|------|------|---------|
| **generate_light_ontology.py** | 13 KB | Regenerate ontology from source |

**Usage**: `python3 generate_light_ontology.py`

---

## 📖 Quick Start Guide

### For Newcomers

1. **Read**: `LIGHT-ONTOLOGY-SUMMARY.md`
2. **Load**: `sysml2-light-ownership.ttl`
3. **Try**: Queries from `SPARQL-QUERY-EXAMPLES.md`

### For Developers

1. **Study**: `LIGHT-ONTOLOGY-README.md`
2. **Reference**: `OWNERSHIP_PROPERTIES_QUICK_REF.md`
3. **Extend**: Modify `generate_light_ontology.py` if needed

### For Data Scientists

1. **Import**: `ownership_props.csv` into your analysis tool
2. **Analyze**: `ownership_props.json` programmatically
3. **Query**: Load `.ttl` into RDF store

---

## 🎯 File Usage Matrix

| Task | Primary File | Supporting Files |
|------|-------------|------------------|
| **Load ontology in Python** | sysml2-light-ownership.ttl | SPARQL-QUERY-EXAMPLES.md |
| **Open in Protégé** | sysml2-light-ownership.owl | LIGHT-ONTOLOGY-README.md |
| **Learn SPARQL** | SPARQL-QUERY-EXAMPLES.md | sysml2-light-ownership.ttl |
| **Understand properties** | OWNERSHIP_PROPERTIES_QUICK_REF.md | ownership_props_report.md |
| **Analyze property data** | ownership_props.csv | ownership_props.json |
| **Get project overview** | LIGHT-ONTOLOGY-SUMMARY.md | - |
| **Regenerate ontology** | generate_light_ontology.py | ownership_props.json |

---

## 📊 File Sizes at a Glance

```
Ontology Files:
  sysml2-light-ownership.owl     127 KB  ████████████████████████
  sysml2-light-ownership.ttl      93 KB  ██████████████████

Analysis Data:
  ownership_props_summary.json    59 KB  ███████████
  ownership_props.json            52 KB  ██████████
  ownership_props_report.md       31 KB  ██████
  ownership_props.csv             26 KB  █████

Documentation:
  SPARQL-QUERY-EXAMPLES.md        11 KB  ██
  LIGHT-ONTOLOGY-README.md        11 KB  ██
  OWNERSHIP_PROPERTIES_QUICK_REF  11 KB  ██
  LIGHT-ONTOLOGY-SUMMARY.md        9 KB  ██

Scripts:
  generate_light_ontology.py      13 KB  ███
```

---

## 🔄 File Dependencies

```
┌─────────────────────────┐
│  Full SysML Ontology    │
│  (sysml2/owl/...)       │
└───────────┬─────────────┘
            │
            │ extract
            ▼
┌─────────────────────────┐
│  ownership_props.json   │ ◄──── Source data
└───────────┬─────────────┘
            │
            │ generate
            ▼
┌─────────────────────────┐
│  generate_light_        │
│  ontology.py            │ ◄──── Generator script
└───────────┬─────────────┘
            │
            │ produces
            ▼
┌─────────────────────────┬─────────────────────────┐
│ sysml2-light-           │ sysml2-light-           │
│ ownership.ttl           │ ownership.owl           │
└─────────────────────────┴─────────────────────────┘
            │
            │ documented by
            ▼
┌─────────────────────────┬─────────────────────────┐
│ LIGHT-ONTOLOGY-         │ SPARQL-QUERY-           │
│ README.md               │ EXAMPLES.md             │
└─────────────────────────┴─────────────────────────┘
```

---

## 💾 Storage & Version Control

### Recommended for Git

**Essential files** (always commit):
- ✅ sysml2-light-ownership.ttl
- ✅ sysml2-light-ownership.owl
- ✅ All .md documentation files
- ✅ generate_light_ontology.py
- ✅ ownership_props.json

**Optional** (can regenerate):
- ⚠️ ownership_props_summary.json
- ⚠️ ownership_props.csv
- ⚠️ ownership_props_report.md

### File Portability

**Self-contained**:
- sysml2-light-ownership.ttl ✓
- sysml2-light-ownership.owl ✓

**Requires context**:
- generate_light_ontology.py (needs full ontology)
- SPARQL examples (need ontology loaded)

---

## 🎓 Educational Path

### Beginner
1. Read: LIGHT-ONTOLOGY-SUMMARY.md
2. Load: sysml2-light-ownership.ttl (any RDF tool)
3. Try: First 10 queries from SPARQL-QUERY-EXAMPLES.md

### Intermediate
1. Study: LIGHT-ONTOLOGY-README.md
2. Explore: OWNERSHIP_PROPERTIES_QUICK_REF.md
3. Practice: All queries from SPARQL-QUERY-EXAMPLES.md

### Advanced
1. Analyze: ownership_props.json
2. Customize: generate_light_ontology.py
3. Extend: Add new property categories

---

## 🔍 Finding Information

| Question | File |
|----------|------|
| What is this project? | LIGHT-ONTOLOGY-SUMMARY.md |
| How do I use it? | LIGHT-ONTOLOGY-README.md |
| What properties exist? | OWNERSHIP_PROPERTIES_QUICK_REF.md |
| How do I query it? | SPARQL-QUERY-EXAMPLES.md |
| How was it generated? | generate_light_ontology.py |
| What's the raw data? | ownership_props.json |
| Which file should I use? | LIGHT-ONTOLOGY-FILES.md (this file) |

---

## 📞 Support

For questions about:
- **Ontology content**: See LIGHT-ONTOLOGY-README.md
- **Querying**: See SPARQL-QUERY-EXAMPLES.md
- **Properties**: See OWNERSHIP_PROPERTIES_QUICK_REF.md
- **Generation**: See comments in generate_light_ontology.py

---

**Last Updated**: February 24, 2026  
**Version**: 1.0
