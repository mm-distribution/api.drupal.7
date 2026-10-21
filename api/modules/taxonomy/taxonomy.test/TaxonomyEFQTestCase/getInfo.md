# TaxonomyEFQTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 2061–2067 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L2061-L2067)
- **Class:** [TaxonomyEFQTestCase](../TaxonomyEFQTestCase.md)
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
      'name' => 'Taxonomy EntityFieldQuery',
      'description' => 'Verifies operation of a taxonomy-based EntityFieldQuery.',
      'group' => 'Taxonomy',
    );
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
