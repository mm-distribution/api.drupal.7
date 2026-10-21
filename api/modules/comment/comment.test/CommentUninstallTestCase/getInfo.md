# CommentUninstallTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 2393–2399 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L2393-L2399)
- **Class:** [CommentUninstallTestCase](../CommentUninstallTestCase.md)
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
      'name' => 'Comment module uninstallation',
      'description' => 'Tests that the comments module can be properly uninstalled.',
      'group' => 'Comment',
    );
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
