# SearchKeywordsConditions::getInfo()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1224–1230 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1224-L1230)
- **Class:** [SearchKeywordsConditions](../SearchKeywordsConditions.md)
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
      'name' => 'Keywords and conditions',
      'description' => 'Verify the search pulls in keywords and extra conditions.',
      'group' => 'Search',
    );
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
