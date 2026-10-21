# RdfGetRdfNamespacesTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/rdf/rdf.test`](../_file.md), lines 696–702 · [local source](../../../../../source/modules/rdf/rdf.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test#L696-L702)
- **Class:** [RdfGetRdfNamespacesTestCase](../RdfGetRdfNamespacesTestCase.md)
- **Module/theme:** rdf

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'RDF namespaces',
      'description' => 'Test hook_rdf_namespaces() and ensure only "safe" namespaces are returned.',
      'group' => 'RDF',
    );
  }
```

---
_Drupal 7.103 · [modules/rdf/rdf.test](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test) · Licensed GPL-2.0-or-later (see LICENSE)._
