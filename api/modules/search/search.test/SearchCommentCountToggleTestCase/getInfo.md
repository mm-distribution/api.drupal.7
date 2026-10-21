# SearchCommentCountToggleTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1057–1063 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1057-L1063)
- **Class:** [SearchCommentCountToggleTestCase](../SearchCommentCountToggleTestCase.md)
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
      'name' => 'Comment count toggle',
      'description' => 'Verify that comment count display toggles properly on comment status of node.',
      'group' => 'Search',
    );
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
