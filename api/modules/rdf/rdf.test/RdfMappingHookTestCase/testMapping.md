# RdfMappingHookTestCase::testMapping()

- **Type:** Method
- **File:** [`modules/rdf/rdf.test`](../_file.md), lines 24–38 · [local source](../../../../../source/modules/rdf/rdf.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test#L24-L38)
- **Class:** [RdfMappingHookTestCase](../RdfMappingHookTestCase.md)
- **Module/theme:** rdf

## Signature

```php
function testMapping()
```

## Documentation

```text
Test that hook_rdf_mapping() correctly returns and processes mapping.
```

## Code

```php
  function testMapping() {
    // Test that the mapping is returned correctly by the hook.
    $mapping = rdf_mapping_load('test_entity', 'test_bundle');
    $this->assertIdentical($mapping['rdftype'], array('sioc:Post'), 'Mapping for rdftype is sioc:Post.');
    $this->assertIdentical($mapping['title'], array('predicates' => array('dc:title')), 'Mapping for title is dc:title.');
    $this->assertIdentical($mapping['created'], array(
      'predicates' => array('dc:created'),
      'datatype' => 'xsd:dateTime',
      'callback' => 'date_iso8601',
    ), t('Mapping for created is dc:created with datatype xsd:dateTime and callback date_iso8601.'));
    $this->assertIdentical($mapping['uid'], array('predicates' => array('sioc:has_creator', 'dc:creator'), 'type' => 'rel'), 'Mapping for uid is sioc:has_creator and dc:creator, and type is rel.');

    $mapping = rdf_mapping_load('test_entity', 'test_bundle_no_mapping');
    $this->assertEqual($mapping, array(), 'Empty array returned when an entity type, bundle pair has no mapping.');
  }
```

---
_Drupal 7.103 · [modules/rdf/rdf.test](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test) · Licensed GPL-2.0-or-later (see LICENSE)._
