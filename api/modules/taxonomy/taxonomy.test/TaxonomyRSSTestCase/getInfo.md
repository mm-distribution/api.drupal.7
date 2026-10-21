# TaxonomyRSSTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 1082–1088 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L1082-L1088)
- **Class:** [TaxonomyRSSTestCase](../TaxonomyRSSTestCase.md)
- **Module/theme:** taxonomy

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
      'name' => 'Taxonomy RSS Content.',
      'description' => 'Ensure that data added as terms appears in RSS feeds if "RSS Category" format is selected.',
      'group' => 'Taxonomy',
    );
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
