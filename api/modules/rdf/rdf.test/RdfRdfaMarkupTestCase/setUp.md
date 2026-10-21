# RdfRdfaMarkupTestCase::setUp()

- **Type:** Method
- **File:** [`modules/rdf/rdf.test`](../_file.md), lines 53–55 · [local source](../../../../../source/modules/rdf/rdf.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test#L53-L55)
- **Class:** [RdfRdfaMarkupTestCase](../RdfRdfaMarkupTestCase.md)
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
    parent::setUp('rdf', 'field_test', 'rdf_test');
  }
```

---
_Drupal 7.103 · [modules/rdf/rdf.test](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test) · Licensed GPL-2.0-or-later (see LICENSE)._
