# RdfTrackerAttributesTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/rdf/rdf.test`](../_file.md), lines 581–587 · [local source](../../../../../source/modules/rdf/rdf.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test#L581-L587)
- **Class:** [RdfTrackerAttributesTestCase](../RdfTrackerAttributesTestCase.md)
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
      'name' => 'RDF tracker page mapping',
      'description' => 'Test the mapping for the tracker page and ensure the proper RDFa markup in included.',
      'group' => 'RDF',
    );
  }
```

---
_Drupal 7.103 · [modules/rdf/rdf.test](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test) · Licensed GPL-2.0-or-later (see LICENSE)._
