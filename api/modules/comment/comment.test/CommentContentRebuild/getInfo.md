# CommentContentRebuild::getInfo()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 1814–1820 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L1814-L1820)
- **Class:** [CommentContentRebuild](../CommentContentRebuild.md)
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
      'name' => 'Comment Rebuild',
      'description' => 'Test to make sure the comment content is rebuilt.',
      'group' => 'Comment',
    );
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
