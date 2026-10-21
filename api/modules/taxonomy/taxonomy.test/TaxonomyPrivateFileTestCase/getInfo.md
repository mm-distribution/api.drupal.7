# TaxonomyPrivateFileTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 2266–2272 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L2266-L2272)
- **Class:** [TaxonomyPrivateFileTestCase](../TaxonomyPrivateFileTestCase.md)
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
      'name' => 'Taxonomy term private file access',
      'description' => 'Verifies private files on terms have appropriate access control.',
      'group' => 'Taxonomy',
    );
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
