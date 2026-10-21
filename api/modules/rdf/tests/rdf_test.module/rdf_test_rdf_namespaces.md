# rdf_test_rdf_namespaces()

- **Type:** Function
- **File:** [`modules/rdf/tests/rdf_test.module`](_file.md), lines 60–66 · [local source](../../../../../source/modules/rdf/tests/rdf_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/tests/rdf_test.module#L60-L66)
- **Module/theme:** rdf_test
- **Implements:** [hook_rdf_namespaces()](../../rdf.api.php/hook_rdf_namespaces.md)

## Signature

```php
function rdf_test_rdf_namespaces()
```

## Documentation

```text
Implements hook_rdf_namespaces().
```

## Code

```php
function rdf_test_rdf_namespaces() {
  return array(
    'dc'       => 'http://purl.org/conflicting/namespace',
    'foaf'     => 'http://xmlns.com/foaf/0.1/',
    'foaf1'    => 'http://xmlns.com/foaf/0.1/',
  );
}
```

---
_Drupal 7.103 · [modules/rdf/tests/rdf_test.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/tests/rdf_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
