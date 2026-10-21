# CommentHelperCase::setCommentSettings()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 209–213 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L209-L213)
- **Class:** [CommentHelperCase](../CommentHelperCase.md)
- **Module/theme:** comment

## Signature

```php
function setCommentSettings($name, $value, $message)
```

## Documentation

```text
Set comment setting for article content type.

@param string $name
  Name of variable.
@param string $value
  Value of variable.
@param string $message
  Status message to display.
```

## Code

```php
  function setCommentSettings($name, $value, $message) {
    variable_set($name . '_article', $value);
    // Display status message.
    $this->pass($message);
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
