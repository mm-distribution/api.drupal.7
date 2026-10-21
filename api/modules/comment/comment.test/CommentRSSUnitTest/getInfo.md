# CommentRSSUnitTest::getInfo()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 1782–1788 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L1782-L1788)
- **Class:** [CommentRSSUnitTest](../CommentRSSUnitTest.md)
- **Module/theme:** comment

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
      'name' => 'Comment RSS',
      'description' => 'Test comments as part of an RSS feed.',
      'group' => 'Comment',
    );
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
