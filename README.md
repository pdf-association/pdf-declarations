# PDF Declarations: JSON definitions

This repo contains a JSON definition and schema for all PDF Declarations recognized by the PDF Association and as published on this page: <https://pdfa.org/declarations/>.

The JSON strings provide standardized text for use in identifying PDF Declarations in user interfaces or reports. In each string, the key is the
URI for a PDF Declaration and the value is the PDF Association's display string intended for use by software.

If you want to add a PDF Declaration to the PDF Association's [Declaration index](https://pdfa.org/declarations/), please contact [declarations@pdfa.org](mailto:declarations@pdfa.org).

For more information about PDF Declarations, please see the latest [PDF Declarations Specification](https://pdfa.org/resource/pdf-declarations/).

## JSON schema validation

This repo also contains a JSON schema useful in validating the JSON data (e.g., using the Python CLI [check-jsonschema](https://pypi.org/project/check-jsonschema/)):

```console
$ check-jsonschema --schemafile .\declarations\pdf-declarations.schema.json .\declarations\pdf-declarations.json
ok -- validation done
```

---

This informative resource is freely provided to all interested PDF developers, end-users and researchers. It does not reflect an endorsement of any organization, website or corpus. If you curate, maintain, or identify
other specifications or standards that you believe might be useful to PDF users please contact us at [info@pdfa.org](mailto:info@pdfa.org).
