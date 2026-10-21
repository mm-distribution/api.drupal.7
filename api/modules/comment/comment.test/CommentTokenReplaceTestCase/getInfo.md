# CommentTokenReplaceTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 1854–1860 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L1854-L1860)
- **Class:** [CommentTokenReplaceTestCase](../CommentTokenReplaceTestCase.md)
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
      'name' => 'Comment token replacement',
      'description' => 'Generates text using placeholders for dummy content to check comment token replacement.',
      'group' => 'Comment',
    );
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
