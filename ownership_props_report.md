# Ownership-Related Object Properties from SysML.owl

**Total Properties Found:** 86

---

## Summary by Pattern

- **owner** pattern (e.g., Element_owner): 1 properties
- **owned** pattern (e.g., Element_ownedElement): 66 properties
- **owning** pattern (e.g., Element_owningRelationship): 19 properties

---

## ActorMembership_ownedActorParameter

**URI:** `https://www.omg.org/spec/SysML#ActorMembership_ownedActorParameter`

**Label:** ownedActorParameter

**Domain:** ActorMembership

**Range:** PartUsage

**Characteristics:** Functional

**Sub-property Of:**
- ParameterMembership_ownedMemberParameter

**Comment:** The `PartUsage` specifying the actor.

---

## AnnotatingElement_ownedAnnotatingRelationship

**URI:** `https://www.omg.org/spec/SysML#AnnotatingElement_ownedAnnotatingRelationship`

**Label:** ownedAnnotatingRelationship

**Domain:** AnnotatingElement

**Range:** Annotation

**Characteristics:** Functional

**Inverse Of:** Annotation_owningAnnotatingElement

**Comment:** The `ownedRelationships` of this `AnnotatingElement` that are `Annotations`, for which this `AnnotatingElement` is the `annotatingElement`.

---

## Annotation_owningAnnotatedElement

**URI:** `https://www.omg.org/spec/SysML#Annotation_owningAnnotatedElement`

**Label:** owningAnnotatedElement

**Domain:** Annotation

**Range:** Element

**Characteristics:** Functional

**Sub-property Of:**
- Annotation_annotatedElement
- Relationship_owningRelatedElement

**Comment:** The `annotatedElement` of this `Annotation`, when it is also its `owningRelatedElement`.

---

## Annotation_owningAnnotatingElement

**URI:** `https://www.omg.org/spec/SysML#Annotation_owningAnnotatingElement`

**Label:** owningAnnotatingElement

**Domain:** Annotation

**Range:** AnnotatingElement

**Characteristics:** Functional

**Sub-property Of:**
- Annotation_annotatingElement
- Relationship_owningRelatedElement

**Comment:** The `annotatingElement` of this `Annotation`, when it is also its `owningRelatedElement`.

---

## Classifier_ownedSubclassification

**URI:** `https://www.omg.org/spec/SysML#Classifier_ownedSubclassification`

**Label:** ownedSubclassification

**Domain:** Classifier

**Range:** Subclassification

**Characteristics:** Functional

**Inverse Of:** Subclassification_owningClassifier

**Comment:** The `ownedSpecializations` of this `Classifier` that are `Subclassifications`, for which this `Classifier` is the `subclassifier`.

---

## ConjugatedPortDefinition_ownedPortConjugator

**URI:** `https://www.omg.org/spec/SysML#ConjugatedPortDefinition_ownedPortConjugator`

**Label:** ownedPortConjugator

**Domain:** ConjugatedPortDefinition

**Range:** PortConjugation

**Characteristics:** Functional

**Inverse Of:** PortConjugation_conjugatedPortDefinition

**Comment:** The `PortConjugation` that is the `ownedConjugator` of this `ConjugatedPortDefinition`, linking it to its `originalPortDefinition`.

---

## Conjugation_owningType

**URI:** `https://www.omg.org/spec/SysML#Conjugation_owningType`

**Label:** owningType

**Domain:** Conjugation

**Range:** Type

**Characteristics:** Functional

**Sub-property Of:**
- Conjugation_conjugatedType
- Relationship_owningRelatedElement

**Comment:** The `conjugatedType` of this `Conjugation` that is also its `owningRelatedElement`.

---

## Definition_ownedAction

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedAction`

**Label:** ownedAction

**Domain:** Definition

**Range:** ActionUsage

**Sub-property Of:**
- Definition_ownedOccurrence

**Comment:** The `ActionUsages` that are `ownedUsages` of this `Definition`.

---

## Definition_ownedAllocation

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedAllocation`

**Label:** ownedAllocation

**Domain:** Definition

**Range:** AllocationUsage

**Sub-property Of:**
- Definition_ownedConnection

**Comment:** The `AllocationUsages` that are `ownedUsages` of this `Definition`.

---

## Definition_ownedAnalysisCase

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedAnalysisCase`

**Label:** ownedAnalysisCase

**Domain:** Definition

**Range:** AnalysisCaseUsage

**Sub-property Of:**
- Definition_ownedCase

**Comment:** The `AnalysisCaseUsages` that are `ownedUsages` of this `Definition`.

---

## Definition_ownedAttribute

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedAttribute`

**Label:** ownedAttribute

**Domain:** Definition

**Range:** AttributeUsage

**Sub-property Of:**
- Definition_ownedUsage

**Comment:** The `AttributeUsages` that are `ownedUsages` of this `Definition`.

---

## Definition_ownedCalculation

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedCalculation`

**Label:** ownedCalculation

**Domain:** Definition

**Range:** CalculationUsage

**Sub-property Of:**
- Definition_ownedAction

**Comment:** The `CalculationUsages` that are `ownedUsages` of this `Definition`.

---

## Definition_ownedCase

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedCase`

**Label:** ownedCase

**Domain:** Definition

**Range:** CaseUsage

**Sub-property Of:**
- Definition_ownedCalculation

**Comment:** The code>CaseUsages` that are `ownedUsages` of this `Definition`.

---

## Definition_ownedConcern

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedConcern`

**Label:** ownedConcern

**Domain:** Definition

**Range:** ConcernUsage

**Sub-property Of:**
- Definition_ownedRequirement

**Comment:** The `ConcernUsages` that are `ownedUsages` of this `Definition`.

---

## Definition_ownedConnection

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedConnection`

**Label:** ownedConnection

**Domain:** Definition

**Range:** ConnectorAsUsage

**Sub-property Of:**
- Definition_ownedPart

**Comment:** The `ConnectorAsUsages` that are `ownedUsages` of this `Definition`. Note that this list includes `BindingConnectorAsUsages` and `SuccessionAsUsages`, even though these are `ConnectorAsUsages` but not `ConnectionUsages`.

---

## Definition_ownedConstraint

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedConstraint`

**Label:** ownedConstraint

**Domain:** Definition

**Range:** ConstraintUsage

**Sub-property Of:**
- Definition_ownedOccurrence

**Comment:** The `ConstraintUsages` that are `ownedUsages` of this `Definition`.

---

## Definition_ownedEnumeration

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedEnumeration`

**Label:** ownedEnumeration

**Domain:** Definition

**Range:** EnumerationUsage

**Sub-property Of:**
- Definition_ownedAttribute

**Comment:** The `EnumerationUsages` that are `ownedUsages` of this `Definition`.

---

## Definition_ownedFlow

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedFlow`

**Label:** ownedFlow

**Domain:** Definition

**Range:** FlowConnectionUsage

**Sub-property Of:**
- Definition_ownedConnection

**Comment:** The `FlowConnectionUsages` that are `ownedUsages` of this `Definition`.

---

## Definition_ownedInterface

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedInterface`

**Label:** ownedInterface

**Domain:** Definition

**Range:** InterfaceUsage

**Sub-property Of:**
- Definition_ownedConnection

**Comment:** The `InterfaceUsages` that are `ownedUsages` of this `Definition`.

---

## Definition_ownedItem

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedItem`

**Label:** ownedItem

**Domain:** Definition

**Range:** ItemUsage

**Sub-property Of:**
- Definition_ownedOccurrence

**Comment:** The `ItemUsages` that are `ownedUsages` of this `Definition`.

---

## Definition_ownedMetadata

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedMetadata`

**Label:** ownedMetadata

**Domain:** Definition

**Range:** MetadataUsage

**Sub-property Of:**
- Definition_ownedItem

**Comment:** The `MetadataUsages` that are `ownedUsages` of this `Definition`.

---

## Definition_ownedOccurrence

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedOccurrence`

**Label:** ownedOccurrence

**Domain:** Definition

**Range:** OccurrenceUsage

**Sub-property Of:**
- Definition_ownedUsage

**Comment:** The `OccurrenceUsages` that are `ownedUsages` of this `Definition`.

---

## Definition_ownedPart

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedPart`

**Label:** ownedPart

**Domain:** Definition

**Range:** PartUsage

**Sub-property Of:**
- Definition_ownedItem

**Comment:** The `PartUsages` that are `ownedUsages` of this `Definition`.

---

## Definition_ownedPort

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedPort`

**Label:** ownedPort

**Domain:** Definition

**Range:** PortUsage

**Sub-property Of:**
- Definition_ownedUsage

**Comment:** The `PortUsages` that are `ownedUsages` of this `Definition`.

---

## Definition_ownedReference

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedReference`

**Label:** ownedReference

**Domain:** Definition

**Range:** ReferenceUsage

**Sub-property Of:**
- Definition_ownedUsage

**Comment:** The `ReferenceUsages` that are `ownedUsages` of this `Definition`.

---

## Definition_ownedRendering

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedRendering`

**Label:** ownedRendering

**Domain:** Definition

**Range:** RenderingUsage

**Sub-property Of:**
- Definition_ownedPart

**Comment:** The `RenderingUsages` that are `ownedUsages` of this `Definition`.

---

## Definition_ownedRequirement

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedRequirement`

**Label:** ownedRequirement

**Domain:** Definition

**Range:** RequirementUsage

**Sub-property Of:**
- Definition_ownedConstraint

**Comment:** The `RequirementUsages` that are `ownedUsages` of this `Definition`.

---

## Definition_ownedState

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedState`

**Label:** ownedState

**Domain:** Definition

**Range:** StateUsage

**Sub-property Of:**
- Definition_ownedAction

**Comment:** The `StateUsages` that are `ownedUsages` of this `Definition`.

---

## Definition_ownedTransition

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedTransition`

**Label:** ownedTransition

**Domain:** Definition

**Range:** TransitionUsage

**Sub-property Of:**
- Definition_ownedUsage

**Comment:** The `TransitionUsages` that are `ownedUsages` of this `Definition`.

---

## Definition_ownedUsage

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedUsage`

**Label:** ownedUsage

**Domain:** Definition

**Range:** Usage

**Sub-property Of:**
- Definition_usage
- Type_ownedFeature

**Comment:** The `Usages` that are `ownedFeatures` of this `Definition`.

---

## Definition_ownedUseCase

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedUseCase`

**Label:** ownedUseCase

**Domain:** Definition

**Range:** UseCaseUsage

**Sub-property Of:**
- Definition_ownedCase

**Comment:** The `UseCaseUsages` that are `ownedUsages` of this `Definition`.

---

## Definition_ownedVerificationCase

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedVerificationCase`

**Label:** ownedVerificationCase

**Domain:** Definition

**Range:** VerificationCaseUsage

**Sub-property Of:**
- Definition_ownedCase

**Comment:** The `VerificationCaseUsages` that are `ownedUsages` of this `Definition`.

---

## Definition_ownedView

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedView`

**Label:** ownedView

**Domain:** Definition

**Range:** ViewUsage

**Sub-property Of:**
- Definition_ownedPart

**Comment:** The `ViewUsages` that are `ownedUsages` of this `Definition`.

---

## Definition_ownedViewpoint

**URI:** `https://www.omg.org/spec/SysML#Definition_ownedViewpoint`

**Label:** ownedViewpoint

**Domain:** Definition

**Range:** ViewpointUsage

**Sub-property Of:**
- Definition_ownedRequirement

**Comment:** The `ViewpointUsages` that are `ownedUsages` of this `Definition`.

---

## Disjoining_owningType

**URI:** `https://www.omg.org/spec/SysML#Disjoining_owningType`

**Label:** owningType

**Domain:** Disjoining

**Range:** Type

**Characteristics:** Functional

**Sub-property Of:**
- Disjoining_typeDisjoined
- Relationship_owningRelatedElement

**Comment:** A `typeDisjoined` that is also an `owningRelatedElement`.

---

## Element_ownedAnnotation

**URI:** `https://www.omg.org/spec/SysML#Element_ownedAnnotation`

**Label:** ownedAnnotation

**Domain:** Element

**Range:** Annotation

**Characteristics:** Functional

**Inverse Of:** Annotation_owningAnnotatedElement

**Comment:** The `ownedRelationships` of this `Element` that are `Annotations`, for which this `Element` is the `annotatedElement`.`

---

## Element_ownedElement

**URI:** `https://www.omg.org/spec/SysML#Element_ownedElement`

**Label:** ownedElement

**Domain:** Element

**Range:** Element

**Comment:** The Elements owned by this Element, derived as the `ownedRelatedElements` of the `ownedRelationships` of this Element.

---

## Element_ownedRelationship

**URI:** `https://www.omg.org/spec/SysML#Element_ownedRelationship`

**Label:** ownedRelationship

**Domain:** Element

**Range:** Relationship

**Characteristics:** Functional

**Inverse Of:** Relationship_owningRelatedElement

**Comment:** The Relationships for which this Element is the `owningRelatedElement`.

---

## Element_owner

**URI:** `https://www.omg.org/spec/SysML#Element_owner`

**Label:** owner

**Domain:** Element

**Range:** Element

**Inverse Of:** Element_ownedElement

**Comment:** The owner of this Element, derived as the `owningRelatedElement` of the `owningRelationship` of this Element, if any.

---

## Element_owningMembership

**URI:** `https://www.omg.org/spec/SysML#Element_owningMembership`

**Label:** owningMembership

**Domain:** Element

**Range:** OwningMembership

**Characteristics:** Functional

**Inverse Of:** OwningMembership_ownedMemberElement

**Comment:** The `owningRelationship` of this `Element`, if that `Relationship` is a `Membership`.

---

## Element_owningNamespace

**URI:** `https://www.omg.org/spec/SysML#Element_owningNamespace`

**Label:** owningNamespace

**Domain:** Element

**Range:** Namespace

**Inverse Of:** Namespace_ownedMember

**Comment:** The `Namespace` that owns this `Element`, which is the `membershipOwningNamespace` of the `owningMembership` of this `Element`, if any.

---

## Element_owningRelationship

**URI:** `https://www.omg.org/spec/SysML#Element_owningRelationship`

**Label:** owningRelationship

**Domain:** Element

**Range:** Relationship

**Inverse Of:** Relationship_ownedRelatedElement

**Comment:** The Relationship for which this Element is an `ownedRelatedElement`, if any.

---

## FeatureInverting_owningFeature

**URI:** `https://www.omg.org/spec/SysML#FeatureInverting_owningFeature`

**Label:** owningFeature

**Domain:** FeatureInverting

**Range:** Feature

**Characteristics:** Functional

**Sub-property Of:**
- FeatureInverting_featureInverted
- Relationship_owningRelatedElement

**Comment:** A `featureInverted` that is also the `owningRelatedElement` of this `FeatureInverting`.

---

## FeatureMembership_ownedMemberFeature

**URI:** `https://www.omg.org/spec/SysML#FeatureMembership_ownedMemberFeature`

**Label:** ownedMemberFeature

**Domain:** FeatureMembership

**Range:** Feature

**Characteristics:** Functional

**Sub-property Of:**
- Featuring_feature
- OwningMembership_ownedMemberElement

**Comment:** The `Feature` that this `FeatureMembership` relates to its `owningType`, making it an `ownedFeature` of the `owningType`.

---

## FeatureMembership_owningType

**URI:** `https://www.omg.org/spec/SysML#FeatureMembership_owningType`

**Label:** owningType

**Domain:** FeatureMembership

**Range:** Type

**Characteristics:** Functional

**Sub-property Of:**
- Featuring_type
- Membership_membershipOwningNamespace

**Comment:** The `Type` that owns this `FeatureMembership`.

---

## FeatureTyping_owningFeature

**URI:** `https://www.omg.org/spec/SysML#FeatureTyping_owningFeature`

**Label:** owningFeature

**Domain:** FeatureTyping

**Range:** Feature

**Characteristics:** Functional

**Sub-property Of:**
- FeatureTyping_typedFeature
- Specialization_owningType

**Comment:** A `typedFeature` that is also the `owningRelatedElement` of this `FeatureTyping`.

---

## Feature_ownedFeatureChaining

**URI:** `https://www.omg.org/spec/SysML#Feature_ownedFeatureChaining`

**Label:** ownedFeatureChaining

**Domain:** Feature

**Range:** FeatureChaining

**Characteristics:** Functional

**Inverse Of:** FeatureChaining_featureChained

**Comment:** The `ownedRelationships` of this `Feature` that are `FeatureChainings`, for which the `Feature` will be the `featureChained`.

---

## Feature_ownedFeatureInverting

**URI:** `https://www.omg.org/spec/SysML#Feature_ownedFeatureInverting`

**Label:** ownedFeatureInverting

**Domain:** Feature

**Range:** FeatureInverting

**Characteristics:** Functional

**Inverse Of:** FeatureInverting_owningFeature

**Comment:** The `ownedRelationships` of this `Feature` that are `FeatureInvertings` and for which the `Feature` is the `featureInverted`.

---

## Feature_ownedRedefinition

**URI:** `https://www.omg.org/spec/SysML#Feature_ownedRedefinition`

**Label:** ownedRedefinition

**Domain:** Feature

**Range:** Redefinition

**Sub-property Of:**
- Feature_ownedSubsetting

**Comment:** The `ownedSubsettings` of this `Feature` that are `Redefinitions`, for which the `Feature` is the `redefiningFeature`.

---

## Feature_ownedReferenceSubsetting

**URI:** `https://www.omg.org/spec/SysML#Feature_ownedReferenceSubsetting`

**Label:** ownedReferenceSubsetting

**Domain:** Feature

**Range:** ReferenceSubsetting

**Characteristics:** Functional

**Inverse Of:** ReferenceSubsetting_referencingFeature

**Comment:** The one `ownedSubsetting` of this `Feature`, if any, that is a `ReferenceSubsetting`, for which the `Feature` is the `referencingFeature`.

---

## Feature_ownedSubsetting

**URI:** `https://www.omg.org/spec/SysML#Feature_ownedSubsetting`

**Label:** ownedSubsetting

**Domain:** Feature

**Range:** Subsetting

**Characteristics:** Functional

**Inverse Of:** Subsetting_owningFeature

**Comment:** The `ownedSpecializations` of this `Feature` that are `Subsettings`, for which the `Feature` is the `subsettingFeature`.

---

## Feature_ownedTypeFeaturing

**URI:** `https://www.omg.org/spec/SysML#Feature_ownedTypeFeaturing`

**Label:** ownedTypeFeaturing

**Domain:** Feature

**Range:** TypeFeaturing

**Characteristics:** Functional

**Inverse Of:** TypeFeaturing_owningFeatureOfType

**Comment:** The `ownedRelationships` of this `Feature` that are `TypeFeaturings` and for which the `Feature` is the `featureOfType`.

---

## Feature_ownedTyping

**URI:** `https://www.omg.org/spec/SysML#Feature_ownedTyping`

**Label:** ownedTyping

**Domain:** Feature

**Range:** FeatureTyping

**Characteristics:** Functional

**Inverse Of:** FeatureTyping_owningFeature

**Comment:** The `ownedSpecializations` of this `Feature` that are `FeatureTypings`, for which the `Feature` is the `typedFeature`.

---

## Feature_owningFeatureMembership

**URI:** `https://www.omg.org/spec/SysML#Feature_owningFeatureMembership`

**Label:** owningFeatureMembership

**Domain:** Feature

**Range:** FeatureMembership

**Characteristics:** Functional

**Inverse Of:** FeatureMembership_ownedMemberFeature

**Comment:** The `FeatureMembership` that owns this `Feature` as an `ownedMemberFeature`, determining its `owningType`.

---

## Feature_owningType

**URI:** `https://www.omg.org/spec/SysML#Feature_owningType`

**Label:** owningType

**Domain:** Feature

**Range:** Type

**Inverse Of:** Type_ownedFeature

**Sub-property Of:**
- Feature_featuringType

**Comment:** The `Type` that is the `owningType` of the `owningFeatureMembership` of this `Feature`.

---

## FramedConcernMembership_ownedConcern

**URI:** `https://www.omg.org/spec/SysML#FramedConcernMembership_ownedConcern`

**Label:** ownedConcern

**Domain:** FramedConcernMembership

**Range:** ConcernUsage

**Characteristics:** Functional

**Sub-property Of:**
- RequirementConstraintMembership_ownedConstraint

**Comment:** The `ConcernUsage` that is the `ownedConstraint` of this `FramedConcernMembership`.

---

## Namespace_ownedImport

**URI:** `https://www.omg.org/spec/SysML#Namespace_ownedImport`

**Label:** ownedImport

**Domain:** Namespace

**Range:** Import

**Characteristics:** Functional

**Inverse Of:** Import_importOwningNamespace

**Comment:** The `ownedRelationships` of this `Namespace` that are `Imports`, for which the `Namespace` is the `importOwningNamespace`.

---

## Namespace_ownedMember

**URI:** `https://www.omg.org/spec/SysML#Namespace_ownedMember`

**Label:** ownedMember

**Domain:** Namespace

**Range:** Element

**Sub-property Of:**
- Namespace_member

**Comment:** The owned `members` of this `Namespace`, which are the <cpde>`ownedMemberElements` of the `ownedMemberships` of the `Namespace`.

---

## Namespace_ownedMembership

**URI:** `https://www.omg.org/spec/SysML#Namespace_ownedMembership`

**Label:** ownedMembership

**Domain:** Namespace

**Range:** Membership

**Characteristics:** Functional

**Inverse Of:** Membership_membershipOwningNamespace

**Sub-property Of:**
- Namespace_membership

**Comment:** The `ownedRelationships` of this `Namespace` that are `Memberships`, for which the `Namespace` is the `membershipOwningNamespace`.

---

## ObjectiveMembership_ownedObjectiveRequirement

**URI:** `https://www.omg.org/spec/SysML#ObjectiveMembership_ownedObjectiveRequirement`

**Label:** ownedObjectiveRequirement

**Domain:** ObjectiveMembership

**Range:** RequirementUsage

**Characteristics:** Functional

**Sub-property Of:**
- FeatureMembership_ownedMemberFeature

**Comment:** The RequirementUsage that is the `ownedMemberFeature` of this RequirementUsage.

---

## OwningMembership_ownedMemberElement

**URI:** `https://www.omg.org/spec/SysML#OwningMembership_ownedMemberElement`

**Label:** ownedMemberElement

**Domain:** OwningMembership

**Range:** Element

**Characteristics:** Functional

**Sub-property Of:**
- Membership_memberElement
- Relationship_ownedRelatedElement

**Comment:** The `Element` that becomes an `ownedMember` of the `membershipOwningNamespace` due to this `OwningMembership`.

---

## ParameterMembership_ownedMemberParameter

**URI:** `https://www.omg.org/spec/SysML#ParameterMembership_ownedMemberParameter`

**Label:** ownedMemberParameter

**Domain:** ParameterMembership

**Range:** Feature

**Characteristics:** Functional

**Sub-property Of:**
- FeatureMembership_ownedMemberFeature

**Comment:** The `Feature` that is identified as a `parameter` by this `ParameterMembership`.

---

## Relationship_ownedRelatedElement

**URI:** `https://www.omg.org/spec/SysML#Relationship_ownedRelatedElement`

**Label:** ownedRelatedElement

**Domain:** Relationship

**Range:** Element

**Sub-property Of:**
- Relationship_relatedElement

**Comment:** The `relatedElements` of this Relationship that are owned by the Relationship.

---

## Relationship_owningRelatedElement

**URI:** `https://www.omg.org/spec/SysML#Relationship_owningRelatedElement`

**Label:** owningRelatedElement

**Domain:** Relationship

**Range:** Element

**Characteristics:** Functional

**Sub-property Of:**
- Relationship_relatedElement

**Comment:** The `relatedElement` of this Relationship that owns the Relationship, if any.

---

## RequirementConstraintMembership_ownedConstraint

**URI:** `https://www.omg.org/spec/SysML#RequirementConstraintMembership_ownedConstraint`

**Label:** ownedConstraint

**Domain:** RequirementConstraintMembership

**Range:** ConstraintUsage

**Characteristics:** Functional

**Sub-property Of:**
- FeatureMembership_ownedMemberFeature

**Comment:** The `ConstraintUsage` that is the `ownedMemberFeature` of this `RequirementConstraintMembership`.

---

## RequirementVerificationMembership_ownedRequirement

**URI:** `https://www.omg.org/spec/SysML#RequirementVerificationMembership_ownedRequirement`

**Label:** ownedRequirement

**Domain:** RequirementVerificationMembership

**Range:** RequirementUsage

**Characteristics:** Functional

**Sub-property Of:**
- RequirementConstraintMembership_ownedConstraint

**Comment:** The owned `RequirementUsage` that acts as the `ownedConstraint` for this `RequirementVerificationMembership`. This will either be the `verifiedRequirement`, or it will subset the `verifiedRequirement`.

---

## ResultExpressionMembership_ownedResultExpression

**URI:** `https://www.omg.org/spec/SysML#ResultExpressionMembership_ownedResultExpression`

**Label:** ownedResultExpression

**Domain:** ResultExpressionMembership

**Range:** Expression

**Characteristics:** Functional

**Sub-property Of:**
- FeatureMembership_ownedMemberFeature

**Comment:** The `Expression` that provides the result for the owner of the `ResultExpressionMembership`.

---

## Specialization_owningType

**URI:** `https://www.omg.org/spec/SysML#Specialization_owningType`

**Label:** owningType

**Domain:** Specialization

**Range:** Type

**Characteristics:** Functional

**Sub-property Of:**
- Relationship_owningRelatedElement
- Specialization_specific

**Comment:** The `Type` that is the `specific` `Type` of this `Specialization` and owns it as its `owningRelatedElement`.

---

## StakeholderMembership_ownedStakeholderParameter

**URI:** `https://www.omg.org/spec/SysML#StakeholderMembership_ownedStakeholderParameter`

**Label:** ownedStakeholderParameter

**Domain:** StakeholderMembership

**Range:** PartUsage

**Characteristics:** Functional

**Sub-property Of:**
- ParameterMembership_ownedMemberParameter

**Comment:** The `PartUsage` specifying the stakeholder.

---

## Subclassification_owningClassifier

**URI:** `https://www.omg.org/spec/SysML#Subclassification_owningClassifier`

**Label:** owningClassifier

**Domain:** Subclassification

**Range:** Classifier

**Characteristics:** Functional

**Sub-property Of:**
- Specialization_owningType

**Comment:** The `Classifier` that owns this `Subclassification` relationship, which must also be its `subclassifier`.

---

## SubjectMembership_ownedSubjectParameter

**URI:** `https://www.omg.org/spec/SysML#SubjectMembership_ownedSubjectParameter`

**Label:** ownedSubjectParameter

**Domain:** SubjectMembership

**Range:** Usage

**Characteristics:** Functional

**Sub-property Of:**
- ParameterMembership_ownedMemberParameter

**Comment:** The `Usage</code< that is the `ownedMemberParameter` of this `SubjectMembership`.

---

## Subsetting_owningFeature

**URI:** `https://www.omg.org/spec/SysML#Subsetting_owningFeature`

**Label:** owningFeature

**Domain:** Subsetting

**Range:** Feature

**Characteristics:** Functional

**Sub-property Of:**
- Specialization_owningType
- Subsetting_subsettingFeature

**Comment:** A `subsettingFeature` that is also the `owningRelatedElement` of this `Subsetting`.

---

## TypeFeaturing_owningFeatureOfType

**URI:** `https://www.omg.org/spec/SysML#TypeFeaturing_owningFeatureOfType`

**Label:** owningFeatureOfType

**Domain:** TypeFeaturing

**Range:** Feature

**Characteristics:** Functional

**Sub-property Of:**
- Relationship_owningRelatedElement
- TypeFeaturing_featureOfType

**Comment:** A `featureOfType` that is also the `owningRelatedElement` of this `TypeFeaturing`.

---

## Type_ownedConjugator

**URI:** `https://www.omg.org/spec/SysML#Type_ownedConjugator`

**Label:** ownedConjugator

**Domain:** Type

**Range:** Conjugation

**Characteristics:** Functional

**Inverse Of:** Conjugation_owningType

**Comment:** A `Conjugation` owned by this `Type` for which the `Type` is the `originalType`.

---

## Type_ownedDifferencing

**URI:** `https://www.omg.org/spec/SysML#Type_ownedDifferencing`

**Label:** ownedDifferencing

**Domain:** Type

**Range:** Differencing

**Characteristics:** Functional

**Inverse Of:** Differencing_typeDifferenced

**Comment:** The `ownedRelationships` of this `Type` that are `Differencings`, having this `Type` as their `typeDifferenced`.

---

## Type_ownedDisjoining

**URI:** `https://www.omg.org/spec/SysML#Type_ownedDisjoining`

**Label:** ownedDisjoining

**Domain:** Type

**Range:** Disjoining

**Characteristics:** Functional

**Inverse Of:** Disjoining_owningType

**Comment:** The `ownedRelationships` of this `Type` that are `Disjoinings`, for which the `Type` is the `typeDisjoined` `Type`.

---

## Type_ownedEndFeature

**URI:** `https://www.omg.org/spec/SysML#Type_ownedEndFeature`

**Label:** ownedEndFeature

**Domain:** Type

**Range:** Feature

**Sub-property Of:**
- Type_endFeature
- Type_ownedFeature

**Comment:** All `endFeatures` of this `Type` that are `ownedFeatures`.

---

## Type_ownedFeature

**URI:** `https://www.omg.org/spec/SysML#Type_ownedFeature`

**Label:** ownedFeature

**Domain:** Type

**Range:** Feature

**Sub-property Of:**
- Namespace_ownedMember

**Comment:** The `ownedMemberFeatures` of the `ownedFeatureMemberships` of this `Type`.

---

## Type_ownedFeatureMembership

**URI:** `https://www.omg.org/spec/SysML#Type_ownedFeatureMembership`

**Label:** ownedFeatureMembership

**Domain:** Type

**Range:** FeatureMembership

**Characteristics:** Functional

**Inverse Of:** FeatureMembership_owningType

**Sub-property Of:**
- Type_featureMembership

**Comment:** The `ownedMemberships` of this `Type` that are `FeatureMemberships`, for which the `Type` is the `owningType`. Each such `FeatureMembership` identifies an `ownedFeature` of the `Type`.

---

## Type_ownedIntersecting

**URI:** `https://www.omg.org/spec/SysML#Type_ownedIntersecting`

**Label:** ownedIntersecting

**Domain:** Type

**Range:** Intersecting

**Characteristics:** Functional

**Inverse Of:** Intersecting_typeIntersected

**Comment:** The `ownedRelationships` of this `Type` that are `Intersectings`, have the `Type` as their `typeIntersected`.

---

## Type_ownedSpecialization

**URI:** `https://www.omg.org/spec/SysML#Type_ownedSpecialization`

**Label:** ownedSpecialization

**Domain:** Type

**Range:** Specialization

**Characteristics:** Functional

**Inverse Of:** Specialization_owningType

**Comment:** The `ownedRelationships` of this `Type` that are `Specializations`, for which the `Type` is the `specific` `Type`.

---

## Type_ownedUnioning

**URI:** `https://www.omg.org/spec/SysML#Type_ownedUnioning`

**Label:** ownedUnioning

**Domain:** Type

**Range:** Unioning

**Characteristics:** Functional

**Inverse Of:** Unioning_typeUnioned

**Comment:** The `ownedRelationships` of this `Type` that are `Unionings`, having the `Type` as their `typeUnioned`.

---

## Usage_owningDefinition

**URI:** `https://www.omg.org/spec/SysML#Usage_owningDefinition`

**Label:** owningDefinition

**Domain:** Usage

**Range:** Definition

**Inverse Of:** Definition_ownedUsage

**Comment:** The `Definition` that owns this `Usage` (if any).

---

## Usage_owningUsage

**URI:** `https://www.omg.org/spec/SysML#Usage_owningUsage`

**Label:** owningUsage

**Domain:** Usage

**Range:** Usage

**Inverse Of:** Usage_nestedUsage

**Comment:** The `Usage` in which this `Usage` is nested (if any).

---

## VariantMembership_ownedVariantUsage

**URI:** `https://www.omg.org/spec/SysML#VariantMembership_ownedVariantUsage`

**Label:** ownedVariantUsage

**Domain:** VariantMembership

**Range:** Usage

**Characteristics:** Functional

**Sub-property Of:**
- OwningMembership_ownedMemberElement

**Comment:** The `Usage` that represents a variant in the context of the `owningVariationDefinition` or `owningVariationUsage`.

---

## ViewRenderingMembership_ownedRendering

**URI:** `https://www.omg.org/spec/SysML#ViewRenderingMembership_ownedRendering`

**Label:** ownedRendering

**Domain:** ViewRenderingMembership

**Range:** RenderingUsage

**Characteristics:** Functional

**Sub-property Of:**
- FeatureMembership_ownedMemberFeature

**Comment:** The owned `RenderingUsage` that is either itself the `referencedRendering` or subsets the `referencedRendering`.

---

