# RdfCrudTestCase::setUp()

- **Type:** Method
- **File:** [`modules/rdf/rdf.test`](../_file.md), lines 220–222 · [local source](../../../../../source/modules/rdf/rdf.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test#L220-L222)
- **Class:** [RdfCrudTestCase](../RdfCrudTestCase.md)
- **Module/theme:** rdf

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('rdf', 'rdf_test');
  }
```

---
_Drupal 7.103 · [modules/rdf/rdf.test](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test) · Licensed GPL-2.0-or-later (see LICENSE)._
