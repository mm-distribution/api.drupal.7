# SearchCommentTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 760–766 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L760-L766)
- **Class:** [SearchCommentTestCase](../SearchCommentTestCase.md)
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
      'name' => 'Comment Search tests',
      'description' => 'Test integration searching comments.',
      'group' => 'Search',
    );
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
