# SearchSetLocaleTest::getInfo()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 2144–2150 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L2144-L2150)
- **Class:** [SearchSetLocaleTest](../SearchSetLocaleTest.md)
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
      'name' => 'Search with numeric locale set',
      'description' => 'Check that search works with numeric locale settings',
      'group' => 'Search',
    );
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
