# rdf_test_rdf_mapping()

- **Type:** Function
- **File:** [`modules/rdf/tests/rdf_test.module`](_file.md), lines 11–55 · [local source](../../../../../source/modules/rdf/tests/rdf_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/tests/rdf_test.module#L11-L55)
- **Module/theme:** rdf_test
- **Implements:** [hook_rdf_mapping()](../../rdf.api.php/hook_rdf_mapping.md)

## Signature

```php
function rdf_test_rdf_mapping()
```

## Documentation

```text
Implements hook_rdf_mapping().
```

## Code

```php
function rdf_test_rdf_mapping() {
  return array(
    array(
      'type' => 'test_entity',
      'bundle' => 'test_bundle',
      'mapping' => array(
        'rdftype' => array('sioc:Post'),
        'title' => array(
          'predicates' => array('dc:title'),
        ),
        'created' => array(
          'predicates' => array('dc:created'),
          'datatype' => 'xsd:dateTime',
          'callback' => 'date_iso8601',
        ),
        'uid' => array(
          'predicates' => array('sioc:has_creator', 'dc:creator'),
          'type' => 'rel',
        ),
        'foobar' => array(
          'predicates' => array('foo:bar'),
        ),
        'foobar1' => array(
          'datatype' => 'foo:bar1type',
          'predicates' => array('foo:bar1'),
        ),
        'foobar_objproperty1' => array(
          'predicates' => array('sioc:has_creator', 'dc:creator'),
          'type' => 'rel',
        ),
        'foobar_objproperty2' => array(
          'predicates' => array('sioc:reply_of'),
          'type' => 'rev',
        ),
      ),
    ),
    array(
      'type' => 'node',
      'bundle' => 'blog',
      'mapping' => array(
        'rdftype' => array('sioct:Weblog'),
      ),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/rdf/tests/rdf_test.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/tests/rdf_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
