# sysml2

[![Documentation](https://img.shields.io/badge/Version-20250201-blue)](https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation) 

An OML representation of the SysML2 vocabulary from OMG.

## Source

`ecore/SysML.ecore` is the SysML v2 metamodel (`nsURI https://www.omg.org/spec/SysML/20250201`), copied
unchanged from [`org.omg.sysml/model/SysML.ecore`](https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/2026-08/org.omg.sysml/model/SysML.ecore)
of the pilot implementation at tag `2026-08` (commit `692170b71867353b8f90341e61556f49a5beb0e5`).
The vocabulary IRI is unversioned (`https://www.omg.org/spec/SysML#`); the metamodel version is the
ecore's `nsURI`.

`oml/www.omg.org/spec/SysML.oml` and `owl/www.omg.org/spec/SysML.owl` and `owl/www.omg.org/spec/SysML/bundle.owl`
are generated from it. The other vocabularies under `oml/` and `owl/` are maintained by hand, and the
reasoner entailments under `owl/www.omg.org/spec/SysML/bundle/` are not part of this procedure.

## Regenerating

Requires JDK 21. Build the openCAESAR [ecore2oml](https://github.com/opencaesar/ecore-adapter) (2.13.0)
and [oml2owl](https://github.com/opencaesar/owl-adapter) (2.13.1) command-line tools with
`./gradlew ecore2oml:installDist` and `./gradlew oml2owl:installDist` in their checkouts.

1. Replace `ecore/SysML.ecore` with the pilot's `org.omg.sysml/model/SysML.ecore` at the new tag.
2. Convert it to OML, mapping the Ecore primitive types to XSD/OWL datatypes and the versioned
   `nsURI` to the unversioned vocabulary IRI (substitute the new `nsURI`). `ecore2oml` resolves the
   imported vocabularies (`rdfs`, `xsd`, `owl`, `ecore`) from its output folder, so convert into a
   copy of `oml/` and copy back only `SysML.oml`:

   ```
   cp -r oml /tmp/oml && rm /tmp/oml/www.omg.org/spec/SysML.oml
   ecore2oml -i ecore -o /tmp/oml \
     -ns 'http://www.eclipse.org/emf/2002/Ecore#EObject=http://www.w3.org/2002/07/owl#Thing' \
     -ns 'http://www.eclipse.org/emf/2002/Ecore#EString=http://www.w3.org/2001/XMLSchema#string' \
     -ns 'http://www.eclipse.org/emf/2002/Ecore#EFloat=http://www.w3.org/2001/XMLSchema#float' \
     -ns 'http://www.eclipse.org/emf/2002/Ecore#EDouble=http://www.w3.org/2002/07/owl#real' \
     -ns 'http://www.eclipse.org/emf/2002/Ecore#EInt=http://www.w3.org/2001/XMLSchema#int' \
     -ns 'http://www.eclipse.org/emf/2002/Ecore#EBoolean=http://www.w3.org/2001/XMLSchema#boolean' \
     -ns 'https://www.omg.org/spec/SysML/20250201#=https://www.omg.org/spec/SysML#'
   cp /tmp/oml/www.omg.org/spec/SysML.oml oml/www.omg.org/spec/SysML.oml
   ```

3. Convert the OML to OWL without OML metadata annotations, and copy back `SysML.owl` and
   `SysML/bundle.owl`:

   ```
   oml2owl -i oml/catalog.xml -o /tmp/owl/catalog.xml -an suppress
   cp /tmp/owl/www.omg.org/spec/SysML.owl owl/www.omg.org/spec/SysML.owl
   cp /tmp/owl/www.omg.org/spec/SysML/bundle.owl owl/www.omg.org/spec/SysML/bundle.owl
   ```

4. Update the version badge and the source tag and commit above.

Run over the previous `ecore/SysML.ecore` (20240201), steps 2 and 3 reproduce the previous
`SysML.oml`, `SysML.owl` and `bundle.owl` byte for byte (with the `20240201` `nsURI` and the UML
`PrimitiveTypes` datatypes it then referenced mapped the same way).
