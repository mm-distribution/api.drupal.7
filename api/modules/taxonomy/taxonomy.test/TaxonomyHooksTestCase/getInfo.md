# TaxonomyHooksTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 1469–1475 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L1469-L1475)
- **Class:** [TaxonomyHooksTestCase](../TaxonomyHooksTestCase.md)
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
      'name' => 'Taxonomy term hooks',
      'description' => 'Hooks for taxonomy term load/save/delete.',
      'group' => 'Taxonomy',
    );
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
