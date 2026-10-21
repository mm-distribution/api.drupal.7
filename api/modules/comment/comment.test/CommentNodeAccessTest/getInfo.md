# CommentNodeAccessTest::getInfo()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 1504–1510 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L1504-L1510)
- **Class:** [CommentNodeAccessTest](../CommentNodeAccessTest.md)
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
      'name' => 'Comment node access',
      'description' => 'Test comment viewing with node access.',
      'group' => 'Comment',
    );
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
