# SearchPageText::getInfo()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 252–258 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L252-L258)
- **Class:** [SearchPageText](../SearchPageText.md)
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
      'name' => 'Search page text',
      'description' => 'Tests the bike shed text on the no results page, and various other text on search pages.',
      'group' => 'Search'
    );
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
