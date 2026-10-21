# CommentThreadingTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 2218–2224 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L2218-L2224)
- **Class:** [CommentThreadingTestCase](../CommentThreadingTestCase.md)
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
      'name' => 'Comment Threading',
      'description' => 'Test to make sure the comment number increments properly.',
      'group' => 'Comment',
    );
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
