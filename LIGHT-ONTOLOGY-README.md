# SysML2 Light Ontology - Ownership Relationships

## Overview

This is a **lightweight version** of the SysML2 RDF ontology, specifically designed for efficient querying of **ownership and containment relationships**. It extracts the essential classes and properties needed to understand and query the ownership hierarchy in SysML models.

## Files

- **`sysml2-light-ownership.ttl`** (93 KB) - Turtle/RDF format, human-readable
- **`sysml2-light-ownership.owl`** (127 KB) - RDF/XML format, compatible with Protégé and other OWL tools
- **`generate_light_ontology.py`** - Script used to generate the light ontology from the full SysML ontology

## Statistics

| Metric | Count |
|--------|-------|
| **Classes** | 68 |
| **Object Properties** | 86 |
| Functional Properties | 47 |
| Properties with inverseOf | 28 |
| Properties with subPropertyOf | 60 |

**Reduction**: From 344 classes and 696 properties in the full ontology to 68 classes and 86 properties (~80% reduction)

## What's Included

### Core Classes

The light ontology includes only classes that participate in ownership relationships:

#### Foundational Classes
- `Element` - Root class for all SysML elements
- `Relationship` - Base for all relationships
- `Namespace` - Elements that can contain other elements
- `Membership` - Relationships between namespaces and members
- `OwningMembership` - Memberships with ownership semantics

#### Type Hierarchy
- `Type` - Types in the model
- `Classifier` - Types with classification
- `Feature` - Structural/behavioral characteristics
- `Definition` - Reusable type definitions
- `Usage` - Uses of definitions

#### Specialized Membership Types
- `FeatureMembership` - Membership for features
- `ParameterMembership` - Membership for parameters
- `ActorMembership` - Actor parameters
- `RequirementConstraintMembership` - Requirement constraints
- `StakeholderMembership`, `SubjectMembership`, etc.

#### Specialization Relationships
- `Specialization` - Generalization/specialization
- `Subsetting`, `Redefinition` - Feature specialization
- `FeatureTyping` - Type assignments
- `Subclassification` - Classifier specialization

#### Definition & Usage Types
- **Definitions**: 22+ specialized definition types (ActionDefinition, PartDefinition, etc.)
- **Usages**: 24+ specialized usage types (ActionUsage, PartUsage, RequirementUsage, etc.)

#### Annotations
- `AnnotatingElement` - Elements that annotate
- `Annotation` - Annotation relationships

### Object Properties

All 86 ownership-related properties are included, organized into these categories:

#### 1. Core Element Ownership (6 properties)
- `Element_owner` / `Element_ownedElement` (inverse pair)
- `Element_ownedRelationship` / `Element_owningRelationship` (inverse pair)
- `Element_owningMembership`
- `Element_owningNamespace`
- `Element_ownedAnnotation`

#### 2. Namespace & Membership (7 properties)
- `Namespace_ownedMember`
- `Namespace_ownedMembership`
- `Namespace_ownedImport`
- `OwningMembership_ownedMemberElement`
- `OwningMembership_ownedMemberElementId`
- `Membership_membershipOwningNamespace`

#### 3. Relationship Ownership (2 properties)
- `Relationship_owningRelatedElement`
- `Relationship_ownedRelatedElement`

#### 4. Type & Feature Ownership (19 properties)
- `Type_ownedFeature`
- `Type_ownedFeatureMembership`
- `Type_ownedConjugator`
- `Type_ownedDifferencing`
- `Type_ownedDisjoining`
- `Type_ownedIntersecting`
- `Type_ownedUnioning`
- `Feature_owningType`
- `Feature_owningFeatureMembership`
- `Feature_ownedTyping`
- `Feature_ownedSubsetting`
- `Feature_ownedRedefinition`
- `Feature_ownedReferenceSubsetting`
- `Feature_ownedFeatureChaining`
- `Feature_ownedFeatureInverting`
- `Feature_ownedTypeFeaturing`
- And more...

#### 5. Definition & Usage (32 properties)
- `Definition_ownedUsage`
- `Definition_ownedAction`
- `Definition_ownedPart`
- `Definition_ownedPort`
- `Definition_ownedAttribute`
- `Definition_ownedConnection`
- `Definition_ownedFlow`
- `Definition_ownedItem`
- `Definition_ownedAllocation`
- `Definition_ownedConstraint`
- `Definition_ownedRequirement`
- `Definition_ownedState`
- `Definition_ownedTransition`
- `Definition_ownedCase`
- `Definition_ownedAnalysisCase`
- `Definition_ownedVerificationCase`
- `Definition_ownedUseCase`
- `Definition_ownedView`
- `Definition_ownedViewpoint`
- `Definition_ownedRendering`
- `Definition_ownedMetadata`
- `Definition_ownedInterface`
- `Definition_ownedCalculation`
- `Definition_ownedOccurrence`
- `Definition_ownedEnumeration`
- `Definition_ownedConcern`
- `Definition_ownedReference`
- `Usage_owningDefinition`
- And inverse properties...

#### 6. Specialized Memberships (11 properties)
- `FeatureMembership_ownedMemberFeature`
- `FeatureMembership_owningType`
- `ParameterMembership_ownedMemberParameter`
- `ActorMembership_ownedActorParameter`
- `StakeholderMembership_ownedStakeholderParameter`
- `SubjectMembership_ownedSubjectParameter`
- `RequirementConstraintMembership_ownedConstraint`
- `ObjectiveMembership_ownedObjectiveRequirement`
- `RequirementVerificationMembership_ownedRequirement`
- `FramedConcernMembership_ownedConcern`
- `ResultExpressionMembership_ownedResultExpression`

#### 7. Annotation Ownership (4 properties)
- `AnnotatingElement_ownedAnnotatingRelationship`
- `Annotation_owningAnnotatedElement`
- `Annotation_owningAnnotatingElement`

#### 8. Other Specializations (5 properties)
- `Classifier_ownedSubclassification`
- `Subclassification_owningClassifier`
- `Conjugation_owningType`
- `Disjoining_owningType`
- `Specialization_owningType`
- `Subsetting_owningFeature`
- `FeatureTyping_owningFeature`
- `FeatureInverting_owningFeature`
- `TypeFeaturing_owningFeatureOfType`
- `ConjugatedPortDefinition_ownedPortConjugator`

## What's Excluded

To keep the ontology lightweight, the following are **NOT included**:

- Data properties (strings, booleans, IDs, etc.) - only object properties
- Non-ownership object properties (e.g., `type`, `feature`, `member`)
- Enumerated datatypes
- Classes not involved in ownership (e.g., Behavior, Class, DataType, Association, etc.)
- Cardinality restrictions and complex OWL axioms
- Documentation and Comment classes

## Use Cases

This light ontology is optimized for:

### 1. **Ownership Hierarchy Queries**
Find all elements owned by a specific element:
```sparql
SELECT ?owned WHERE {
    :MyElement :Element_ownedElement ?owned .
}
```

### 2. **Ownership Path Traversal**
Find the ownership chain from an element to root:
```sparql
SELECT ?owner WHERE {
    :MyElement :Element_owner+ ?owner .
}
```

### 3. **Definition-Usage Queries**
Find all parts owned by a definition:
```sparql
SELECT ?part WHERE {
    :MyPartDefinition :Definition_ownedPart ?part .
}
```

### 4. **Namespace Membership Queries**
Find all members of a namespace:
```sparql
SELECT ?member WHERE {
    :MyPackage :Namespace_ownedMember ?member .
}
```

### 5. **Type Feature Queries**
Find all features owned by a type:
```sparql
SELECT ?feature WHERE {
    :MyType :Type_ownedFeature ?feature .
}
```

### 6. **Requirement Hierarchy**
Find all requirements owned by a requirement definition:
```sparql
SELECT ?req WHERE {
    :MyReqDef :Definition_ownedRequirement ?req .
}
```

### 7. **Specialization Tracking**
Find typing relationships:
```sparql
SELECT ?typing WHERE {
    ?feature :Feature_ownedTyping ?typing .
    ?typing :FeatureTyping_owningFeature ?feature .
}
```

## Property Characteristics

### Functional Properties (47 properties)
Many ownership properties are **functional**, meaning an element can have only one owner:
- `Element_owningMembership` - Each element has at most one owning membership
- `Feature_owningType` - Each feature is owned by at most one type
- `FeatureMembership_ownedMemberFeature` - Each membership owns exactly one feature
- All specialized `ownedMemberX` properties

### Inverse Properties (28 pairs)
Key inverse property pairs for bidirectional navigation:
- `Element_owner` ↔ `Element_ownedElement`
- `Element_owningRelationship` ↔ `Relationship_ownedRelatedElement`
- `Element_owningMembership` ↔ `OwningMembership_ownedMemberElement`
- `Feature_owningType` ↔ `Type_ownedFeature`
- And 24 more pairs...

### Property Hierarchies (60 properties)
Many properties have **subPropertyOf** relationships:
- All specialized `Definition_ownedX` properties are sub-properties of more general ones
- Example: `Definition_ownedPart` → `Definition_ownedOccurrence` → `Definition_ownedUsage`

## Integration with Full Ontology

This light ontology:
- Uses the **same namespaces** as the full SysML ontology (`https://www.omg.org/spec/SysML#`)
- Can be **merged** with the full ontology for complete semantics
- Is **query-compatible** with data validated against the full ontology
- Provides a **performance-optimized subset** for ownership-focused applications

## Generation

The light ontology was automatically generated using `generate_light_ontology.py`:

```bash
python3 generate_light_ontology.py
```

The script:
1. Loads ownership properties extracted from the full ontology
2. Identifies all classes involved in ownership relationships
3. Extracts class definitions (labels, comments, subclass relationships)
4. Generates both Turtle and RDF/XML formats

## Loading the Ontology

### In Python (rdflib)
```python
from rdflib import Graph

g = Graph()
g.parse('sysml2-light-ownership.ttl', format='turtle')

# Query
query = """
PREFIX sysml: <https://www.omg.org/spec/SysML#>
SELECT ?element ?owner WHERE {
    ?element sysml:Element_owner ?owner .
}
"""
results = g.query(query)
```

### In SPARQL Endpoint
```bash
# Load into Apache Jena Fuseki
./fuseki-server --file=sysml2-light-ownership.ttl /sysml
```

### In Protégé
Open `sysml2-light-ownership.owl` in Protégé for visualization and reasoning.

## Performance

Compared to the full ontology:

| Metric | Full Ontology | Light Ontology | Reduction |
|--------|---------------|----------------|-----------|
| File Size (TTL) | ~2.5 MB | 93 KB | **~96%** |
| Classes | 344 | 68 | **~80%** |
| Properties | 696 | 86 | **~88%** |
| Parse Time* | ~2.5s | ~0.3s | **~88%** |
| Query Time* | Variable | Faster | ~50-70% |

*Estimated based on typical RDF triple store performance

## Validation

The light ontology has been validated for:
- ✓ Valid Turtle syntax
- ✓ Valid RDF/XML syntax
- ✓ Consistent namespace usage
- ✓ Complete property domains and ranges
- ✓ Inverse property consistency
- ✓ SubPropertyOf hierarchy validity

## Future Enhancements

Potential additions:
- Add cardinality restrictions for mandatory relationships
- Include key data properties (elementId, name)
- Add transitive closure properties for ownership paths
- Create SHACL shapes for validation
- Add SWRL rules for derived ownership

## References

- **Full SysML2 Ontology**: `sysml2/owl/www.omg.org/spec/SysML.owl`
- **SysML v2 Specification**: https://www.omg.org/spec/SysML/
- **Extracted Properties**: `ownership_props.json`, `OWNERSHIP_PROPERTIES_QUICK_REF.md`

## License

Same as the parent repository (see LICENSE file).

---

**Generated**: 2026-02-24  
**Version**: 1.0  
**Ontology IRI**: `https://www.omg.org/spec/SysML-Light-Ownership`
