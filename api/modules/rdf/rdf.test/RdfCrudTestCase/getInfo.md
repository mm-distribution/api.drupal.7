# RdfCrudTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/rdf/rdf.test`](../_file.md), lines 212–218 · [local source](../../../../../source/modules/rdf/rdf.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test#L212-L218)
- **Class:** [RdfCrudTestCase](../RdfCrudTestCase.md)
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
      'name' => 'RDF mapping CRUD functions',
      'description' => 'Test the RDF mapping CRUD functions.',
      'group' => 'RDF',
    );
  }
```

---
_Drupal 7.103 · [modules/rdf/rdf.test](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test) · Licensed GPL-2.0-or-later (see LICENSE)._
