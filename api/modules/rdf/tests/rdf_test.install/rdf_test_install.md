# rdf_test_install()

- **Type:** Function
- **File:** [`modules/rdf/tests/rdf_test.install`](_file.md), lines 11–25 · [local source](../../../../../source/modules/rdf/tests/rdf_test.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/tests/rdf_test.install#L11-L25)
- **Module/theme:** rdf_test
- **Implements:** [hook_install()](../../../system/system.api.php/hook_install.md)

## Signature

```php
function rdf_test_install()
```

## Documentation

```text
Implements hook_install().
```

## Code

```php
function rdf_test_install() {
  $rdf_mappings = array(
    array(
      'type' => 'node',
      'bundle' => 'test_bundle_hook_install',
      'mapping' => array(
        'rdftype' => array('foo:mapping_install1', 'bar:mapping_install2'),
      ),
    ),
  );

  foreach ($rdf_mappings as $rdf_mapping) {
    rdf_mapping_save($rdf_mapping);
  }
}
```

---
_Drupal 7.103 · [modules/rdf/tests/rdf_test.install](https://github.com/drupal/drupal/blob/7.103/modules/rdf/tests/rdf_test.install) · Licensed GPL-2.0-or-later (see LICENSE)._
