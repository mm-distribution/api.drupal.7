# SearchExcerptTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1618–1624 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1618-L1624)
- **Class:** [SearchExcerptTestCase](../SearchExcerptTestCase.md)
- **Module/theme:** search

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
      'name' => 'Search excerpt extraction',
      'description' => 'Tests that the search_excerpt() function works.',
      'group' => 'Search',
    );
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
