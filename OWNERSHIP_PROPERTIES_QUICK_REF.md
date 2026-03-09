# SysML v2 Ownership Properties - Quick Reference

## Summary Statistics
- **Total Properties:** 86
- **'owner' pattern:** 1 property
- **'owned' pattern:** 66 properties
- **'owning' pattern:** 19 properties
- **Functional:** 61 properties
- **Inverse Functional:** 11 properties
- **With inverseOf:** 31 properties

## Core Element Ownership Properties

| Property | Domain | Range | Functional | Inverse Of | Description |
|----------|--------|-------|------------|------------|-------------|
| `Element_owner` | Element | Element | No | Element_ownedElement | The owner of this Element |
| `Element_ownedElement` | Element | Element | No | - | Elements owned by this Element |
| `Element_ownedRelationship` | Element | Relationship | InvFunc | Relationship_owningRelatedElement | Relationships owned by this Element |
| `Element_owningRelationship` | Element | Relationship | No | Relationship_ownedRelatedElement | The Relationship that owns this Element |
| `Element_owningMembership` | OwningMembership | Element | Yes/InvFunc | OwningMembership_ownedMemberElement | The owning Membership |
| `Element_owningNamespace` | Element | Namespace | No | Namespace_ownedMember | The Namespace that owns this Element |

## Namespace & Membership Properties

| Property | Domain | Range | Functional | Inverse Of |
|----------|--------|-------|------------|------------|
| `Namespace_ownedMember` | Namespace | Element | No | - |
| `Namespace_ownedMembership` | Namespace | Membership | Yes/InvFunc | Membership_membershipOwningNamespace |
| `Namespace_ownedImport` | Namespace | Import | Yes/InvFunc | Import_importOwningNamespace |
| `OwningMembership_ownedMemberElement` | OwningMembership | Element | Yes | - |

## Type & Feature Ownership Properties

| Property | Domain | Range | Functional | Inverse Of |
|----------|--------|-------|------------|------------|
| `Type_ownedFeature` | Type | Feature | No | - |
| `Type_ownedFeatureMembership` | Type | FeatureMembership | Yes/InvFunc | FeatureMembership_owningType |
| `Type_ownedSpecialization` | Type | Specialization | Yes/InvFunc | Specialization_owningType |
| `Type_ownedEndFeature` | Type | Feature | No | - |
| `Type_ownedConjugator` | Type | Conjugation | Yes/InvFunc | Conjugation_owningType |
| `Type_ownedDisjoining` | Type | Disjoining | Yes/InvFunc | Disjoining_owningType |
| `Type_ownedDifferencing` | Type | Differencing | Yes/InvFunc | Differencing_typeDifferenced |
| `Type_ownedIntersecting` | Type | Intersecting | Yes/InvFunc | Intersecting_typeIntersected |
| `Type_ownedUnioning` | Type | Unioning | Yes/InvFunc | Unioning_typeUnioned |
| `Feature_owningType` | Feature | Type | No | Type_ownedFeature |
| `Feature_owningFeatureMembership` | Feature | FeatureMembership | Yes/InvFunc | FeatureMembership_ownedMemberFeature |
| `Feature_ownedTyping` | Feature | FeatureTyping | Yes/InvFunc | FeatureTyping_owningFeature |
| `Feature_ownedSubsetting` | Feature | Subsetting | Yes/InvFunc | Subsetting_owningFeature |
| `Feature_ownedRedefinition` | Feature | Redefinition | No | - |
| `Feature_ownedFeatureChaining` | Feature | FeatureChaining | Yes/InvFunc | FeatureChaining_featureChained |
| `Feature_ownedFeatureInverting` | Feature | FeatureInverting | Yes/InvFunc | FeatureInverting_owningFeature |
| `Feature_ownedReferenceSubsetting` | Feature | ReferenceSubsetting | Yes/InvFunc | ReferenceSubsetting_referencingFeature |
| `Feature_ownedTypeFeaturing` | Feature | TypeFeaturing | Yes/InvFunc | TypeFeaturing_owningFeatureOfType |
| `FeatureMembership_owningType` | FeatureMembership | Type | Yes | - |
| `FeatureMembership_ownedMemberFeature` | FeatureMembership | Feature | Yes | - |

## Relationship Ownership Properties

| Property | Domain | Range | Functional |
|----------|--------|-------|------------|
| `Relationship_ownedRelatedElement` | Relationship | Element | No |
| `Relationship_owningRelatedElement` | Relationship | Element | Yes |

## Specialization Hierarchy

| Property | Domain | Range | Functional |
|----------|--------|-------|------------|
| `Specialization_owningType` | Specialization | Type | Yes |
| `Subclassification_owningClassifier` | Subclassification | Classifier | Yes |
| `Subsetting_owningFeature` | Subsetting | Feature | Yes |
| `FeatureTyping_owningFeature` | FeatureTyping | Feature | Yes |

## Definition & Usage Ownership

| Property | Domain | Range | Sub-property Of |
|----------|--------|-------|-----------------|
| `Definition_ownedUsage` | Definition | Usage | Definition_usage, Type_ownedFeature |
| `Definition_ownedAction` | Definition | ActionUsage | Definition_ownedOccurrence |
| `Definition_ownedAttribute` | Definition | AttributeUsage | Definition_ownedUsage |
| `Definition_ownedCalculation` | Definition | CalculationUsage | Definition_ownedAction |
| `Definition_ownedCase` | Definition | CaseUsage | Definition_ownedCalculation |
| `Definition_ownedConnection` | Definition | ConnectorAsUsage | Definition_ownedPart |
| `Definition_ownedConstraint` | Definition | ConstraintUsage | Definition_ownedOccurrence |
| `Definition_ownedItem` | Definition | ItemUsage | Definition_ownedOccurrence |
| `Definition_ownedOccurrence` | Definition | OccurrenceUsage | Definition_ownedUsage |
| `Definition_ownedPart` | Definition | PartUsage | Definition_ownedItem |
| `Definition_ownedPort` | Definition | PortUsage | Definition_ownedUsage |
| `Definition_ownedReference` | Definition | ReferenceUsage | Definition_ownedUsage |
| `Definition_ownedRequirement` | Definition | RequirementUsage | Definition_ownedConstraint |
| `Definition_ownedState` | Definition | StateUsage | Definition_ownedAction |
| `Definition_ownedTransition` | Definition | TransitionUsage | Definition_ownedUsage |
| `Usage_owningDefinition` | Usage | Definition | - |
| `Usage_owningUsage` | Usage | Usage | - |

### Specialized Definition Properties

- `Definition_ownedAllocation` → AllocationUsage
- `Definition_ownedAnalysisCase` → AnalysisCaseUsage  
- `Definition_ownedConcern` → ConcernUsage
- `Definition_ownedEnumeration` → EnumerationUsage
- `Definition_ownedFlow` → FlowConnectionUsage
- `Definition_ownedInterface` → InterfaceUsage
- `Definition_ownedMetadata` → MetadataUsage
- `Definition_ownedRendering` → RenderingUsage
- `Definition_ownedUseCase` → UseCaseUsage
- `Definition_ownedVerificationCase` → VerificationCaseUsage
- `Definition_ownedView` → ViewUsage
- `Definition_ownedViewpoint` → ViewpointUsage

## Specialized Membership Properties

| Property | Domain | Range | Sub-property Of |
|----------|--------|-------|-----------------|
| `ParameterMembership_ownedMemberParameter` | ParameterMembership | Feature | FeatureMembership_ownedMemberFeature |
| `ActorMembership_ownedActorParameter` | ActorMembership | PartUsage | ParameterMembership_ownedMemberParameter |
| `SubjectMembership_ownedSubjectParameter` | SubjectMembership | Usage | ParameterMembership_ownedMemberParameter |
| `StakeholderMembership_ownedStakeholderParameter` | StakeholderMembership | PartUsage | ParameterMembership_ownedMemberParameter |
| `ObjectiveMembership_ownedObjectiveRequirement` | ObjectiveMembership | RequirementUsage | FeatureMembership_ownedMemberFeature |
| `RequirementConstraintMembership_ownedConstraint` | RequirementConstraintMembership | ConstraintUsage | FeatureMembership_ownedMemberFeature |
| `RequirementVerificationMembership_ownedRequirement` | RequirementVerificationMembership | RequirementUsage | RequirementConstraintMembership_ownedConstraint |
| `FramedConcernMembership_ownedConcern` | FramedConcernMembership | ConcernUsage | RequirementConstraintMembership_ownedConstraint |
| `ResultExpressionMembership_ownedResultExpression` | ResultExpressionMembership | Expression | FeatureMembership_ownedMemberFeature |
| `VariantMembership_ownedVariantUsage` | VariantMembership | Usage | OwningMembership_ownedMemberElement |
| `ViewRenderingMembership_ownedRendering` | ViewRenderingMembership | RenderingUsage | FeatureMembership_ownedMemberFeature |

## Annotation Properties

| Property | Domain | Range | Inverse Of |
|----------|--------|-------|------------|
| `Element_ownedAnnotation` | Element | Annotation | Annotation_owningAnnotatedElement |
| `AnnotatingElement_ownedAnnotatingRelationship` | AnnotatingElement | Annotation | Annotation_owningAnnotatingElement |
| `Annotation_owningAnnotatedElement` | Annotation | Element | - |
| `Annotation_owningAnnotatingElement` | Annotation | AnnotatingElement | - |

## Other Specialized Properties

| Property | Domain | Range |
|----------|--------|-------|
| `Classifier_ownedSubclassification` | Classifier | Subclassification |
| `ConjugatedPortDefinition_ownedPortConjugator` | ConjugatedPortDefinition | PortConjugation |
| `Conjugation_owningType` | Conjugation | Type |
| `Disjoining_owningType` | Disjoining | Type |
| `FeatureInverting_owningFeature` | FeatureInverting | Feature |
| `TypeFeaturing_owningFeatureOfType` | TypeFeaturing | Feature |

## Key Inverse Property Pairs

| Property A | Property B |
|------------|------------|
| `Element_owner` ⟷ `Element_ownedElement` |
| `Element_ownedRelationship` ⟷ `Relationship_owningRelatedElement` |
| `Element_owningRelationship` ⟷ `Relationship_ownedRelatedElement` |
| `Element_owningMembership` ⟷ `OwningMembership_ownedMemberElement` |
| `Element_owningNamespace` ⟷ `Namespace_ownedMember` |
| `Type_ownedFeature` ⟷ `Feature_owningType` |
| `Type_ownedFeatureMembership` ⟷ `FeatureMembership_owningType` |
| `Type_ownedSpecialization` ⟷ `Specialization_owningType` |
| `Feature_owningFeatureMembership` ⟷ `FeatureMembership_ownedMemberFeature` |
| `Definition_ownedUsage` ⟷ `Usage_owningDefinition` |
| `Usage_owningUsage` ⟷ `Usage_nestedUsage` |

## Files Available

1. **ownership_props.json** - Complete raw data with all property details
2. **ownership_props.csv** - Spreadsheet format for import/analysis  
3. **ownership_props_summary.json** - Categorized summary data
4. **ownership_props_report.md** - Detailed markdown report
5. **ownership_properties_summary.txt** - Comprehensive text summary
6. **OWNERSHIP_PROPERTIES_QUICK_REF.md** - This quick reference

## Usage for Light Ontology Generation

When generating a light ontology, consider including:

1. **Core ownership properties** (Element_owner, Element_ownedElement, etc.)
2. **Type/Feature hierarchy** (Type_ownedFeature, Feature_owningType)
3. **Namespace membership** (Namespace_ownedMember, etc.)
4. **Key inverse relationships** to maintain bidirectional navigation
5. **Functional/InverseFunctional characteristics** for constraint validation

Properties can be simplified by:
- Removing specialized Definition_owned* properties if only basic structure is needed
- Using just the core ownership properties if specialized memberships aren't required
- Including only top-level properties and omitting deeply nested specializations
