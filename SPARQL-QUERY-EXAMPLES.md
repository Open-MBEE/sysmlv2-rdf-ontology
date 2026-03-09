# SPARQL Query Examples - SysML2 Light Ontology

This document provides practical SPARQL query examples for querying ownership relationships using the SysML2 Light Ontology.

## Setup

```sparql
PREFIX sysml: <https://www.omg.org/spec/SysML#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
```

---

## Basic Ownership Queries

### 1. Find Direct Owner of an Element

```sparql
SELECT ?owner WHERE {
    :MyElement sysml:Element_owner ?owner .
}
```

### 2. Find All Elements Owned by an Element

```sparql
SELECT ?ownedElement WHERE {
    :MyElement sysml:Element_ownedElement ?ownedElement .
}
```

### 3. Find Ownership Chain to Root

```sparql
SELECT ?ancestor WHERE {
    :MyElement sysml:Element_owner+ ?ancestor .
}
ORDER BY DESC(COUNT(?intermediate))
```

### 4. Find All Descendants

```sparql
SELECT ?descendant WHERE {
    :MyElement sysml:Element_ownedElement+ ?descendant .
}
```

### 5. Find Elements with No Owner (Root Elements)

```sparql
SELECT ?rootElement WHERE {
    ?rootElement a sysml:Element .
    FILTER NOT EXISTS { ?rootElement sysml:Element_owner ?owner }
}
```

---

## Namespace & Membership Queries

### 6. Find All Members of a Namespace

```sparql
SELECT ?member WHERE {
    :MyPackage sysml:Namespace_ownedMember ?member .
}
```

### 7. Find Namespace Containing an Element

```sparql
SELECT ?namespace WHERE {
    :MyElement sysml:Element_owningNamespace ?namespace .
}
```

### 8. Find All Memberships in a Namespace

```sparql
SELECT ?membership ?member WHERE {
    :MyNamespace sysml:Namespace_ownedMembership ?membership .
    ?membership sysml:OwningMembership_ownedMemberElement ?member .
}
```

### 9. Find Elements by Membership Type

```sparql
SELECT ?element WHERE {
    ?membership a sysml:FeatureMembership .
    ?membership sysml:OwningMembership_ownedMemberElement ?element .
}
```

---

## Type & Feature Queries

### 10. Find All Features of a Type

```sparql
SELECT ?feature WHERE {
    :MyType sysml:Type_ownedFeature ?feature .
}
```

### 11. Find the Owning Type of a Feature

```sparql
SELECT ?type WHERE {
    :MyFeature sysml:Feature_owningType ?type .
}
```

### 12. Find Feature Membership Relationships

```sparql
SELECT ?feature ?type WHERE {
    ?membership a sysml:FeatureMembership .
    ?membership sysml:FeatureMembership_ownedMemberFeature ?feature .
    ?membership sysml:FeatureMembership_owningType ?type .
}
```

### 13. Find Features with Typing Relationships

```sparql
SELECT ?feature ?typing ?typeRef WHERE {
    ?feature sysml:Feature_ownedTyping ?typing .
    ?typing sysml:FeatureTyping_type ?typeRef .
}
```

---

## Definition & Usage Queries

### 14. Find All Parts Owned by a Definition

```sparql
SELECT ?part WHERE {
    :MyPartDefinition sysml:Definition_ownedPart ?part .
}
```

### 15. Find All Actions in a Behavior

```sparql
SELECT ?action WHERE {
    :MyBehavior sysml:Definition_ownedAction ?action .
}
```

### 16. Find Definition Owning a Usage

```sparql
SELECT ?definition WHERE {
    :MyUsage sysml:Usage_owningDefinition ?definition .
}
```

### 17. Find All Usages by Type

```sparql
SELECT ?usage WHERE {
    ?definition sysml:Definition_ownedUsage ?usage .
    ?usage a sysml:PartUsage .
}
```

### 18. Find Requirements in a Requirement Definition

```sparql
SELECT ?req WHERE {
    :MyReqDef sysml:Definition_ownedRequirement ?req .
}
```

### 19. Find Ports Owned by a Part

```sparql
SELECT ?port WHERE {
    :MyPartDef sysml:Definition_ownedPort ?port .
}
```

### 20. Find Connections Between Parts

```sparql
SELECT ?connection WHERE {
    :MySystemDef sysml:Definition_ownedConnection ?connection .
}
```

---

## Specialization Queries

### 21. Find Subsetting Relationships

```sparql
SELECT ?subsetting ?subsettedFeature WHERE {
    ?feature sysml:Feature_ownedSubsetting ?subsetting .
    ?subsetting sysml:Subsetting_subsettedFeature ?subsettedFeature .
}
```

### 22. Find Redefinition Relationships

```sparql
SELECT ?redefining ?redefined WHERE {
    ?redefining sysml:Feature_ownedRedefinition ?redefinition .
    ?redefinition sysml:Redefinition_redefinedFeature ?redefined .
}
```

### 23. Find Subclassifications

```sparql
SELECT ?subclass ?superclass WHERE {
    ?subclass sysml:Classifier_ownedSubclassification ?subclassification .
    ?subclassification sysml:Subclassification_superclassifier ?superclass .
}
```

### 24. Find All Specializations of a Type

```sparql
SELECT ?specific ?general WHERE {
    ?specific sysml:Type_ownedSpecialization ?specialization .
    ?specialization sysml:Specialization_general ?general .
}
```

---

## Annotation Queries

### 25. Find All Annotations on an Element

```sparql
SELECT ?annotation WHERE {
    :MyElement sysml:Element_ownedAnnotation ?annotation .
}
```

### 26. Find Annotated Elements

```sparql
SELECT ?annotated WHERE {
    ?annotation sysml:Annotation_annotatedElement ?annotated .
}
```

### 27. Find Comments on Elements

```sparql
SELECT ?comment ?body WHERE {
    :MyElement sysml:Element_ownedAnnotation ?annotation .
    ?annotation a sysml:Comment .
    ?annotation sysml:Comment_body ?body .
}
```

---

## Complex Queries

### 28. Find All Ownership Relationships (Generic)

```sparql
SELECT ?subject ?property ?object WHERE {
    ?subject ?property ?object .
    ?property rdfs:subPropertyOf* sysml:Element_ownedElement .
}
```

### 29. Count Elements by Type

```sparql
SELECT ?type (COUNT(?element) AS ?count) WHERE {
    ?element a ?type .
    FILTER(STRSTARTS(STR(?type), "https://www.omg.org/spec/SysML#"))
}
GROUP BY ?type
ORDER BY DESC(?count)
```

### 30. Find Ownership Depth of an Element

```sparql
SELECT (COUNT(?owner) AS ?depth) WHERE {
    :MyElement sysml:Element_owner+ ?owner .
}
```

### 31. Find Sibling Elements (Same Owner)

```sparql
SELECT ?sibling WHERE {
    :MyElement sysml:Element_owner ?parent .
    ?parent sysml:Element_ownedElement ?sibling .
    FILTER(?sibling != :MyElement)
}
```

### 32. Find All Parameter Memberships

```sparql
SELECT ?membership ?parameter ?namespace WHERE {
    ?membership a sysml:ParameterMembership .
    ?membership sysml:ParameterMembership_ownedMemberParameter ?parameter .
    ?membership sysml:Membership_membershipOwningNamespace ?namespace .
}
```

### 33. Find Actor Parameters in Requirements

```sparql
SELECT ?requirement ?actor WHERE {
    ?requirement a sysml:RequirementUsage .
    ?membership a sysml:ActorMembership .
    ?membership sysml:ActorMembership_ownedActorParameter ?actor .
    ?membership sysml:FeatureMembership_owningType ?requirement .
}
```

### 34. Find Constraint Hierarchies

```sparql
SELECT ?parent ?child WHERE {
    ?parent sysml:Definition_ownedConstraint ?child .
    ?child a sysml:ConstraintUsage .
}
```

### 35. Find State Hierarchies

```sparql
SELECT ?parentState ?childState WHERE {
    ?parentState sysml:Definition_ownedState ?childState .
    ?childState a sysml:StateUsage .
}
```

### 36. Find Transitions Between States

```sparql
SELECT ?state ?transition WHERE {
    ?state sysml:Definition_ownedTransition ?transition .
    ?transition a sysml:TransitionUsage .
}
```

---

## Aggregation & Statistics Queries

### 37. Count Direct Children of Elements

```sparql
SELECT ?element (COUNT(?child) AS ?childCount) WHERE {
    ?element sysml:Element_ownedElement ?child .
}
GROUP BY ?element
ORDER BY DESC(?childCount)
```

### 38. Find Elements with Most Features

```sparql
SELECT ?type (COUNT(?feature) AS ?featureCount) WHERE {
    ?type sysml:Type_ownedFeature ?feature .
}
GROUP BY ?type
ORDER BY DESC(?featureCount)
```

### 39. Find Deepest Ownership Hierarchies

```sparql
SELECT ?root (MAX(?depth) AS ?maxDepth) WHERE {
    ?root sysml:Element_ownedElement+ ?descendant .
    {
        SELECT ?descendant (COUNT(?intermediate) AS ?depth) WHERE {
            ?root sysml:Element_ownedElement+ ?intermediate .
            ?intermediate sysml:Element_ownedElement* ?descendant .
        }
        GROUP BY ?descendant
    }
}
GROUP BY ?root
ORDER BY DESC(?maxDepth)
```

### 40. List All Property Types Used

```sparql
SELECT DISTINCT ?property WHERE {
    ?subject ?property ?object .
    ?property rdfs:subPropertyOf* sysml:Element_ownedElement .
}
ORDER BY ?property
```

---

## Property Path Queries

### 41. Find Elements Related Through Any Ownership Property

```sparql
SELECT ?element1 ?element2 WHERE {
    ?element1 (sysml:Element_ownedElement|
               sysml:Type_ownedFeature|
               sysml:Namespace_ownedMember) ?element2 .
}
```

### 42. Find Full Ownership Path

```sparql
SELECT ?path WHERE {
    :LeafElement sysml:Element_owner* ?path .
}
ORDER BY DESC(?path)
```

### 43. Find Alternative Ownership Paths

```sparql
SELECT ?element ?path WHERE {
    :RootElement (sysml:Element_ownedElement|
                  sysml:Namespace_ownedMember)+ ?path .
}
```

---

## Validation Queries

### 44. Find Elements with Multiple Owners (Invalid)

```sparql
SELECT ?element (COUNT(?owner) AS ?ownerCount) WHERE {
    ?element sysml:Element_owner ?owner .
}
GROUP BY ?element
HAVING (COUNT(?owner) > 1)
```

### 45. Find Orphaned Relationships

```sparql
SELECT ?relationship WHERE {
    ?relationship a sysml:Relationship .
    FILTER NOT EXISTS { ?relationship sysml:Relationship_owningRelatedElement ?owner }
}
```

### 46. Find Memberships Without Members

```sparql
SELECT ?membership WHERE {
    ?membership a sysml:OwningMembership .
    FILTER NOT EXISTS { 
        ?membership sysml:OwningMembership_ownedMemberElement ?member 
    }
}
```

### 47. Verify Inverse Properties

```sparql
SELECT ?element ?owner WHERE {
    ?element sysml:Element_owner ?owner .
    FILTER NOT EXISTS { ?owner sysml:Element_ownedElement ?element }
}
```

---

## Graph Traversal Queries

### 48. Breadth-First Traversal

```sparql
SELECT ?element ?level WHERE {
    {
        SELECT :RootElement AS ?element (0 AS ?level)
    } UNION {
        :RootElement sysml:Element_ownedElement ?element .
        BIND(1 AS ?level)
    } UNION {
        :RootElement sysml:Element_ownedElement/sysml:Element_ownedElement ?element .
        BIND(2 AS ?level)
    }
}
ORDER BY ?level
```

### 49. Find Leaf Nodes (No Children)

```sparql
SELECT ?leaf WHERE {
    ?leaf a sysml:Element .
    FILTER NOT EXISTS { ?leaf sysml:Element_ownedElement ?child }
}
```

### 50. Find Common Ancestor

```sparql
SELECT ?ancestor WHERE {
    :Element1 sysml:Element_owner+ ?ancestor .
    :Element2 sysml:Element_owner+ ?ancestor .
}
LIMIT 1
```

---

## Tips for Query Performance

1. **Use Property Paths Wisely**: `+` and `*` can be expensive
2. **Filter Early**: Apply filters as early as possible
3. **Limit Results**: Use LIMIT when exploring data
4. **Index on IDs**: Ensure elementId properties are indexed
5. **Use DESCRIBE**: For exploratory queries: `DESCRIBE :MyElement`

## Example: Complete Query Session

```sparql
# 1. Find a part definition
SELECT ?partDef WHERE {
    ?partDef a sysml:PartDefinition .
} LIMIT 1

# 2. Find all its owned parts
SELECT ?part WHERE {
    <found_part_def_uri> sysml:Definition_ownedPart ?part .
}

# 3. Find features of each part
SELECT ?part ?feature WHERE {
    <found_part_def_uri> sysml:Definition_ownedPart ?part .
    ?part sysml:Type_ownedFeature ?feature .
}

# 4. Find ports on the definition
SELECT ?port WHERE {
    <found_part_def_uri> sysml:Definition_ownedPort ?port .
}

# 5. Find connections
SELECT ?connection WHERE {
    <found_part_def_uri> sysml:Definition_ownedConnection ?connection .
}
```

---

**For more information**, see `LIGHT-ONTOLOGY-README.md`
