# SearchPageOverride::getInfo()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1950–1956 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1950-L1956)
- **Class:** [SearchPageOverride](../SearchPageOverride.md)
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
      'name' => 'Search page override',
      'description' => 'Verify that hook_search_page can override search page display.',
      'group' => 'Search',
    );
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
