# TaxonomyVocabularyFunctionalTest::getInfo()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 52–58 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L52-L58)
- **Class:** [TaxonomyVocabularyFunctionalTest](../TaxonomyVocabularyFunctionalTest.md)
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
      'name' => 'Taxonomy vocabulary interface',
      'description' => 'Test the taxonomy vocabulary interface.',
      'group' => 'Taxonomy',
    );
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
