# RDF Mapping API

- **Topic id:** `rdf`
- **Defined in:** [`modules/rdf/rdf.module`](../modules/rdf/rdf.module/_file.md), line 21 · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L21)

## Documentation

```text
@defgroup rdf RDF Mapping API
@{
Functions to describe entities and bundles in RDF.

The RDF module introduces RDF and RDFa to Drupal. RDF is a W3C standard to
describe structured data. RDF can be serialized as RDFa in XHTML attributes
to augment visual data with machine-readable hints.
@see http://www.w3.org/RDF/
@see http://www.w3.org/TR/xhtml-rdfa-primer/

Modules can provide mappings of their bundles' data and metadata to RDF
classes and properties. This module takes care of injecting these mappings
into variables available to theme functions and templates. All Drupal core
themes are coded to be RDFa compatible.

Example mapping from node.module:
@code
  array(
    'type' => 'node',
    'bundle' => RDF_DEFAULT_BUNDLE,
    'mapping' => array(
      'rdftype' => array('sioc:Item', 'foaf:Document'),
      'title' => array(
        'predicates' => array('dc:title'),
      ),
      'created' => array(
        'predicates' => array('dc:date', 'dc:created'),
        'datatype' => 'xsd:dateTime',
        'callback' => 'date_iso8601',
      ),
     'body' => array(
        'predicates' => array('content:encoded'),
      ),
      'uid' => array(
        'predicates' => array('sioc:has_creator'),
      ),
      'name' => array(
        'predicates' => array('foaf:name'),
      ),
    ),
  );
@endcode
```

## Members (derived, 11)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [hook_rdf_mapping()](../modules/rdf/rdf.api.php/hook_rdf_mapping.md) (function) — Allow modules to define RDF mappings for field bundles.
- [hook_rdf_namespaces()](../modules/rdf/rdf.api.php/hook_rdf_namespaces.md) (function) — Allow modules to define namespaces for RDF mappings.
- [rdf_get_namespaces()](../modules/rdf/rdf.module/rdf_get_namespaces.md) (function) — Returns an array of RDF namespaces defined in modules that implement hook_rdf_namespaces().
- [rdf_mapping_delete()](../modules/rdf/rdf.module/rdf_mapping_delete.md) (function) — Deletes the mapping for the given bundle from the database.
- [rdf_mapping_load()](../modules/rdf/rdf.module/rdf_mapping_load.md) (function) — Returns the mapping for attributes of a given entity type/bundle pair.
- [rdf_mapping_save()](../modules/rdf/rdf.module/rdf_mapping_save.md) (function) — Saves an RDF mapping to the database.
- [rdf_rdf_namespaces()](../modules/rdf/rdf.module/rdf_rdf_namespaces.md) (function) — Implements hook_rdf_namespaces().
- [rdf_rdfa_attributes()](../modules/rdf/rdf.module/rdf_rdfa_attributes.md) (function) — Builds an array of RDFa attributes for a given mapping. This array will typically be passed through drupal_attributes() to create the attributes variables that are available to template files. These include $attributes, $title_attributes, $content_attributes and the field-specific $item_attributes variables. For more information, see theme_rdf_template_variable_wrapper().
- [theme_rdf_metadata()](../modules/rdf/rdf.module/theme_rdf_metadata.md) (function) — Returns HTML for a series of empty spans for exporting RDF metadata in RDFa.
- [theme_rdf_template_variable_wrapper()](../modules/rdf/rdf.module/theme_rdf_template_variable_wrapper.md) (function) — Returns HTML for a template variable wrapped in an HTML element with the RDF attributes.
- [RDF_DEFAULT_BUNDLE](../modules/rdf/rdf.module/_file.md#rdf_default_bundle) (constant) — RDF bundle flag: Default bundle.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
