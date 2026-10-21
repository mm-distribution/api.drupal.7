# RdfCommentAttributesTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/rdf/rdf.test`](../_file.md), lines 421–427 · [local source](../../../../../source/modules/rdf/rdf.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test#L421-L427)
- **Class:** [RdfCommentAttributesTestCase](../RdfCommentAttributesTestCase.md)
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
      'name' => 'RDF comment mapping',
      'description' => 'Tests the RDFa markup of comments.',
      'group' => 'RDF',
    );
  }
```

---
_Drupal 7.103 · [modules/rdf/rdf.test](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test) · Licensed GPL-2.0-or-later (see LICENSE)._
